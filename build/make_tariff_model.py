#!/usr/bin/env python3
"""Build the shared Tariff-Impact Model template (Research + Standard Cost).

Run from the repo root (build/build.py calls it):

    python3 build/make_tariff_model.py            # writes dist/Tariff-Impact-Model-Template.xlsx
    python3 build/make_tariff_model.py --out X    # writes somewhere else

What it makes: a LIVE Excel workbook. Every result is an Excel formula, not a typed value.
Tabs: README, Action (Research fills: the WHAT), Items (Standard Cost fills: the $ inputs),
Calc (formulas only), Summary (formulas only), Review (maker-checker sign-off log).

Rules this script follows:
- Formulas work in Excel 2010+ and LibreOffice Calc: no dynamic arrays, LET, LAMBDA, XLOOKUP,
  IFS or wildcard criteria. Lookups use INDEX/MATCH, COUNTIF(S), SUMIFS and SUMPRODUCT.
- The sample rows are SYNTHETIC (a fictional action and invented items) and say so on the sheet.
- The output is byte-for-byte deterministic: fixed document timestamps and fixed zip entry times.

Explained tab by tab in docs/templates/domain/tariff-impact-model-guide.md.
"""

import argparse
import datetime as dt
import re
import tempfile
import zipfile
from pathlib import Path

from openpyxl import Workbook
from openpyxl.formatting.rule import FormulaRule
from openpyxl.styles import Alignment, Border, Font, NamedStyle, PatternFill, Side
from openpyxl.utils import get_column_letter
from openpyxl.workbook.defined_name import DefinedName
from openpyxl.worksheet.datavalidation import DataValidation

ROOT = Path(__file__).resolve().parent.parent
DEFAULT_OUT = ROOT / "dist" / "Tariff-Impact-Model-Template.xlsx"

TEMPLATE_VERSION = "1.0"
TEMPLATE_DATE = dt.datetime(2026, 10, 8, 0, 0, 0)
FIRST = 5            # first data row on Action lists, Items and Calc
ITEM_ROWS = 250      # capacity of Items / Calc
LIST_ROWS = 50       # capacity of each scope list on Action
LAST = FIRST + ITEM_ROWS - 1
LIST_LAST = FIRST + LIST_ROWS - 1

NAVY = "1F3864"
FONT = "Calibri"
INPUT_YELLOW = "FFF2CC"
CALC_GREY = "F2F2F2"
GREEN = PatternFill("solid", fgColor="C6EFCE")
RED = PatternFill("solid", fgColor="FFC7CE")
AMBER = PatternFill("solid", fgColor="FFEB9C")
THIN = Side(style="thin", color="BFBFBF")
GRID = Border(left=THIN, right=THIN, top=THIN, bottom=THIN)

# ------------------------------------------------------------------ styles ----

STYLE_SPECS = {
    # name: (font kwargs, fill colour or None, number format, wrap, border)
    "TIM Title": (dict(size=16, bold=True, color=NAVY), None, "General", False, False),
    "TIM Subtitle": (dict(italic=True, color="595959"), None, "General", False, False),
    "TIM Warning": (dict(bold=True, color="C00000"), None, "General", False, False),
    "TIM Section": (dict(size=12, bold=True, color=NAVY), None, "General", False, False),
    "TIM Header": (dict(bold=True, color="FFFFFF"), NAVY, "General", True, True),
    "TIM Label": (dict(bold=True, size=10), None, "General", True, True),
    "TIM Text": (dict(size=10), None, "General", True, False),
    "TIM Note": (dict(size=9, italic=True, color="595959"), None, "General", True, True),
    "TIM Input": (dict(size=10), INPUT_YELLOW, "General", True, True),
    "TIM Input Text": (dict(size=10), INPUT_YELLOW, "@", True, True),
    "TIM Input Pct": (dict(size=10), INPUT_YELLOW, "0.0%", False, True),
    "TIM Input Money": (dict(size=10), INPUT_YELLOW, "#,##0.00", False, True),
    "TIM Input Qty": (dict(size=10), INPUT_YELLOW, "#,##0", False, True),
    "TIM Input Date": (dict(size=10), INPUT_YELLOW, "yyyy-mm-dd", False, True),
    "TIM Calc": (dict(size=10), CALC_GREY, "General", False, True),
    "TIM Calc Pct": (dict(size=10), CALC_GREY, "0.0%", False, True),
    "TIM Calc Money": (dict(size=10), CALC_GREY, "#,##0.00", False, True),
    "TIM Calc Unit": (dict(size=10), CALC_GREY, "#,##0.0000", False, True),
    "TIM Calc Whole": (dict(size=10), CALC_GREY, "#,##0", False, True),
    "TIM Calc Date": (dict(size=10), CALC_GREY, "yyyy-mm-dd", False, True),
    "TIM Calc Key": (dict(size=8, color="808080"), CALC_GREY, "0.000000000", False, True),
}


def add_styles(wb):
    for name, (font, fill, fmt, wrap, border) in STYLE_SPECS.items():
        st = NamedStyle(name=name)
        st.font = Font(name=FONT, **font)
        if fill:
            st.fill = PatternFill("solid", fgColor=fill)
        st.number_format = fmt
        st.alignment = Alignment(wrap_text=wrap, vertical="top")
        if border:
            st.border = GRID
        wb.add_named_style(st)


def put(ws, ref, value, style):
    cell = ws[ref]
    cell.value = value
    cell.style = style
    return cell


def title(ws, text, subtitle, warning=None):
    put(ws, "A1", text, "TIM Title")
    put(ws, "A2", subtitle, "TIM Subtitle")
    if warning:
        put(ws, "A3", warning, "TIM Warning")


def headers(ws, row, col, names):
    for i, name in enumerate(names):
        put(ws, f"{get_column_letter(col + i)}{row}", name, "TIM Header")


def widths(ws, spec):
    for col, w in spec.items():
        ws.column_dimensions[col].width = w


def list_dv(ws, values, rng, prompt=None):
    dv = DataValidation(type="list", formula1='"' + ",".join(values) + '"', allow_blank=True)
    dv.error, dv.errorTitle, dv.showErrorMessage = "Pick a value from the list.", "Not allowed", True
    if prompt:
        dv.prompt, dv.showInputMessage = prompt, True
    ws.add_data_validation(dv)
    dv.add(rng)


