# Analytics Practice Pack: Exercises

Last updated: 2026-10-17 · Owner: BSA Manager

- **Purpose:** eleven hands-on exercises on synthetic import data. Exercises 1 to 8 (M3 core) build the data skills both tracks need: profiling, joins without fan-out, effective-dated lookups, broker audit, USMCA claim checks, PPV, tariff scenario modeling, Power BI measures and a findings memo. Exercises 9 to 11 (M3 analytics depth) add KPI design, a star-schema Power BI model with a prior-period measure, and variance statistics (price, quantity and mix; outlier rules). Each exercise has SQL Server steps and Excel/Power Query or Power BI steps.
- **Who uses it:** Hire A (Research) and Hire B (Standard Cost) do every exercise. The Senior reviews Exercises 1 to 7 and 9 to 11 against the answer key. The key is trainer-only: it stays in [COMPANY: trainer-only location], never in the hires' OneNote sections or the onboarding folder. The Manager reads the Exercise 8 memo.
- **When:** Exercises 1-2 in W1, 3-4 in W2, 5-6 in W3, 7-8 in W4; then 9 in W7, 10 in W8 and 11 in W9, about 1.5 h of self-study a week. Exercises 1 to 6 are day-30 evidence (A30-5 and B30-5 in `docs/01-30-60-90-plan.md`). Exercises 9 and 10 reviewed and Exercise 11 submitted are a day-60 Should criterion for both hires (A60-9 and B60-9 in Section 4 of the plan). Day-by-day slots for W1-W2 are in `docs/02-weeks-1-2-schedule.md`.

## How the pack works

| Exercise | Week and slots | Track lean | Time box | Reviewed |
|---|---|---|---|---|
| 1 Data profiling | W1: Tue 10/20 16:00 setup, Wed 10/21 08:30 | Both | 2.25 h | Senior, Thu 10/29 |
| 2 Duty by HTS chapter and origin | W1: Thu 10/22 08:30 | Both | 1.5 h | Senior, Thu 10/29 |
| 3 Broker audit: applied vs expected rate | W2: Mon 10/26 10:00, Tue 10/27 16:00 | Research-leaning | 2.75 h | Senior, Thu 10/29 |
| 4 USMCA claim check | W2: Wed 10/28 15:30, Thu 10/29 08:15 | Research-leaning | 3 h | Senior, W3 |
| 5 PPV: actual landed vs standard | W3 (Hire B may start in W2) | Standard Cost-leaning | 3 h | Senior, W3 |
| 6 Tariff scenario impact | W3 | Shared | 3 h | Senior, W3 |
| 7 Power BI page with DAX measures | W4 | Both (Hire B goes deeper) | 3 h | Senior, W4; Power BI depth in W7 |
| 8 One-page findings memo | W4 | Both, written individually | 1.5 h | Manager, W4 work review |
| 9 KPI design | W7 (11/30–12/4), post by 12:00 Wed 12/2 | Both, each for their own process | 1.25 h | Senior, W7 office hours (Wed 12/2) |
| 10 Star-schema model in Power BI | W8 (12/7–12/11), post by Tue 12/8 | Both (Hire B goes deeper) | 1.5 h | Senior, W8 office hours (Wed 12/9) |
| 11 Variance statistics | W9, submit by Thu 12/17 | Both | 1.25 h | Senior, in writing in W10 |

"Leaning" means both hires do the core exercise, and the leaning hire also does the stretch and presents the result at the review. Exercise 6 is shared on purpose: Hire A owns the scope logic (the WHAT), Hire B owns the dollars (the $), as in the boundary rule.

Exercises 9 to 11 build on the W7 Senior session on Power BI and warehouse depth (Tue 12/1) and reuse your saved views and queries from Exercises 1, 2, 3, 5 and 7. Exercise 9 is the homework of that session: post it by 12:00 on Wed 12/2, so the Senior can read it first and use that afternoon's office hours for the differences. Post Exercise 10 by the end of Tue 12/8 for the W8 office hours (Wed 12/9). There are no Senior office hours in W9 (`docs/01-30-60-90-plan.md` Section 5), so submit Exercise 11 by the end of Thu 12/17; the Senior reviews it in writing in W10. Take questions on the written review to the recap block of the next Senior session or to your 1:1.

Rules for every exercise:

- Work on your own copy. Never edit the files in the onboarding folder.
- Save every SQL query with a header comment (purpose, source tables, author, date, exercise). Name every Power Query step so a reviewer can follow it.
- Write down the row count before and after every join or filter. A row count that changes when it should not is the most common error in this pack.
- Post each exercise to OneNote section 07 Analytics: the query or workbook, the result tables, three lines on what you learned, and open questions.
- The answer key and the script that generated the data are trainer-only. You do not get the key before the day-30 review (its Exercise 9 to 11 sections not before the day-60 review), and you do not get the script before the day-60 review: the key holds the answers, and the script's comments list every planted problem and its cause. Use each exercise's "Check yourself" to test your own work.
- When the Senior reviews a posted exercise, they tell you which results differ from the key, not what the right number is. Find the cause of each difference and write it down. A difference you can explain is worth more than a lucky match.
- Stuck for 15 minutes on the same step? Log the question with what you tried (the stuck rule in `docs/05-time-management.md`), move to the next step, and bring it to the Senior's office hours.
- Run the SQL in your practice scratch database (Setup, Option B), never in the team database. Outside your own sandbox tables, creating a view or table in the team database is a schema change, and schema changes go through the Senior (`docs/primers/data-platform-primer.md` 1.1, rules 4 and 5).
- Copilot Chat may help you draft a query, a DAX measure or a KPI definition (`docs/primers/copilot-chat-guide.md`). Treat its output as a draft: check every number against your own query, and log the use in your Copilot use log. Before you paste anything that is not this synthetic data (for example the sanitized extract in Exercise 3), check [COMPANY: AI acceptable-use policy].

## The practice data

The data is **synthetic**: a fictional importer of hardware, electrical and household goods into the US, Canada and Mexico. Items, suppliers, brokers, entries, values, costs and rates are invented. So is work_items, a fictional Jira export of the team's own Research and Standard Cost work, added for Exercise 9. HTS codes have a real-looking format (the first 6 digits are real HS subheadings, the last 4 are random). **Synthetic: do not use for classification.** The duty rates and tariff scenarios are not the real rates or actions for these codes. For real rates and actions use `docs/primers/current-tariff-landscape.md`.

Facts about the data:

- Entries and receipts fall between 2026-01-02 and 2026-09-30: nine months. To annualize, multiply by 12 / 9.
- work_items shows each item's status on 2026-09-30, the data cut-off. All its dates fall on weekdays.
- All money is in USD. Rates are decimals: 0.0340 means 3.4%.
- Like real extracts, the data has deliberate data-quality problems. Finding them is part of the work.

### Tables

| Table | One row is | Key | Rows |
|---|---|---|---|
| items | An item: classification master and US standard cost | item_id | 150 |
| suppliers | A supplier | supplier_id | 31 |
| brokers | A customs broker | broker_id | 6 |
| entries | A customs entry (US entry, Canadian CAD, Mexican pedimento) | entry_no | 400 |
| entry_lines | A line on an entry, as the broker filed it | entry_no + line_no (meant to be unique) | 1,966 |
| duty_rates_reference | The expected rate for an import country, HTS and origin over a date range | import_country + hts10 + country_of_origin + effective_from | 228 |
| receipts | A PO receipt line into the US warehouse | receipt_id | 1,500 |
| tariff_scenario | A fictional proposed tariff action: one row per HTS prefix and origin | scenario_id + hts_prefix + country_of_origin | 11 |
| work_items | A Research or Standard Cost work item (a fictional Jira issue), status on 2026-09-30 | work_item_id | 38 |

### How the tables join

- entry_lines to entries on entry_no (gives import_country, entry_date, port, broker_id).
- entry_lines to items on item_id (gives hts10, country_of_origin, usmca_eligible_flag, std_cost).
- items to suppliers on supplier_id; entries to brokers on broker_id; receipts to items on item_id.
- duty_rates_reference joins on import_country (from entries), hts10 and country_of_origin (from items), **and** entry_date between effective_from and effective_to (both inclusive).
- tariff_scenario joins on import_country and country_of_origin, where hts10 starts with hts_prefix.
- work_items joins to no other table. Its action_ref links a Tariff-Impact Brief to the Tariff $ model for the same fictional action.

### Columns that need care

