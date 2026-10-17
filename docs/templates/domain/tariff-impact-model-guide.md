# Tariff-Impact Model Guide

Last updated: 2026-10-17 · Owner: BSA Manager

- **Purpose:** explains the shared Tariff-Impact Model (Tariff-Impact-Model-Template.xlsx in the onboarding folder, template v2.0) tab by tab and formula by formula, the workflow between Research and Standard Cost, how to check it, and what it cannot do. Read it before you put a number from the model in front of anyone.
- **Who uses it:** Hire A (Research) fills the Action tab, the WHAT. Hire B (Standard Cost) fills the Items tab and owns the $ results. The Senior checks the Action tab; the Manager checks the $ and approves release.
- **When:** for every tariff action that needs a cost or margin answer. Pre-read in W2 (Mon 10/26). Joint tariff drill in W7 and W8 (Hire A scopes, Hire B models, maker-checker demo). Evidence for B60-1, and for A90-1 and B90-1 when a live action arrives. Modules M5R and M5C. For a live action, the urgency rule in `docs/01-30-60-90-plan.md` ("Live tariff actions during training") decides who is maker.

## What the model is, in one paragraph

Watch first: the 2-minute video *From a tariff action to a cost impact: the Research to Standard Cost handoff* — [COMPANY: Stream link].

One workbook per tariff action and importing country. Research copies the checked Tariff-Impact Brief (`docs/templates/domain/tariff-impact-brief.md`) into the Action tab: rates, dates, the HTS scope list, exclusions, origins, item-level determinations and, when the action has more than one rate, the rate lines. Standard Cost pastes an item extract into the Items tab: HTS, origin, unit of measure, customs value, quantity, current duty rate, current standard cost, sell price and, for actions that tax only part of the value, each item's dutiable share. The Calc tab decides, row by row, whether each item is in scope, which rate applies, and works out the duty change, the new estimated standard cost and the margin change. The Summary tab totals it, lists the top 10 items, breaks it down by HTS chapter and origin, and says whether the model is ready for review. The Review tab is the maker-checker log. Every result is a live formula, so a change on Action or Items flows through at once.

## Workflow

| Step | Who | Tab | What to do | Done when |
|---|---|---|---|---|
| 1 Copy | Hire A, at intake; Hire B the same day | All | Hire A copies the template to [COMPANY: tariff model folder] as `TIM_[Action ID]_[import country]_v0.1.xlsx`, links it on both Jira stories, and clears the SAMPLE rows on Action and Review. Hire B clears the Items SAMPLE rows and the sample chapter on Summary (A47). Select, press Delete; never delete rows | One linked file; no email copies; no SAMPLE rows left |
| 2 Fill the WHAT | Hire A (maker) | Action | Fill column B, the HTS scope list, the exclusion list, the origin list, the determinations and any rate lines from the checked brief | Summary B26 and B27 read YES. Until Items is loaded, Action column W shows WAIT (amber) instead of OK |
| 3 Check the WHAT | Senior or Manager | Action, Review | Compare every Action entry with the brief and its sources. Log the review | Review line with "Approved for release" |
| 4 Fill the $ inputs | Hire B (maker) | Items | Set the quantity period and currency (K1, K2). Paste the extract as values, one row per item and import country, all per the Oracle primary unit of measure. Record the source and date in column N | Item count = extract row count |
| 5 Clear the checks | Hire B; Hire A for Action | Calc, Summary | Fix every CHECK in Calc column AJ that comes from the Items data. Explain each NOTE. Raise every CHECK that comes from the Action tab on the Research story: Action F, J, W (including "no Items row" after the paste) or AI, a NO in B26, and the rate and scope CHECKs in AJ. Hire A corrects or removes the Action entry; Hire B never edits Action | Summary B19 = 0 and B30 = YES |
| 6 Sense-check | Hire B | Summary | Explain the top 10 and the origin and chapter totals in one line each | Covering note drafted |
| 7 Check the $ | Manager | All, Review | Recalculate 3 items by hand, confirm counts and totals against the extract, run the Review checklist | Review line with "Approved for release" |
| 8 Release | Manager approves | Summary | Send the Summary with a covering note that states the brief version, the quantity period and basis, and the limits | Sent; filed on the Jira epic |
| 9 Change | Whoever changes it | Review | Any change after a sign-off: new version number, new review line | Versions match on Action B24, Review and file name |

Boundary rule: Research decides scope (which items are in or out, and why), rates, duty base rules and stacking. Standard Cost never decides scope: it computes the $ on Research's determinations. Standard Cost never edits the Action tab, and never works around it on Items (for example by blanking an origin or changing an HTS to push an item out). Research never edits the Items tab. If Hire B thinks an item is wrongly in or out of scope, or a rate looks wrong, Hire B comments on the Research story; Hire A decides and, if needed, changes the Action tab and re-releases the brief.

## Colours, protection and conventions