def number_dv(ws, kind, rng, low, high, message):
    dv = DataValidation(type=kind, operator="between", formula1=str(low), formula2=str(high), allow_blank=True)
    dv.error, dv.errorTitle, dv.showErrorMessage = message, "Check the value", True
    ws.add_data_validation(dv)
    dv.add(rng)


def length_dv(ws, rng, length, message):
    dv = DataValidation(type="textLength", operator="equal", formula1=str(length), allow_blank=True)
    dv.error, dv.errorTitle, dv.showErrorMessage = message, "Check the value", True
    ws.add_data_validation(dv)
    dv.add(rng)


def name(wb, label, ref):
    wb.defined_names[label] = DefinedName(label, attr_text=ref)


# ------------------------------------------------------------------ README ----

README_ROWS = [
    ("section", "What this workbook is"),
    ("", "The one shared model for a tariff action. Research (Hire A) records the WHAT on the Action tab. "
         "Standard Cost (Hire B) loads the items on the Items tab. Calc and Summary work out the $ impact with live formulas."),
    ("", "Boundary rule: Research owns scope, HTS, origins, rates, dates and stacking (from the checked Tariff-Impact Brief). "
         "Standard Cost owns the item data, landed cost, margin and the Oracle cost update. Nobody edits the other track's tab; ask instead."),
    ("", "Guide (every tab and formula explained): docs/templates/domain/tariff-impact-model-guide.md. "
         "Brief template: docs/templates/domain/tariff-impact-brief.md."),
    ("section", "Colour key"),
    ("Yellow", "Input cell. Type or paste values here only."),
    ("Grey", "Formula cell. Do not type over it. If a formula looks wrong, raise it with the Manager; do not patch it with a typed number."),
    ("Green / red", "Status from conditional formatting: green = in scope or check passed; red = a CHECK that must be cleared before review."),
    ("section", "How to use it (one copy per tariff action and importing country)"),
    ("1", "Copy this template. Name the copy TIM_[Action ID]_[import country]_v0.1.xlsx and save it in [COMPANY: tariff model folder]. Link it on the Jira story; never email copies."),
    ("2", "Delete the SAMPLE rows on Action (lists and determinations), Items and Review before real use."),
    ("3", "Research (maker): fill the Action tab from the checked brief: fields in column B, the HTS scope list, the exclusion list, the origin list and any item-level determinations."),
    ("4", "Research checker (Senior or Manager): compare the Action tab with the brief line by line. Log the review on the Review tab."),
    ("5", "Standard Cost (maker): paste the item extract into Items ([COMPANY: Oracle cost extract or warehouse query], with the extract date in column L). Keep HTS, item numbers and origin codes as text."),
    ("6", "Clear every CHECK in Calc column AB. Summary B24 must read YES before review."),
    ("7", "Standard Cost checker (Manager): recalculate 3 items by hand, confirm the item count and totals against the extract, confirm the Summary reconciles. Log the review on the Review tab."),
    ("8", "Release: only a version with a checker sign-off on the Review tab goes to the business. Any change after sign-off is a new version and a new review."),
    ("section", "Maker-checker rule"),
    ("", "Every model released to the business gets a documented second-person review (Senior or Manager): name, date, version, findings. "
         "This applies after day 90 too. The maker never signs their own review."),
    ("section", "Limits (read before you trust a number)"),
    ("", "Ad valorem rates only. Specific or compound rates (per kg, per unit) need an ad valorem equivalent agreed with Research and the checker."),
    ("", "Landed cost change = duty change only. Fees (for example US MPF), freight and brokerage are assumed unchanged. Duty-based taxes "
         "(Canada GST, Mexico IVA) are left out because they are normally recoverable; confirm with Finance."),
    ("", "Annual impact assumes the action applies for a full year at the Items volume. It does not model in-transit stock, stock already on hand, "
         "the end date, timing within the cost period or supplier price changes."),
    ("", "Current duty rate and current standard cost come from the Items tab as given. The model assumes the current standard cost already includes duty at the current rate."),
    ("", "Capacity: 250 item rows and 50 rows per scope list. To extend, see the guide."),
    ("section", "Template version"),
    ("", f"Template v{TEMPLATE_VERSION}, built {TEMPLATE_DATE:%Y-%m-%d} by build/make_tariff_model.py. Owner: BSA Manager. "
         "Change the generator script, not a copy of the workbook."),
]