| Column | Meaning | Watch out |
|---|---|---|
| items.hts10 | 10-digit code, stored as text | Excel turns it into a number if you let it. Keep it as Text |
| items.country_of_origin | Non-preferential origin (2-letter ISO code) | Not the supplier's country. Compare suppliers.supplier_country |
| items.usmca_eligible_flag | Y = a USMCA certification is on file for the item | Master data. It can be wrong |
| items.std_cost | US standard cost per unit, including freight and duty at the rate in effect on 2026-01-01 | Unit is the selling unit in the description (box, pack, each) |
| entry_lines.program_claimed | USMCA when the broker claimed USMCA (CUSMA, T-MEC); blank (NULL) when no preference was claimed | A blank here is not an error. See Exercise 3 |
| entry_lines.duty_amount | entered_value x duty_rate_applied, rounded to the cent | This is the duty actually paid |
| duty_rates_reference.expected_rate | base_rate + additional_rate. The non-preferential rate | A valid USMCA claim means 0% in this data |
| receipts.actual_landed_unit_cost | Actual cost per unit including freight and duty | Same unit as std_cost |
| work_items.released_date | The date the checked output was released | Blank (NULL) = still open on 2026-09-30 |
| work_items.checker_signoff_date | The date the checker signed off | Blank = no documented sign-off. A date after released_date is a sign-off after release |
| work_items.errors_after_release | Material errors found after release | Blank while the item is open. Blank is not zero |

### Rules of this practice world

These simplify reality so the exercises have one right answer. Say them in your memo when they matter.

