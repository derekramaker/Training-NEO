# Analytics Practice Pack: Answer Key

Last updated: 2026-10-08 · Owner: BSA Manager

- **Purpose:** exact answers, reference T-SQL and DAX, and what good looks like for the eight exercises in `docs/analytics/practice-exercises.md`. Also lists the planted data problems and the "fingerprint" numbers that show which mistake a learner made.
- **Who uses it:** trainer-only. The Senior, to review Exercises 1 to 7; the Manager, to review the Exercise 8 memo and the day-30 evidence (A30-5 and B30-5). The hires never get this key or `data/analytics/generate_practice_data.py` before the day-30 review. When you review a posted exercise, tell the hire which results differ from the key, not the right numbers; the hire finds and explains each cause.
- **When:** Thu 10/29 (Exercises 1-3), W3 (Exercises 4-6), W4 (Exercises 7-8). The build writes this page to `dist/trainer-only/answer-key.docx`. Keep it in [COMPANY: trainer-only location], never in the hires' OneNote sections or the onboarding folder (`docs/02-weeks-1-2-schedule.md`, Manager prep). After the day-30 review the Manager decides whether to share it.

## How to use this key

- The numbers are for the data built by `data/analytics/generate_practice_data.py`, version 1.1, seed 20261019 (the data rows are the same as version 1.0). The generator is deterministic: rerunning it gives byte-identical CSV, SQL, README and xlsx files. If anyone changes the generator, recompute this key; the generator stops with an error if a planted count changes.
- How the numbers were verified: recomputed on 2026-10-08 with fresh pandas code from `dist/practice-data/*.csv`, after the last generator change. The T-SQL on this page reproduced them to the cent on SQL Server 2022 (Developer edition) loaded with `dist/practice-data/load_practice_data.sql`. The later T-SQL edits (NULLIF in denominators, `12.0 / 9`, qty in `v_scenario_lines`, the copy check in Exercise 1) do not change any result but have not been rerun on SQL Server: rerun them once when you load the data. The Excel formula routes for Exercises 3 and 6 (SUMIFS with date criteria; SUMIFS with wildcards) were recalculated in LibreOffice with plain cell ranges and match; the structured-reference form shown in the exercises is the same formula. The DAX in Exercise 7 has not been run in Power BI; check it in W4.
- Tolerance: SQL and pandas agree to the cent. Excel sums of decimals may differ by 0.01 on large totals. Anything bigger is a mistake to explain.
- Money is USD. Percentages are rounded to 2 decimals unless stated.
- Review the method, not only the number: row counts recorded, control totals tied, NULLs and orphans reported.

## Planted problems at a glance

| Problem | Count | Where it shows | Found in |
|---|---|---|---|
| Duplicate entry lines (4 US entries loaded twice) | 24 extra rows | US26-00110, US26-00114, US26-00163, US26-00177 | Ex 1 |
| Entry lines whose item is not in items (orphans) | 4 lines, 3 item IDs | SYN-9001, SYN-9002 (2 lines), SYN-9003 | Ex 1, 2, 3 |
| Items with no HTS | 6 items, 94 clean lines | SYN-1034, 1051, 1097, 1100, 1105, 1120 | Ex 1, 2, 3, 6 |
| CN-origin items flagged USMCA-eligible | 2 items, 30 claim lines | SYN-1016, SYN-1143 | Ex 1, 4 |
| USMCA-origin items with no certification | 4 items | SYN-1104 (US), SYN-1132 (MX), SYN-1133 (CA), SYN-1149 (MX) | Ex 1, 4, 6 |
| Applied rate differs from expected rate | 49 lines: 7 over, 42 under | 44 US, 3 CA, 2 MX | Ex 3 |
| Invalid USMCA claims | 45 lines | 38 non-USMCA origin, 7 no certification | Ex 4 |
| Missed USMCA savings | 12 lines | Eligible, dutiable, no claim | Ex 4 stretch |
| Effective-dated reference rates | 11 combinations with 2 periods | US imports, CN origin, chapters 73 and 76, change on 2026-06-01 | Ex 3, 4 |
| Supplier country differs from origin | 24 items | Trading companies in HK and TW, a US distributor | Ex 1, 2 |
| Outlier receipts | 12 receipts | 9 at about 10x to 13x standard, 3 at 0.1x | Ex 5 |
| Overlapping scenario prefixes | 20 lines | SCN-01: 7318 and 731815 for CN | Ex 6 |

## Exercise 1: Data profiling

### Answers

| Table | Rows | NULLs |
|---|---|---|
| items | 150 | hts10: 6 |
| suppliers | 31 | none |
| brokers | 6 | none |
| entries | 400 (US 230, CA 95, MX 75) | none |
| entry_lines | 1,966 raw, 1,942 clean | program_claimed: 1,314 raw (1,296 clean) |
| duty_rates_reference | 228 | none |
| receipts | 1,500 | none |
| tariff_scenario | 11 | none |

- The NULLs in program_claimed are **expected**: they mean no preference was claimed. The 6 NULL hts10 values are **errors**.
- Duplicates: 24 keys appear twice, so 24 extra rows, all in 4 US entries with 6 lines each: US26-00110, US26-00114, US26-00163, US26-00177. The copies are exact (all columns identical: `SELECT DISTINCT *` gives 1,942 rows, the same as the distinct keys) and sit at the end of the file. They add $246,133.28 of entered value and $15,286.85 of duty.
- Totals: raw entered value $16,851,370.12 and duty $871,664.92; clean entered value **$16,605,236.84** and duty **$856,378.07** (the control total for every later exercise). Clean lines by import country: US 1,138, CA 444, MX 360.
- Orphans: 4 clean lines, $25,480.37 entered value, $993.73 duty.

| entry_no | line_no | item_id | entered_value | duty_amount |
|---|---|---|---|---|
| US26-00003 | 3 | SYN-9001 | 5,242.15 | 204.44 |
| US26-00050 | 3 | SYN-9002 | 1,789.15 | 69.78 |
| US26-00149 | 4 | SYN-9002 | 14,639.04 | 570.92 |
| US26-00167 | 6 | SYN-9003 | 3,810.03 | 148.59 |

- No entry line points to a missing entry, and every entry has lines. Every item has entry lines and receipts.
- Item master issues:

| item_id | Description | Origin | Flag | Issue |
|---|---|---|---|---|
| SYN-1034 | Plastic cable clip, pack of 50 | CN | N | HTS missing |
| SYN-1051 | Steel shelving unit, 5-tier | CN | N | HTS missing |
| SYN-1097 | Stainless threaded elbow, 1/2 in | IN | N | HTS missing |
| SYN-1100 | Hex bolt, zinc-plated steel, M6 x 30 mm, box of 100 | VN | N | HTS missing |
| SYN-1105 | Hex nut, steel, M6, box of 200 | VN | N | HTS missing |
| SYN-1120 | Oscillating floor fan, 18 in | CN | N | HTS missing |
| SYN-1016 | Slip-joint pliers, 10 in | CN | Y | Flag Y, origin outside USMCA |
| SYN-1143 | Duplex receptacle, 15 A tamper-resistant | CN | Y | Flag Y, origin outside USMCA |
| SYN-1104 | Cordless drill, 18 V | US | N | USMCA origin, no certification |
| SYN-1132 | Duplex receptacle, 15 A | MX | N | USMCA origin, no certification |
| SYN-1133 | Aluminum sheet pan, 13 x 18 in | CA | N | USMCA origin, no certification |
| SYN-1149 | Wall switch, 15 A single-pole | MX | N | USMCA origin, no certification |

- Supplier country differs from origin on 24 items: HK trading companies supplying CN goods (9), a TW trading company supplying CN goods (7) and VN goods (1), a US distributor supplying MX goods (7). This is **not an error**: origin is where the goods are made, not where the seller is. It is a trap for anyone who uses the supplier's country for tariff questions.
- All 144 non-NULL HTS codes are 10 digits. Entry dates run 2026-01-05 to 2026-09-30; receipt dates 2026-01-02 to 2026-09-30. program_claimed holds only 'USMCA' (646 clean lines) or NULL (1,296).
- Stretch (a): duty_amount equals ROUND(entered_value x duty_rate_applied, 2) on every line.

### Reference T-SQL