def build_readme(wb):
    ws = wb.active
    ws.title = "README"
    title(ws, "Tariff-Impact Model (template)",
          "Shared by Research (the WHAT) and Standard Cost (the $). One copy per tariff action.",
          "All sample rows in this template are SYNTHETIC and use a FICTIONAL action. Delete them before real use.")
    r = 5
    for label, text in README_ROWS:
        if label == "section":
            r += 1
            put(ws, f"A{r}", text, "TIM Section")
        else:
            put(ws, f"A{r}", label, "TIM Label")
            put(ws, f"B{r}", text, "TIM Text")
            ws.row_dimensions[r].height = 15 * max(1, -(-len(text) // 120))
        r += 1
    widths(ws, {"A": 14, "B": 130})
    ws.freeze_panes = "A4"
    ws.sheet_properties.tabColor = "808080"


# ------------------------------------------------------------------ Action ----

# (label, defined name, sample value, style, note)
ACTION_FIELDS = [
    ("Action ID", "act_ID", "TA-US-FIC-01", "TIM Input Text",
     "Brief section 1. Same ID in the Jira label and the file name."),
    ("Action name", "act_Name",
     "FICTIONAL EXAMPLE: US additional duty on iron or steel fasteners (heading 7318) from Country X", "TIM Input",
     "Brief section 1."),
    ("Importing country (US, CA or MX)", "act_Country", "US", "TIM Input Text",
     "Brief section 1. One model per importing country."),
    ("Legal authority category", "act_Authority", "Section 301", "TIM Input",
     "Brief section 3. Category only; the citation goes in the next rows."),
    ("Tariff-Impact Brief ID and version", "act_Brief", "TIB-TA-US-FIC-01 v1.0", "TIM Input Text",
     "Brief section 1. The model must match a checked brief version."),
    ("Primary legal source", "act_Source",
     "FICTIONAL: Federal Register notice 92 FR 00000; HTSUS heading 9903.XX.01", "TIM Input",
     "Brief section 4. Citation of the notice, order or decree."),
    ("Effective date", "act_EffDate", dt.date(2027, 3, 1), "TIM Input Date",
     "Brief section 5."),
    ("Effective time and basis", "act_Basis",
     "12:01 a.m. ET; goods entered for consumption, or withdrawn from warehouse for consumption, on or after the effective date",
     "TIM Input", "Brief section 5. Quote the notice wording."),
    ("In-transit provision", "act_InTransit",
     "FICTIONAL: not covered if loaded on the final mode of transit before the effective date and entered before 2027-04-30",
     "TIM Input", "Brief section 5. Not applied by the formulas; Standard Cost handles in-transit stock separately."),
    ("End date (blank if none)", "act_EndDate", None, "TIM Input Date",
     "Brief section 5. Not applied by the formulas."),
    ("Additional duty rate (% of customs value)", "act_Rate", 0.25, "TIM Input Pct",
     "Brief section 7. Ad valorem only."),
    ("Rate change type (ADD or REPLACE)", "act_RateType", "ADD", "TIM Input Text",
     "ADD: the rate above is added to the item's current rate. REPLACE: the rate above replaces this action's earlier rate (next row)."),
    ("Earlier rate of this action being replaced", "act_PriorRate", 0, "TIM Input Pct",
     "REPLACE only. Brief section 7. Must already be inside each item's current rate."),
    ("USMCA-qualifying goods exempt? (Y, N or N/A)", "act_USMCAExempt", "N/A", "TIM Input Text",
     "Brief section 6.5. Y removes items flagged USMCA-qualifying on the Items tab."),
    ("Stacking interpretation", "act_Stacking",
     "Adds to the HTSUS column 1 General rate. FICTIONAL: no other additional duty applies to the sample items.",
     "TIM Input", "Brief section 6.6. Item-level exceptions go in the determinations list (column P)."),
    ("Research maker", "act_Maker", "Hire A", "TIM Input", "Brief section 12."),
    ("Research checker", "act_Checker", "Senior", "TIM Input", "Brief section 12."),
    ("Date brief checked", "act_Checked", dt.date(2027, 2, 18), "TIM Input Date", "Brief section 12."),
    ("Model version", "act_ModelVersion", "v1.1 (SAMPLE)", "TIM Input Text",
     "Matches the latest line on the Review tab and the file name."),
]
AUTHORITIES = ["Section 232", "Section 301", "Section 201", "Section 122", "Section 338", "IEEPA", "AD/CVD",
               "Canada surtax order", "Mexico decree (DOF)", "Other"]

SAMPLE_SCOPE_HTS = [("7318", "FICTIONAL annex line 1: heading 7318, screws, bolts, nuts, washers, rivets and similar, of iron or steel")]
SAMPLE_EXCL_HTS = [("7318.24", "FICTIONAL exclusion: cotters and cotter pins (annex note 2)")]
SAMPLE_COO = [("XX", "Country X (FICTIONAL; XX is an ISO user-assigned code)")]
SAMPLE_DETERMINATIONS = [("SAMPLE-005", "OUT",
                          "FICTIONAL product exclusion: fasteners certified for civil aircraft; certificate on file", "Brief 6.4")]


def build_action(wb):
    ws = wb.create_sheet("Action")
    title(ws, "Action: the WHAT (Research fills this tab from the checked Tariff-Impact Brief)",
          "Standard Cost reads this tab but never changes it. Questions go to Research on the Jira story.",
          "SAMPLE: the values below describe a FICTIONAL action for training. No such action exists.")
    headers(ws, 4, 1, ["Field", "Value", "Where it comes from"])
    for i, (label, dname, value, style, note) in enumerate(ACTION_FIELDS):
        r = FIRST + i
        put(ws, f"A{r}", label, "TIM Label")
        put(ws, f"B{r}", value, style)
        put(ws, f"C{r}", note, "TIM Note")
        name(wb, dname, f"Action!$B${r}")
    field_row = {d: FIRST + i for i, (_, d, *_rest) in enumerate(ACTION_FIELDS)}

    # Scope lists, side by side, all with their header on row 4.
    headers(ws, 4, 5, ["In-scope HTS prefix (as written)", "Digits (formula)", "Annex line or description (source)"])
    headers(ws, 4, 9, ["Excluded HTS prefix (as written)", "Digits (formula)", "Exclusion basis (source)"])
    headers(ws, 4, 13, ["Origin (ISO 2)", "Country or note"])
    headers(ws, 4, 16, ["Item number", "Determination (IN or OUT)", "Reason", "Brief ref"])
    for r in range(FIRST, LIST_LAST + 1):
        for col in "EIMP":
            put(ws, f"{col}{r}", None, "TIM Input Text")
        for col in "GKNRS":
            put(ws, f"{col}{r}", None, "TIM Input")
        put(ws, f"Q{r}", None, "TIM Input Text")
        for src, dst in (("E", "F"), ("I", "J")):
            put(ws, f"{dst}{r}",
                f'=IF(TRIM({src}{r}&"")="","",SUBSTITUTE(SUBSTITUTE(SUBSTITUTE(TRIM({src}{r}&""),".","")," ",""),"-",""))',
                "TIM Calc")
    for i, (prefix, desc) in enumerate(SAMPLE_SCOPE_HTS):
        ws[f"E{FIRST + i}"].value, ws[f"G{FIRST + i}"].value = prefix, desc
    for i, (prefix, desc) in enumerate(SAMPLE_EXCL_HTS):
        ws[f"I{FIRST + i}"].value, ws[f"K{FIRST + i}"].value = prefix, desc
    for i, (code, desc) in enumerate(SAMPLE_COO):
        ws[f"M{FIRST + i}"].value, ws[f"N{FIRST + i}"].value = code, desc
    for i, (item, det, reason, ref) in enumerate(SAMPLE_DETERMINATIONS):
        r = FIRST + i
        ws[f"P{r}"].value, ws[f"Q{r}"].value, ws[f"R{r}"].value, ws[f"S{r}"].value = item, det, reason, ref

    name(wb, "scope_HTS", f"Action!$F${FIRST}:$F${LIST_LAST}")
    name(wb, "excl_HTS", f"Action!$J${FIRST}:$J${LIST_LAST}")
    name(wb, "scope_COO", f"Action!$M${FIRST}:$M${LIST_LAST}")
    name(wb, "det_Item", f"Action!$P${FIRST}:$P${LIST_LAST}")
    name(wb, "det_Status", f"Action!$Q${FIRST}:$Q${LIST_LAST}")

    list_dv(ws, ["US", "CA", "MX"], f"B{field_row['act_Country']}")
    list_dv(ws, AUTHORITIES, f"B{field_row['act_Authority']}")
    list_dv(ws, ["ADD", "REPLACE"], f"B{field_row['act_RateType']}",
            "ADD = on top of the current rate. REPLACE = replaces this action's earlier rate.")
    list_dv(ws, ["Y", "N", "N/A"], f"B{field_row['act_USMCAExempt']}")
    for key in ("act_Rate", "act_PriorRate"):
        number_dv(ws, "decimal", f"B{field_row[key]}", 0, 10, "Enter a rate between 0% and 1000%, as a percentage.")
    for key in ("act_EffDate", "act_EndDate", "act_Checked"):
        number_dv(ws, "date", f"B{field_row[key]}", 36526, 73051, "Enter a date (yyyy-mm-dd).")
    length_dv(ws, f"M{FIRST}:M{LIST_LAST}", 2, "Use the 2-letter ISO country code, no spaces.")
    list_dv(ws, ["IN", "OUT"], f"Q{FIRST}:Q{LIST_LAST}")

    widths(ws, {"A": 30, "B": 44, "C": 38, "D": 2, "E": 16, "F": 11, "G": 38, "H": 2, "I": 16, "J": 11, "K": 34,
                "L": 2, "M": 9, "N": 30, "O": 2, "P": 14, "Q": 13, "R": 38, "S": 10})
    ws.row_dimensions[4].height = 32
    ws.freeze_panes = "A5"
    ws.sheet_properties.tabColor = "2E75B6"


# ------------------------------------------------------------------- Items ----

ITEM_HEADERS = ["Item number", "Description", "Import country (US, CA, MX)", "HTS, 10 digits (text)",
                "Country of origin (ISO 2)", "USMCA qualifying (Y/N)", "Unit customs value", "Annual quantity",
                "Current duty rate (% of customs value)", "Current standard cost per unit", "Sell price per unit",
                "Source and notes"]
ITEM_STYLES = ["TIM Input Text", "TIM Input", "TIM Input Text", "TIM Input Text", "TIM Input Text", "TIM Input Text",
               "TIM Input Money", "TIM Input Qty", "TIM Input Pct", "TIM Input Money", "TIM Input Money", "TIM Input"]

# SYNTHETIC rows. The first 6 HTS digits are real HS subheadings; the last 4 digits are invented.
# Values, rates, costs and prices are invented. XX and XY are ISO user-assigned codes for fictional countries.
SAMPLE_ITEMS = [
    ("SAMPLE-001", "Hex cap screw, steel, zinc plated", "US", "7318.15.9001", "XX", "N", 4.20, 120000, 0.05, 4.95, 7.40, "In scope by rules"),
    ("SAMPLE-002", "Hex nut, steel", "US", "7318169001", "XX", "N", 0.85, 400000, 0.00, 1.02, 1.55, "In scope; HTS pasted without dots"),
    ("SAMPLE-003", "Flat washer, steel", "US", "7318.22.9001", "XX", "N", 0.12, 900000, 0.00, 0.15, 0.24, "In scope by rules"),
    ("SAMPLE-004", "Cotter pin, steel", "US", "7318.24.9001", "XX", "N", 0.30, 50000, 0.00, 0.36, 0.60, "Out: excluded subheading"),
    ("SAMPLE-005", "Bolt certified for civil aircraft", "US", "7318.15.9002", "XX", "N", 12.50, 8000, 0.025, 14.10, 22.00, "Out: Research determination"),
    ("SAMPLE-006", "Hex cap screw, steel, from Country Y", "US", "7318.15.9001", "XY", "N", 3.90, 60000, 0.05, 4.60, 7.40, "Out: origin not listed"),
    ("SAMPLE-007", "Carriage bolt, steel, from Mexico, USMCA", "US", "7318.15.9003", "MX", "Y", 2.10, 150000, 0.00, 2.45, 3.90, "Out: origin not listed"),
    ("SAMPLE-008", "Carriage bolt, steel, from Mexico, non-qualifying", "US", "7318.15.9003", "MX", "N", 2.30, 40000, 0.05, 2.70, 3.90, "Out: origin not listed"),
    ("SAMPLE-009", "Self-tapping screw, steel, from Canada", "US", "7318.14.9001", "CA", "N", 0.40, 300000, 0.05, 0.47, 0.80, "Out: origin not listed"),
    ("SAMPLE-010", "Mounting bracket, steel (not a fastener)", "US", "7326.90.9001", "XX", "N", 6.00, 20000, 0.029, 6.80, 11.50, "Out: HTS not listed"),
    ("SAMPLE-011", "Ball valve, brass", "US", "8481.80.9001", "XX", "N", 18.00, 5000, 0.04, 20.50, 34.00, "Out: HTS not listed"),
    ("SAMPLE-012", "Rivet, steel", "US", "7318.23.9001", "XX", "N", 0.05, 0, 0.00, 0.06, 0.10, "In scope; no forecast volume"),
    ("SAMPLE-013", "Hex cap screw, steel, imported into Canada", "CA", "7318.15.9001", "XX", "N", 4.20, 30000, 0.00, 4.95, 7.40, "Out: different import country"),
]


def build_items(wb):
    ws = wb.create_sheet("Items")
    title(ws, "Items: the $ inputs (Standard Cost fills this tab from the item extract)",
          "Source: [COMPANY: Oracle cost extract or warehouse query]. One row per item and import country. Paste values only.",
          "SAMPLE ROWS 5-17 ARE SYNTHETIC: invented items, values and rates; HTS last 4 digits are made up. Delete before real use.")
    headers(ws, 4, 1, ITEM_HEADERS)
    for r in range(FIRST, LAST + 1):
        for c, style in enumerate(ITEM_STYLES, 1):
            put(ws, f"{get_column_letter(c)}{r}", None, style)
    for i, row in enumerate(SAMPLE_ITEMS):
        for c, v in enumerate(row, 1):
            ws.cell(row=FIRST + i, column=c).value = v
    rng = lambda col: f"{col}{FIRST}:{col}{LAST}"  # noqa: E731
    list_dv(ws, ["US", "CA", "MX"], rng("C"))
    length_dv(ws, rng("E"), 2, "Use the 2-letter ISO country code, no spaces.")
    list_dv(ws, ["Y", "N"], rng("F"), "Y only if a valid USMCA certification supports the claim.")
    for col in "GJK":
        number_dv(ws, "decimal", rng(col), 0, 100000000, "Enter a number of 0 or more.")
    number_dv(ws, "whole", rng("H"), 0, 2000000000, "Enter a whole number of 0 or more.")
    number_dv(ws, "decimal", rng("I"), 0, 10, "Enter the rate as a percentage, for example 2.5%.")
    widths(ws, {"A": 14, "B": 38, "C": 11, "D": 15, "E": 10, "F": 11, "G": 12, "H": 12, "I": 13, "J": 13,
                "K": 12, "L": 30})
    ws.row_dimensions[4].height = 45
    ws.freeze_panes = "B5"
    ws.auto_filter.ref = f"A4:L{LAST}"
    ws.sheet_properties.tabColor = "C55A11"


# -------------------------------------------------------------------- Calc ----

CALC_COLUMNS = [
    # (header, formula template using {r}, style, width)
    ("Item number", '=IF(TRIM(Items!A{r}&"")="","",TRIM(Items!A{r}&""))', "TIM Calc", 14),
    ("Description", '=IF($A{r}="","",Items!B{r}&"")', "TIM Calc", 30),
    ("HTS digits",
     '=IF($A{r}="","",SUBSTITUTE(SUBSTITUTE(SUBSTITUTE(TRIM(Items!D{r}&""),".","")," ",""),"-",""))', "TIM Calc", 12),
    ("HTS chapter", '=IF($A{r}="","",LEFT($C{r},2))', "TIM Calc", 8),
    ("Origin", '=IF($A{r}="","",UPPER(TRIM(Items!E{r}&"")))', "TIM Calc", 8),
    ("Import country matches (Y/N)",
     '=IF($A{r}="","",IF(UPPER(TRIM(Items!C{r}&""))=UPPER(TRIM(act_Country&"")),"Y","N"))', "TIM Calc", 10),
    ("HTS on scope list (Y/N)",
     '=IF($A{r}="","",IF(SUMPRODUCT((scope_HTS<>"")*(LEFT($C{r},LEN(scope_HTS))=scope_HTS))>0,"Y","N"))', "TIM Calc", 10),
    ("HTS on exclusion list (Y/N)",
     '=IF($A{r}="","",IF(SUMPRODUCT((excl_HTS<>"")*(LEFT($C{r},LEN(excl_HTS))=excl_HTS))>0,"Y","N"))', "TIM Calc", 10),
    ("Origin on scope list (Y/N)",
     '=IF($A{r}="","",IF($E{r}="","N",IF(COUNTIF(scope_COO,$E{r})>0,"Y","N")))', "TIM Calc", 10),
    ("USMCA exempt (Y/N)",
     '=IF($A{r}="","",IF(AND(UPPER(TRIM(act_USMCAExempt&""))="Y",UPPER(TRIM(Items!F{r}&""))="Y"),"Y","N"))',
     "TIM Calc", 10),
    ("Research determination",
     '=IF($A{r}="","",IFERROR(UPPER(TRIM(INDEX(det_Status,MATCH($A{r},det_Item,0))&"")),""))', "TIM Calc", 12),
    ("In scope (Y/N)",
     '=IF($A{r}="","",IF($K{r}="IN","Y",IF($K{r}="OUT","N",'
     'IF(AND($F{r}="Y",$G{r}="Y",$H{r}="N",$I{r}="Y",$J{r}="N"),"Y","N"))))', "TIM Calc", 9),
    ("Scope reason",
     '=IF($A{r}="","",IF($K{r}="IN","In: Research determination",IF($K{r}="OUT","Out: Research determination",'
     'IF($F{r}="N","Out: different import country",IF($G{r}="N","Out: HTS not on scope list",'
     'IF($H{r}="Y","Out: HTS on exclusion list",IF($I{r}="N","Out: origin not on scope list",'
     'IF($J{r}="Y","Out: USMCA-qualifying, exempt","In: matches scope rules"))))))))', "TIM Calc", 28),
    ("Current duty rate", '=IF($A{r}="","",N(Items!I{r}))', "TIM Calc Pct", 10),
    ("New duty rate",
     '=IF($A{r}="","",IF($L{r}="Y",$N{r}+N(act_Rate)-IF(UPPER(TRIM(act_RateType&""))="REPLACE",N(act_PriorRate),0),$N{r}))',
     "TIM Calc Pct", 10),
    ("Duty per unit before", '=IF($A{r}="","",N(Items!G{r})*$N{r})', "TIM Calc Unit", 11),
    ("Duty per unit after", '=IF($A{r}="","",N(Items!G{r})*$O{r})', "TIM Calc Unit", 11),
    ("Landed cost change per unit", '=IF($A{r}="","",$Q{r}-$P{r})', "TIM Calc Unit", 11),
    ("Est. new standard cost per unit", '=IF($A{r}="","",N(Items!J{r})+$R{r})', "TIM Calc Unit", 12),
    ("Margin % before",
     '=IF($A{r}="","",IF(N(Items!K{r})=0,"",(N(Items!K{r})-N(Items!J{r}))/N(Items!K{r})))', "TIM Calc Pct", 10),
    ("Margin % after",
     '=IF($A{r}="","",IF(N(Items!K{r})=0,"",(N(Items!K{r})-$S{r})/N(Items!K{r})))', "TIM Calc Pct", 10),
    ("Margin change (points)", '=IF(OR($T{r}="",$U{r}=""),"",$U{r}-$T{r})', "TIM Calc Pct", 10),
    ("Annual quantity", '=IF($A{r}="","",N(Items!H{r}))', "TIM Calc Whole", 11),
    ("Annual impact (change x quantity)", '=IF($A{r}="","",$R{r}*$W{r})', "TIM Calc Money", 13),
    ("Annual revenue", '=IF($A{r}="","",N(Items!K{r})*$W{r})', "TIM Calc Money", 13),
    ("Annual margin $ before", '=IF($A{r}="","",(N(Items!K{r})-N(Items!J{r}))*$W{r})', "TIM Calc Money", 13),
    ("Annual margin $ after", '=IF($A{r}="","",$Z{r}-$X{r})', "TIM Calc Money", 13),
    ("Data check",
     '=IF($A{r}="","",IF(TRIM(Items!C{r}&"")="","CHECK: import country missing",'
     'IF(OR(LEN($C{r})<>10,ISERROR(VALUE($C{r}))),"CHECK: HTS must be 10 digits",'
     'IF(LEN($E{r})<>2,"CHECK: origin code missing or not 2 letters",'
     'IF(OR(Items!G{r}="",Items!I{r}="",Items!J{r}=""),"CHECK: value, rate or cost missing",'
     'IF(ISNUMBER(Items!G{r})*ISNUMBER(Items!I{r})*ISNUMBER(Items!J{r})=0,"CHECK: text in a number column",'
     'IF(AND($L{r}="Y",UPPER(TRIM(act_RateType&""))="REPLACE",$N{r}<N(act_PriorRate)),'
     '"CHECK: current rate is below the rate being replaced",'
     'IF(AND($L{r}="Y",$W{r}=0),"NOTE: in scope, no volume","OK"))))))))', "TIM Calc", 30),
    ("Rank key (helper for Summary top 10)",
     '=IF($A{r}="","",IF(AND($L{r}="Y",$X{r}<>0),ABS($X{r})+ROW()/1000000000,""))', "TIM Calc Key", 12),
]


def build_calc(wb):
    ws = wb.create_sheet("Calc")
    title(ws, "Calc: formulas only (do not type on this tab)",
          "Row n here is row n on Items. Grey = formula. Scope rules come from the Action tab; values come from the Items tab.")
    headers(ws, 4, 1, [h for h, *_ in CALC_COLUMNS])
    for c, (_, formula, style, width) in enumerate(CALC_COLUMNS, 1):
        letter = get_column_letter(c)
        ws.column_dimensions[letter].width = width
        for r in range(FIRST, LAST + 1):
            put(ws, f"{letter}{r}", formula.format(r=r), style)
    ws.conditional_formatting.add(f"L{FIRST}:L{LAST}", FormulaRule(formula=[f'$L{FIRST}="Y"'], fill=GREEN))
    ws.conditional_formatting.add(f"AB{FIRST}:AB{LAST}", FormulaRule(formula=[f'LEFT($AB{FIRST},5)="CHECK"'], fill=RED))
    ws.conditional_formatting.add(f"AB{FIRST}:AB{LAST}", FormulaRule(formula=[f'LEFT($AB{FIRST},4)="NOTE"'], fill=AMBER))
    ws.row_dimensions[4].height = 45
    ws.freeze_panes = "B5"
    ws.auto_filter.ref = f"A4:{get_column_letter(len(CALC_COLUMNS))}{LAST}"
    ws.sheet_properties.tabColor = "7F7F7F"


# ----------------------------------------------------------------- Summary ----

def build_summary(wb):
    ws = wb.create_sheet("Summary")
    title(ws, "Summary: what the action does to cost and margin (formulas only, except yellow chapter list)",
          "Send nothing from here until B24 reads YES and the Review tab shows a checker sign-off for this version.")
    rng = lambda col: f"Calc!${col}${FIRST}:${col}${LAST}"  # noqa: E731
    headers(ws, 4, 1, ["Measure", "Value", "How it is calculated"])
    kpis = [
        ("Action ID", "=act_ID&\"\"", "TIM Calc", "Action tab"),
        ("Action name", "=act_Name&\"\"", "TIM Calc", "Action tab"),
        ("Importing country", "=act_Country&\"\"", "TIM Calc", "Action tab"),
        ("Effective date", "=act_EffDate", "TIM Calc Date", "Action tab"),
        ("Additional duty rate", "=act_Rate", "TIM Calc Pct", "Action tab"),
        ("Brief ID and version", "=act_Brief&\"\"", "TIM Calc", "Action tab"),
        ("Items in model", f'=SUMPRODUCT(--({rng("A")}<>""))', "TIM Calc Whole", "Rows on Items with an item number"),
        ("Items in scope", f'=COUNTIF({rng("L")},"Y")', "TIM Calc Whole", "Calc column L = Y"),
        ("Research determinations applied",
         f'=COUNTIF({rng("K")},"IN")&" IN, "&COUNTIF({rng("K")},"OUT")&" OUT"', "TIM Calc",
         "Items matched to the determinations list on Action"),
        ("In-scope items with no volume", f'=COUNTIFS({rng("L")},"Y",{rng("W")},0)', "TIM Calc Whole",
         "Listed, but they add 0 to the totals. Get a volume or state why none"),
        ("Rows with a CHECK flag", f'=SUMPRODUCT(--(LEFT({rng("AB")},5)="CHECK"))', "TIM Calc Whole",
         "Must be 0 before review"),
        ("Annual impact, in-scope items", f'=SUMIFS({rng("X")},{rng("L")},"Y")', "TIM Calc Money",
         "Sum of landed cost change x annual quantity"),
        ("Annual revenue, in-scope items", f'=SUMIFS({rng("Y")},{rng("L")},"Y")', "TIM Calc Money",
         "Sell price x annual quantity"),
        ("Margin % before, in-scope items", f'=IF(B17=0,"",SUMIFS({rng("Z")},{rng("L")},"Y")/B17)',
         "TIM Calc Pct", "Revenue-weighted"),
        ("Margin % after, in-scope items", f'=IF(B17=0,"",SUMIFS({rng("AA")},{rng("L")},"Y")/B17)',
         "TIM Calc Pct", "Revenue-weighted"),
        ("Margin change (points)", '=IF(B17=0,"",B19-B18)', "TIM Calc Pct", "After minus before"),
        ("Action tab complete?",
         '=IF(AND(act_ID&""<>"",act_Country&""<>"",act_Brief&""<>"",ISNUMBER(act_EffDate),ISNUMBER(act_Rate),'
         'act_RateType&""<>"",act_USMCAExempt&""<>"",SUMPRODUCT(--(scope_HTS<>""))>0,'
         'SUMPRODUCT(--(scope_COO<>""))>0),"YES","NO")', "TIM Calc",
         "Required fields and at least one HTS prefix and one origin"),
        ("Origin table reconciles?", '=IF(ABS(C49-B16)<0.005,"YES","NO")', "TIM Calc",
         "Origin table total equals the annual impact"),
        ("Chapter table reconciles?", '=IF(ABS(C64)<0.005,"YES","NO: add the missing chapter")', "TIM Calc",
         "Nothing left in 'Other chapters'"),
        ("Ready for checker review?", '=IF(AND(B21="YES",B15=0,B22="YES",B23="YES"),"YES","NO")', "TIM Calc",
         "All four checks above pass"),
    ]
    for i, (label, formula, style, how) in enumerate(kpis):
        r = FIRST + i
        put(ws, f"A{r}", label, "TIM Label")
        put(ws, f"B{r}", formula, style)
        put(ws, f"C{r}", how, "TIM Note")
    assert FIRST + len(kpis) - 1 == 24
    for ref in ("B21", "B22", "B23", "B24"):
        ws.conditional_formatting.add(ref, FormulaRule(formula=[f'{ref}="YES"'], fill=GREEN))
        ws.conditional_formatting.add(ref, FormulaRule(formula=[f'LEFT({ref},2)="NO"'], fill=RED))
    ws.conditional_formatting.add("B15", FormulaRule(formula=["B15>0"], fill=RED))

    # By country of origin: rows follow the origin list on the Action tab (first 20 entries).
    put(ws, "A26", "By country of origin (in-scope items)", "TIM Section")
    headers(ws, 27, 1, ["Origin (from Action list)", "Items in scope", "Annual impact", "Share of impact"])
    for i in range(20):
        r = 28 + i
        put(ws, f"A{r}", f'=IF(Action!$M${FIRST + i}="","",UPPER(TRIM(Action!$M${FIRST + i}&"")))', "TIM Calc")
        put(ws, f"B{r}", f'=IF(A{r}="","",COUNTIFS({rng("E")},A{r},{rng("L")},"Y"))', "TIM Calc Whole")
        put(ws, f"C{r}", f'=IF(A{r}="","",SUMIFS({rng("X")},{rng("E")},A{r},{rng("L")},"Y"))', "TIM Calc Money")
        put(ws, f"D{r}", f'=IF(OR(A{r}="",$B$16=0),"",C{r}/$B$16)', "TIM Calc Pct")
    put(ws, "A48", "Other origins (Research IN determinations)", "TIM Label")
    put(ws, "B48", "=B12-SUM(B28:B47)", "TIM Calc Whole")
    put(ws, "C48", "=B16-SUM(C28:C47)", "TIM Calc Money")
    put(ws, "D48", '=IF($B$16=0,"",C48/$B$16)', "TIM Calc Pct")
    put(ws, "A49", "Total", "TIM Label")
    put(ws, "B49", "=SUM(B28:B48)", "TIM Calc Whole")
    put(ws, "C49", "=SUM(C28:C48)", "TIM Calc Money")
    put(ws, "D49", '=IF($B$16=0,"",C49/$B$16)', "TIM Calc Pct")

    # By HTS chapter: yellow list of chapters (text), plus an 'Other' row that must be zero.
    put(ws, "A51", "By HTS chapter (in-scope items). Type each chapter in scope as 2 digits", "TIM Section")
    headers(ws, 52, 1, ["HTS chapter (2 digits)", "Items in scope", "Annual impact", "Share of impact"])
    for i in range(10):
        r = 53 + i
        put(ws, f"A{r}", None, "TIM Input Text")
        put(ws, f"B{r}", f'=IF(A{r}="","",COUNTIFS({rng("D")},A{r}&"",{rng("L")},"Y"))', "TIM Calc Whole")
        put(ws, f"C{r}", f'=IF(A{r}="","",SUMIFS({rng("X")},{rng("D")},A{r}&"",{rng("L")},"Y"))', "TIM Calc Money")
        put(ws, f"D{r}", f'=IF(OR(A{r}="",$B$16=0),"",C{r}/$B$16)', "TIM Calc Pct")
    ws["A53"].value = "73"
    put(ws, "A63", "Other chapters (must be 0)", "TIM Label")
    put(ws, "B63", "=B12-SUM(B53:B62)", "TIM Calc Whole")
    put(ws, "C63", "=B16-SUM(C53:C62)", "TIM Calc Money")
    put(ws, "D63", '=IF($B$16=0,"",C63/$B$16)', "TIM Calc Pct")
    put(ws, "A64", "Check: Other chapters impact", "TIM Label")
    put(ws, "C64", "=C63", "TIM Calc Money")
    ws.conditional_formatting.add("B63:C63", FormulaRule(formula=["ABS($C$63)>=0.005"], fill=RED))
    length_dv(ws, "A53:A62", 2, "Type the chapter as 2 digits, for example 73 or 08.")

    # Top 10 by absolute annual impact (ties broken by row, so every item appears once).
    put(ws, "A66", "Top 10 in-scope items by size of annual impact", "TIM Section")
    headers(ws, 67, 1, ["Rank", "Item", "Description", "Origin", "HTS digits", "Annual impact",
                        "Change per unit", "Margin % after", "Rank key (helper)"])
    key_rng = rng("AC")
    for k in range(1, 11):
        r = 67 + k
        put(ws, f"A{r}", k, "TIM Calc Whole")
        put(ws, f"I{r}", f'=IF(COUNT({key_rng})<A{r},"",LARGE({key_rng},A{r}))', "TIM Calc Key")
        for col, src, style in (("B", "A", "TIM Calc"), ("C", "B", "TIM Calc"), ("D", "E", "TIM Calc"),
                                ("E", "C", "TIM Calc"), ("F", "X", "TIM Calc Money"),
                                ("G", "R", "TIM Calc Unit"), ("H", "U", "TIM Calc Pct")):
            put(ws, f"{col}{r}", f'=IF($I{r}="","",INDEX({rng(src)},MATCH($I{r},{key_rng},0)))', style)

    widths(ws, {"A": 40, "B": 22, "C": 46, "D": 14, "E": 13, "F": 14, "G": 13, "H": 12, "I": 13})
    ws.freeze_panes = "A4"
    ws.sheet_properties.tabColor = "548235"
    ws.page_setup.orientation = "landscape"
    ws.page_setup.fitToWidth, ws.page_setup.fitToHeight = 1, 0
    ws.sheet_properties.pageSetUpPr.fitToPage = True


# ------------------------------------------------------------------ Review ----

REVIEW_HEADERS = ["Version", "Date", "Maker (name, track, what was prepared)", "Checker", "What the checker compared",
                  "Findings", "Findings closed? (Y/N)", "Decision", "Released to", "Release date"]
SAMPLE_REVIEWS = [
    ("v1.0 (SAMPLE)", dt.date(2027, 2, 18), "Hire A, Research: Action tab", "Senior",
     "Action tab against brief v1.0: every HTS prefix, exclusion, origin, rate, date and determination",
     "SAMPLE: stacking note reworded to quote the brief; closed", "Y", "Approved for release", "Standard Cost (Hire B)",
     dt.date(2027, 2, 18)),
    ("v1.1 (SAMPLE)", dt.date(2027, 2, 19), "Hire B, Standard Cost: Items, Summary", "Manager",
     "Item count and totals against the extract; 3 items recalculated by hand; Summary B24 = YES",
     "SAMPLE: none", "Y", "Approved for release", "[COMPANY: Pricing lead], Finance", dt.date(2027, 2, 19)),
]
CHECKLIST = [
    "Version on this tab = Action B23 = file name",
    "Brief version on Action matches the checked brief",
    "Every HTS prefix, exclusion and origin traced to the brief",
    "Rate, rate type, effective date and USMCA rule match the brief",
    "Item count on Items = extract row count",
    "No CHECK flags (Summary B15 = 0)",
    "3 items recalculated by hand to $0.01",
    "Top 10 items make business sense",
    "Origin and chapter tables reconcile",
    "No typed numbers over grey formula cells",
    "Out-of-scope reasons spot-checked (5 rows)",
    "Limits stated in the covering note",
]


def build_review(wb):
    ws = wb.create_sheet("Review")
    title(ws, "Review: maker-checker sign-off log",
          "One line per review. The maker fills columns A-C; the checker fills D-H. Nothing is released without a line here.",
          "SAMPLE lines below are FICTIONAL. Delete them before real use.")
    headers(ws, 4, 1, REVIEW_HEADERS)
    styles = ["TIM Input Text", "TIM Input Date", "TIM Input", "TIM Input", "TIM Input", "TIM Input",
              "TIM Input Text", "TIM Input", "TIM Input", "TIM Input Date"]
    for r in range(FIRST, 45):
        for c, style in enumerate(styles, 1):
            put(ws, f"{get_column_letter(c)}{r}", None, style)
    for i, row in enumerate(SAMPLE_REVIEWS):
        for c, v in enumerate(row, 1):
            ws.cell(row=FIRST + i, column=c).value = v
    list_dv(ws, ["Y", "N"], "G5:G44")
    list_dv(ws, ["Approved for release", "Approved with changes", "Returned to maker"], "H5:H44")
    number_dv(ws, "date", "B5:B44", 36526, 73051, "Enter a date (yyyy-mm-dd).")
    number_dv(ws, "date", "J5:J44", 36526, 73051, "Enter a date (yyyy-mm-dd).")

    headers(ws, 4, 12, ["Checker checklist (each review)", "Done (Y/N)"])
    for i, item in enumerate(CHECKLIST):
        put(ws, f"L{FIRST + i}", item, "TIM Text")
        put(ws, f"M{FIRST + i}", None, "TIM Input Text")
    list_dv(ws, ["Y", "N"], f"M{FIRST}:M{FIRST + len(CHECKLIST) - 1}")
    widths(ws, {"A": 13, "B": 11, "C": 30, "D": 12, "E": 40, "F": 34, "G": 10, "H": 20, "I": 22, "J": 11,
                "K": 2, "L": 46, "M": 10})
    ws.row_dimensions[4].height = 32
    ws.freeze_panes = "A5"
    ws.sheet_properties.tabColor = "7030A0"


# ------------------------------------------------------------------- write ----

FIXED_ZIP_TIME = (2026, 10, 8, 0, 0, 0)
FIXED_ISO = TEMPLATE_DATE.strftime("%Y-%m-%dT%H:%M:%SZ")


def make_deterministic(src, dst):
    """Rewrite the xlsx zip with fixed timestamps so identical input gives identical bytes."""
    with zipfile.ZipFile(src) as zin:
        entries = [(info.filename, zin.read(info.filename)) for info in zin.infolist()]
    dst.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(dst, "w", compression=zipfile.ZIP_DEFLATED) as zout:
        for fname, data in entries:
            if fname == "docProps/core.xml":
                text = data.decode("utf-8")
                text = re.sub(r"(<dcterms:(created|modified)[^>]*>)[^<]*(</dcterms:\2>)",
                              lambda m: m.group(1) + FIXED_ISO + m.group(3), text)
                data = text.encode("utf-8")
            info = zipfile.ZipInfo(fname, date_time=FIXED_ZIP_TIME)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o600 << 16
            zout.writestr(info, data)


def build(out):
    wb = Workbook()
    add_styles(wb)
    build_readme(wb)
    build_action(wb)
    build_items(wb)
    build_calc(wb)
    build_summary(wb)
    build_review(wb)
    wb.calculation.fullCalcOnLoad = True
    wb.properties.creator = "BSA Manager"
    wb.properties.title = "Tariff-Impact Model (template)"
    wb.properties.created = TEMPLATE_DATE
    wb.properties.modified = TEMPLATE_DATE
    wb.properties.lastModifiedBy = "build/make_tariff_model.py"
    with tempfile.TemporaryDirectory() as tmp:
        raw = Path(tmp) / "raw.xlsx"
        wb.save(raw)
        make_deterministic(raw, out)
    return out


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--out", type=Path, default=DEFAULT_OUT, help="output .xlsx path")
    args = parser.parse_args()
    out = build(args.out.resolve())
    try:
        shown = out.relative_to(ROOT)
    except ValueError:
        shown = out
    print(f"tariff model: {shown}")


if __name__ == "__main__":
    main()