- A USMCA claim is **valid** only when the item's country_of_origin is US, CA or MX **and** usmca_eligible_flag = 'Y'. In real life USMCA originating status comes from the product-specific rule of origin and the certification, not from the origin field (see `docs/primers/customs-trade-compliance-primer.md`, sections 10.1 and 10.7). In real data, investigate a mismatch before calling a claim invalid.
- One hts10 per item is used for all three import countries. In reality each country has its own 10-digit code; only the first 6 digits are shared (primer section 3.2).
- HTS and origin come from the item master, not from the filed line. Real broker data carries the filed HTS and origin, and comparing them to the master is part of a real audit.
- No fees (MPF, HMF, DTA) and no import taxes (GST, IVA).
- Receipts are US warehouse receipts only; std_cost is that warehouse's standard.
- PPV sign: positive = unfavorable (actual above standard). [COMPANY: confirm Finance's sign convention, and whether PPV is measured on landed cost or on PO price only.]

## Setup

### Option A: Excel and Power Query (no database needed; use this in W1)

1. Copy Practice-Data.xlsx from the onboarding folder to your working folder [COMPANY: OneDrive or SharePoint folder]. Read its README sheet.
2. Create a new blank workbook for your work, for example `M3-practice-HireA.xlsx`.
3. Data > Get Data > From File > From Excel Workbook, and pick your copy. In the Navigator tick "Select multiple items", select the nine `tbl_` tables (not the sheets), then click Transform Data. (tbl_work_items is used only in Exercise 9.)
4. In Power Query, check the type icon on every column header. Codes (item_id, hts10, entry_no, receipt_id, po_no, supplier_id, broker_id, country codes, flags, hts_prefix) must be Text. Dates must be Date. qty, line_no and errors_after_release are Whole Number. Money and rates are Decimal Number. If the hts10 icon shows "123" (a number), change the type to Text and choose Replace current.
5. View tab: tick Column quality, Column distribution and Column profile. In the status bar at the bottom, change "Column profiling based on top 1000 rows" to "based on entire data set". Otherwise the profile only looks at 1,000 rows.
6. Home > Close & Load To > Only Create Connection, for the nine source queries. Load to a sheet only the result queries you build.

If you use the CSVs in the practice-data folder of the onboarding folder instead, import them with Data > From Text/CSV and set the types in Power Query. Never double-click a CSV to open it: Excel converts hts10 to a number and may reinterpret dates.

### Option B: SQL Server scratch database

You need a database where you may create tables and views. The access in AR-07 (`docs/04-access-request-checklist.md`: read, plus rights on your own tables in the sandbox schema) is not enough, because the load script creates its own schema. In order of preference:

1. [COMPANY: sandbox or development database where analysts may create tables]. Ask the Senior.
2. SQL Server Developer or Express edition on your laptop, only if IT approves the install.
3. Until one of these exists, use Option A. Exercises 1 and 2 do not need SQL.

To load: open load_practice_data.sql (in the practice-data folder of the onboarding folder) in SQL Server Management Studio (or VS Code with the MSSQL extension), connect to the scratch database, and run the whole script (F5). It creates schema `practice`, the nine tables and all rows in a few seconds, and ends with a row count per table that must match the Tables section above. Rerun it any time to reset the data. Never run it against a production database.

If you cannot run the script, the SSMS Import Flat File wizard (right-click the database > Tasks > Import Flat File) loads one CSV at a time. Name each table exactly as its CSV file. On the Modify Columns page set every code column to a text type (nvarchar), dates to date, money and rates to decimal, and allow nulls. If the tables land in schema dbo, run `CREATE SCHEMA practice;` once and then `ALTER SCHEMA practice TRANSFER dbo.items;` for each table. Afterwards check that blanks became NULL: `SELECT COUNT(*) FROM practice.items WHERE hts10 = '';` must return 0; if not, run `UPDATE practice.items SET hts10 = NULL WHERE hts10 = '';` and do the same for entry_lines.program_claimed.

### SQL habits for this pack

Start every saved query with a header like this:

```sql
-- Purpose: Exercise 3 broker audit, applied vs expected rate
-- Source:  practice.v_entry_lines_clean, practice.entries, practice.items, practice.duty_rates_reference
-- Author:  Hire A          Date: 2026-10-26
-- Checks:  non-preference lines before join = ____ ; rows after rate join = ____
```

- Always name the schema: `practice.items`, not `items`.
- Keep money in DECIMAL. Compute rates as `SUM(duty) / SUM(value)`, never as the average of line rates.
- To annualize, write `SUM(x) * 12.0 / 9`. In T-SQL `12 / 9` on its own is integer division and returns 1, and `SUM(qty) * 12 / 9` truncates because qty is an INT.
- Wrap every denominator in `NULLIF(..., 0)`, for example `SUM(duty_amount) / NULLIF(SUM(entered_value), 0)`. A zero or empty group then gives NULL instead of stopping the query with a divide-by-zero error.
- A comparison with NULL is never true: `program_claimed <> 'USMCA'` does not return rows where program_claimed is NULL. Use `IS NULL`.
- Don't round inside a calculation. Round only the number you report.

## Exercise 1: Data profiling

W1 · Both · 2.25 h · Reviewed by the Senior on Thu 10/29

**Goal.** Know what is in each table before you trust any number from it: row counts, NULLs, duplicate keys, orphans and master-data contradictions. End with a profiling log and a clean entry-lines table that every later exercise uses.

**Business context.** Every Research or Standard Cost answer starts from an extract: broker line data, the item master, a cost extract. A tariff model built on an extract with duplicate lines overstates the exposure; a PPV report on receipts with unit-of-measure errors explains nothing. Profiling first is the habit that makes your numbers survive review. It is also the first step of e2open data cleansing (M10).

**Data needed.** All eight tables.

**Questions to answer.**

1. How many rows does each table have, and does that match the load?
2. Which columns have NULLs, how many, and in each case is the NULL an error or does it mean something?
3. Is entry_no + line_no unique in entry_lines? If not: how many extra rows, in which entries, and how much entered value and duty do they add?
4. How many entry lines have an item_id that is not in items (orphans)? Which items, what value?
5. Item master: which items have no HTS? Which items have a USMCA flag that contradicts their origin? How many items are bought from a supplier in a different country from the item's origin, and is that an error?
6. What is the date range of entries and receipts? Which values appear in program_claimed? Is every non-NULL hts10 exactly 10 digits?

**Steps: SQL Server.**

1. Row counts: one `SELECT COUNT(*)` per table, combined with `UNION ALL`.
2. NULLs: `COUNT(*) - COUNT(column)` gives the number of NULLs, because COUNT(column) skips them. Do it for every column of items and entry_lines, and the key columns of the rest.
3. Duplicates: `GROUP BY entry_no, line_no HAVING COUNT(*) > 1`. Then compare `COUNT(*)` with the count of distinct keys, and sum entered_value and duty_amount of the extra rows.
4. Create the clean view below. Every later exercise uses it. In your notes, explain each line in your own words.

```sql
CREATE OR ALTER VIEW practice.v_entry_lines_clean AS
WITH numbered AS (
    SELECT el.*,
           ROW_NUMBER() OVER (PARTITION BY el.entry_no, el.line_no ORDER BY el.entry_no) AS copy_no
    FROM practice.entry_lines AS el
)
SELECT entry_no, line_no, item_id, qty, entered_value, duty_rate_applied, duty_amount, program_claimed
FROM numbered
WHERE copy_no = 1;
```

`ORDER BY el.entry_no` is a placeholder: every row in a partition has the same entry_no, so SQL keeps an arbitrary copy. That is safe only if the copies are identical, so prove it first: `SELECT COUNT(*) FROM (SELECT DISTINCT * FROM practice.entry_lines) AS d;` must equal the number of distinct keys from step 3. In real data, order by a load timestamp or file ID so the copy you keep is the one you meant to keep.

5. Orphans: `LEFT JOIN practice.items` and keep the rows `WHERE i.item_id IS NULL`. Also check entry lines whose entry_no is not in entries.
6. Master checks: items `WHERE hts10 IS NULL`; flag Y with origin outside US, CA and MX; flag N with origin inside; supplier country different from origin (join suppliers).
7. Format: `WHERE hts10 IS NOT NULL AND (LEN(hts10) <> 10 OR hts10 LIKE '%[^0-9]%')` finds codes that are not 10 digits.

**Steps: Excel and Power Query.**

1. For each source query, read the Column profile (count, empty, distinct, unique) on the entire data set and note anything odd.
2. entry_lines: right-click the query > Reference. In the new query, select entry_no and line_no (Ctrl+click), then Home > Keep Rows > Keep Duplicates. The rows left are every copy of a duplicated key. Group By entry_no to see which entries.
3. Make another Reference of entry_lines, select entry_no and line_no, Home > Remove Rows > Remove Duplicates, and name it `lines_clean`. Every later exercise uses it. Prove the copies were identical before you trust it: in a throwaway Reference, select all columns (Ctrl+A) and Remove Duplicates. The row count must equal lines_clean's.
4. Orphans: Home > Merge Queries as New, lines_clean to items on item_id, Join Kind "Left Anti (rows only in first)". The rows left are orphans.
5. items: filter hts10 to null. Add a Conditional Column for the flag and origin checks. Merge suppliers on supplier_id and compare supplier_country with country_of_origin.
6. Keep your answers in a profiling log table on a sheet (see Deliverable).

**Deliverable.** A profiling log with one row per check: check, result (count and value), error or expected, impact on later analysis, suggested action and owner (by role). Plus the clean view or the lines_clean query.

**Check yourself.** Raw rows minus clean rows must equal the extra rows you found. Raw duty minus clean duty must equal the duty on the extra rows.

**Stretch.** (a) Check the arithmetic: does duty_amount equal ROUND(entered_value x duty_rate_applied, 2) on every line? (b) Turn your checks into one rerunnable script or one query group you could run on next month's extract. (c) Write three e2open data-cleansing rules suggested by what you found.

## Exercise 2: Duty paid by HTS chapter and country of origin

W1 · Both · 1.5 h · Reviewed by the Senior on Thu 10/29

**Goal.** Total entered value, duty paid and effective duty rate by HTS chapter (first 2 digits) and country of origin, reconciled to the clean control total from Exercise 1.

**Business context.** "How much duty do we pay on chapter 73 from China?" is the first question in almost every tariff discussion. Research uses it to size the exposure to an action before any modeling. Standard Cost uses the effective duty rate (duty divided by customs value) to sanity-check the duty built into standard costs.

**Data needed.** Clean entry lines (Exercise 1), items, entries.

**Steps: SQL Server.**

1. Join the clean view to items with a LEFT JOIN. Write down why LEFT and not INNER, and what an INNER JOIN would lose.
2. Chapter = `LEFT(hts10, 2)`. Label a missing HTS and a missing origin `'UNK'` with COALESCE, so those lines stay in the totals.
3. GROUP BY chapter and origin: lines, SUM(entered_value), SUM(duty_amount), and effective rate `100.0 * SUM(duty_amount) / NULLIF(SUM(entered_value), 0)`.
4. Totals by chapter alone, by origin alone, and the grand total. `GROUP BY GROUPING SETS ((chapter), (origin), ())` does all three in one query; two simple queries are fine too.
5. Prove the grand total equals the clean duty total from Exercise 1.
6. Repeat by import country (join entries).

**Steps: Excel and Power Query.**

1. Merge Queries as New: lines_clean to items on item_id, Left Outer. Expand hts10 and country_of_origin.
2. Select hts10, Add Column > Extract > First Characters, 2. Rename it hts_chapter. Replace null with UNK in hts_chapter and country_of_origin (Transform > Replace Values, value to find: null).
3. Load to a sheet as a table. Insert a PivotTable: rows hts_chapter, columns country_of_origin, values Sum of duty_amount.
4. Add the effective rate as a calculated field (PivotTable Analyze > Fields, Items and Sets > Calculated Field): `= duty_amount / entered_value`. Pivot calculated fields divide the sums, which is what you want.
5. Check the pivot grand total against Exercise 1.

**Deliverable.** The top 10 chapter and origin combinations by duty, totals by chapter and by origin, the reconciliation to the control total, and three observations a Research or Standard Cost BSA would care about.

**Check yourself.** The sum of all groups equals the clean duty total. You can say which items make up the UNK rows and why.

**Stretch.** (a) Redo the origin totals using the supplier's country instead of the item's origin and compare CN. Explain in two sentences why the supplier country is the wrong field for tariff questions. (b) Add duty by month and spot the month where duty jumps.

## Exercise 3: Broker audit, applied rate vs expected rate

W2 · Research-leaning · 2.75 h · Reviewed by the Senior on Thu 10/29

**Goal.** For every clean line where no preference was claimed, compare the rate the broker applied with the rate expected for that import country, HTS, origin and entry date. Count matches, over-applied and under-applied lines, and quantify the overpayment and underpayment in dollars.

**Business context.** The importer stays liable for the duty even when a licensed broker files (primer sections 1 and 7.3). Research owns the rate rule: what rate applies, from which date. This audit shows whether the rule reached the filings. Standard Cost cares because duty overpaid or underpaid flows into landed cost and PPV.

**Data needed.** Clean entry lines, entries, items, duty_rates_reference.

**Rules.**

- Scope: clean lines with program_claimed NULL. USMCA claims are Exercise 4.
- Expected rate: the reference row for the same import country, hts10 and origin whose effective_from <= entry_date <= effective_to.
- variance_usd = entered_value x (duty_rate_applied - expected_rate). Positive = overpaid, negative = underpaid. Don't round per line.
- Lines you cannot audit (item not in master, HTS missing, no reference row) get their own status. They are not matches.

**Steps: SQL Server.**

1. Count the scope with `WHERE program_claimed IS NULL`. Then run it with `WHERE program_claimed <> 'USMCA'` and explain the difference.
2. Join entries (INNER) and items (LEFT).
3. LEFT JOIN duty_rates_reference on import_country, hts10 and country_of_origin only, and count the rows. Then add `AND e.entry_date BETWEEN r.effective_from AND r.effective_to` and count again. The count must now equal step 1. Explain what happened in between.
4. Status with CASE: not auditable (item not in master; HTS missing; no reference rate), Match, Over, Under.
5. Summary by status: lines, entered value, variance_usd.
6. By broker: lines audited, mismatches, overpaid, underpaid, net.
7. Save the query as a view, `practice.v_rate_audit`. Exercises 7 and 8 reuse it.
8. List the mismatches sorted by the absolute variance. Look for patterns: dates, broker, origin, chapter, and whether the applied rate equals a rate in another period or the base rate alone.

**Steps: Excel and Power Query.**

1. Reference lines_clean, filter program_claimed to null, then merge entries (Inner) and items (Left Outer) and expand the columns you need.
2. Merge duty_rates_reference: select import_country, hts10 and country_of_origin in the same order in both tables (Ctrl+click), Left Outer. Expand effective_from, effective_to, base_rate, additional_rate and expected_rate. Note the row count (right-click the query > Reference, then Transform > Count Rows).
3. Add Column > Custom Column `in_period`: `if [effective_from] = null then true else [entry_date] >= [effective_from] and [entry_date] <= [effective_to]`. Filter it to TRUE. The row count must now equal your scope.
4. Custom Column `audit_status`: `if [country_of_origin] = null then "Not auditable: item not in master" else if [hts10] = null then "Not auditable: HTS missing" else if [expected_rate] = null then "Not auditable: no reference rate" else if Number.Abs([duty_rate_applied] - [expected_rate]) < 0.00005 then "Match" else if [duty_rate_applied] > [expected_rate] then "Over" else "Under"`.
5. Custom Column `variance_usd`: `[entered_value] * ([duty_rate_applied] - [expected_rate])`. Load and pivot by audit_status and broker_id.

Formula alternative (no Power Query): bring import_country, entry_date and broker_id onto each line with XLOOKUP from entries, and hts10 and country_of_origin from items. Then `expected_rate = SUMIFS(ref[expected_rate], ref[import_country], [@import_country], ref[hts10], [@hts10], ref[country_of_origin], [@country_of_origin], ref[effective_from], "<="&[@entry_date], ref[effective_to], ">="&[@entry_date])` and the same criteria in COUNTIFS. The COUNTIFS result must be 1 on every auditable line: 0 means no reference, 2 would mean overlapping periods.

**Deliverable.** Audit summary by status, the broker table, the mismatch list with your pattern notes, and three lines on what you would tell the Senior.

**Check yourself.** Match + Over + Under + not auditable = scope lines. The row count after the date condition equals the scope.

**Stretch.** Hire A: classify every mismatch into a pattern (old rate after a change, new rate before a change, additional duty missed, 0% applied, other) and draft three questions the Senior could put to the broker with the worst pattern. You do not contact brokers yourself. Hire B (the Thu 10/29 slot): for each item in the sanitized standard cost extract, compute the implied duty rate = duty element / material (purchase) cost. Take the item's US HTS and country of origin from the AS400 trade item extract and look up the General rate for that HTS in hts.usitc.gov. List the items whose implied rate differs by more than 1 percentage point, with one possible reason each: additional duty (see `docs/primers/current-tariff-landscape.md`), a preference such as USMCA, a rate change since the cost period, freight or fees inside the duty element, or a data error. Material cost only approximates customs value; say so. Each difference is a question for Research and the Senior, not a conclusion. Read-only; no system writes.

## Exercise 4: USMCA claim check

W2 · Research-leaning · 3 h · Reviewed by the Senior in W3

**Goal.** Find the USMCA claims that are invalid under the practice rule, quantify the duty at stake, and trace each group of invalid claims to a root cause: our master data or the broker.

**Business context.** An invalid preference claim means duty was underpaid, and the importer must correct it (primer section 10.7: escalate the same day). Many invalid claims trace back to master data the team owns, such as a wrong flag or a missing certification. Research brings the origin knowledge; Standard Cost cares because duty at stake changes landed cost.

**Data needed.** Clean entry lines, entries, items, duty_rates_reference.

**Rules.**

- Valid claim: origin is US, CA or MX and usmca_eligible_flag = 'Y'. Anything else claimed as USMCA is invalid.
- Duty at stake = entered_value x the expected (non-preferential) rate in effect on the entry date.

**Steps: SQL Server.**

1. Filter clean lines `WHERE program_claimed = 'USMCA'`. Count lines and entered value.
2. LEFT JOIN items. Add `claim_status` with CASE: item not in master; origin not US, CA or MX; no certification on file (flag not Y); otherwise Valid.
3. LEFT JOIN duty_rates_reference with the date condition from Exercise 3 and compute duty at stake.
4. Summarize by claim_status. Then group the invalid lines by item, by import country and by broker.
5. Save it as a view, `practice.v_usmca_claims`.
6. For each item with several invalid lines, decide: is the cause the item master (the flag) or the broker (a one-off claim)? What evidence supports that?

**Steps: Excel and Power Query.** Reference lines_clean, filter program_claimed to "USMCA", merge entries and items, add a Conditional Column for claim_status, merge duty_rates_reference as in Exercise 3 (with the in_period filter), add duty_at_stake, load and pivot by claim_status, item_id and broker_id.

**Deliverable.** A claims summary (valid and invalid by reason: lines, value, duty at stake), the invalid claims by item with your root-cause call, and recommended actions with an owner by role. The correction route (post-summary correction, prior disclosure, CAD adjustment, rectificación) is the Senior's or Manager's decision, not yours.

**Check yourself.** Valid + invalid lines = all claims. Every invalid line has an expected rate, or you can say why not.

**Stretch.** Missed savings: find eligible items (origin US, CA or MX and flag Y) entered with no claim on dutiable lines. Count them and total the duty paid. In the US a post-importation claim can be made within one year of importation (primer section 10.7); for Canada and Mexico ask the Senior. Which of these lines are still inside the US one-year window, and when does the earliest one expire?

## Exercise 5: PPV, actual landed cost vs standard

W3 (Hire B may start in W2) · Standard Cost-leaning · 3 h · Reviewed by the Senior in W3

**Goal.** Compute purchase price variance (PPV) on 2026 receipts, separate the outliers, find the top movers and explain the biggest driver.

**Business context.** PPV is what Finance asks Standard Cost to explain every period. Duty is part of landed cost, so when a tariff rate changes during the year and the standard does not, PPV shows it. For Research, this is where the WHAT becomes dollars.

**Data needed.** receipts, items; duty_rates_reference and entries for the stretch.

**Rules.**

- PPV per receipt = (actual_landed_unit_cost - std_cost) x qty. Positive = unfavorable.
- PPV % = SUM(PPV) / SUM(std_cost x qty).
- Outlier: actual_landed_unit_cost > 3 x std_cost, or < std_cost / 3. Report outliers separately; never delete them.

**Steps: SQL Server.**

1. Join receipts to items and check that no receipt is lost.
2. Compute std_value_usd, ppv_usd and an is_outlier flag. Write the outlier test with multiplication (`actual > 3 * std OR actual * 3 < std`) so a zero standard cannot cause a divide error.
3. Save it as a view, `practice.v_ppv`.
4. Totals for all receipts, outliers, and excluding outliers. `GROUP BY ROLLUP (is_outlier)` gives all three.
5. List the outliers with actual / std. What is the likely cause of each group?
6. Top 10 items by absolute PPV, excluding outliers: `SELECT TOP (10) ... ORDER BY ABS(SUM(ppv_usd)) DESC`.
7. PPV and PPV % by month (`DATEFROMPARTS(YEAR(receipt_date), MONTH(receipt_date), 1)`), by origin and by chapter. Where and when does PPV % change? Compare with the effective dates in duty_rates_reference.

**Steps: Excel and Power Query.** Merge receipts with items (std_cost, description, country_of_origin, hts10). Add custom columns: `std_value = [std_cost] * [qty]`, `ppv = ([actual_landed_unit_cost] - [std_cost]) * [qty]`, `is_outlier = [actual_landed_unit_cost] > 3 * [std_cost] or [actual_landed_unit_cost] * 3 < [std_cost]`, and a month column (Add Column > Date > Month > Start of Month on receipt_date). Load, then pivot by is_outlier, item, month and origin. Add PPV % as a pivot calculated field `= ppv / std_value`.

**Deliverable.** The PPV summary (all, outliers, excluding outliers), the outlier list with the likely cause, the top 10 movers with a one-line driver hypothesis each, and three sentences on the biggest driver.

**Check yourself.** PPV of all receipts = PPV of outliers + PPV excluding outliers. Every top-10 item has a hypothesis you could test.

**Stretch.** Hire B: estimate the duty-driven part of the biggest driver. Take the average customs value per unit from 2026 US entry lines (sum of entered_value / sum of qty per item), multiply by the rate increase and by the receipt quantity after the change date, and compare with the PPV of those receipts. Then list the items whose standard cost needs an update and the checks Finance will expect (`docs/templates/domain/standard-cost-update-checklist.md`). Every cost update gets maker-checker review.

## Exercise 6: Tariff scenario impact

W3 · Shared (Hire A: scope logic; Hire B: dollars) · 3 h · Reviewed by the Senior in W3

**Goal.** The annualized duty impact of the three fictional scenarios in tariff_scenario, by scenario, origin and HTS chapter, with the items driving it and the limits of the estimate.

**Business context.** This is Research's most frequent job: an action is about to take effect, Research decides the scope (codes, origins, exemptions, which rule wins when two rows overlap) and Standard Cost turns it into dollars. It is a small version of the Tariff-Impact Model (`docs/templates/domain/tariff-impact-model-guide.md`), with the same boundary rule.

**Data needed.** Clean entry lines, entries, items, tariff_scenario.

**Rules.**

- Base: clean lines whose item has an HTS (Jan to Sep 2026).
- A line matches a scenario row when import_country and country_of_origin are equal and hts10 starts with hts_prefix.
- If more than one prefix of the same scenario matches a line, the **longest prefix wins** (the specific line overrides the heading).
- usmca_exempt = 'Y': lines of items with usmca_eligible_flag = 'Y' are exempt.
- YTD impact = entered_value x additional_rate. Annualized impact = YTD impact x 12 / 9.
- Full-year view: ignore the effective date. List it as a limit.

**Steps: SQL Server.**

1. Build the base (clean lines + entries + items, hts10 not NULL). Keep qty: stretch (c) needs it.
2. Join tariff_scenario on import_country, country_of_origin and `b.hts10 LIKE s.hts_prefix + '%'`. Count the rows, then count the distinct line and scenario pairs. If they differ, some lines match two prefixes. (These counts include the lines that step 4 exempts.)
3. Keep the longest prefix: `ROW_NUMBER() OVER (PARTITION BY entry_no, line_no, scenario_id ORDER BY LEN(hts_prefix) DESC)` and keep row 1.
4. Flag exempt lines; exclude them from the impact but report how much the exemption is worth.
5. Annualized impact by scenario; by scenario, origin and chapter; by scenario and prefix; top 5 items.
6. Save it as a view, `practice.v_scenario_lines`. Exercise 7 uses it.
7. List lines you could not evaluate (HTS missing) whose import country and origin match a scenario. Could any of them be in scope? Who decides?

**Steps: Excel (formulas).** Load a table from lines_clean merged with entries and items, with import_country, country_of_origin, hts10 (Text), usmca_eligible_flag and entered_value. On a calculation sheet, one row per scenario row, use SUMIFS with a wildcard, for example `=SUMIFS(lines[entered_value], lines[import_country], "US", lines[country_of_origin], "CN", lines[hts10], "7318*")`. Wildcards only work because hts10 is text. For the overlapping prefix, subtract the longer prefix's sum from the shorter one before applying the shorter one's rate. For the exempt scenario add the criterion `lines[usmca_eligible_flag], "N"`. Multiply by the rate and by 12/9.

Power Query alternative: first filter hts10 to remove null (those lines go on your "not evaluable" list in step 7). Then add a Custom Column whose formula is just `tariff_scenario` (every line gets the whole table), expand it, keep rows where import country and origin match and `Text.StartsWith([hts10], [hts_prefix])` is true, add `Text.Length([hts_prefix])`, then Group By line and scenario with Max of the length and keep only the longest.

**Deliverable.** A table by scenario (lines, YTD value, annualized impact), a table by scenario, origin and chapter, the top 5 items, and a limits and caveats list: what you could not evaluate and why, the volume basis, and what the full-year view ignores.

**Check yourself.** By-origin totals and by-chapter totals both add up to each scenario total. You can state how many lines matched two prefixes and what double counting would have added.

**Stretch.** (a) Impact from each effective date to 2026-12-31: annualized impact x days in that window / 365, counting both dates (`DATEDIFF(day, effective_date, '2026-12-31') + 1`). (b) Hire A: for each HTS-missing item, say from its description whether it is likely in scope, and what Research needs to confirm it. (c) Hire B, with Hire A as Research: run SCN-02 (Canada import, US origin, 25%) through a copy of Tariff-Impact-Model-Template.xlsx from the onboarding folder, following `docs/templates/domain/tariff-impact-model-guide.md`. Hire A, or the Senior acting as Research, fills the Action tab with the SCN-02 rows of tariff_scenario and clears the template's sample action. Hire B does not edit the Action tab: Hire B uses the values Research provides and asks Research if they look wrong. Hire B fills the Items tab with all 18 US-origin items that have Canadian entry lines; the model, not Hire B, decides from the Action tab which are in scope. Per item: unit customs value = YTD entered value / YTD qty; quantity for a 12-month period = YTD qty x 12.0 / 9 (state the basis where the guide asks); current duty rate: 0% for items with usmca_eligible_flag = 'Y' (a valid CUSMA claim means 0% in this data), otherwise the CA expected_rate from duty_rates_reference. Leave standard cost and sell price blank and say why (the practice std_cost is the US warehouse's). The model then shows a CHECK on every row ("value, rate or cost missing" once the other columns are filled), so Summary B19 counts every row and B30 reads NO: that is expected for this practice run, and B20 still computes the impact. Say so in your note. Replace the sample 73 in the Summary chapter list with 85 and 94 (A47:A48) so B29 reads YES. Confirm the model's impact equals your SQL annualized impact for SCN-02. If the impact is zero, check whether the Action tab still holds the sample action, and go back to Research.

