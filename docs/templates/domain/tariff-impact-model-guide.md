# Tariff-Impact Model Guide

Last updated: 2026-10-08 · Owner: BSA Manager

- **Purpose:** explains the shared Tariff-Impact Model (`dist/Tariff-Impact-Model-Template.xlsx`) tab by tab and formula by formula, the workflow between Research and Standard Cost, how to check it, and what it cannot do. Read it before you put a number from the model in front of anyone.
- **Who uses it:** Hire A (Research) fills the Action tab, the WHAT. Hire B (Standard Cost) fills the Items tab and owns the $ results. The Senior checks the Action tab; the Manager checks the $ and approves release.
- **When:** for every tariff action that needs a cost or margin answer. Pre-read in W2 (Mon 10/26). Joint tariff drill in W7 and W8 (Hire A scopes, Hire B models, maker-checker demo). Evidence for B60-1, and for A90-1 and B90-1 when a live action arrives. Modules M5R and M5C.

## What the model is, in one paragraph

One workbook per tariff action and importing country. Research copies the checked Tariff-Impact Brief (`docs/templates/domain/tariff-impact-brief.md`) into the Action tab: rate, dates, HTS scope list, exclusions, origins and item-level determinations. Standard Cost pastes an item extract into the Items tab: HTS, origin, customs value, volume, current duty rate, current standard cost and sell price. The Calc tab decides, row by row, whether each item is in scope and works out the duty change, the new estimated standard cost and the margin change. The Summary tab totals it by origin and HTS chapter and lists the top 10 items. The Review tab is the maker-checker log. Every result is a live formula, so a change on Action or Items flows through at once.

## Workflow

| Step | Who | Tab | What to do | Done when |
|---|---|---|---|---|
| 1 Copy | Hire A, at intake | All | Copy the template to [COMPANY: tariff model folder] as `TIM_[Action ID]_[import country]_v0.1.xlsx`. Link it on both Jira stories. Delete the SAMPLE rows on Action, Items and Review | One linked file; no email copies |
| 2 Fill the WHAT | Hire A (maker) | Action | Fill column B, the HTS scope list, the exclusion list, the origin list and the determinations list from the checked brief | Summary B21 reads YES |
| 3 Check the WHAT | Senior or Manager | Action, Review | Compare every Action entry with the brief and its sources. Log the review | Review line with "Approved for release" |
| 4 Fill the $ inputs | Hire B (maker) | Items | Paste the extract as values. Record the extract source and date in column L | Item count = extract row count |
| 5 Clear the checks | Hire B | Calc, Summary | Fix every CHECK in Calc column AB. Explain each NOTE | Summary B15 = 0 and B24 = YES |
| 6 Sense-check | Hire B | Summary | Explain the top 10 and the origin and chapter totals in one line each | Covering note drafted |
| 7 Check the $ | Manager | All, Review | Recalculate 3 items by hand, confirm counts and totals against the extract, run the Review checklist | Review line with "Approved for release" |
| 8 Release | Manager approves | Summary | Send the Summary with a covering note that states the brief version, the volume basis and the limits | Sent; filed on the Jira epic |
| 9 Change | Whoever changes it | Review | Any change after a sign-off: new version number, new review line | Versions match on Action B23, Review and file name |

Boundary rule: Standard Cost never edits the Action tab, and Research never edits the Items tab. If Hire B thinks an item is wrongly in or out of scope, Hire B comments on the Research story; Hire A decides and, if needed, adds an item-level determination on the Action tab and re-releases the brief.

## Colours and conventions

- **Yellow cells are inputs.** Grey cells are formulas: never type over them. Formula cells carry named styles that start with "TIM Calc"; input cells use styles that start with "TIM Input".
- Header rows are frozen on every data tab. Items and Calc have filters on the header row.
- Data validation guards the inputs: lists for country, Y/N, ADD/REPLACE, IN/OUT and review decisions; 2-letter length for origin codes; ranges for rates, values, quantities and dates.
- Item numbers, HTS numbers and origin codes are stored as text. Paste them into cells already formatted as text, or with Paste Special > Values, so Excel does not drop leading zeros.
- Rates are percentages: 25% is stored as 0.25. Type `25%`, not `25`.
- Tab colours: grey for README and Calc, blue for Action (Research), orange for Items (Standard Cost), green for Summary, purple for Review.

