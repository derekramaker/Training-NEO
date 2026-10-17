PRACTICE DATA: SYNTHETIC. Invented for training. Not real items, suppliers, brokers, entries, values, costs or rates.
HTS codes look real (first 6 digits are real HS subheadings, last 4 are random). Synthetic: do not use for classification.
Duty rates and tariff scenarios are invented. They are not the real rates or actions for these codes.
Generator: the team's practice-data script (trainer-only), version 1.1 (2026-10-08), seed 20261019. Same output on every run.
Entry and receipt dates: 2026-01-02 to 2026-09-30 (9 months). All money is USD.
Exercises: docs/analytics/practice-exercises.md (Analytics Practice Pack in OneNote). The answer key is trainer-only: the Senior reviews your results against it.

TABLES (one row = ...; key)
items: one item; item_id. hts10 and country_of_origin are the classification master. usmca_eligible_flag Y = USMCA certification on file. std_cost = US org standard cost per unit (includes duty and freight). list_price = sell price per unit.
suppliers: one supplier; supplier_id. supplier_country is where the supplier is, not where the goods are made.
brokers: one customs broker; broker_id.
entries: one customs entry (US entry, Canadian CAD, Mexican pedimento); entry_no. import_country = country the goods entered.
entry_lines: one line on an entry, as the broker filed it; entry_no + line_no (meant to be unique). program_claimed = USMCA, or blank when no preference was claimed. duty_amount = entered_value x duty_rate_applied, rounded to the cent.
duty_rates_reference: the rate we expect for an import country + hts10 + origin, effective-dated (effective_from to effective_to, inclusive); key = those 3 columns + effective_from. expected_rate = base_rate + additional_rate. It is the non-preferential rate: a valid USMCA claim in this data means 0%.
receipts: one PO receipt line into the US warehouse; receipt_id. actual_landed_unit_cost = actual cost per unit including freight and duty.
tariff_scenario: one row per scenario + HTS prefix + origin. Fictional proposed actions for Exercise 6. If several prefixes in one scenario match an item, the longest prefix wins. usmca_exempt Y = items with usmca_eligible_flag Y are exempt.

RATES are decimals: 0.0340 means 3.4%.
LOADING: Excel/Power Query: use Practice-Data.xlsx (one Excel table per sheet). SQL Server: run load_practice_data.sql in a scratch database, or import the CSVs (see the exercises, Setup).
Keep hts10, item_id and other codes as TEXT. If Excel turns hts10 into a number, re-import and set the column type to Text.
The data contains deliberate data-quality problems, like real data. Finding them is part of the exercises.

ADDED IN VERSION 1.2 (2026-10-17): the work_items table. The eight tables above are unchanged from version 1.1 (2026-10-08).
work_items: one work item (a fictional Jira issue) for the team's Research or Standard Cost work, Jan to Sep 2026; work_item_id. Status as of 2026-09-30. released_date blank = still open. checker_signoff_date blank = no documented checker sign-off. errors_after_release = material errors found after release (blank while the item is open). action_ref links a brief and its $ model. All dates are business days (Monday to Friday). Used in Exercise 9.
