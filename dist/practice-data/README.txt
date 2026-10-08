PRACTICE DATA: SYNTHETIC. Invented for training. Not real items, suppliers, brokers, entries, values, costs or rates.
HTS codes look real (first 6 digits are real HS subheadings, last 4 are random). Synthetic: do not use for classification.
Duty rates and tariff scenarios are invented. They are not the real rates or actions for these codes.
Generator: data/analytics/generate_practice_data.py, version 1.0 (2026-10-08), seed 20261019. Same output on every run.
Entry and receipt dates: 2026-01-02 to 2026-09-30 (9 months). All money is USD.
Exercises: docs/analytics/practice-exercises.md. Answers: docs/analytics/answer-key.md (Manager and Senior).

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