```sql
-- Purpose: Exercise 1 data profiling (answer key)
-- Source:  practice schema loaded by dist/practice-data/load_practice_data.sql
SELECT 'items' AS table_name, COUNT(*) AS row_count FROM practice.items
UNION ALL SELECT 'suppliers', COUNT(*) FROM practice.suppliers
UNION ALL SELECT 'brokers', COUNT(*) FROM practice.brokers
UNION ALL SELECT 'entries', COUNT(*) FROM practice.entries
UNION ALL SELECT 'entry_lines', COUNT(*) FROM practice.entry_lines
UNION ALL SELECT 'duty_rates_reference', COUNT(*) FROM practice.duty_rates_reference
UNION ALL SELECT 'receipts', COUNT(*) FROM practice.receipts
UNION ALL SELECT 'tariff_scenario', COUNT(*) FROM practice.tariff_scenario;

-- NULLs: COUNT(column) skips NULLs
SELECT COUNT(*) AS item_rows,
       COUNT(*) - COUNT(hts10) AS hts10_nulls,
       COUNT(*) - COUNT(country_of_origin) AS origin_nulls,
       COUNT(*) - COUNT(std_cost) AS std_cost_nulls
FROM practice.items;

SELECT COUNT(*) AS line_rows,
       COUNT(*) - COUNT(item_id) AS item_id_nulls,
       COUNT(*) - COUNT(program_claimed) AS program_claimed_nulls
FROM practice.entry_lines;

-- Duplicate keys
SELECT entry_no, line_no, COUNT(*) AS copies
FROM practice.entry_lines
GROUP BY entry_no, line_no
HAVING COUNT(*) > 1
ORDER BY entry_no, line_no;

SELECT COUNT(*) AS raw_rows,
       (SELECT COUNT(*) FROM (SELECT DISTINCT entry_no, line_no FROM practice.entry_lines) AS k) AS distinct_keys,
       (SELECT COUNT(*) FROM (SELECT DISTINCT * FROM practice.entry_lines) AS d) AS distinct_full_rows,   -- = distinct_keys: copies are exact
       SUM(entered_value) AS raw_entered_value,
       SUM(duty_amount) AS raw_duty
FROM practice.entry_lines;
GO
CREATE OR ALTER VIEW practice.v_entry_lines_clean AS
WITH numbered AS (
    SELECT el.*,
           ROW_NUMBER() OVER (PARTITION BY el.entry_no, el.line_no ORDER BY el.entry_no) AS copy_no
    FROM practice.entry_lines AS el
)
SELECT entry_no, line_no, item_id, qty, entered_value, duty_rate_applied, duty_amount, program_claimed
FROM numbered
WHERE copy_no = 1;
GO
SELECT COUNT(*) AS clean_rows, SUM(entered_value) AS clean_entered_value, SUM(duty_amount) AS clean_duty
FROM practice.v_entry_lines_clean;

-- Orphans
SELECT el.entry_no, el.line_no, el.item_id, el.entered_value, el.duty_amount
FROM practice.v_entry_lines_clean AS el
LEFT JOIN practice.items AS i ON i.item_id = el.item_id
WHERE i.item_id IS NULL
ORDER BY el.entry_no;

SELECT COUNT(*) AS lines_without_entry_header
FROM practice.v_entry_lines_clean AS el
WHERE NOT EXISTS (SELECT 1 FROM practice.entries AS e WHERE e.entry_no = el.entry_no);

-- Item master checks
SELECT item_id, description, country_of_origin, usmca_eligible_flag,
       CASE WHEN hts10 IS NULL THEN 'HTS missing'
            WHEN usmca_eligible_flag = 'Y' AND country_of_origin NOT IN ('US', 'CA', 'MX') THEN 'Flag Y, origin outside USMCA'
            WHEN usmca_eligible_flag = 'N' AND country_of_origin IN ('US', 'CA', 'MX') THEN 'USMCA origin, no certification'
       END AS issue
FROM practice.items
WHERE hts10 IS NULL
   OR (usmca_eligible_flag = 'Y' AND country_of_origin NOT IN ('US', 'CA', 'MX'))
   OR (usmca_eligible_flag = 'N' AND country_of_origin IN ('US', 'CA', 'MX'))
ORDER BY issue, item_id;

SELECT COUNT(*) AS bad_hts_format
FROM practice.items
WHERE hts10 IS NOT NULL AND (LEN(hts10) <> 10 OR hts10 LIKE '%[^0-9]%');

SELECT s.supplier_country, s.supplier_type, i.country_of_origin, COUNT(*) AS items
FROM practice.items AS i
JOIN practice.suppliers AS s ON s.supplier_id = i.supplier_id
WHERE s.supplier_country <> i.country_of_origin
GROUP BY s.supplier_country, s.supplier_type, i.country_of_origin
ORDER BY items DESC;

SELECT MIN(entry_date) AS first_entry, MAX(entry_date) AS last_entry FROM practice.entries;

SELECT COALESCE(program_claimed, '(NULL)') AS program_claimed, COUNT(*) AS lines
FROM practice.v_entry_lines_clean
GROUP BY program_claimed;

-- Stretch (a): arithmetic check, expect 0
SELECT COUNT(*) AS duty_amount_mismatches
FROM practice.v_entry_lines_clean
WHERE duty_amount <> ROUND(entered_value * duty_rate_applied, 2);
```

## Exercise 2: Duty paid by HTS chapter and country of origin

### Answers

Grand total (clean lines, all programs): 1,942 lines, entered value $16,605,236.84, duty **$856,378.07**, effective duty rate **5.16%**.

Top 10 chapter and origin combinations by duty:

| Chapter | Origin | Lines | Entered value | Duty paid | Eff. rate |
|---|---|---|---|---|---|
| 73 | CN | 126 | 1,277,353.17 | 175,677.53 | 13.75% |
| 85 | CN | 130 | 1,196,559.75 | 99,862.15 | 8.35% |
| 84 | CN | 68 | 704,448.07 | 81,227.44 | 11.53% |
| 82 | CN | 75 | 600,901.83 | 53,409.79 | 8.89% |
| 76 | CN | 50 | 390,125.59 | 50,972.50 | 13.07% |
| 39 | CN | 66 | 463,993.73 | 45,977.58 | 9.91% |
| 85 | KR | 81 | 932,489.30 | 30,633.85 | 3.29% |
| UNK | CN | 40 | 400,884.29 | 29,924.76 | 7.46% |
| 73 | VN | 60 | 510,393.25 | 28,125.94 | 5.51% |
| UNK | VN | 31 | 449,934.33 | 27,748.89 | 6.17% |

There are 52 chapter and origin combinations in total.

By chapter:

| Chapter | Lines | Entered value | Duty paid | Eff. rate |
|---|---|---|---|---|
| 73 | 296 | 2,801,938.88 | 220,945.77 | 7.89% |
| 84 | 363 | 3,261,568.52 | 144,152.60 | 4.42% |
| 85 | 376 | 3,807,192.60 | 141,277.94 | 3.71% |
| 82 | 199 | 1,496,266.97 | 106,682.39 | 7.13% |
| UNK | 98 | 1,072,848.20 | 67,327.84 | 6.28% |
| 39 | 169 | 1,103,607.05 | 58,699.20 | 5.32% |
| 76 | 119 | 890,749.73 | 52,892.37 | 5.94% |
| 83 | 38 | 301,191.50 | 20,677.59 | 6.87% |
| 63 | 44 | 306,986.48 | 17,188.28 | 5.60% |
| 94 | 117 | 1,092,460.18 | 17,130.09 | 1.57% |
| 42 | 35 | 122,747.66 | 5,509.35 | 4.49% |
| 40 | 88 | 347,679.07 | 3,894.65 | 1.12% |

By origin:

| Origin | Lines | Entered value | Duty paid | Eff. rate |
|---|---|---|---|---|
| CN | 655 | 5,576,219.97 | 579,514.22 | 10.39% |
| VN | 228 | 1,916,238.59 | 99,374.10 | 5.19% |
| IN | 105 | 759,713.73 | 42,727.17 | 5.62% |
| DE | 71 | 629,360.60 | 34,889.63 | 5.54% |
| TW | 105 | 981,659.44 | 34,043.91 | 3.47% |
| KR | 81 | 932,489.30 | 30,633.85 | 3.29% |
| IT | 36 | 289,848.11 | 13,673.77 | 4.72% |
| US | 208 | 1,657,872.27 | 10,385.54 | 0.63% |
| MX | 275 | 2,668,658.94 | 7,220.35 | 0.27% |
| CA | 174 | 1,167,695.52 | 2,921.80 | 0.25% |
| UNK | 4 | 25,480.37 | 993.73 | 3.90% |

By import country: US 1,138 lines, $9,795,831.25, duty $645,972.49 (6.59%); MX 360 lines, $3,099,323.83, $142,800.32 (4.61%); CA 444 lines, $3,710,081.76, $67,605.26 (1.82%).