- **Yellow cells are inputs.** Grey cells are formulas. Input cells use named styles that start with "TIM Input"; formula cells use styles that start with "TIM Calc".
- **Every tab is protected without a password.** Only yellow cells can change, and rows and columns cannot be inserted or deleted, because that would break the row-by-row link between Items and Calc. Items allows sort and filter; Calc allows filter. Unprotect a tab (Review > Unprotect Sheet in Excel; Tools > Protect Sheet in LibreOffice) only with the Manager's agreement, and protect it again before review.
- Header rows are frozen on every data tab. Items and Calc have filters on the header row.
- Data validation guards the inputs: lists for country, Y/N, ADD/REPLACE, USMCA treatment, FULL/PART, IN/OUT and review decisions; 2-letter length for origin codes; ranges for rates, shares, values, quantities and dates. Pasting bypasses validation, so the formulas re-check what a paste can break: Action columns F and J (HTS prefixes), W (determinations) and AI (rate lines), Summary B26 (column B and the origin list) and Calc column AJ (the Items data).
- **Pasted text is cleaned before it is compared.** Leading and trailing spaces, non-breaking spaces (character 160, common in text copied from web pages and PDFs) and non-printing characters are removed, and codes are compared in capitals. So `XX `, ` xx` and XX followed by a non-breaking space all match XX, and IN, OUT, Y, N, ADD, REPLACE, FULL and PART are read the same way. A space inside a code is not removed: `X X` is 3 characters and raises a CHECK or a NO.
- Item numbers, HTS numbers and origin codes are stored as text. Paste with Paste Special > Values, so Excel keeps leading zeros and the cells keep their input format (a normal paste can also bring in the source cell's locked setting).
- Rates and shares are percentages: 25% is stored as 0.25. Type `25%`, not `25`.
- Tab colours: grey for README and Calc, blue for Action (Research), orange for Items (Standard Cost), green for Summary, purple for Review.

## Tab by tab

### README

How to use the workbook, the colour key, protection, the maker-checker rule, the limits and the template version. Nothing on it is used by formulas.

### Action (Research, the WHAT)

Fields in column B, rows 5 to 24. Each has a workbook-level defined name, so formulas read `act_Rate` instead of `Action!$B$15`.

| Cell | Field | Name | Used by formulas? | Notes |
|---|---|---|---|---|
| B5 | Action ID | act_ID | Summary | Same ID as the brief, the file name and the Jira story |
| B6 | Action name | act_Name | Summary | Plain-language name |
| B7 | Importing country | act_Country | Calc F; Action W | US, CA or MX (B26 checks it). One model per importing country |
| B8 | Legal authority category | act_Authority | No | From the list |
| B9 | Brief ID and version | act_Brief | Summary | Must be a checked version |
| B10 | Primary legal source | act_Source | No | Citation |
| B11 | Effective date | act_EffDate | Summary | Shown, not applied (see limits) |
| B12 | Effective time and basis | act_Basis | No | Quote from the brief |
| B13 | In-transit provision | act_InTransit | No | Not applied |
| B14 | End date | act_EndDate | No | Not applied |
| B15 | Default additional rate | act_Rate | Calc R | Applies to in-scope items that match no rate line. Blank = every in-scope item must match a rate line |
| B16 | Rate change type | act_RateType | Calc S | ADD or REPLACE, for B15 and for every rate line with AD blank (B26 checks it) |
| B17 | Default earlier rate replaced | act_PriorRate | Calc S | REPLACE only |
| B18 | USMCA-qualifying goods | act_USMCAExempt | Calc J | Y (exempt), PARTIAL, N or N/A (B26 checks it) |
| B19 | Stacking interpretation | act_Stacking | No | Quoted from brief 6.6 |
| B20 | Duty base for the default rate | act_DefaultBase | Calc P | FULL, PART or blank (= FULL; B26 checks it) |
| B21 to B23 | Research maker, checker, date checked | act_Maker, act_Checker, act_Checked | No | Who checked the brief |
| B24 | Model version | act_ModelVersion | No | Matches Review and the file name |

Lists (all start on row 5, header on row 4):

| Columns | List | Names used by formulas | How to fill it |
|---|---|---|---|
| E to H | In-scope HTS prefixes (300 rows) | scope_HTS (F), scope_Group (H) | One prefix per row exactly as the annex writes it (4, 6, 8 or 10 digits, dots allowed). Column F strips dots, spaces (normal and non-breaking) and hyphens. It also flags a result that is not 2, 4, 6, 8 or 10 digits, which catches a footnote number copied as a plain digit (`7318 1` gives 73181) and a prefix pasted as a number that lost its leading zero (`0303.89` gives 30389). If anything else is left (a letter, a footnote marker such as `1/`), or the result is not 2, 4, 6, 8 or 10 digits, F shows "CHECK: not 2, 4, 6, 8 or 10 digits" in red, the prefix matches nothing, and B26 reads NO. Column H, the rate group, is needed only when rate lines differ by product list: use the brief's Chapter 99 heading or annex name (for example `9903.XX.01`) |
| I to K | Excluded HTS prefixes (300 rows) | excl_HTS (J) | Same rules. Only exclusions defined by HTS go here |
| M to N | Origins in scope (50 rows) | scope_COO (M) | 2-letter ISO codes, one per row, each once. B26 reads NO if a code is not 2 letters after cleaning. For an action on all origins, list every origin in your candidate query (brief Part 9) |
| P to W | Item-level determinations (100 rows) | det_Key (V), det_Status (R), det_Displaced (S), det_Check (W) | Item number and import country; IN, OUT or blank; any other duty the action switches off on that item; the reason and brief section. V and W are formulas |
| Y to AI | Rate lines (30 rows) | rate_ID (Y), rate_Group (Z), rate_COO (AA), rate_USMCA (AB), rate_Rate (AC), rate_Prior (AD), rate_Base (AE), rate_Displaced (AF), rate_Check (AI) | One row per brief Part 7 line that differs from B15. AH (items using the line) and AI (check) are formulas |

#### Rate lines: several rates in one action

Most actions have one rate: put it in B15 and leave the rate lines empty. When brief Part 7 has more than one rate line (for example a different rate for one origin, a second annex, or relief for USMCA-qualifying goods), give each extra line a row:

- **Line ID** (Y): the brief's line number, for example `R2`. Must be unique.
- **Keys** (Z, AA, AB): rate group (from the scope list), origin, and USMCA-qualifying (Y = only qualifying items, N = only non-qualifying, blank = either). A blank key matches everything. A line matches an in-scope item when all its filled keys match.
- **Rate, earlier rate, base, displaced duty** (AC to AF): the additional rate; the earlier rate of this action that the line replaces (next bullet); FULL or PART (blank = FULL); any other duty this line switches off (see stacking below).
- **Adds or replaces** (brief Part 7, "Adds to or replaces"): B16 and B17 apply to B15 and to every line with AD blank. A line that replaces an earlier rate of this action gets that rate in AD, whatever B16 says. A line that only adds while B16 is REPLACE gets 0% in AD. With REPLACE, an in-scope item that finds no earlier rate (no AD on its line and no B17) is a CHECK in Calc AJ, and B26 reads NO when there is no earlier rate anywhere.

When more than one line matches an item, the most specific wins: a line that names the origin beats one that names the USMCA status, which beats one that names only the rate group. A line with no keys matches every in-scope item. An in-scope item that matches no line takes B15. Two matching lines with the same keys are a CHECK, because the model cannot choose. If the instrument's precedence differs from this order, add a more specific line (for example origin plus rate group) and say so in the brief.

Column AI checks each line: ID missing; rate missing or outside 0% to 1000%; ID listed twice; rate group not on the scope list; origin not on the origin list; USMCA not Y, N or blank; duty base not FULL, PART or blank; earlier or displaced rate not a number. A rate above 100% is an amber NOTE (was `25` pasted instead of `25%`?). Column AH counts the in-scope items that use the line; a line used by 0 items is not an error, but the checker asks why.

#### Item-level determinations

Use them for exclusions written as product descriptions, borderline items, and items whose stacking differs from the rest. Each row is keyed by item number AND import country, and both are cleaned and upper-cased before matching, so a trailing space pasted from the brief does not break the match.

- **IN or OUT** (R) overrides the HTS, exclusion, origin and USMCA tests, but never the import-country test: an IN determination cannot pull a Canadian row into a US model.
- **Blank** (R) leaves scope to the rules. Use it to record only a displaced duty (S).
- **Check** (W) must read OK. It flags, in this order: an import country that is not B7; a row listed twice; a determination other than IN, OUT or blank (a pasted `EXCLUDED` would otherwise be ignored and the scope rules would decide); a displaced rate that is not a number; a row with neither a determination nor a displaced rate; and, once Items has rows, a row with no matching Items row. Until Items has rows, W shows "WAIT: Items not loaded yet" in amber, which B27 does not count. Summary B15 counts the rows listed; B27 is NO while any row shows a CHECK.

A determination is per item, while many exclusions are per entry ("accompanied by a certificate"). An item certified on only some shipments cannot be OUT: keep it IN (as in brief example Q2). If Research can state the certified share of the volume from a source, Research records it in the brief, names two model rows with distinct item numbers (for example ITEM-123-CERT and ITEM-123-NOCERT) and lists them on the Action tab as OUT and IN. Standard Cost enters those two Items rows with the quantity split as the brief states it, explained in column N. Two rows with the same item number and import country are a duplicate CHECK. SAMPLE-005 is OUT because its supplier certifies every shipment.

#### Duty base and partial USMCA relief

- **FULL** (the default) applies the rate to the whole unit customs value.
- **PART** applies it to a share of the customs value only, for example the value of the metal content or the non-US content. Set B20 (default rate) or the rate line's column AE to PART. Research states the rule and the source of the share in brief Part 7; Standard Cost enters each item's share on Items column M from that source and notes it in column N; the checker traces the shares. A PART item with no share is a CHECK; a share entered on a FULL item is also a CHECK.
- **USMCA treatment (B18).** Y = USMCA-qualifying items are out of scope. PARTIAL = they stay in scope and get relief through a rate line with USMCA = Y: either a lower rate, or a PART base for the non-US content. B26 is NO if B18 is PARTIAL and no such line exists. N = no relief. N/A = no USMCA-party origin in scope.

#### Stacking: duties the action switches off

Some actions say another additional duty no longer applies to the goods they cover (a non-stacking rule, brief 6.6). The new duty is added and the other one is removed. Two ways to enter the removed duty, as % of the full customs value:

- **Per rate line** (column AF), when every item on that line pays the other duty at the same rate, for example all goods of one origin.
- **Per item** (determinations column S), when only some items pay it. The item value wins over the line value.

The removed duty must already be inside the item's current rate on Items (column J). If it is not, Calc shows "CHECK: current rate is below the duty being replaced or displaced". Use B19 for the quoted interaction text. Duties that simply add on top need nothing: the default is ADD.

### Items (Standard Cost, the $ inputs)

Settings at the top: K1 is the quantity period label (Annual by default; for example Q2 2027 or Remaining 2027), shown on the Summary. K2 is the currency of every value on the tab ([COMPANY: model currency]).

One row per item and import country, rows 5 to 254. Source: [COMPANY: Oracle cost extract or warehouse query].

| Column | Field | Rules |
|---|---|---|
| A | Item number | Text. Matched to the determinations after trimming |
| B | Description | Free text |
| C | Import country | US, CA or MX |
| D | HTS | 10 digits as text; dots allowed |
| E | Country of origin | 2-letter ISO code from the classification master, not the supplier address |
| F | USMCA qualifying | Y only where a current certification supports the claim, and only for origins US, CA or MX |
| G | Unit of measure | The Oracle primary unit of measure. H, I, K and L must all be per this unit |
| H | Unit customs value | The duty base per unit for that import country. Convert a value per customs or invoice unit (per box, per dozen, per kg) to the Oracle primary unit before pasting, and record the conversion in column N |
| I | Quantity for the period | In the unit in G, for the period in K1. State the basis in column N (for example the next 12 months' forecast) |
| J | Current duty rate | All duties now paid on the item as % of customs value (base rate plus any additional duties already in force, including any the action will displace) |
| K | Current standard cost | From Oracle, per unit in G; assumed to include duty at the current rate |
| L | Sell price | Per unit in G, from [COMPANY: price list source]. Blank if not sold: the item still counts in the impact but not in the margin % |
| M | Dutiable share | PART-base items only: the share of customs value the action taxes, from the source Research names. Blank = 100% |
| N | Source and notes | Extract name and run date; conversions; anything unusual |

**Same-unit rule.** Customs value, quantity, standard cost and sell price must be in the same unit, the Oracle primary unit of measure in column G. A mismatch multiplies the duty change by the pack size. Calc flags a missing unit (CHECK) and an in-scope customs value above the standard cost (NOTE), which is the usual sign of a unit mismatch.

**Several Oracle organizations.** The standard cost extract has one row per item and organization. The model needs one row per item and import country, and a duplicate row is a CHECK because it would count the impact twice. Either build one model per organization, or aggregate first: quantities summed, customs value and standard cost weighted by quantity. Say which in column N.

The 14 SAMPLE rows are synthetic: invented items, values, rates, costs and prices. The first 6 HTS digits are real HS subheadings; the last 4 digits are made up. XX and XY are ISO user-assigned codes standing for fictional Countries X and Y.

### Calc (formulas only)

Row n on Calc reads row n on Items. Every formula starts with `IF($A5="","",...)` (or returns 0 for helpers) so empty rows stay blank and do not count in totals. The formulas below are for row 5; columns AL to AQ are helpers.

Shorthand: where a formula below shows `tidy(x)`, the workbook has `TRIM(CLEAN(SUBSTITUTE(x&"",[NBSP]," ")))`, where [NBSP] is the non-breaking space character itself, between quotes. It looks like a normal space in the formula bar. The formulas use the character rather than `CHAR(160)` because CHAR reads the computer's own character set, so it returns a different character on a Mac and in some LibreOffice settings. Codes and keys are compared as `UPPER(tidy(x))`.

**Identification**

- **A Item number:** `=IF(tidy(Items!A5)="","",tidy(Items!A5))`. Cleaned text, so numeric and text item numbers both match.
- **B Description:** `=IF($A5="","",Items!B5&"")`.
- **C HTS digits:** `=IF($A5="","",SUBSTITUTE(SUBSTITUTE(SUBSTITUTE(SUBSTITUTE(CLEAN(Items!D5&""),[NBSP],""),".","")," ",""),"-",""))`. Dots, spaces, non-breaking spaces and hyphens removed; AJ checks that exactly 10 digits are left.
- **D HTS chapter:** `=IF($A5="","",LEFT($C5,2))`.
- **E Origin:** `=IF($A5="","",UPPER(tidy(Items!E5)))`.

**Scope tests (each returns Y or N)**

- **F Import country matches:** `=IF($A5="","",IF(UPPER(tidy(Items!C5))=UPPER(tidy(act_Country)),"Y","N"))`.
- **G HTS on scope list:** `=IF($A5="","",IF($AM5>0,"Y","N"))`. AM is the scope match score (below).
- **H HTS on exclusion list:** `=IF($A5="","",IF(SUMPRODUCT((excl_HTS<>"")*(LEFT($C5,LEN(excl_HTS))=excl_HTS))>0,"Y","N"))`. For every prefix on the list, it compares that many leading digits of the item's HTS. One match is enough. SUMPRODUCT handles the list without array entry, in Excel and LibreOffice.
- **I Origin on scope list:** `=IF($A5="","",IF($E5="","N",IF(SUMPRODUCT(--(UPPER(tidy(scope_COO))=$E5))>0,"Y","N")))`. The origin list is cleaned the same way, so `XX ` on the list still matches XX.
- **J USMCA exempt:** `=IF($A5="","",IF(AND(UPPER(tidy(act_USMCAExempt))="Y",UPPER(tidy(Items!F5))="Y"),"Y","N"))`. Only when B18 = Y.
- **K Research determination:** `=IF($A5="","",IF($AQ5=0,"",UPPER(tidy(INDEX(det_Status,$AQ5)))))`. IN, OUT or blank, from the determination row found in AQ. Any other value is ignored here, and Action W shows a CHECK for it.
- **L In scope:** `=IF($A5="","",IF($F5="N","N",IF($K5="IN","Y",IF($K5="OUT","N",IF(AND($G5="Y",$H5="N",$I5="Y",$J5="N"),"Y","N")))))`. The import country is tested first. Then a determination wins. Otherwise the item is in scope only if it is on the scope list, not excluded, from a listed origin and not USMCA-exempt.
- **M Scope reason:** names the first reason that applies, in this order: different import country, Research determination (IN or OUT), HTS not on scope list, HTS on exclusion list, origin not on scope list, USMCA-qualifying exempt, otherwise "In: matches scope rules". Filter on it when you review.

**Which rate applies**

- **N Rate group:** `=IF(OR($A5="",$AM5=0),"",UPPER(tidy(INDEX(scope_Group,MOD($AM5,1000)))))`. The group of the longest scope prefix that matches the item.
- **O Rate line used:** the matching line's ID, or "Default (B15)" when no line matches. Blank when out of scope.
- **P Duty base:** FULL or PART, from the line (column AE) or from B20.
- **Q Current duty rate:** `=IF($A5="","",N(Items!J5))`. `N()` turns blanks and text into 0 so the arithmetic never errors; AJ flags those rows.
- **R Additional rate:** the line's rate (AC) or B15; 0 when out of scope.
- **S Earlier rate replaced:** the line's AD when it holds a number (whatever B16 says); otherwise B17 when B16 is REPLACE; otherwise 0. Items on B15 take B17 when B16 is REPLACE.
- **T Dutiable share applied:** `=IF($A5="","",IF(AND($L5="Y",$P5="PART",ISNUMBER(Items!M5)),Items!M5,1))`.
- **U Other duty displaced:** the item's determination value (S) if there is one, otherwise the line's AF, otherwise 0.

**Duty, cost and margin**

- **V New duty rate:** `=IF($A5="","",IF($L5="Y",$Q5+$T5*($R5-$S5)-$U5,$Q5))`. In scope: current rate, plus the share times (additional rate minus any earlier rate it replaces), minus any duty it displaces. Out of scope: unchanged. It is a rate on the full customs value.
- **W Duty per unit before:** `=IF($A5="","",N(Items!H5)*$Q5)`.
- **X Duty per unit after:** `=IF($A5="","",N(Items!H5)*$V5)`.
- **Y Landed cost change per unit:** `=IF($A5="","",$X5-$W5)`. Only the duty changes (see limits).
- **Z Estimated new standard cost per unit:** `=IF($A5="","",N(Items!K5)+$Y5)`. An estimate for decisions, not the Oracle load value: the cost update follows `docs/templates/domain/standard-cost-update-checklist.md`.
- **AA Margin % before:** `=IF($A5="","",IF(N(Items!L5)=0,"",(N(Items!L5)-N(Items!K5))/N(Items!L5)))`. Blank when there is no sell price.
- **AB Margin % after:** `=IF($A5="","",IF(N(Items!L5)=0,"",(N(Items!L5)-$Z5)/N(Items!L5)))`. Assumes the sell price does not change.
- **AC Margin change:** `=IF(OR($AA5="",$AB5=""),"",$AB5-$AA5)`. Percentage points, displayed with a % format (-14.2% means 14.2 points lower).

**Figures for the period**

- **AD Quantity:** `=IF($A5="","",N(Items!I5))`.
- **AE Impact:** `=IF($A5="","",$Y5*$AD5)`. Change per unit x quantity. Counts every item, priced or not.
- **AF Has a sell price:** `=IF($A5="","",IF(N(Items!L5)>0,"Y","N"))`.
- **AG Revenue:** `=IF($A5="","",IF($AF5="Y",N(Items!L5)*$AD5,0))`.
- **AH Margin $ before:** `=IF($A5="","",IF($AF5="Y",(N(Items!L5)-N(Items!K5))*$AD5,0))`. 0 for items with no sell price, so they cannot drag the margin % down.
- **AI Margin $ after:** `=IF($A5="","",IF($AF5="Y",$AH5-$AE5,0))`.

**Controls**

- **AJ Data check:** returns the first problem found, in this order. CHECKs: duplicate item and import country; import country missing; import country must be US, CA or MX; HTS must be 10 digits (also catches a lost leading zero, letters or other characters); origin code missing or not 2 letters; unit of measure missing; value, rate or cost missing; text in a number column (H, J, K, and I, L, M when filled); dutiable share must be 0% to 100% (catches `40` pasted for 40%); USMCA flag must be Y, N or blank; USMCA flag on an origin other than US, CA or MX; in scope but no rate; REPLACE but no earlier rate (B17 or the rate line's AD); two rate lines match equally; HTS prefix listed twice on the scope list; dutiable share missing (PART base); dutiable share entered, but the rate taxes the full value; current rate is below the duty being replaced or displaced. NOTEs: in scope, no quantity; in scope, no sell price; customs value above standard cost (check unit of measure); current rate above 100% (check it was entered as a percentage). Otherwise "OK". Who clears them: Hire B fixes the Items data; the rate and scope CHECKs (no rate, REPLACE without an earlier rate, two lines match, prefix listed twice) come from the Action tab and go to Research (workflow step 5). CHECK rows turn red and NOTE rows amber. Every CHECK must be cleared before review. A NOTE needs a one-line explanation in the covering note.
- **AK Rank key:** `=IF($A5="","",IF(AND($L5="Y",$AE5<>0),ABS($AE5)+ROW()/1000000000,""))`. The size of the impact plus a tiny row-based amount so equal impacts still rank separately. Used only by the Summary top 10.

**Helpers (AL to AQ)**

- **AL Key:** `=IF($A5="","",UPPER($A5)&"/"&UPPER(tidy(Items!C5)))`, for example `SAMPLE-001/US`. Determinations use the same key (Action V).
- **AM Scope match score:** `=IF($A5="",0,SUMPRODUCT(MAX((scope_HTS<>"")*(LEFT($C5,LEN(scope_HTS))=scope_HTS)*(LEN(scope_HTS)*1000+ROW(scope_HTS)-4))))`. For the longest matching prefix: its length x 1000 plus its row on the list. 0 = no match. SUMPRODUCT makes MAX work on the list without array entry.
- **AN Scope ties:** how many matching prefixes have that length (more than 1 means the same prefix is listed twice).
- **AO Rate line score:** for the best matching rate line: its specificity (1, plus 1 for a rate group, 2 for a USMCA status and 4 for an origin) x 100, plus its row on the list. 0 = no line matches, so B15 applies. The line keys (Z, AA, AB) are compared as `UPPER(tidy(...))`, so a pasted space cannot switch a line off.
- **AP Rate line ties:** how many matching lines have that specificity (more than 1 is a CHECK).
- **AQ Determination row:** `=IF($A5="",0,IFERROR(MATCH($AL5,det_Key,0),0))`.

### Summary (formulas only, except the yellow chapter list)

| Cell | Measure | Formula idea |
|---|---|---|
| B5 to B12 | Action ID, name, importing country, effective date, default rate, number of rate lines, brief version, quantity period | Read from Action and Items K1 |
| B13 | Items in model | `=SUMPRODUCT(--(Calc!$A$5:$A$254<>""))` |
| B14 | Items in scope | `=COUNTIF(Calc!$L$5:$L$254,"Y")` |
| B15 | Research determinations listed | Rows on the Action determinations list |
| B16 | Research determinations applied | IN and OUT counts in Calc K, and in-scope items with a displaced duty (Calc U) |
| B17, B18 | In-scope items with no quantity; without a sell price | COUNTIFS on Calc L with AD = 0, or AF = N |
| B19 | Rows with a CHECK flag | `=SUMPRODUCT(--(LEFT(Calc!$AJ$5:$AJ$254,5)="CHECK"))`. Must be 0 |
| B20 | Impact for the period, in-scope items | `=SUMIFS(Calc!$AE$5:$AE$254,Calc!$L$5:$L$254,"Y")`. The label shows the period from Items K1 |
| B21 | Of which: items without a sell price | Same, with Calc AF = N |
| B22 | Revenue, in-scope items with a sell price | SUMIFS on Calc AG |
| B23, B24 | Margin % before and after, in-scope items with a sell price | Calc AH or AI (SUMIFS on in-scope) divided by B22: revenue-weighted, unpriced items excluded from both sides |
| B25 | Margin change | B24 - B23, in points |
| B26 | Action tab complete? | YES, or "NO:" and the first problem, checked in this order: B5 missing; B7 not US, CA or MX; B9 or B11 missing; B15 not a percentage from 0% to 1000%; no rate (B15 or a rate line); B16 not ADD or REPLACE; B17 not a number; REPLACE with no earlier rate anywhere (B17 or AD); B18 not Y, PARTIAL, N or N/A; B20 not FULL, PART or blank; no HTS prefix, or a prefix in F or J that is not 2, 4, 6, 8 or 10 digits; no origin, or an origin that is not a 2-letter code; PARTIAL with no USMCA = Y rate line |
| B27 | Determinations and rate lines check out? | No CHECK on Action columns W and AI: every determination valid and, once Items is loaded, matched to one Items row of this import country |
| B28 | Origin table reconciles? | YES when the origin table totals (B113 and C113) equal B14 and B20 |
| B29 | Chapter table reconciles? | YES when "Other chapters" (B57 and C57) is zero: no in-scope item, even one with no impact, is missing from the chapter list |
| B30 | Ready for checker review? | YES when Items has rows (B13 > 0), B26 to B29 are YES and B19 is 0 |

- **Top 10 (rows 34 to 43).** Column I takes the k-th largest rank key with `LARGE`; columns B to H look the row up with `INDEX/MATCH`. Ranked by size of impact, so a duty decrease (negative impact) ranks by its size too. Column E shows the rate line used.
- **By HTS chapter (rows 46 to 57).** Type each chapter in scope as 2 digits in the yellow cells A47 to A56 (the sample has 73). Row 57 "Other chapters" is what is left over: both the count and the $ must be 0; if not, a chapter is missing from the list.
- **By country of origin (rows 62 to 113).** One row per row of the Action origin list (all 50). Row 112 "Other origins" is computed directly: in-scope items whose origin is not on the list, which can only happen through an IN determination. Row 113 adds the rows up: the count must equal B14 and the $ must equal B20. It fails if an origin is listed twice on Action, because that origin is then counted twice.

### Review (maker-checker log)

One line per review: version, date, maker (name, track, what was prepared), checker, what the checker compared, findings, findings closed (Y/N), decision (Approved for release, Approved with changes, Returned to maker), released to, release date. The checklist in columns L and M is run at every review. The maker never fills the checker columns. When the checker approves with changes, the checker confirms the changes in the released version and records that version. The same details also go on the Jira story, as the control rule in `docs/01-30-60-90-plan.md` requires.

## Sample results (check your understanding)

With the template as delivered (FICTIONAL action: additional 25% ad valorem, ADD, full customs value, origin XX, scope prefix 7318, exclusion 7318.24, SAMPLE-005 determined OUT, SAMPLE-003 paying a FICTIONAL 10% duty that the action displaces), the expected results are (verified by recalculating in LibreOffice and by hand):

| Item | In scope? | Scope reason | Change per unit | Annual impact |
|---|---|---|---|---|
| SAMPLE-001 | Y | Matches scope rules | 4.20 x 25% = 1.0500 | 1.05 x 120,000 = 126,000.00 |
| SAMPLE-002 | Y | Matches scope rules (HTS pasted without dots) | 0.85 x 25% = 0.2125 | 85,000.00 |
| SAMPLE-003 | Y | Matches scope rules; 10% displaced | 0.12 x (25% - 10%) = 0.0180 | 16,200.00 |
| SAMPLE-004 | N | HTS on exclusion list (7318.24) | 0 | 0 |
| SAMPLE-005 | N | Research determination | 0 | 0 |
| SAMPLE-006 to 009 | N | Origin not on scope list (XY, MX, MX, CA) | 0 | 0 |
| SAMPLE-010, 011 | N | HTS not on scope list (7326, 8481) | 0 | 0 |
| SAMPLE-012 | Y | Matches scope rules; NOTE: no quantity | 0.0125 | 0 |
| SAMPLE-013 | N | Different import country (CA) | 0 | 0 |
| SAMPLE-014 | Y | Matches scope rules; NOTE: no sell price | 0.50 x 25% = 0.1250 | 1,250.00 |

Totals: 14 items, 5 in scope, impact 228,450.00 (of which 1,250.00 on the unpriced SAMPLE-014), in-scope revenue 1,724,000.00, margin 33.5% before and 20.3% after (-13.2 points), Summary B30 = YES.

By hand, SAMPLE-001: duty before 4.20 x 5% = 0.21; after 4.20 x 30% = 1.26; new standard 4.95 + 1.05 = 6.00; margin before (7.40 - 4.95) / 7.40 = 33.1%; after (7.40 - 6.00) / 7.40 = 18.9%. SAMPLE-003: current rate 10% (0% base plus the FICTIONAL 10%); new rate 10% + 25% - 10% = 25%; duty 0.012 before and 0.030 after; new standard 0.16 + 0.018 = 0.178; margin 33.3% before and 25.8% after.

## Drills (do them on a copy, starting each from the delivered sample)

**Drill 1: USMCA exemption.** On Action, add MX to the origin list (M6) and set B18 to Y. Expected: SAMPLE-007 (MX, USMCA Y) stays out with "Out: USMCA-qualifying, exempt"; SAMPLE-008 (MX, USMCA N) comes in: new rate 30%, change 2.30 x 25% = 0.5750 per unit, impact 23,000.00. Totals: 6 in scope, 251,450.00; the origin table shows XX 228,450.00 and MX 23,000.00.

**Drill 2: rate increase on an existing action.** Set B16 to REPLACE and B17 to 10%, then set SAMPLE-001's current rate (Items J5) to 15% (a 5% base rate plus the earlier 10%). Expected: SAMPLE-001 new rate 15% + 25% - 10% = 30%, change 4.20 x 15% = 0.6300, impact 75,600.00. SAMPLE-002, 003, 012 and 014 show "CHECK: current rate is below the duty being replaced or displaced": their current rates cannot contain the earlier 10% (SAMPLE-003 would need 20%, for the earlier 10% plus the displaced 10%). B19 = 4 and B30 reads NO. Lesson: with REPLACE, the current rate on Items must already include the earlier rate, and the check tells you when it does not.

**Drill 3: break it on purpose.** On Items: type the HTS 303899001 for SAMPLE-002 (a chapter 03 code that lost its leading zero); delete SAMPLE-006's origin code; type `1.50 USD` as SAMPLE-009's customs value (validation stops it, which is the first control; now paste it from a text cell instead, which bypasses validation); and type SAMPLE-001 over SAMPLE-011's item number. On Action, change P5 to SAMPLE-05. Expected: CHECKs for HTS, origin, text in a number column, and a duplicate item on both SAMPLE-001 rows; Action W5 shows "CHECK: no Items row for this item and import country", SAMPLE-005 flips to in scope, and B27 and B30 read NO. Then try `SAMPLE-005 ` with a trailing space: it matches again. Undo everything.

**Drill 4: an item with no sell price.** Clear SAMPLE-003's sell price (Items L7). Expected: the impact B20 stays 228,450.00 and B21 rises to 17,450.00; revenue B22 falls to 1,508,000.00; margin 33.6% before and 19.6% after. Lesson: an unpriced item is in the cost impact but cannot distort the margin %.

**Drill 5: several rate lines and a partial duty base.** Add XY to the origin list (M6). Add a scope prefix 7326.90 (E6) with rate group `ANNEX III` (H6). Add two rate lines: Y5 `R2`, AA5 `XY`, AC5 10%; Y6 `R3`, Z6 `ANNEX III`, AC6 25%, AE6 PART. On Items, set SAMPLE-010's dutiable share (M14) to 20%. Expected: SAMPLE-006 uses R2: 3.90 x 10% = 0.3900, impact 23,400.00. SAMPLE-010 uses R3 on a PART base: 6.00 x 20% x 25% = 0.3000, impact 6,000.00. The other in-scope items still show "Default (B15)". Total 257,850.00; AH5 and AH6 each show 1. Now clear M14: SAMPLE-010 shows "CHECK: dutiable share missing (PART base)".

**Drill 6: partial USMCA relief.** Add MX to the origin list (M6) and set B18 to PARTIAL. Add a rate line: Y5 `R4`, AA5 `MX`, AB5 `Y`, AC5 25%, AE5 PART (qualifying goods pay only on their non-US content). On Items, set SAMPLE-007's dutiable share (M11) to 40%. Expected: SAMPLE-007 (USMCA Y) is in scope on R4: 2.10 x 40% x 25% = 0.2100, impact 31,500.00. SAMPLE-008 (USMCA N) takes B15: 23,000.00. Total 282,950.00 and B30 = YES. Delete the rate line and B26 reads "NO: PARTIAL needs a rate line with USMCA = Y".

**Drill 7: pasted values that bypass validation.** Build each value in a scratch workbook, copy it, and paste it into the copy with Paste Special > Values, one at a time, undoing each. (a) `73I8` (a capital I, not a 1) in Action E5: F5 shows "CHECK: not 2, 4, 6, 8 or 10 digits", every item drops out of scope, and B26 reads "NO: an HTS prefix is not 2, 4, 6, 8 or 10 digits (column F or J)". (b) `EXCLUDED` in Action R5: W5 shows "CHECK: determination must be IN, OUT or blank" and B27 reads NO. (c) `="X"&UNICHAR(160)&"X"` (an X, a non-breaking space, an X; UNICHAR needs Excel 2013 or later, or LibreOffice) in Action M5: B26 reads "NO: an origin in column M is not a 2-letter code". B30 reads NO each time. Then paste `="XX"&UNICHAR(160)` into M5: the model cleans it, and every result matches the sample. Lesson: a NO on the Summary names the problem; a value the model can clean needs no action.

## Extending the template

- **More rows than the capacities (250 items, 300 HTS prefixes and 300 exclusions, 50 origins, 100 determinations, 30 rate lines):** the Manager changes `ITEM_ROWS`, `HTS_ROWS`, `ORIGIN_ROWS`, `DET_ROWS` or `RATE_ROWS` in `build/make_tariff_model.py`, rebuilds with `python3 build/make_tariff_model.py`, and copies the new template to the onboarding folder. The defined names, Summary ranges, validation and formats all follow. This is the only supported route: the Manager owns the template.
- **Two actions on the same items:** build one model per action. Once the first action is in effect, its rate becomes part of the current rate on Items for the second model. To show the combined effect of two actions that have not yet started, put the first action's rate in the current rate column of the second model, and say so in the covering note. If the second action switches off the first one on some goods, record that as a displaced duty (stacking section above), not by editing the current rate.
- **Template changes:** raise them with the Manager. Change the generator, rebuild, and bump `TEMPLATE_VERSION`. Never fix a formula in one copy only.

## Limits (state them in every covering note)

- **Ad valorem only.** Specific and compound rates (per kg, per unit, per litre) need an ad valorem equivalent per item, agreed with Research and the checker, entered as the rate.
- **Duty only.** Landed cost change = duty change. Customs fees such as US MPF (ad valorem with per-entry limits), freight, brokerage and supplier prices are assumed unchanged. Duty-based import taxes (Canada GST, Mexico IVA) are left out because they are normally recoverable; confirm with Finance.
- **Whole-period view.** The impact applies the action to the whole quantity period on Items (K1). The model does not apply the effective date, end date, in-transit relief, stock already on hand or timing within a cost period. Standard Cost handles those in the cost update and the variance explanation.
- **Duty paid is assumed.** Goods imported under duty deferral or recovery (Mexico IMMEX temporary imports, US goods later exported with drawback) may not bear the duty, or may recover part of it, depending on the action (brief 6.8 and 6.9). Exclude or adjust those flows and say so in the covering note.
- **Customs value and dutiable share are inputs.** The model does not build the duty base or calculate content values. Each import country has its own valuation rules (see `docs/primers/customs-trade-compliance-primer.md`).
- **Current rate and standard cost are trusted as given.** If the current standard does not include duty at the current rate, the new standard estimate is wrong.
- **One currency and one unit per row.** All values on Items are in the currency in K2 and per the unit in column G.
- **No AD/CVD by producer.** AD/CVD rates vary by producer and exporter; model them only with rate lines or item rates that Research supplies.
- **No legal judgement.** The model applies the scope, rates and precedence it is given. Scope comes only from the checked brief.

## Common mistakes

- Typing over a formula, or unprotecting a tab to "fix" a number. Fix the input or ask the Manager.
- Deleting SAMPLE rows instead of clearing them. Protection blocks it; if a tab was unprotected, the link between Items and Calc breaks.
- Pasting HTS or item numbers as numbers. Leading zeros vanish and matches fail. AJ flags HTS problems; Action column W flags determinations that match no Items row.
- Pasting an annex list from a PDF or web page with its footnote markers (`7318 1/`, or a plain digit after a space, `7318 1`). Action column F flags every prefix that is not plain digits; fix it from the source.
- Mixing units: a customs value per box with a standard cost per each. Watch for the "customs value above standard cost" NOTE.
- Pasting a per-organization extract without aggregating it: every duplicate row is a CHECK.
- Using the supplier's country instead of the country of origin.
- Putting a second rate in a comment or in B19 instead of a rate line, so the formulas never see it.
- Leaving the SAMPLE rows in a real model.
- Releasing a version that has no checker line on the Review tab, or whose version differs from Action B24.
- Emailing the file. Link the one copy on Jira instead.

## Excel and LibreOffice notes

- The formulas avoid dynamic arrays, LET, LAMBDA, XLOOKUP, IFS and wildcard criteria, so they work in Excel 2010 and later and in LibreOffice Calc. The longest-prefix and rate-line choices use `SUMPRODUCT(MAX(...))`, which evaluates the list without array entry in both. Template v2.0 was recalculated in LibreOffice 24.2 with no formula errors, the sample and every drill above were checked by hand, and the result matched. The non-breaking space is matched by the character itself, not by `CHAR(160)`, so the cleaning does not depend on the computer: CHAR reads the computer's own character set, which differs between Windows, Mac and some LibreOffice settings. Open it once in your Excel version before first real use and confirm the sample totals match.
- Excel recalculates the whole workbook when the file opens. If Excel opens it in Protected View, click Enable Editing so the formulas calculate.
- In LibreOffice, if values look stale, use Data > Calculate > Recalculate Hard.
- Pasting from another workbook can bring in its styles and names. Use Paste Special > Values.