## Tab by tab

### README

How to use the workbook, the colour key, the maker-checker rule, the limits and the template version. Nothing on it is used by formulas.

### Action (Research, the WHAT)

Fields in column B (rows 5 to 23). Each has a workbook-level defined name, so formulas read `act_Rate` instead of `Action!$B$15`.

| Cell | Field | Name | Used by formulas? | Notes |
|---|---|---|---|---|
| B5 | Action ID | act_ID | Summary | Same ID as the Jira label and the file name |
| B6 | Action name | act_Name | Summary | Plain-language name |
| B7 | Importing country | act_Country | Calc F | US, CA or MX. One model per importing country |
| B8 | Legal authority category | act_Authority | No | From the list |
| B9 | Brief ID and version | act_Brief | Summary | Must be a checked version |
| B10 | Primary legal source | act_Source | No | Citation |
| B11 | Effective date | act_EffDate | Summary | Shown, not applied (see limits) |
| B12 | Effective time and basis | act_Basis | No | Quote from the brief |
| B13 | In-transit provision | act_InTransit | No | Not applied |
| B14 | End date | act_EndDate | No | Not applied |
| B15 | Additional duty rate | act_Rate | Calc O | Ad valorem, % of customs value |
| B16 | Rate change type | act_RateType | Calc O, AB | ADD or REPLACE |
| B17 | Earlier rate being replaced | act_PriorRate | Calc O, AB | REPLACE only |
| B18 | USMCA-qualifying goods exempt? | act_USMCAExempt | Calc J | Y, N or N/A |
| B19 | Stacking interpretation | act_Stacking | No | Text from the brief |
| B20 to B22 | Research maker, checker, date checked | act_Maker, act_Checker, act_Checked | No | Who checked the brief |
| B23 | Model version | act_ModelVersion | No | Matches Review and the file name |

Lists (rows 5 to 54, all with their header on row 4):

| Columns | List | Name used by formulas | How to fill it |
|---|---|---|---|
| E to G | In-scope HTS prefixes | scope_HTS (column F) | One prefix per row exactly as the annex writes it (4, 6, 8 or 10 digits, dots allowed). Column F strips dots, spaces and hyphens: `=IF(TRIM(E5&"")="","",SUBSTITUTE(SUBSTITUTE(SUBSTITUTE(TRIM(E5&""),".","")," ",""),"-",""))` |
| I to K | Excluded HTS prefixes | excl_HTS (column J) | Same rules. Only exclusions defined by HTS go here |
| M to N | Origins in scope | scope_COO (column M) | 2-letter ISO codes, one per row |
| P to S | Item-level determinations | det_Item (P), det_Status (Q) | Items Research has decided by hand: IN or OUT, with the reason and the brief section. Use it for exclusions written as product descriptions, borderline items and "does not apply when another action applies" cases |

A determination overrides the rules for that item. Use it sparingly and always with a reason a checker can verify.

### Items (Standard Cost, the $ inputs)

One row per item and import country, rows 5 to 254. Source: [COMPANY: Oracle cost extract or warehouse query].