- The UNK chapter (98 lines) is the 94 lines of the 6 items without HTS plus the 4 orphan lines. The UNK origin (4 lines) is the orphans.
- Good observations: CN is 68% of duty on 34% of value; chapter 73 from CN pays 13.75% because of the (fictional) additional duty; USMCA origins pay almost nothing because most of their lines claim USMCA; $1.07M of value (6.5%) sits in UNK and cannot be analyzed by chapter.
- Stretch (a): grouping by supplier country gives CN duty of $363,406.72 instead of $579,514.22, because 16 CN-origin items are bought through HK and TW trading companies. Wrong field for tariff questions: duties follow origin, not the seller's location.
- Stretch (b): duty by month is about $76K to $98K from January to May and $96K to $115K from June (June $108,481.90, July $114,871.89), after the fictional rate change.

### Reference T-SQL

```sql
-- Purpose: Exercise 2 duty by HTS chapter and origin (answer key)
-- Source:  practice.v_entry_lines_clean, practice.items, practice.entries
WITH lines AS (
    SELECT COALESCE(LEFT(i.hts10, 2), 'UNK') AS hts_chapter,
           COALESCE(i.country_of_origin, 'UNK') AS country_of_origin,
           el.entered_value,
           el.duty_amount
    FROM practice.v_entry_lines_clean AS el
    LEFT JOIN practice.items AS i ON i.item_id = el.item_id   -- LEFT keeps the 4 orphans
)
SELECT hts_chapter, country_of_origin,
       COUNT(*) AS lines,
       SUM(entered_value) AS entered_value,
       SUM(duty_amount) AS duty_paid,
       CAST(100.0 * SUM(duty_amount) / NULLIF(SUM(entered_value), 0) AS DECIMAL(9, 2)) AS effective_rate_pct
FROM lines
GROUP BY hts_chapter, country_of_origin
ORDER BY duty_paid DESC;

-- Chapter totals, origin totals and the grand total in one result
WITH lines AS (
    SELECT COALESCE(LEFT(i.hts10, 2), 'UNK') AS hts_chapter,
           COALESCE(i.country_of_origin, 'UNK') AS country_of_origin,
           el.entered_value, el.duty_amount
    FROM practice.v_entry_lines_clean AS el
    LEFT JOIN practice.items AS i ON i.item_id = el.item_id
)
SELECT COALESCE(hts_chapter, '(all)') AS hts_chapter,
       COALESCE(country_of_origin, '(all)') AS country_of_origin,
       COUNT(*) AS lines, SUM(entered_value) AS entered_value, SUM(duty_amount) AS duty_paid,
       CAST(100.0 * SUM(duty_amount) / NULLIF(SUM(entered_value), 0) AS DECIMAL(9, 2)) AS effective_rate_pct
FROM lines
GROUP BY GROUPING SETS ((hts_chapter), (country_of_origin), ())
ORDER BY CASE WHEN hts_chapter IS NULL AND country_of_origin IS NULL THEN 0
              WHEN country_of_origin IS NULL THEN 1 ELSE 2 END,
         duty_paid DESC;

SELECT e.import_country, COUNT(*) AS lines, SUM(el.entered_value) AS entered_value, SUM(el.duty_amount) AS duty_paid,
       CAST(100.0 * SUM(el.duty_amount) / NULLIF(SUM(el.entered_value), 0) AS DECIMAL(9, 2)) AS effective_rate_pct
FROM practice.v_entry_lines_clean AS el
JOIN practice.entries AS e ON e.entry_no = el.entry_no
GROUP BY e.import_country
ORDER BY duty_paid DESC;
```

## Exercise 3: Broker audit, applied rate vs expected rate

### Answers

Scope: 1,296 clean lines with no preference claimed. `WHERE program_claimed <> 'USMCA'` returns **0** rows, because a comparison with NULL is never true.

| Status | Lines | Entered value | Variance USD |
|---|---|---|---|
| Match | 1,149 | 9,769,640.55 | 0.00 |
| Over | 7 | 79,153.58 | +9,596.24 |
| Under | 42 | 326,545.70 | -40,993.91 |
| Not auditable: HTS missing | 94 | 1,047,367.83 | n/a |
| Not auditable: item not in master | 4 | 25,480.37 | n/a |
| Total | 1,296 | 11,248,188.03 | -31,397.66 net |

- Audited lines: 1,198 ($10,175,339.83). No line lacks a reference rate once the date condition is in place.
- Row-count control: joining the reference on the three keys alone (LEFT joins, as in the exercise steps) gives **1,403** rows for the 1,296 lines, because each of the 107 US lines of CN-origin chapter 73/76 goods matches both rate periods. With an inner join to items the same mistake shows as 1,305 rows for the 1,198 auditable lines. With the date condition: 1,296.
- Overpaid $9,596.24; underpaid $40,993.91; **net underpaid $31,397.66**. If a learner rounds expected duty per line first, the totals become $9,596.25 and $40,993.88: accept it if they say so.

By broker (audited lines only):

| Broker | Audited | Mismatches | Overpaid | Underpaid | Net |
|---|---|---|---|---|---|
| BRK-US2 | 346 | 28 | 7,049.52 | -28,295.17 | -21,245.65 |
| BRK-US1 | 445 | 16 | 2,546.72 | -12,000.84 | -9,454.12 |
| BRK-MX1 | 105 | 2 | 0.00 | -442.30 | -442.30 |
| BRK-CA1 | 149 | 2 | 0.00 | -200.29 | -200.29 |
| BRK-CA2 | 85 | 1 | 0.00 | -55.30 | -55.30 |
| BRK-MX2 | 68 | 0 | 0.00 | 0.00 | 0.00 |

Patterns (stretch, Hire A):

| Pattern | Lines | Over | Under | Net USD |
|---|---|---|---|---|
| Old rate after the 2026-06-01 change | 18 | 0 | 18 | -23,779.82 |
| 0% applied, no preference claimed | 10 | 0 | 10 | -11,222.20 |
| Additional duty missed (base rate only) | 7 | 0 | 7 | -4,955.33 |
| Other rate (classification question) | 9 | 2 | 7 | -565.76 |
| New rate before the change | 5 | 5 | 0 | +9,125.46 |

- The 18 old-rate lines are 14 by BRK-US2 and 4 by BRK-US1: the broker-level story for the memo. All 5 new-rate-before-the-change lines are in May 2026.
- Planted causes for reference: 11 lines missed the US additional duty on CN goods; 4 of them have a 0% base rate, so the data shows them as "0% applied". Six more lines had 0% applied on a dutiable line.

Ten largest mismatches by absolute variance:

| entry_no / line | Item, origin | Date, broker | Applied vs expected | Variance |
|---|---|---|---|---|
| US26-00143 / 1 | SYN-1011, CN | 2026-06-26, BRK-US2 | 12.50% vs 27.50% | -3,065.82 |
| US26-00175 / 2 | SYN-1025, CN | 2026-08-07, BRK-US2 | 0.00% vs 14.50% | -3,042.56 |
| US26-00009 / 3 | SYN-1043, CN | 2026-01-13, BRK-US1 | 0.00% vs 16.50% | -2,576.53 |
| US26-00112 / 2 | SYN-1085, CN | 2026-05-21, BRK-US2 | 29.50% vs 14.50% | +2,406.03 |
| US26-00111 / 1 | SYN-1013, CN | 2026-05-20, BRK-US2 | 28.90% vs 13.90% | +2,226.52 |
| US26-00178 / 4 | SYN-1102, CN | 2026-08-11, BRK-US2 | 12.90% vs 27.90% | -2,171.31 |
| US26-00117 / 2 | SYN-1102, CN | 2026-05-25, BRK-US1 | 27.90% vs 12.90% | +2,075.93 |
| US26-00168 / 2 | SYN-1013, CN | 2026-07-28, BRK-US1 | 13.90% vs 28.90% | -2,056.87 |
| US26-00065 / 6 | SYN-1022, CN | 2026-03-23, BRK-US1 | 3.90% vs 13.90% | -1,946.75 |
| US26-00107 / 2 | SYN-1053, CN | 2026-05-12, BRK-US2 | 25.00% vs 10.00% | +1,906.84 |

### Reference T-SQL