## Exercise 7: Power BI page with DAX measures

W4 · Both (Hire B goes deeper) · 3 h · Reviewed by the Senior in W4; Power BI depth follows in W7

**Goal.** A one-page Power BI report on a small star schema, with four measures that tie to your Exercise 2, 5 and 6 answers: Total Duty, Effective Duty Rate, PPV %, Scenario Impact.

**Business context.** The reporting backlog moves to you from W10 (M8), and the business reads its numbers in Power BI. Knowing the difference between a measure and a column, what filter context does, and why a Power BI total can differ from SQL (skill S-M3-04) is the base for every report change you will make.

**Data needed.** From SQL: v_entry_lines_clean joined to entries, items, v_ppv, v_scenario_lines. From Excel: your lines_clean (with entry fields), items, receipts with is_outlier, and the Exercise 6 scenario lines from the Power Query alternative (one row per line and scenario).

**Model.**

- Facts: EntryLines (one row per clean entry line, with import_country, entry_date and broker_id brought in from entries), Receipts (one row per receipt, with is_outlier), ScenarioLines (one row per line and scenario after the longest-prefix rule, with is_exempt).
- EntryLines also carries hts_chapter = `COALESCE(LEFT(hts10, 2), 'UNK')` and origin = `COALESCE(country_of_origin, 'UNK')`, brought in from items while shaping (in the SQL view or in Power Query). The chapter visuals then tie to Exercise 2, UNK row included. Items has no chapter column, and the orphan lines have no Items row at all.
- Dimensions: Items, and a Calendar table built in DAX for 2026, marked as the date table.
- Relationships: Items to each fact on item_id, Calendar to EntryLines[entry_date] and Receipts[receipt_date] (not to ScenarioLines); one-to-many, single direction.