| Column | Field | Rules |
|---|---|---|
| A | Item number | Text. Must match the Action determinations list exactly |
| B | Description | Free text |
| C | Import country | US, CA or MX |
| D | HTS | 10 digits as text; dots allowed |
| E | Country of origin | 2-letter ISO code from the classification master, not the supplier address |
| F | USMCA qualifying | Y only where a current certification supports the claim |
| G | Unit customs value | The duty base per unit for that import country, in the model currency ([COMPANY: model currency]) |
| H | Annual quantity | The volume basis agreed for this model (for example the next 12 months' forecast). State the basis in column L |
| I | Current duty rate | All duties now paid on the item as % of customs value (base rate plus any additional duties already in force) |
| J | Current standard cost per unit | From Oracle; assumed to include duty at the current rate |
| K | Sell price per unit | From [COMPANY: price list source]; blank if not sold |
| L | Source and notes | Extract name and run date; anything unusual |

The 13 SAMPLE rows are synthetic: invented items, values, rates, costs and prices. The first 6 HTS digits are real HS subheadings; the last 4 digits are made up. XX and XY are ISO user-assigned codes standing for fictional Countries X and Y.

### Calc (formulas only)

Row n on Calc reads row n on Items. Every formula starts with `IF($A5="","",...)` so empty rows stay blank and do not count in totals. The formulas below are for row 5.

**Identification**

- **A Item number:** `=IF(TRIM(Items!A5&"")="","",TRIM(Items!A5&""))`. Copies the item number as trimmed text, so numeric and text item numbers both match the determinations list.
- **B Description:** `=IF($A5="","",Items!B5&"")`.
- **C HTS digits:** `=IF($A5="","",SUBSTITUTE(SUBSTITUTE(SUBSTITUTE(TRIM(Items!D5&""),".","")," ",""),"-",""))`. HTS as digits only, as text.
- **D HTS chapter:** `=IF($A5="","",LEFT($C5,2))`. First 2 digits, as text.
- **E Origin:** `=IF($A5="","",UPPER(TRIM(Items!E5&"")))`.

**Scope tests (each returns Y or N)**

- **F Import country matches:** `=IF($A5="","",IF(UPPER(TRIM(Items!C5&""))=UPPER(TRIM(act_Country&"")),"Y","N"))`.
- **G HTS on scope list:** `=IF($A5="","",IF(SUMPRODUCT((scope_HTS<>"")*(LEFT($C5,LEN(scope_HTS))=scope_HTS))>0,"Y","N"))`. For every prefix on the list, it takes as many leading digits of the item's HTS as the prefix has and compares them. One match is enough. Blank list rows are ignored by the `(scope_HTS<>"")` term. SUMPRODUCT handles the list without array entry, in both Excel and LibreOffice.
- **H HTS on exclusion list:** the same test against `excl_HTS`.
- **I Origin on scope list:** `=IF($A5="","",IF($E5="","N",IF(COUNTIF(scope_COO,$E5)>0,"Y","N")))`. A blank origin is never in scope (and is flagged in AB).
- **J USMCA exempt:** `=IF($A5="","",IF(AND(UPPER(TRIM(act_USMCAExempt&""))="Y",UPPER(TRIM(Items!F5&""))="Y"),"Y","N"))`. Y only when the action exempts USMCA-qualifying goods and the item is flagged qualifying.
- **K Research determination:** `=IF($A5="","",IFERROR(UPPER(TRIM(INDEX(det_Status,MATCH($A5,det_Item,0))&"")),""))`. IN, OUT or blank, looked up with INDEX/MATCH.
- **L In scope:** `=IF($A5="","",IF($K5="IN","Y",IF($K5="OUT","N",IF(AND($F5="Y",$G5="Y",$H5="N",$I5="Y",$J5="N"),"Y","N"))))`. A determination wins. Otherwise the item is in scope only if all five tests pass: right import country, HTS on the scope list, not excluded, origin listed, not USMCA-exempt.
- **M Scope reason:** a nested IF that names the first reason that applies, in this order: Research determination, different import country, HTS not on scope list, HTS on exclusion list, origin not on scope list, USMCA-qualifying exempt, otherwise "In: matches scope rules". Filter on it when you review.

**Duty, cost and margin**

- **N Current duty rate:** `=IF($A5="","",N(Items!I5))`. `N()` turns blanks and text into 0 so the arithmetic never errors; AB flags those rows.
- **O New duty rate:** `=IF($A5="","",IF($L5="Y",$N5+N(act_Rate)-IF(UPPER(TRIM(act_RateType&""))="REPLACE",N(act_PriorRate),0),$N5))`. In scope with ADD: current + additional. In scope with REPLACE: current + new rate - earlier rate of the same action. Out of scope: unchanged.
- **P Duty per unit before:** `=IF($A5="","",N(Items!G5)*$N5)`. Customs value x current rate.
- **Q Duty per unit after:** `=IF($A5="","",N(Items!G5)*$O5)`.
- **R Landed cost change per unit:** `=IF($A5="","",$Q5-$P5)`. Only the duty changes (see limits).
- **S Estimated new standard cost per unit:** `=IF($A5="","",N(Items!J5)+$R5)`. Current standard plus the change. An estimate for decisions, not the Oracle load value: the cost update follows `docs/templates/domain/standard-cost-update-checklist.md`.
- **T Margin % before:** `=IF($A5="","",IF(N(Items!K5)=0,"",(N(Items!K5)-N(Items!J5))/N(Items!K5)))`. Blank when there is no sell price.
- **U Margin % after:** `=IF($A5="","",IF(N(Items!K5)=0,"",(N(Items!K5)-$S5)/N(Items!K5)))`. Assumes the sell price does not change.
- **V Margin change:** `=IF(OR($T5="",$U5=""),"",$U5-$T5)`. Percentage points, displayed with a % format (-14.2% means 14.2 points lower).

**Annual figures**

- **W Annual quantity:** `=IF($A5="","",N(Items!H5))`.
- **X Annual impact:** `=IF($A5="","",$R5*$W5)`. Landed cost change x annual quantity.
- **Y Annual revenue:** `=IF($A5="","",N(Items!K5)*$W5)`.
- **Z Annual margin $ before:** `=IF($A5="","",(N(Items!K5)-N(Items!J5))*$W5)`.
- **AA Annual margin $ after:** `=IF($A5="","",$Z5-$X5)`.

**Controls**

- **AB Data check:** returns the first problem found, in this order: "CHECK: import country missing"; "CHECK: HTS must be 10 digits" (also catches a lost leading zero or letters); "CHECK: origin code missing or not 2 letters"; "CHECK: value, rate or cost missing"; "CHECK: text in a number column"; "CHECK: current rate is below the rate being replaced" (REPLACE only: the item's current rate cannot contain the earlier rate, so the new rate would be understated); "NOTE: in scope, no volume". Otherwise "OK". CHECK rows turn red and NOTE rows amber. Every CHECK must be cleared before review. A NOTE needs a one-line explanation in the covering note.
- **AC Rank key:** `=IF($A5="","",IF(AND($L5="Y",$X5<>0),ABS($X5)+ROW()/1000000000,""))`. The size of the annual impact plus a tiny row-based amount so two items with the same impact still get different ranks. Used only by the Summary top 10.

### Summary (formulas only, except the yellow chapter list)

| Cell | Measure | Formula idea |
|---|---|---|
| B5 to B10 | Action ID, name, importing country, effective date, rate, brief version | Read from the Action tab |
| B11 | Items in model | `=SUMPRODUCT(--(Calc!$A$5:$A$254<>""))` |
| B12 | Items in scope | `=COUNTIF(Calc!$L$5:$L$254,"Y")` |
| B13 | Research determinations applied | Counts of IN and OUT in Calc column K |
| B14 | In-scope items with no volume | `=COUNTIFS(Calc!$L$5:$L$254,"Y",Calc!$W$5:$W$254,0)` |
| B15 | Rows with a CHECK flag | `=SUMPRODUCT(--(LEFT(Calc!$AB$5:$AB$254,5)="CHECK"))`. Must be 0 |
| B16 | Annual impact, in-scope items | `=SUMIFS(Calc!$X$5:$X$254,Calc!$L$5:$L$254,"Y")` |
| B17 | Annual revenue, in-scope items | SUMIFS on Calc column Y |
| B18, B19 | Margin % before and after, in-scope items | Annual margin $ (Calc Z or AA, SUMIFS on in-scope) divided by B17: revenue-weighted |
| B20 | Margin change | B19 - B18, in points |
| B21 | Action tab complete? | YES when the required Action fields are filled and there is at least one HTS prefix and one origin |
| B22 | Origin table reconciles? | YES when the origin table total (C49) equals B16 |
| B23 | Chapter table reconciles? | YES when "Other chapters" (C63) is zero |
| B24 | Ready for checker review? | YES when B21, B22 and B23 are YES and B15 is 0 |

- **By country of origin (rows 28 to 49).** Column A copies the first 20 origins from the Action list. Items and impact use `COUNTIFS` and `SUMIFS` on Calc columns E (origin) and L (in scope = Y). Row 48 "Other origins" catches in-scope items whose origin is not on the list, which can only happen through an IN determination.
- **By HTS chapter (rows 53 to 64).** Type each chapter in scope as 2 digits in the yellow cells (the sample has 73). Row 63 "Other chapters" is what is left over and must be 0; if not, a chapter is missing from the list.
- **Top 10 (rows 68 to 77).** Column I takes the k-th largest rank key with `LARGE`; columns B to H look the row up with `INDEX/MATCH` on the rank key. Ranked by size of impact, so a duty decrease (negative impact) ranks by its size too.

### Review (maker-checker log)

One line per review: version, date, maker (name, track, what was prepared), checker, what the checker compared, findings, findings closed (Y/N), decision (Approved for release, Approved with changes, Returned to maker), released to, release date. The checklist in columns L and M is run at every review. The maker never fills the checker columns. The same details also go on the Jira story, as the control rule in `docs/01-30-60-90-plan.md` requires.

## Sample results (check your understanding)

With the template as delivered (FICTIONAL action: additional 25% ad valorem, ADD, origin XX, scope prefix 7318, exclusion 7318.24, SAMPLE-005 determined OUT), the expected results are (verified by recalculating in LibreOffice and by hand):

| Item | In scope? | Scope reason | Change per unit | Annual impact |
|---|---|---|---|---|
| SAMPLE-001 | Y | Matches scope rules | 4.20 x 25% = 1.0500 | 1.05 x 120,000 = 126,000.00 |
| SAMPLE-002 | Y | Matches scope rules (HTS pasted without dots) | 0.85 x 25% = 0.2125 | 85,000.00 |
| SAMPLE-003 | Y | Matches scope rules | 0.12 x 25% = 0.0300 | 27,000.00 |
| SAMPLE-004 | N | HTS on exclusion list (7318.24) | 0 | 0 |
| SAMPLE-005 | N | Research determination | 0 | 0 |
| SAMPLE-006 to 009 | N | Origin not on scope list (XY, MX, MX, CA) | 0 | 0 |
| SAMPLE-010, 011 | N | HTS not on scope list (7326, 8481) | 0 | 0 |
| SAMPLE-012 | Y | Matches scope rules; NOTE: no volume | 0.0125 | 0 |
| SAMPLE-013 | N | Different import country (CA) | 0 | 0 |

Totals: 13 items, 4 in scope, annual impact 238,000.00, in-scope revenue 1,724,000.00, margin 34.0% before and 20.2% after (-13.8 points), Summary B24 = YES. SAMPLE-001 check by hand: duty before 4.20 x 5% = 0.21; after 4.20 x 30% = 1.26; new standard 4.95 + 1.05 = 6.00; margin before (7.40 - 4.95) / 7.40 = 33.1%; after (7.40 - 6.00) / 7.40 = 18.9%.

## Drills (do them on a copy)

**Drill 1: USMCA exemption.** On Action, add MX to the origin list (M6) and set B18 to Y. Expected: SAMPLE-007 (MX, USMCA Y) stays out with "Out: USMCA-qualifying, exempt"; SAMPLE-008 (MX, USMCA N) comes in: new rate 30%, change 2.30 x 25% = 0.5750 per unit, annual impact 23,000.00. Totals: 5 in scope, 261,000.00; the origin table shows XX 238,000.00 and MX 23,000.00.

**Drill 2: rate increase on an existing action.** Reset the copy. Set B16 to REPLACE and B17 to 10%, then set SAMPLE-001's current rate (Items I5) to 15% (a 5% base rate plus the earlier 10%). Expected: SAMPLE-001 new rate 15% + 25% - 10% = 30%, change 4.20 x 15% = 0.6300, annual 75,600.00. SAMPLE-002, 003 and 012 show "CHECK: current rate is below the rate being replaced", because their current rates (0%) cannot contain the earlier 10%, and B24 reads NO. Lesson: with REPLACE, the current rate on Items must already include the earlier rate, and the check will tell you when it does not.

**Drill 3: break it on purpose.** On three different sample rows: type the HTS 303899001 (a chapter 03 code that lost its leading zero); delete an origin code; and type `1.50 USD` in a unit customs value cell. Validation should stop the last one, which is the first control. Now paste `1.50 USD` from a text cell instead: pasting bypasses validation, and Calc column AB catches it. Each row shows a different CHECK, and Summary B15 counts them. Then undo.

## Extending the template

- **More than 250 items or 50 list rows:** change `ITEM_ROWS` or `LIST_ROWS` in `build/make_tariff_model.py` and rebuild with `python3 build/make_tariff_model.py`. The defined names, Summary ranges, validation and formats all follow. This is the preferred route, because the Manager owns the template.
- **In a copy, by hand (only if you cannot rebuild):** copy the last Items and Calc rows down, then edit every `$5:$254` range on Summary (B11 to B19, the origin and chapter tables, the top 10) and the defined names (Formulas > Name Manager in Excel; Sheet > Named Ranges and Expressions > Manage in LibreOffice). Ask the checker to re-verify the totals.
- **Two actions on the same items:** build one model per action. Once the first action is in effect, its rate becomes part of the current rate on Items for the second model. To show the combined effect of two actions that have not yet started, put the first action's rate in the current rate column of the second model, and say so in the covering note.
- **Template changes:** raise them with the Manager. Change the generator, rebuild, and bump `TEMPLATE_VERSION`. Never fix a formula in one copy only.

## Limits (state them in every covering note)

- **Ad valorem only.** Specific and compound rates (per kg, per unit, per litre) need an ad valorem equivalent per item, agreed with Research and the checker, entered as the rate.
- **Duty only.** Landed cost change = duty change. Customs fees such as US MPF (ad valorem with per-entry limits), freight, brokerage and supplier prices are assumed unchanged. Duty-based import taxes (Canada GST, Mexico IVA) are left out because they are normally recoverable; confirm with Finance.
- **Full-year view.** The annual impact applies the action to a full year of the Items volume. The model does not apply the effective date, end date, in-transit relief, stock already on hand or timing within a cost period. Standard Cost handles those in the cost update and the PPV explanation.
- **Customs value is an input.** The model does not build the duty base. Each import country has its own valuation rules (see `docs/primers/customs-trade-compliance-primer.md`).
- **Current rate and standard cost are trusted as given.** If the current standard does not include duty at the current rate, the new standard estimate is wrong.
- **One currency.** All values on Items must be in the same currency ([COMPANY: model currency]).
- **No AD/CVD by producer.** AD/CVD rates vary by producer and exporter; model them only with item-level rates that Research supplies.
- **No legal judgement.** The model applies the scope it is given. Scope comes only from the checked brief.

## Common mistakes

- Typing over a grey formula to "fix" a number. Fix the input or ask the Manager.
- Pasting HTS or item numbers as numbers. Leading zeros vanish and matches fail. AB flags HTS problems; item number mismatches show as determinations not applied (Summary B13).
- Using the supplier's country instead of the country of origin.
- Leaving the SAMPLE rows in a real model.
- Releasing a version that has no checker line on the Review tab, or whose version differs from Action B23.
- Emailing the file. Link the one copy on Jira instead.

## Excel and LibreOffice notes

- The formulas avoid dynamic arrays, LET, LAMBDA, XLOOKUP, IFS and wildcard criteria, so they work in Excel 2010 and later and in LibreOffice Calc. The template was recalculated in LibreOffice 24.2 with no errors, and the sample results above were checked by hand. Open it once in your Excel version before first real use and confirm the sample totals match.
- Excel recalculates the whole workbook when the file opens. If Excel opens it in Protected View, click Enable Editing so the formulas calculate.
- In LibreOffice, if values look stale, use Data > Calculate > Recalculate Hard.
- Pasting from another workbook can bring in its styles and names. Use Paste Special > Values.