```sql
-- Purpose: Exercise 3 broker audit (answer key)
-- Source:  v_entry_lines_clean, entries, items, duty_rates_reference (effective-dated)
GO
CREATE OR ALTER VIEW practice.v_rate_audit AS
WITH np AS (   -- non-preference lines: no program claimed
    SELECT el.entry_no, el.line_no, el.item_id, el.entered_value, el.duty_rate_applied, el.duty_amount,
           e.import_country, e.entry_date, e.broker_id, i.hts10, i.country_of_origin
    FROM practice.v_entry_lines_clean AS el
    JOIN practice.entries AS e ON e.entry_no = el.entry_no
    LEFT JOIN practice.items AS i ON i.item_id = el.item_id
    WHERE el.program_claimed IS NULL
)
SELECT np.*,
       r.base_rate, r.additional_rate, r.expected_rate,
       CASE WHEN np.country_of_origin IS NULL THEN 'Not auditable: item not in master'
            WHEN np.hts10 IS NULL THEN 'Not auditable: HTS missing'
            WHEN r.expected_rate IS NULL THEN 'Not auditable: no reference rate'
            WHEN np.duty_rate_applied = r.expected_rate THEN 'Match'
            WHEN np.duty_rate_applied > r.expected_rate THEN 'Over'
            ELSE 'Under'
       END AS audit_status,
       np.entered_value * (np.duty_rate_applied - r.expected_rate) AS variance_usd
FROM np
LEFT JOIN practice.duty_rates_reference AS r
       ON r.import_country = np.import_country
      AND r.hts10 = np.hts10
      AND r.country_of_origin = np.country_of_origin
      AND np.entry_date BETWEEN r.effective_from AND r.effective_to;
GO
-- Control: one audit row per non-preference line (expect 1,296 and 1,296)
SELECT (SELECT COUNT(*) FROM practice.v_entry_lines_clean WHERE program_claimed IS NULL) AS nonpref_lines,
       (SELECT COUNT(*) FROM practice.v_rate_audit) AS audit_rows;

SELECT audit_status, COUNT(*) AS lines, SUM(entered_value) AS entered_value,
       CAST(SUM(variance_usd) AS DECIMAL(18, 2)) AS variance_usd
FROM practice.v_rate_audit
GROUP BY audit_status
ORDER BY audit_status;

SELECT broker_id,
       COUNT(*) AS lines_audited,
       SUM(CASE WHEN audit_status IN ('Over', 'Under') THEN 1 ELSE 0 END) AS mismatches,
       CAST(SUM(CASE WHEN variance_usd > 0 THEN variance_usd ELSE 0 END) AS DECIMAL(18, 2)) AS overpaid_usd,
       CAST(SUM(CASE WHEN variance_usd < 0 THEN variance_usd ELSE 0 END) AS DECIMAL(18, 2)) AS underpaid_usd,
       CAST(SUM(variance_usd) AS DECIMAL(18, 2)) AS net_usd
FROM practice.v_rate_audit
WHERE audit_status IN ('Match', 'Over', 'Under')
GROUP BY broker_id
ORDER BY net_usd;

-- The fan-out trap: no date condition (expect 1,305 = 1,198 auditable lines + 107 that match both periods)
SELECT COUNT(*) AS rows_without_date_condition
FROM practice.v_entry_lines_clean AS el
JOIN practice.entries AS e ON e.entry_no = el.entry_no
JOIN practice.items AS i ON i.item_id = el.item_id
JOIN practice.duty_rates_reference AS r
  ON r.import_country = e.import_country AND r.hts10 = i.hts10 AND r.country_of_origin = i.country_of_origin
WHERE el.program_claimed IS NULL;

-- Stretch: pattern of each mismatch
SELECT pattern, COUNT(*) AS lines,
       SUM(CASE WHEN audit_status = 'Over' THEN 1 ELSE 0 END) AS over_lines,
       SUM(CASE WHEN audit_status = 'Under' THEN 1 ELSE 0 END) AS under_lines,
       CAST(SUM(variance_usd) AS DECIMAL(18, 2)) AS net_usd
FROM (
    SELECT a.*,
           CASE WHEN EXISTS (SELECT 1 FROM practice.duty_rates_reference AS o
                             WHERE o.import_country = a.import_country AND o.hts10 = a.hts10
                               AND o.country_of_origin = a.country_of_origin
                               AND a.entry_date NOT BETWEEN o.effective_from AND o.effective_to
                               AND o.expected_rate = a.duty_rate_applied)
                     THEN CASE WHEN a.additional_rate > 0.10 THEN 'Old rate after the change'
                               ELSE 'New rate before the change' END
                WHEN a.duty_rate_applied = 0 THEN '0% applied, no preference claimed'
                WHEN a.duty_rate_applied = a.base_rate AND a.additional_rate > 0 THEN 'Additional duty missed (base rate only)'
                ELSE 'Other rate (classification question)'
           END AS pattern
    FROM practice.v_rate_audit AS a
    WHERE a.audit_status IN ('Over', 'Under')
) AS p
GROUP BY pattern
ORDER BY net_usd;

SELECT TOP (10) entry_no, line_no, item_id, country_of_origin, entry_date, broker_id,
       duty_rate_applied, expected_rate, CAST(variance_usd AS DECIMAL(18, 2)) AS variance_usd
FROM practice.v_rate_audit
WHERE audit_status IN ('Over', 'Under')
ORDER BY ABS(variance_usd) DESC;
```

## Exercise 4: USMCA claim check

### Answers

All USMCA claims on clean lines: 646 lines, $5,357,048.81 entered value.

| Claim status | Lines | Entered value | Duty at stake |
|---|---|---|---|
| Valid | 601 | 4,975,687.84 | 179,835.04 (duty saved by valid claims) |
| Invalid: origin not US, CA or MX | 38 | 319,806.41 | 26,302.43 |
| Invalid: no certification on file | 7 | 61,554.56 | 3,074.21 |
| Invalid total | 45 | 381,360.97 | **29,376.64** |

Invalid claims by item:

| Item | Origin, flag | Lines | Duty at stake | Root cause |
|---|---|---|---|---|
| SYN-1016 Slip-joint pliers | CN, Y | 19 | 15,775.19 | Master data: flag wrong, every line claims |
| SYN-1143 Duplex receptacle | CN, Y | 11 | 4,795.70 | Master data: flag wrong, every line claims |
| SYN-1104 Cordless drill | US, N | 3 | 2,169.81 | No certification on file |
| SYN-1132 Duplex receptacle | MX, N | 2 | 505.71 | No certification on file |
| SYN-1149 Wall switch | MX, N | 1 | 374.71 | No certification on file |
| SYN-1133 Aluminum sheet pan | CA, N | 1 | 23.99 | No certification on file |
| 8 other items, 1 line each | VN, IN, TW, KR, CN; N | 8 | 5,731.55 | Broker one-offs (claim on a non-USMCA origin) |

- Item rows are rounded one by one, so they add up to within a few cents of the totals above.
- The eight one-off lines: SYN-1066 $1,835.46, SYN-1054 $1,104.04, SYN-1112 $987.44, SYN-1060 $573.71, SYN-1145 $513.13, SYN-1009 $433.26, SYN-1032 $284.51, SYN-1087 $0.00 (a 0% line: no duty at stake, but the claim is still wrong).
- By import country: US 21 lines, $19,035.04; MX 13 lines, $6,309.85; CA 11 lines, $4,031.74. By broker: BRK-US1 13 lines $9,615.15; BRK-US2 8 $9,419.90; BRK-MX1 10 $4,932.00; BRK-MX2 3 $1,377.86; BRK-CA1 10 $3,969.72; BRK-CA2 1 $62.03.
- The key insight: 30 of 45 invalid lines (67%) and $20,570.89 of the $29,376.64 come from two wrong flags in **our** item master, spread across all brokers. Fixing the master stops them; chasing brokers does not.
- Fingerprints: a rule using only the flag finds 15 invalid lines (misses the 30 caused by wrong flags); a rule using only origin finds 38 (misses the 7 uncertified).
- Stretch, missed savings: 12 lines, $4,763.07 of duty paid (CA 6 lines $2,146.55; MX 1 line $407.60; US 5 lines $2,208.92). The US lines date from 2026-01-30 to 2026-09-29; under the one-year US post-importation window in the primer, the earliest expires on 2027-01-30. Expect the learner to escalate to the Senior, not to file anything.

### Reference T-SQL