**Measures to write.** Write these yourself. The Senior checks them against the reference DAX in the W4 review.

| Measure | Definition |
|---|---|
| Total Entered Value | Sum of entered_value on EntryLines |
| Total Duty | Sum of duty_amount on EntryLines |
| Effective Duty Rate | Total Duty / Total Entered Value, safe when the value is zero |
| PPV % | PPV / standard value received, receipts with is_outlier = FALSE only |
| Scenario Impact | Sum of entered_value x additional_rate on non-exempt ScenarioLines, x 12 / 9 |

**Layout spec (one page, 16:9).**

| Area | Visual | Fields | Why |
|---|---|---|---|
| Top row | Four cards | Total Duty, Effective Duty Rate, PPV %, Scenario Impact | The four numbers the Manager asks for first |
| Left | Slicers | Calendar month, EntryLines import_country, Items country_of_origin, ScenarioLines scenario_id | Filter context practice: see which cards each slicer changes |
| Middle left | Clustered bar | Total Duty by EntryLines hts_chapter | Where the duty is |
| Middle right | Matrix | EntryLines hts_chapter rows, EntryLines origin columns, Total Duty and Effective Duty Rate | Exercise 2 in one visual |
| Bottom left | Line chart | PPV % by month | Shows when PPV moved |
| Bottom right | Table | Scenario Impact by scenario_id and country_of_origin | Exercise 6 in one visual |

Add a text box: "Synthetic practice data, Jan to Sep 2026. Not for business use."

**Steps.**

1. Power BI Desktop: Get data > SQL Server (Import mode) and select the views, or Get data > Excel workbook and select your result tables. Shape types in Power Query, then Close & Apply.
2. Model view: create the relationships; check cardinality and direction. Create the Calendar table (Modeling > New table) and mark it as the date table (Table tools > Mark as date table).
3. Create the measures (Home > New measure). Format the rates as percentages.
4. Build the visuals per the layout spec.
5. Tie out: with no slicers, each card must equal your Exercise 2, 5 and 6 answers. Then pick one origin and recheck Total Duty against a SQL query with the same filter.
6. Save the .pbix to [COMPANY: your OneDrive working folder]. Do not publish it to a shared workspace.

If Power BI Desktop is not installed yet (AR-09), build the model in Excel: Power Pivot > Manage, add the tables to the Data Model and create the relationships. Excel cannot create DAX calculated tables, so make the Calendar with Design > Date Table > New (it creates the table and marks it as the date table) and use its Month column. Build ScenarioLines with the Exercise 6 Power Query alternative. Write the measures in the Calculation Area and show them in a PivotTable; the measure DAX is the same.

**Deliverable.** The .pbix (or Excel file), a screenshot in OneNote, the measure list with a one-line definition each, and a tie-out table: measure, Power BI value, SQL or Excel value, difference.

**Check yourself.** Each card ties to your earlier answer. You can explain why the import_country slicer changes Total Duty but not PPV % (receipts are US only and have no import country), and why the month slicer does not change Scenario Impact (it is an annualized figure on a table with no Calendar relationship).

**Stretch.** Hire B: add a what-if parameter for the additional rate and show Scenario Impact at that rate; show duty by month with a marker at 2026-06-01; write a measure for PPV $ excluding outliers using CALCULATE and explain the filter it adds. Hire A: add a drill-through page listing the Exercise 3 mismatches for a selected broker.

## Exercise 8: One-page findings memo to the Manager

W4 · Both, written individually · 1.5 h · Reviewed by the Manager in the W4 work review

**Goal.** One page that tells the Manager what Exercises 1 to 6 found, how big it is, how sure you are, and what should happen next. Written for a reader who will not open your data.

**Business context.** An analysis only matters if someone acts on it. Your day-30 small real analysis (A30-5 and B30-5) uses this format, and so will every Research brief cover note and every PPV explanation you send to Finance.

**Structure.**

- **Header:** To, From, Date, Subject (name the data and the period).
- **Bottom line:** three bullets, each with a number.
- **Findings:** up to five. For each: what you found, how big it is, the evidence (query or tab), and how confident you are.
- **Recommended actions:** each with an owner by role (Research, Standard Cost, Senior, Manager) and a date.
- **Method and controls:** sources, period, cleaning steps, control totals, who reviewed the queries.
- **Limits and caveats:** what the numbers do not cover.
- **Open questions:** what you need from the Manager or the Senior.

Rules: one page (about 400 words). Round for reading ($31.4K), but every number must trace to a saved query. Separate fact from inference ("the pattern suggests"). Say it is synthetic practice data. No acronym without its meaning on first use.