```sql
-- Purpose: Exercise 4 USMCA claim check (answer key)
GO
CREATE OR ALTER VIEW practice.v_usmca_claims AS
SELECT el.entry_no, el.line_no, el.item_id, el.entered_value, el.duty_amount,
       e.import_country, e.entry_date, e.broker_id,
       i.hts10, i.country_of_origin, i.usmca_eligible_flag,
       CASE WHEN i.item_id IS NULL THEN 'Invalid: item not in master'
            WHEN i.country_of_origin NOT IN ('US', 'CA', 'MX') THEN 'Invalid: origin not US, CA or MX'
            WHEN i.usmca_eligible_flag <> 'Y' THEN 'Invalid: no certification on file'
            ELSE 'Valid'
       END AS claim_status,
       r.expected_rate,
       el.entered_value * r.expected_rate AS duty_at_stake_usd
FROM practice.v_entry_lines_clean AS el
JOIN practice.entries AS e ON e.entry_no = el.entry_no
LEFT JOIN practice.items AS i ON i.item_id = el.item_id
LEFT JOIN practice.duty_rates_reference AS r
       ON r.import_country = e.import_country AND r.hts10 = i.hts10 AND r.country_of_origin = i.country_of_origin
      AND e.entry_date BETWEEN r.effective_from AND r.effective_to
WHERE el.program_claimed = 'USMCA';
GO
SELECT claim_status, COUNT(*) AS lines, SUM(entered_value) AS entered_value,
       CAST(SUM(duty_at_stake_usd) AS DECIMAL(18, 2)) AS duty_at_stake_usd
FROM practice.v_usmca_claims
GROUP BY claim_status
ORDER BY claim_status;

SELECT item_id, country_of_origin, usmca_eligible_flag, claim_status, COUNT(*) AS lines,
       CAST(SUM(duty_at_stake_usd) AS DECIMAL(18, 2)) AS duty_at_stake_usd
FROM practice.v_usmca_claims
WHERE claim_status <> 'Valid'
GROUP BY item_id, country_of_origin, usmca_eligible_flag, claim_status
ORDER BY lines DESC, duty_at_stake_usd DESC;

SELECT import_country, broker_id, COUNT(*) AS invalid_lines,
       CAST(SUM(duty_at_stake_usd) AS DECIMAL(18, 2)) AS duty_at_stake_usd
FROM practice.v_usmca_claims
WHERE claim_status <> 'Valid'
GROUP BY import_country, broker_id
ORDER BY import_country, broker_id;

-- Stretch: missed savings (eligible, no claim, duty paid)
SELECT e.import_country, COUNT(*) AS lines, SUM(el.duty_amount) AS duty_paid_usd,
       MIN(e.entry_date) AS earliest_entry, MAX(e.entry_date) AS latest_entry
FROM practice.v_entry_lines_clean AS el
JOIN practice.entries AS e ON e.entry_no = el.entry_no
JOIN practice.items AS i ON i.item_id = el.item_id
WHERE el.program_claimed IS NULL
  AND i.country_of_origin IN ('US', 'CA', 'MX') AND i.usmca_eligible_flag = 'Y'
  AND el.duty_amount > 0
GROUP BY e.import_country
ORDER BY e.import_country;
```

## Exercise 5: PPV, actual landed cost vs standard

### Answers

| Receipt set | Receipts | Standard value | PPV | PPV % |
|---|---|---|---|---|
| All receipts | 1,500 | 7,089,754.96 | 378,973.90 | 5.35% |
| Outliers | 12 | 58,115.38 | 322,074.67 | 554.20% |
| Excluding outliers | 1,488 | 7,031,639.59 | **56,899.24** | **0.81%** |

- Outliers (actual / std): 9 high, between 9.69x and 13.39x (a case cost booked per each); 3 low at 0.10x (decimal shift). Non-outlier receipts range from 0.88x to 1.17x standard, so the rule separates them cleanly.

| Receipt | Item | Date | Actual / std | PPV |
|---|---|---|---|---|
| RCV-000010 | SYN-1002 | 2026-01-02 | 0.10 | -1,949.63 |
| RCV-000031 | SYN-1028 | 2026-01-06 | 9.69 | 41,168.81 |
| RCV-000037 | SYN-1085 | 2026-01-06 | 10.03 | 14,186.11 |
| RCV-000319 | SYN-1012 | 2026-02-26 | 0.10 | -4,690.19 |
| RCV-000379 | SYN-1028 | 2026-03-09 | 10.12 | 64,052.52 |
| RCV-000527 | SYN-1144 | 2026-04-10 | 12.17 | 69,541.61 |
| RCV-000548 | SYN-1132 | 2026-04-15 | 10.26 | 12,824.97 |
| RCV-000668 | SYN-1123 | 2026-05-08 | 9.78 | 24,630.80 |
| RCV-000697 | SYN-1038 | 2026-05-14 | 0.10 | -14,402.50 |
| RCV-000786 | SYN-1103 | 2026-06-01 | 13.39 | 55,183.59 |
| RCV-000988 | SYN-1036 | 2026-06-30 | 9.88 | 33,678.68 |
| RCV-001253 | SYN-1143 | 2026-08-18 | 11.12 | 27,849.91 |

Top 10 items by absolute PPV, excluding outliers:

| Item | Description | Origin, ch. | Receipts | PPV | PPV % |
|---|---|---|---|---|---|
| SYN-1011 | Hex bolt, M12 x 60 mm, box of 100 | CN, 73 | 17 | 11,202.84 | 7.0% |
| SYN-1095 | Cordless drill, 20 V | DE, 84 | 6 | 7,112.54 | 10.1% |
| SYN-1100 | Hex bolt, M6 x 30 mm, box of 100 | VN, UNK | 11 | -6,863.83 | -6.5% |
| SYN-1115 | Battery charger, 18 V | MX, 85 | 11 | 4,821.55 | 4.6% |
| SYN-1005 | Stainless threaded elbow, 1 in | CN, 73 | 14 | 4,253.33 | 4.7% |
| SYN-1121 | Hex bolt, M10 x 50 mm, box of 100 | IN, 73 | 15 | -4,123.59 | -5.4% |
| SYN-1070 | Steel shelving unit, 4-tier | US, 94 | 10 | 3,638.95 | 12.6% |
| SYN-1006 | Screwdriver set, 10-piece | CN, 82 | 8 | 3,455.67 | 10.4% |
| SYN-1103 | Flat washer, 8 mm, box of 500 | CN, 73 | 18 | 3,391.59 | 6.7% |
| SYN-1093 | Stainless mixing bowl set, 5-piece | CN, 73 | 12 | 3,278.36 | 7.3% |

By origin, excluding outliers: CN $44,119.21 (2.09%); CA $8,380.68 (1.42%); DE $7,090.70 (2.69%); US $3,923.28 (0.49%); MX $3,845.69 (0.37%); TW $3,104.52 (0.69%); KR $576.00 (0.18%); IT -$45.34 (-0.03%); IN -$3,542.73 (-0.89%); VN -$10,552.77 (-1.21%). 87 items are unfavorable and 63 favorable.

The biggest driver: CN-origin chapter 73 and 76 items after the fictional US rate change on 2026-06-01.

| CN, chapters 73 and 76 | Receipts | Standard value | PPV | PPV % |
|---|---|---|---|---|
| Before 2026-06-01 | 67 | 369,817.50 | 517.40 | 0.14% |
| On or after 2026-06-01 | 58 | 290,255.61 | 37,051.96 | 12.77% |

- Those 58 receipts are 65% of the net PPV ($37,051.96 of $56,899.24). Receipts outside CN chapters 73 and 76 (before or after the change): 1,363 receipts, $19,329.88, 0.30%. All receipts except the 58: 1,430 receipts, $19,847.28, 0.29%.
- PPV % by month (excluding outliers) is between -0.03% and 0.36% from January to May, then 1.75% in June, 1.80% in July, 0.80% in August and 1.68% in September.
- The other top movers are supplier price changes, up or down, during the year (for example SYN-1095 and SYN-1070 up, SYN-1100 and SYN-1121 down). A good answer says "price change" as a hypothesis to confirm with Purchasing, not as a fact.
- Stretch (Hire B): duty-driven estimate for the 58 receipts = receipt qty x average 2026 US customs value per unit x 15 points of rate increase = **$35,505.88**, which explains about 96% of their $37,051.96 PPV. The rest is price and freight noise. Expected recommendation: a standard cost update for the CN chapter 73 and 76 items with the current rate, through the checklist with maker-checker review.
- Fingerprints: including outliers gives 5.35% (wrong); a sign reversal gives -0.81%.

### Reference T-SQL

```sql
-- Purpose: Exercise 5 PPV (answer key)
GO
CREATE OR ALTER VIEW practice.v_ppv AS
SELECT rc.receipt_id, rc.po_no, rc.item_id, rc.receipt_date, rc.qty, rc.actual_landed_unit_cost,
       i.std_cost, i.description, i.country_of_origin,
       COALESCE(LEFT(i.hts10, 2), 'UNK') AS hts_chapter,
       i.std_cost * rc.qty AS std_value_usd,
       (rc.actual_landed_unit_cost - i.std_cost) * rc.qty AS ppv_usd,          -- positive = unfavorable
       CASE WHEN rc.actual_landed_unit_cost > 3 * i.std_cost
              OR rc.actual_landed_unit_cost * 3 < i.std_cost THEN 1 ELSE 0 END AS is_outlier
FROM practice.receipts AS rc
JOIN practice.items AS i ON i.item_id = rc.item_id;
GO
SELECT (SELECT COUNT(*) FROM practice.receipts) AS receipts, (SELECT COUNT(*) FROM practice.v_ppv) AS ppv_rows;

SELECT CASE WHEN GROUPING(is_outlier) = 1 THEN 'All receipts'
            WHEN is_outlier = 1 THEN 'Outliers' ELSE 'Excluding outliers' END AS receipt_set,
       COUNT(*) AS receipts,
       SUM(std_value_usd) AS std_value_usd,
       CAST(SUM(ppv_usd) AS DECIMAL(18, 2)) AS ppv_usd,
       CAST(100.0 * SUM(ppv_usd) / NULLIF(SUM(std_value_usd), 0) AS DECIMAL(9, 2)) AS ppv_pct
FROM practice.v_ppv
GROUP BY ROLLUP (is_outlier);

SELECT receipt_id, item_id, receipt_date, qty, std_cost, actual_landed_unit_cost,
       CAST(actual_landed_unit_cost / NULLIF(std_cost, 0) AS DECIMAL(9, 2)) AS actual_to_std,
       CAST(ppv_usd AS DECIMAL(18, 2)) AS ppv_usd
FROM practice.v_ppv
WHERE is_outlier = 1
ORDER BY receipt_id;

SELECT TOP (10) item_id, description, country_of_origin, hts_chapter, COUNT(*) AS receipts,
       CAST(SUM(ppv_usd) AS DECIMAL(18, 2)) AS ppv_usd,
       CAST(100.0 * SUM(ppv_usd) / NULLIF(SUM(std_value_usd), 0) AS DECIMAL(9, 1)) AS ppv_pct
FROM practice.v_ppv
WHERE is_outlier = 0
GROUP BY item_id, description, country_of_origin, hts_chapter
ORDER BY ABS(SUM(ppv_usd)) DESC;

SELECT country_of_origin, COUNT(*) AS receipts,
       CAST(SUM(std_value_usd) AS DECIMAL(18, 2)) AS std_value_usd,
       CAST(SUM(ppv_usd) AS DECIMAL(18, 2)) AS ppv_usd,
       CAST(100.0 * SUM(ppv_usd) / NULLIF(SUM(std_value_usd), 0) AS DECIMAL(9, 2)) AS ppv_pct
FROM practice.v_ppv
WHERE is_outlier = 0
GROUP BY country_of_origin
ORDER BY ppv_usd DESC;

SELECT DATEFROMPARTS(YEAR(receipt_date), MONTH(receipt_date), 1) AS month_start, COUNT(*) AS receipts,
       CAST(SUM(ppv_usd) AS DECIMAL(18, 2)) AS ppv_usd,
       CAST(100.0 * SUM(ppv_usd) / NULLIF(SUM(std_value_usd), 0) AS DECIMAL(9, 2)) AS ppv_pct
FROM practice.v_ppv
WHERE is_outlier = 0
GROUP BY DATEFROMPARTS(YEAR(receipt_date), MONTH(receipt_date), 1)
ORDER BY month_start;

SELECT CASE WHEN receipt_date < '2026-06-01' THEN 'Before 2026-06-01' ELSE 'On or after 2026-06-01' END AS period,
       COUNT(*) AS receipts,
       CAST(SUM(std_value_usd) AS DECIMAL(18, 2)) AS std_value_usd,
       CAST(SUM(ppv_usd) AS DECIMAL(18, 2)) AS ppv_usd,
       CAST(100.0 * SUM(ppv_usd) / NULLIF(SUM(std_value_usd), 0) AS DECIMAL(9, 2)) AS ppv_pct
FROM practice.v_ppv
WHERE is_outlier = 0 AND country_of_origin = 'CN' AND hts_chapter IN ('73', '76')
GROUP BY CASE WHEN receipt_date < '2026-06-01' THEN 'Before 2026-06-01' ELSE 'On or after 2026-06-01' END;

-- Stretch: duty-driven part of the CN chapter 73/76 PPV after the change (15 points of rate)
WITH ucv AS (
    SELECT el.item_id, SUM(el.entered_value) / NULLIF(SUM(el.qty), 0) AS unit_customs_value
    FROM practice.v_entry_lines_clean AS el
    JOIN practice.entries AS e ON e.entry_no = el.entry_no
    WHERE e.import_country = 'US'
    GROUP BY el.item_id
)
SELECT COUNT(*) AS receipts,
       CAST(SUM(p.ppv_usd) AS DECIMAL(18, 2)) AS ppv_usd,
       CAST(SUM(p.qty * u.unit_customs_value * 0.15) AS DECIMAL(18, 2)) AS duty_driven_estimate_usd
FROM practice.v_ppv AS p
LEFT JOIN ucv AS u ON u.item_id = p.item_id
WHERE p.is_outlier = 0 AND p.country_of_origin = 'CN' AND p.hts_chapter IN ('73', '76')
  AND p.receipt_date >= '2026-06-01';
```

## Exercise 6: Tariff scenario impact

### Answers

| Scenario | Lines | YTD value | Annualized value | Annualized impact |
|---|---|---|---|---|
| SCN-01 US: fasteners and valves, CN and VN | 129 | 1,138,691.71 | 1,518,255.61 | 226,988.36 |
| SCN-02 CA: surtax on US goods | 45 | 410,164.48 | 546,885.97 | 136,721.49 |
| SCN-03 US: MX electrical, USMCA exempt | 12 | 97,696.43 | 130,261.91 | 32,565.48 |
| Total | 186 | 1,646,552.62 | 2,195,403.49 | **396,275.33** |

By scenario, origin and chapter (annualized impact): SCN-01 CN ch. 73 $128,043.47 (47 lines); SCN-01 VN ch. 73 $50,556.84 (41); SCN-01 CN ch. 84 $29,794.13 (19); SCN-01 VN ch. 84 $18,593.92 (22); SCN-02 US ch. 85 $96,381.51 (30); SCN-02 US ch. 94 $40,339.99 (15); SCN-03 MX ch. 85 $32,565.48 (12).

By scenario row (prefix and origin): SCN-01 7318 CN $43,479.97 (27 lines); 731815 CN $84,563.50 (20); 8481 CN $29,794.13 (19); 7318 VN $50,556.84 (41); 8481 VN $18,593.92 (22). SCN-02 8504 $45,534.88 (15); 8544 $50,846.62 (15); 9403 $40,339.99 (15). SCN-03 8536 $32,565.48 (12); no MX lines match 8544 or 8504 once the exemption is applied.

Top 5 items by annualized impact:

| Scenario | Item | Origin | Prefix | Annualized impact |
|---|---|---|---|---|
| SCN-01 | SYN-1011 Hex bolt, M12 x 60 mm | CN | 731815 | 58,131.63 |
| SCN-02 | SYN-1021 Extension cord, 50 ft | US | 8544 | 30,480.76 |
| SCN-01 | SYN-1053 Hex bolt, M6 x 30 mm | CN | 731815 | 26,431.87 |
| SCN-02 | SYN-1044 Battery charger, 12 V | US | 8504 | 24,963.00 |
| SCN-03 | SYN-1149 Wall switch, 15 A | MX | 8536 | 24,729.26 |