**Deliverable.** The memo on a OneNote page in 07 Analytics, with links to the saved queries.

**Check yourself.** Could the Manager forward it unchanged? Does every action have an owner? Does every number trace to a query?

**Stretch.** Write the five-line version you would post as a Jira comment, and give the two-minute verbal version at the Friday teach-back.

## Exercise 9: KPI design

W7 · Both, each for their own process · 1.25 h · Post by 12:00 Wed 12/2; reviewed by the Senior in the W7 office hours that afternoon

**Goal.** Write 3 or 4 KPIs for your primary process with the KPI definition checklist below. Then compute two of them on the practice data and say what each one tells the process owner.

**Business context.** Your SOP needs KPIs with a definition, a target and a source (`docs/templates/knowledge/process-sop.md` Section 10), and your SOP v1.0 is day-90 evidence. A metric is any number you track. A KPI is a metric tied to an objective, with a target, an owner and a time frame, and someone acts when it moves. Power BI builds a KPI visual the same way: a value, a target and a status. Most arguments about a KPI are about its definition, not its arithmetic: which items count, which dates, what happens to open items. So write the definition first and compute second.

**Data needed.** work_items (a fictional Jira export of the team's Research and Standard Cost work, status on 2026-09-30). Hire A: practice.v_rate_audit (Exercise 3). Hire B: practice.v_ppv (Exercise 5).

**The KPI definition checklist.** Fill in every field for every KPI.

| Field | What to write | Example: Research on time |
|---|---|---|
| Name and ID | Short and unambiguous | R-KPI-1 Research items released on time |
| Decision it supports | Who acts, and what they do when it moves | The Manager rebalances Research work if it is below target two months running |
| Formula | Numerator and denominator in words. A ratio of sums, never an average of ratios | Items released on or before their due date, divided by items due in the period |
| Grain and filters | What one row is; what is in and what is out | One Jira item; process = Research; due date in the period. An open item past its due date counts as late; an item not yet due is left out |
| Data source and refresh | Table or view, and when it refreshes | Practice: work_items. Real: [COMPANY: Jira project and filter] |
| Owner | One role, accountable | Research process owner (Hire A from day 90) |
| Target and thresholds | Target; what is green, amber, red; whether higher is better | [COMPANY: target]. For practice: green 90% or more, amber 80–90%, red below 80%; higher is better |
| Frequency and time frame | How often it is computed, over what window, and where it is reviewed | Monthly, rolling 3 months, in the Manager 1:1 |
| Leading or lagging | Does it warn early, or report a result? | Lagging |

Two tests for each KPI:

- **SMART.** Doran (1981) wrote it as Specific, Measurable, Assignable, Realistic, Time-related; later versions say Achievable, Relevant and Time-bound. Assignable is the letter teams forget: a KPI without an owner is just a metric.
- **Leading or lagging.** A lagging KPI reports a result that has already happened (on time, PPV %). A leading KPI warns before the result moves (for example, the share of in-scope items with a confirmed HTS before an action takes effect). A good set has both.

**Part A: define your KPIs (about 35 minutes).** Write 3 or 4 KPIs for your process (Hire A: Research; Hire B: Standard Cost). Include at least one timeliness KPI, one quality or control KPI and one leading KPI. Use these candidates or write your own:

| Process | Candidate KPI | Leading or lagging | Practice data |
|---|---|---|---|
| Research | Research items released on time | Lagging | work_items |
| Research | Median turnaround, received to released, in business days | Lagging | work_items |
| Research | Broker filing accuracy: audited lines where the broker applied the expected rate | Lagging | v_rate_audit |
| Research | Share of clean entry lines whose item has an HTS in the master | Leading | v_entry_lines_clean, items |
| Standard Cost | Standard Cost items released on time (models, PPV explanations, cost updates) | Lagging | work_items |
| Standard Cost | Standard cost accuracy: share of standard value received at a landed cost within 5% of standard | Leading | v_ppv |
| Standard Cost | PPV % excluding outliers | Lagging | v_ppv |
| Both | Releases with a checker sign-off on or before the release date | Lagging (control) | work_items |

**Part B: compute two (about 40 minutes).**

- **KPI 1, both hires:** on time for your own process (Hire A: process = Research; Hire B: process = Standard Cost), in total and by item_type, for items due from 2026-01-01 to 2026-09-30.
- **KPI 2, Hire A:** broker filing accuracy = Match lines divided by Match + Over + Under lines in v_rate_audit, in total, by broker and by month.
- **KPI 2, Hire B:** standard cost accuracy = standard value of the receipts whose actual_landed_unit_cost is within 5% of std_cost, divided by all standard value received, without the 12 outlier receipts (as in Exercise 5), in total and by month.

**Rules for the work_items KPIs.**

- Status is as of 2026-09-30. A blank released_date means the item is still open. A comparison with a blank (NULL) date is never true, so an open item fails `released_date <= due_date`. That is right for an open item past its due date. Decide, and write down, what you do with open items that are not yet due.
- Business days are Monday to Friday with no holiday calendar (every date in work_items is a weekday). Turnaround = business days after received_date up to and including released_date. A real KPI uses [COMPANY: holiday calendar].

**Steps: SQL Server.**

1. Profile work_items: rows by process and item_type, open items and their due dates. Write the counts down.
2. On time, by process. Then add item_type to the GROUP BY.

```sql
SELECT process,
       COUNT(*) AS items_due,
       SUM(CASE WHEN released_date <= due_date THEN 1 ELSE 0 END) AS on_time
FROM practice.work_items
WHERE due_date BETWEEN '2026-01-01' AND '2026-09-30'
GROUP BY process;
```

3. List the late items and say why each is late: released late, or open and past due. Use action_ref: when a brief is late, what happens to its $ model?
4. Turnaround: `DATEDIFF(day, received_date, released_date) - 2 * DATEDIFF(week, received_date, released_date)` gives the business days when both dates are weekdays (DATEDIFF with week counts the week boundaries crossed, and here each one is a weekend). Get the median with `PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY ...) OVER (PARTITION BY process)` and SELECT DISTINCT, and compare it with AVG.
5. KPI 2. Hire A: from v_rate_audit, `WHERE audit_status IN ('Match', 'Over', 'Under')`, divide the Match lines by all these lines, in total, by broker and by month. Hire B: from v_ppv, `WHERE is_outlier = 0`, sum std_value_usd where `ABS(actual_landed_unit_cost - std_cost) <= 0.05 * std_cost` and divide by all std_value_usd, by month. Multiply, don't divide, in the test.

**Steps: Excel and Power Query.**

1. Load tbl_work_items to a sheet. Add columns: due_in_period `=AND([@due_date]>=DATE(2026,1,1), [@due_date]<=DATE(2026,9,30))`, on_time `=AND([@released_date]<>"", [@released_date]<=[@due_date])` and turnaround_bd `=IF([@released_date]="", "", NETWORKDAYS([@received_date], [@released_date]) - 1)`. NETWORKDAYS counts both end dates, hence the - 1.
2. On time = `COUNTIFS([process], "Research", [due_in_period], TRUE, [on_time], TRUE) / COUNTIFS([process], "Research", [due_in_period], TRUE)`, with the table name in front of each column.
3. Median turnaround: `=MEDIAN(IF((tbl[process]="Research") * (tbl[released_date]<>""), tbl[turnaround_bd]))`. Excel 365 calculates it as written; older Excel needs Ctrl+Shift+Enter. Use AVERAGEIFS for the mean.
4. KPI 2. Hire A: pivot your Exercise 3 audit query, audit_status by broker_id and by month. Hire B: in your Exercise 5 query add a custom column `within_5pct = Number.Abs([actual_landed_unit_cost] - [std_cost]) <= 0.05 * [std_cost]`, then pivot std_value by month and within_5pct, with is_outlier = FALSE as a filter.

**Deliverable.** A KPI definition sheet with one checklist table per KPI (3 or 4 KPIs); the two computed KPIs, in total and by type, broker or month; and three lines for each: what it says, what the owner should do now, and one thing the definition hides.

**Check yourself.** On-time items + released late + open past due = items due in the period. Research and Standard Cost rows add up to all of work_items. Change one definition choice (drop open items, or count by release date instead of due date) and say how much the KPI moves. Hire A: Match + Over + Under = the audited lines in Exercise 3. Hire B: receipts inside and outside the 5% band add up to the Exercise 5 receipts excluding outliers.

**Stretch.** (a) Both: compute the control KPI (sign-off on or before release). Name the items that fail and explain why "has a sign-off" is a different KPI. (b) Both: compute the median and the mean turnaround for your process and explain the gap. Which one goes in the SOP, and why? (c) Hire B: tariff-model turnaround end to end, in business days from the brief's received_date to its $ model's released_date, per action_ref. Who owns that KPI, and which part of it can Standard Cost control? (d) Copy your KPIs into Section 10 of your SOP draft.

## Exercise 10: Star-schema model in Power BI

W8 · Both (Hire B goes deeper) · 1.5 h · Post by Tue 12/8; reviewed by the Senior in the W8 office hours (Wed 12/9)

**Goal.** Rebuild the entry-line data as a star schema you could hand to the reporting team: the grain declared in writing; one fact table and three dimension tables (item, date, broker); a marked date table; one-to-many, single-direction relationships; and five measures, including a prior-month comparison. Explain why each one is a measure and not a calculated column.

**Business context.** Exercise 7 got the numbers right with shortcuts: chapter and origin were copied onto the fact table so that the UNK rows would show, and the import country came from the fact. That works for one page. It breaks when a second fact table or a second report arrives. Reporting backlog items (M8, from W10) and Hire B's reusable asset (B60-8) need models built the standard way, in Kimball's four steps and in this order: choose the business process, declare the grain, identify the dimensions, identify the facts. Not declaring the grain first is, in Kimball's words, the most frequent design error.

**What is new compared with Exercise 7.**

| Topic | Exercise 7 | Exercise 10 |
|---|---|---|
| Grain | Implied | Written down before anything is built |
| Chapter and origin | Columns copied onto EntryLines | Attributes of the Item dimension, where they belong: they come from the item master |
| Lines whose item is not in items | A (Blank) member in the Items slicers | "Not in item master" rows added to the Item dimension, so every fact row finds its item |
| Supplier country | Not in the model | Flattened into the Item dimension, with no separate Supplier table |
| Import country | A column on EntryLines | An attribute of the Broker dimension |
| Date table | Date and Month | Year, Quarter, Month, Month number and Month name; marked; auto date/time off |
| Measures | Totals and ratios | Adds a prior-month comparison (CALCULATE with DATEADD) and a month-on-month change (DIVIDE) |

**Data needed.** v_entry_lines_clean, entries, items, suppliers, brokers. Or your Power Query lines_clean and the same tables.

**Model.**

- **Grain.** Write it in your notes before you build: one row per customs entry line as filed by the broker (entry_no + line_no), after the duplicate copies are removed. Every column on the fact table must be true at that grain.
- **FactEntryLine:** entry_no, line_no, item_id, entry_date, broker_id, qty, entered_value, duty_amount, duty_rate_applied, program_claimed. entry_no and line_no stay on the fact as a degenerate dimension (identifiers with no table of their own). duty_rate_applied is a rate: keep it for drill-down, but never sum it.
- **DimItem:** item_id (the key: one row per value), description, hts10, hts_chapter (UNK when hts10 is missing), country_of_origin, usmca_eligible_flag, supplier_country, std_cost, item_status. Add one row for each item_id that appears in the clean lines but not in items, with item_status and description "Not in item master" and UNK for chapter, origin and supplier country. Kimball's rule: give a missing dimension value its own "unknown" row instead of leaving the key unmatched.
- **DimBroker:** broker_id, broker_name, import_country. In this data each broker files in one country, so import country can be a broker attribute. If a broker filed in two countries, import country would need its own dimension.
- **DimDate:** built in DAX for 2026, with Year, Quarter, Month (first day of the month), Month number and Month name; marked as the date table.
- **Relationships:** DimItem[item_id], DimBroker[broker_id] and DimDate[Date] each one-to-many to FactEntryLine, single direction.
- **Bus matrix:** two rows (customs entry lines; PO receipts from Exercise 5) and three columns (Date, Item, Broker). Mark which dimensions each process uses. The shared ones are the conformed dimensions.

**Measures to write.** Write them yourself; the Senior checks them against the reference DAX.

| Measure | Definition |
|---|---|
| Total Entered Value | Sum of entered_value |
| Total Duty | Sum of duty_amount |
| Effective Duty Rate | Total Duty / Total Entered Value, with DIVIDE |
| Duty Prior Month | Total Duty in the month before, with CALCULATE and DATEADD on DimDate[Date] |
| Duty MoM % | (Total Duty - Duty Prior Month) / Duty Prior Month, with DIVIDE |

Hint: `DATEADD(DimDate[Date], -1, MONTH)` returns the dates of the current filter context shifted back one month. Use it as the filter argument of CALCULATE.

**Layout (one page).** A matrix with DimDate Month on rows and the five measures as values; slicers on DimBroker import_country, DimItem country_of_origin and DimItem hts_chapter; a card for Total Duty; and the text box "Synthetic practice data, Jan to Sep 2026. Not for business use."

**Steps: SQL Server (shape the star).**

1. Write the grain statement and the bus matrix first.
2. Create `practice.v_dim_item`: items joined to suppliers (for supplier_country), with `COALESCE(LEFT(hts10, 2), 'UNK') AS hts_chapter` and item_status 'In item master'. Then UNION ALL one row per item_id in v_entry_lines_clean that is not in items (NOT EXISTS), with the "Not in item master" values.
3. Create `practice.v_dim_broker` from brokers and `practice.v_fact_entry_line` from v_entry_lines_clean joined to entries (for entry_date and broker_id).
4. Integrity checks, and write the results down: the dimension key is unique (`COUNT(*)` = `COUNT(DISTINCT item_id)`); every fact row finds its item and its broker (a NOT EXISTS count of 0); the fact has as many rows as v_entry_lines_clean.
5. Tie-out query for the prior month: monthly duty, with `LAG(duty) OVER (ORDER BY month_start)` as the prior month. LAG takes the previous row, which is the previous month only because every month has data. DATEADD on a date table does not depend on that.

**Steps: Power BI Desktop.**

1. Get data > SQL Server (Import mode), the three views. No SQL: build DimItem in Power Query (items merged with suppliers; then Merge Queries, lines_clean to items, Left Anti, keep item_id, Remove Duplicates, add the "Not in item master" columns, and Append it to the items query). Name the queries FactEntryLine, DimItem and DimBroker.
2. Turn off auto date/time for this file (File > Options and settings > Options > Current file > Data load). Otherwise Power BI adds a hidden date table for every date column.
3. Modeling > New table: DimDate, from `CALENDAR(DATE(2026, 1, 1), DATE(2026, 12, 31))` with ADDCOLUMNS for the other columns. Sort Month name by Month number (Column tools > Sort by column). Mark it as the date table (Table tools > Mark as date table) on the Date column.
4. Model view: create the three relationships. Check that each is one-to-many with a single cross-filter direction.
5. Home > New measure, five times. Format the rate and the MoM % as percentages.
6. Build the page and tie out: with no slicers, Total Duty and Effective Duty Rate equal your Exercise 2 grand total; each month's Total Duty and Duty Prior Month equal your LAG query.
7. Save the .pbix to [COMPANY: your OneDrive working folder]. Do not publish it to a shared workspace.

Menu names are as of Oct 2026; if one has moved, check https://learn.microsoft.com/en-us/power-bi/transform-model/desktop-date-tables and https://learn.microsoft.com/en-us/power-bi/guidance/auto-date-time.

If Power BI Desktop is not available, build the same model in Excel Power Pivot as in Exercise 7: make the date table with Design > Date Table > New, and write the same measures (DATEADD works there too).

**Deliverable.** The .pbix, the grain statement, the bus matrix, a screenshot of the model view, the measure list, and a tie-out table (month, Total Duty, Duty Prior Month, Duty MoM %, SQL value, difference). Add five lines on why Effective Duty Rate and Duty Prior Month are measures and not calculated columns: what each would show as a column, and why.

**Check yourself.** With no slicers, the card equals your Exercise 2 grand total. The UNK chapter row has the same lines and duty as in Exercise 2, and there is no (Blank) row anywhere. DimItem rows = items rows + the orphan item IDs you found in Exercise 1. The nine monthly Total Duty values add up to the card. January's Duty Prior Month is blank and you can say why; February's equals January's Total Duty.

**Stretch.** (a) Hire B: add Receipts (from v_ppv) as a second fact, related to DimItem and DimDate, and write PPV % with DIVIDE. Show that a DimItem country_of_origin slicer filters both facts while a DimBroker slicer filters only the entry lines, and say why. (b) Hire A: write Duty Prior Quarter (DATEADD by QUARTER) and find the chapter and origin that explain most of the Q3 vs Q2 change. Why does this view not show the June rate change? (c) Both: what would `CALCULATE([Total Duty], SAMEPERIODLASTYEAR(DimDate[Date]))` show on this data, and why? (d) Both: what does Duty Prior Month show in the matrix total row, where no single month is selected? Explain it, and write a version that stays blank there.

## Exercise 11: Variance statistics

W9 · Both · 1.25 h · Submit by Thu 12/17; reviewed by the Senior in writing in W10 (no office hours in W9)

**Goal.** Part A: split the change in US duty paid between Q1 and Q3 2026 into a rate (price) effect and a value (quantity) effect, then split the value effect into mix and volume. Part B: find the unusual receipt lines with the 1.5 x IQR rule and with a z-score, compare both with Exercise 5's business rule, and decide which lines need investigation. Deleting any of them is not an option; say why.

**Business context.** "US duty is up this quarter. Why?" is a question Finance asks, and "rates went up" is half an answer. A decomposition says how much came from rates, how much from importing more, and how much from importing a different mix. Research owns the rate part (the WHAT); Standard Cost turns it into cost and PPV (the $). The statistics part matters as much. An outlier rule finds lines that are unusual; the business decides which are wrong. NIST's guidance is to investigate outliers, and to correct or remove a value only when it is shown to be in error. In cost data, many unusual lines are real price changes: exactly the ones a standard cost update needs.

**Data needed.** Part A: v_entry_lines_clean, entries, items. Part B: v_ppv (Exercise 5).

**Rules, Part A.**

- Scope: clean lines with import_country = US. Base period Q1 (2026-01-01 to 2026-03-31); current period Q3 (2026-07-01 to 2026-09-30). Groups: HTS chapter and origin, as in Exercise 2, UNK included.
- For each group and period: entered value V, duty D and effective rate r = D / V.
- Rate effect = sum over groups of (r in Q3 - r in Q1) x V in Q3. Value effect = sum of (V in Q3 - V in Q1) x r in Q1. Rate effect + value effect = Q3 duty - Q1 duty.
- Mix and volume. The data allows a mix split because value is in dollars for every group. Base mix share m = the group's Q1 value / total Q1 value. Volume effect = sum of (total Q3 value x m - V in Q1) x r in Q1. Mix effect = sum of (V in Q3 - total Q3 value x m) x r in Q1. Mix + volume = value effect.
- Positive = more duty (unfavorable). This is one standard convention, adapted from ACCA's materials mix and yield method: rate valued at current value, value valued at base rate. Other conventions split the same total differently, so name yours. The split also depends on the grouping: name that too.

**Rules, Part B.**

- ratio = actual_landed_unit_cost / std_cost on all 1,500 receipts. Keep the 12 Exercise 5 outliers in: you are testing the rules.
- 1.5 x IQR rule (Tukey fences): take the first and third quartiles Q1 and Q3 of the ratio (here Q1 and Q3 are quartiles, not the quarters of Part A) with linear interpolation (QUARTILE.INC in Excel, PERCENTILE_CONT in SQL Server, PERCENTILE.INC in DAX). IQR = Q3 - Q1. Flag a ratio below Q1 - 1.5 x IQR or above Q3 + 1.5 x IQR. Beyond 3 x IQR is an extreme outlier. Tools differ slightly in how they compute quartiles, so say which tool you used.
- z-score: z = (ratio - mean) / sample standard deviation (STDEV.S in Excel, STDEV in T-SQL). Flag |z| > 3.
- Never delete or overwrite a receipt. Flag it, investigate it, report it separately.

**Steps: SQL Server, Part A.**

1. One query with conditional aggregation: per chapter and origin, the Q1 and Q3 sums of entered_value and duty_amount (`SUM(CASE WHEN e.entry_date BETWEEN '2026-01-01' AND '2026-03-31' THEN el.entered_value ELSE 0 END)` and so on). Check that the groups add up to the US quarter totals.
2. Add the rates and the base mix with window totals (`SUM(v_q1) OVER ()`). Convert to float before dividing, for example `CAST(d_q1 AS float) / NULLIF(v_q1, 0)`. With two DECIMAL sums SQL Server keeps only 6 decimal places of the quotient, and multiplying that rounded rate by a large value moves the effects.
3. Compute the four effects per group, sum them, and check both identities.
4. List the top 5 groups by absolute rate effect and by absolute mix effect. For the biggest rate effect, compare with the 2026-06-01 change in duty_rates_reference. For any other large one, drill down to item: is it a real rate change, or a change in which items (and which claims) make up the group?

**Steps: SQL Server, Part B.**

1. From v_ppv: `CAST(actual_landed_unit_cost AS float) / NULLIF(std_cost, 0) AS ratio`, with receipt_id, item_id, receipt_date, country_of_origin, hts_chapter, is_outlier and ppv_usd.
2. One row of statistics: `SELECT DISTINCT PERCENTILE_CONT(0.25) WITHIN GROUP (ORDER BY ratio) OVER () AS q1`, the same with 0.75, `AVG(ratio) OVER ()` and `STDEV(ratio) OVER ()`.
3. CROSS JOIN the statistics to the receipts and add tukey_flag and z_flag. Count the receipts by is_outlier, tukey_flag and z_flag.
4. Group the flagged receipts that are not business-rule outliers: CN chapters 73 and 76 on or after 2026-06-01, then the rest by item with the first and last flagged date. A run of flags on one item from a date onward is a price change, not a bad line.
5. Recompute the mean, SD and z without the 12 business-rule outliers. What changes?

**Steps: Excel.**

1. Part A: from your US clean lines, insert a PivotTable (rows hts_chapter and country_of_origin in tabular form, columns quarter, values Sum of entered_value and Sum of duty_amount; filter the quarters to 1 and 3). In Power Query, Add Column > Date > Quarter > Quarter of Year gives the quarter. Copy the pivot and Paste Values to a calculation sheet. Add formula columns for both rates, the base mix share and the four effects, and total them.
2. Part B: add a ratio column to your Exercise 5 table. In cells: `=QUARTILE.INC(tbl[ratio], 1)`, `=QUARTILE.INC(tbl[ratio], 3)`, `=AVERAGE(...)`, `=MEDIAN(...)`, `=STDEV.S(...)`. Add flag columns and count them with COUNTIFS. Pivot the flags by is_outlier, and the flagged receipts by item and month.

**Deliverable.** Part A: a bridge from Q1 duty to Q3 duty (rate effect, mix effect, volume effect, with the check), the top groups, and three sentences on what drove the change. Part B: a counts table (business rule, IQR rule, z-score, and their overlap), the flagged receipts grouped by likely cause with an action for each (who checks what, and by when), and four sentences: why the z-score found fewer, which lines need investigation, which are explained, and why deleting them would be wrong.

**Check yourself.** Rate + value effect = Q3 duty - Q1 duty, to the cent. Mix + volume = value effect. Volume effect = (total Q3 value - total Q1 value) x the total Q1 rate, whatever grouping you use. Flagged + not flagged = 1,500 for each rule. Compare the three flag sets receipt by receipt: you can say which receipts each rule catches that the others miss, and why.

**Stretch.** (a) Hire A: redo Part A grouped by origin only, then by item. Explain why the rate effect changes, and why the item-level version needs a rule for items imported in only one of the two quarters. (b) Hire B: for the CN chapter 73 and 76 items, split the change in landed spend on receipts (actual_landed_unit_cost x qty, outliers excluded) between Q1 and Q3 into price and quantity, item by item. Why is there no mix split here? Compare the price effect with the change in spend and explain the difference. (c) Both: compute NIST's modified z-score, M = 0.6745 x (ratio - median) / MAD, where MAD is the median absolute deviation from the median, and flag |M| > 3.5. How many does it flag, and why is it not fooled the way the z-score is?

## Review guide for the Senior

| Criterion | What good looks like |
|---|---|
| Correct | Numbers match the answer key, or the difference is explained and the explanation is right |
| Controlled | Row counts recorded before and after each join; the clean control total ties across exercises |
| Readable | Header comments, named CTEs or Power Query steps, no unexplained magic numbers |
| Careful with NULLs and grain | Missing HTS, orphans and duplicates are counted and reported, not silently dropped |
| Business sense | Each result has a "so what" for Research or Standard Cost and a sensible next step |
| Boundaries | No broker contact, no system writes, corrections escalated to the Senior |
| Definitions first (Exercises 9 to 11) | Every KPI fully defined before it is computed; the grain written before the model is built; the decomposition convention and grouping named |
| Statistics in context | Flags are investigated and explained, never deleted; robust measures (median) used where the data is skewed |

## Related files

- In the onboarding folder: Practice-Data.xlsx, the practice-data folder (CSVs and load_practice_data.sql), Tariff-Impact-Model-Template.xlsx, and BSA-Onboarding.apkg (Unit 04 › Data, SQL and Power BI; Unit 06 › Analytics depth: models, measures, KPIs; more SQL and Power BI cards in Reference › BSA craft and data)
- Trainer-only ([COMPANY: trainer-only location]): the answer key, not shared before the day-30 review (its Exercise 9 to 11 sections not before the day-60 review), and the data generator script, not shared before the day-60 review
- `docs/primers/customs-trade-compliance-primer.md`, `docs/primers/trade-systems-gtm-e2open-primer.md`
- `docs/templates/domain/tariff-impact-model-guide.md`, `docs/templates/domain/standard-cost-update-checklist.md`
- `docs/05-time-management.md` (stuck rule, question log, office hours)
- `docs/templates/knowledge/process-sop.md` (Section 10, KPIs), `docs/primers/data-platform-primer.md` (where you may run SQL), `docs/primers/copilot-chat-guide.md` (AI output is a draft)