- Overlap: at step 2 (before the exemption) the prefix join gives 271 rows for 251 line and scenario pairs, because 20 SCN-01 lines (CN, 731815) match both 7318 and 731815. 65 SCN-03 pairs are exempt, which leaves 186 pairs (206 rows if both prefixes are kept). Counting both prefixes on non-exempt lines adds $50,738.10 (total $447,013.43). The longest prefix (25%) applies.
- USMCA exemption: 65 SCN-03 lines ($750,029.39 YTD value) are exempt; the exemption is worth **$250,009.80** a year. The only SCN-03 impact comes from the two MX items with no certification: SYN-1149 $24,729.26 and SYN-1132 $7,836.22. Getting their certifications in place, if they qualify, removes the whole SCN-03 impact.
- Not evaluable: 43 lines ($506,582.85 YTD value) of 5 HTS-missing items have an import country and origin that match a scenario: SYN-1034 CN, 7 lines, $48,378.19; SYN-1051 CN, 9, $76,387.88; SYN-1100 VN, 4, $95,360.58; SYN-1105 VN, 12, $156,814.11; SYN-1120 CN, 11, $129,642.09. From the descriptions, SYN-1100 (hex bolt) and SYN-1105 (hex nut) from VN look like heading 7318 and could add about **$33,623.29** a year under SCN-01 (10%). Research confirms the classification first; the others (cable clip, shelving, fan) do not look like SCN-01 goods.
- Stretch (a), from the effective date to 2026-12-31: SCN-01 (from 12/1, 31 days) $19,278.46; SCN-02 (from 11/15, 47 days) $17,605.23; SCN-03 (from 2027-01-01) $0.
- Stretch (c): of the 18 US-origin items with Canadian entry lines, the model should put 7 in scope (45 lines, 38,470 units YTD) and show an impact of $136,721.49 for the 12-month quantity (within a few dollars if the unit customs value was rounded). $136,713.28 means the quantity was truncated by integer division (`SUM(qty) * 12 / 9` on an INT). Zero usually means the Action tab still holds the template's sample action. Check that Hire B did not edit the Action tab: Research (Hire A or the Senior) fills it.
- Fingerprints: $297,206.50 means `* (12 / 9)` integer division in T-SQL (the YTD impact); $646,285.13 means the exemption was ignored; $447,013.43 means no longest-prefix rule; $400,707.20 (188 lines) means duplicates were not removed.

### Reference T-SQL

```sql
-- Purpose: Exercise 6 tariff scenarios, annualized (answer key)
GO
CREATE OR ALTER VIEW practice.v_scenario_lines AS
WITH base AS (
    SELECT el.entry_no, el.line_no, el.item_id, el.qty, el.entered_value,
           e.import_country, e.entry_date, i.hts10, i.country_of_origin, i.usmca_eligible_flag
    FROM practice.v_entry_lines_clean AS el
    JOIN practice.entries AS e ON e.entry_no = el.entry_no
    JOIN practice.items AS i ON i.item_id = el.item_id
    WHERE i.hts10 IS NOT NULL
),
matches AS (
    SELECT b.*, s.scenario_id, s.hts_prefix, s.additional_rate, s.usmca_exempt,
           ROW_NUMBER() OVER (PARTITION BY b.entry_no, b.line_no, s.scenario_id
                              ORDER BY LEN(s.hts_prefix) DESC) AS prefix_rank   -- 1 = longest prefix
    FROM base AS b
    JOIN practice.tariff_scenario AS s
      ON s.import_country = b.import_country
     AND s.country_of_origin = b.country_of_origin
     AND b.hts10 LIKE s.hts_prefix + '%'
)
SELECT entry_no, line_no, item_id, qty, entered_value, import_country, entry_date, hts10,
       LEFT(hts10, 2) AS hts_chapter, country_of_origin, usmca_eligible_flag,
       scenario_id, hts_prefix, additional_rate,
       CASE WHEN usmca_exempt = 'Y' AND usmca_eligible_flag = 'Y' THEN 1 ELSE 0 END AS is_exempt,
       entered_value * additional_rate AS impact_ytd_usd
FROM matches
WHERE prefix_rank = 1;
GO
-- Annualize as SUM(x) * 12.0 / 9: it also works on INT columns such as qty. SUM(x) * (12 / 9) multiplies by 1.
SELECT scenario_id, COUNT(*) AS lines, SUM(entered_value) AS ytd_value_usd,
       CAST(SUM(entered_value) * 12.0 / 9 AS DECIMAL(18, 2)) AS annualized_value_usd,
       CAST(SUM(impact_ytd_usd) * 12.0 / 9 AS DECIMAL(18, 2)) AS annualized_impact_usd
FROM practice.v_scenario_lines
WHERE is_exempt = 0
GROUP BY ROLLUP (scenario_id)
ORDER BY GROUPING(scenario_id), scenario_id;

SELECT scenario_id, country_of_origin, hts_chapter, COUNT(*) AS lines,
       CAST(SUM(impact_ytd_usd) * 12.0 / 9 AS DECIMAL(18, 2)) AS annualized_impact_usd
FROM practice.v_scenario_lines
WHERE is_exempt = 0
GROUP BY scenario_id, country_of_origin, hts_chapter
ORDER BY scenario_id, annualized_impact_usd DESC;

SELECT scenario_id, hts_prefix, country_of_origin, COUNT(*) AS lines,
       CAST(SUM(impact_ytd_usd) * 12.0 / 9 AS DECIMAL(18, 2)) AS annualized_impact_usd
FROM practice.v_scenario_lines
WHERE is_exempt = 0
GROUP BY scenario_id, hts_prefix, country_of_origin
ORDER BY scenario_id, hts_prefix, country_of_origin;

SELECT COUNT(*) AS exempt_lines, SUM(entered_value) AS exempt_ytd_value,
       CAST(SUM(impact_ytd_usd) * 12.0 / 9 AS DECIMAL(18, 2)) AS annualized_impact_avoided_usd
FROM practice.v_scenario_lines
WHERE is_exempt = 1;

SELECT TOP (5) scenario_id, item_id, country_of_origin, hts_prefix,
       CAST(SUM(impact_ytd_usd) * 12.0 / 9 AS DECIMAL(18, 2)) AS annualized_impact_usd
FROM practice.v_scenario_lines
WHERE is_exempt = 0
GROUP BY scenario_id, item_id, country_of_origin, hts_prefix
ORDER BY SUM(impact_ytd_usd) DESC;

-- The overlap trap: every matching prefix counted, exempt lines removed (expect 206 rows, 447,013.43).
-- Without the WHERE line this is the step-2 count: 271 rows for 251 line and scenario pairs.
SELECT COUNT(*) AS matched_rows_all_prefixes,
       CAST(SUM(el.entered_value * s.additional_rate) * 12.0 / 9 AS DECIMAL(18, 2)) AS double_counted_impact_usd
FROM practice.v_entry_lines_clean AS el
JOIN practice.entries AS e ON e.entry_no = el.entry_no
JOIN practice.items AS i ON i.item_id = el.item_id
JOIN practice.tariff_scenario AS s
  ON s.import_country = e.import_country AND s.country_of_origin = i.country_of_origin
 AND i.hts10 LIKE s.hts_prefix + '%'
WHERE NOT (s.usmca_exempt = 'Y' AND i.usmca_eligible_flag = 'Y');

-- Lines that cannot be evaluated: HTS missing, import country and origin match a scenario
SELECT i.item_id, i.description, i.country_of_origin, e.import_country,
       COUNT(*) AS lines, SUM(el.entered_value) AS ytd_value_usd
FROM practice.v_entry_lines_clean AS el
JOIN practice.entries AS e ON e.entry_no = el.entry_no
JOIN practice.items AS i ON i.item_id = el.item_id
WHERE i.hts10 IS NULL
  AND EXISTS (SELECT 1 FROM practice.tariff_scenario AS s
              WHERE s.import_country = e.import_country AND s.country_of_origin = i.country_of_origin)
GROUP BY i.item_id, i.description, i.country_of_origin, e.import_country
ORDER BY i.item_id;
```

Excel check for SCN-01 CN (the overlap handled by subtraction), on a table `lines` built from the clean lines with hts10 as text:

```text
7318 only:  =(SUMIFS(lines[entered_value], lines[import_country], "US", lines[country_of_origin], "CN", lines[hts10], "7318*")
             - SUMIFS(lines[entered_value], lines[import_country], "US", lines[country_of_origin], "CN", lines[hts10], "731815*")) * 0.15 * 12/9
             -> 43,479.97
731815:     =SUMIFS(lines[entered_value], lines[import_country], "US", lines[country_of_origin], "CN", lines[hts10], "731815*") * 0.25 * 12/9
             -> 84,563.50
```

## Exercise 7: Power BI page with DAX measures

### Expected card values (no slicers)

| Card | Value | Ties to |
|---|---|---|
| Total Duty | $856,378.07 | Ex 2 grand total |
| Effective Duty Rate | 5.16% | Ex 2 |
| PPV % (excluding outliers) | 0.81% | Ex 5 |
| Scenario Impact | $396,275.33 | Ex 6 total |

Spot checks with one slicer:

| Slicer | Total Duty | Effective Duty Rate | PPV % | Scenario Impact |
|---|---|---|---|---|
| Origin = CN | $579,514.22 | 10.39% | 2.09% | $157,837.60 |
| Import country = US | $645,972.49 | 6.59% | 0.81% (unchanged) | $396,275.33 (unchanged) |
| Scenario = SCN-01 | $856,378.07 (unchanged) | 5.16% (unchanged) | 0.81% (unchanged) | $226,988.36 |

- If Total Duty shows $871,664.92, the duplicates were not removed. If it shows $855,384.34, an inner merge with Items dropped the 4 orphan lines (and the slicer may show no "(Blank)" member).
- The import country slicer cannot filter Receipts or ScenarioLines in this model because it comes from EntryLines; that is the expected behavior, and the learner should be able to explain it.

### Reference DAX

This DAX was written for the model described in the exercise but has not been run in Power BI in this repo; confirm it in W4. Column names assume the SQL views (`is_outlier` and `is_exempt` as 0 or 1). If they came from Power Query as True/False, compare with `FALSE ()` instead of 0.

```text
Calendar =
ADDCOLUMNS (
    CALENDAR ( DATE ( 2026, 1, 1 ), DATE ( 2026, 12, 31 ) ),
    "Month", DATE ( YEAR ( [Date] ), MONTH ( [Date] ), 1 )
)
-- Power BI only: Excel's Data Model cannot create calculated tables.
-- In Excel use Power Pivot > Design > Date Table > New.

Total Entered Value = SUM ( EntryLines[entered_value] )

Total Duty = SUM ( EntryLines[duty_amount] )

Effective Duty Rate = DIVIDE ( [Total Duty], [Total Entered Value] )

-- Receipts loaded from practice.v_ppv (has std_value_usd and ppv_usd)
PPV $ excl Outliers = CALCULATE ( SUM ( Receipts[ppv_usd] ), Receipts[is_outlier] = 0 )

Std Value excl Outliers = CALCULATE ( SUM ( Receipts[std_value_usd] ), Receipts[is_outlier] = 0 )

PPV % = DIVIDE ( [PPV $ excl Outliers], [Std Value excl Outliers] )

-- Same result from the raw receipts table and the Items relationship
Std Value Received = SUMX ( Receipts, Receipts[qty] * RELATED ( Items[std_cost] ) )
Actual Value Received = SUMX ( Receipts, Receipts[qty] * Receipts[actual_landed_unit_cost] )

-- Calculated column on raw Receipts, if is_outlier is not in the source
is_outlier =
VAR a = Receipts[actual_landed_unit_cost]
VAR s = RELATED ( Items[std_cost] )
RETURN IF ( a > 3 * s || a * 3 < s, 1, 0 )

Annualization Factor = DIVIDE ( 12, 9 )   -- data window Jan to Sep 2026

Scenario Impact =
CALCULATE (
    SUMX ( ScenarioLines, ScenarioLines[entered_value] * ScenarioLines[additional_rate] ),
    ScenarioLines[is_exempt] = 0
) * [Annualization Factor]
```

Why these choices (ask the learner to explain them):

- Effective Duty Rate and PPV % are measures, not columns: they must be a ratio of sums in whatever filter context the visual creates.
- is_outlier is a column: it is a fixed attribute of each receipt that you filter by.
- CALCULATE adds the filter `is_outlier = 0` to the current filter context; slicers still apply on top of it.
- DIVIDE returns BLANK (or the alternate result) when the denominator is zero or blank. The / operator would return Infinity or NaN instead, which shows on a card.

### Layout check

Pass if: four cards on top that tie out; slicers that each change the expected cards; chapter bar and chapter-by-origin matrix match Exercise 2, including the UNK chapter row of 98 lines (hts_chapter and origin built on EntryLines, not taken from Items); the PPV % by month line shows the June step (1.75% after 0.16% in May); the scenario table matches Exercise 6; a visible "synthetic practice data" label; the .pbix not published to a shared workspace.

## Exercise 8: What a good memo says

### Model memo (about 400 words)

**To:** BSA Manager · **From:** Hire A · **Date:** Fri 2026-11-13 · **Subject:** Practice data review (synthetic, Jan-Sep 2026): broker rates, USMCA claims, PPV, tariff scenarios

**Bottom line**

- Brokers under-applied duty by $41.0K and over-applied $9.6K on non-preference lines: net $31.4K underpaid. 18 of the 49 mismatches are the 2026-06-01 rate change not applied, 14 of them by BRK-US2.
- 45 USMCA claims are invalid ($29.4K duty at stake). 30 come from two CN-origin items wrongly flagged USMCA-eligible in our item master.
- The three scenarios would add $396.3K a year (SCN-01 $227.0K). The USMCA exemption in SCN-03 is worth $250.0K a year.

**Findings**

1. Rate audit: 1,198 lines audited, 49 mismatches (7 over, 42 under). Patterns: old rate after the change (18, -$23.8K), 0% applied (10, -$11.2K), additional duty missed (7, -$5.0K), new rate before the change (5, +$9.1K), other rates (9). High confidence: each line ties to the reference table.
2. USMCA: SYN-1016 and SYN-1143 cause 30 invalid lines across all brokers ($20.6K); 7 lines on items with no certification; 8 one-off broker claims. 12 eligible lines paid $4.8K without claiming.
3. PPV: $56.9K unfavorable (0.81%) after setting aside 12 outlier receipts ($322.1K: 9 unit-of-measure errors, 3 decimal shifts). CN chapter 73/76 receipts since June carry $37.1K (12.8%); the duty increase explains about $35.5K. Their standards still carry the old rate.
4. Data quality: 24 duplicate lines (4 entries loaded twice; $15.3K duty double counted if kept), 4 lines on items missing from the master, 6 items with no HTS (94 lines, $1.05M) that cannot be audited or modeled. Two of them (VN hex bolt and nut) may fall under SCN-01: about $33.6K a year.

**Recommended actions**

- Correct the USMCA flag on SYN-1016 and SYN-1143 (Hire A maker, Senior checker, by 11/20). Senior decides the correction route for the 45 lines.
- Send the 49 mismatches to the Senior for broker follow-up, starting with BRK-US2's 14 stale-rate lines (by 11/18).
- Hire B to prepare a standard cost update with Finance for the CN chapter 73/76 items, using the rate and item scope Research confirms, with maker-checker review (by 12/4).
- Research to classify the 6 items with no HTS (by 11/25).
- Senior to decide on post-importation claims for the 12 missed lines; the earliest US line's one-year window ends 2027-01-30.

**Method and controls:** 1,942 clean entry lines (1,966 raw); control total duty $856,378.07 ties across all exercises and the Power BI page. Queries saved in [COMPANY: folder]; reviewed by the Senior.

**Limits:** synthetic practice data; USMCA validity per the practice rule; scenario impact is a full-year view on 9 months of volume; no fees or taxes.

### Marking guide

| Criterion | Good | Weak |
|---|---|---|
| Bottom line first | Three bullets with numbers a reader can act on | Starts with method or background |
| Right emphasis | Master-data root cause for USMCA; the rate-change pattern; the PPV driver | Lists every number with equal weight |
| Owners and dates | Every action has a role and a date; corrections go to the Senior | "We should look into it" |
| Traceable | Each number ties to a saved query and the control total | Numbers that cannot be found again |
| Honest limits | Synthetic data, practice USMCA rule, full-year view, no fees | No caveats, or a page of them |
| Boundaries | Research owns scope, Standard Cost owns dollars, no broker contact | Proposes contacting brokers directly |

## Common mistakes and their fingerprints

| Mistake | Result you will see | Right result | Exercise |
|---|---|---|---|
| Duplicates not removed | Duty $871,664.92; 1,966 lines | $856,378.07; 1,942 | 1, 2, 7 |
| INNER JOIN to items | Duty $855,384.34 (orphans lost) | $856,378.07 | 2, 7 |
| `program_claimed <> 'USMCA'` | 0 lines in scope | 1,296 | 3 |
| Rate join without the date condition | 1,403 rows (1,305 with an inner join to items); 133 "mismatches", -$122,265.32 under | 1,296 rows; 49 mismatches | 3 |
| USMCA rule on the flag only | 15 invalid lines | 45 | 4 |
| Outliers left in PPV | 5.35% | 0.81% | 5, 7 |
| Supplier country used as origin | CN duty $363,406.72 | $579,514.22 | 2 |
| No longest-prefix rule | 271 rows at step 2 (206 after the exemption), $447,013.43 | 251 pairs at step 2 (186 after the exemption), $396,275.33 | 6 |
| USMCA exemption ignored | $646,285.13 | $396,275.33 | 6 |
| `* (12 / 9)` in T-SQL | $297,206.50 | $396,275.33 | 6 |

## Related files

- `docs/analytics/practice-exercises.md`
- `data/analytics/generate_practice_data.py`, `dist/Practice-Data.xlsx`, `dist/practice-data/load_practice_data.sql`
- `docs/templates/domain/tariff-impact-model-guide.md`, `docs/templates/domain/standard-cost-update-checklist.md`
- `docs/03-check-ins-and-scorecards.md` (A30-5 and B30-5)
