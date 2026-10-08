# Data Mapping Specification Template

Last updated: 2026-10-08 · Owner: BSA Manager

- **Purpose:** a field-by-field specification of how data moves from a source to a target: transformation rules, data quality rules, cleansing decisions, reconciliation and data-owner sign-off. Built for the AS400 trade system to e2open migration, and for Oracle and broker interfaces.
- **Who uses it:** both hires as makers (day-90 criteria A90-3 for Research data and B90-3 for Standard Cost data); the Senior as checker (data quality, SQL, compliance meaning of fields); the data owner, who signs; the e2open project data or integration lead, who builds loads from it; UAT testers, who reuse the reconciliation.
- **When:** first used in W7, when it is taught in M4 (in W2 the hires map system-level data flows with the table in `docs/primers/trade-systems-gtm-e2open-primer.md` Section 7.3 instead). Drafted in W10 and W11, finished by W13, then kept current through the e2open build, test loads and cutover (M10).

## How to fill this in

Text in [square brackets] is a prompt: replace it. [COMPANY: ...] is a company-specific value.

1. Write one spec per object and direction, for example "Product classification master, AS400 to e2open". Do not mix objects in one spec.
2. Fill the header (Part 1). Take target field names from the e2open project data dictionary or load templates ([COMPANY: location of e2open load templates]). Never guess a target field name. If you don't have the dictionary yet, map to the e2open concept and write "target field TBC".
3. Profile the source before you map it (Part 5). Real values beat field names: a field labelled "HTS" may hold text, dots, or nothing.
4. Fill mapping table A (field mapping), then table B (quality and open questions). Both use the same Map ID. Write one row per target field, so unmapped target fields are visible; the source can be "none (default)" or "derived".
5. Build a value cross-reference (Part 3) for every coded field.
6. Log every data issue in the cleansing log (Part 6) and agree the decision with the data owner.
7. Reconcile after every test load (Part 7) and keep the queries and results.
8. The data owner signs (Part 8). Any change after sign-off creates a new version and needs a new signature.

### Reading AS400 (IBM i) data: what trips people up

- A library is like a schema, a physical file like a table, a logical file like a view or index, and a field like a column. System names are 10 characters or fewer and often cryptic. Get each field's text description and type from the file's field description ([COMPANY: who can run DSPFFD or provide the AS400 data dictionary]).
- Numbers may be packed or zoned decimal with implied decimal places. Confirm the decimal positions of every numeric field before you convert it.
- Dates are often stored as numbers: YYYYMMDD, or CYYMMDD where C is 0 for the 1900s and 1 for the 2000s (1261019 is 2026-10-19). Values such as 0 or 9999999 often mean "no date". Confirm the convention field by field.
- Text is EBCDIC on the server and is converted by the extract. Check that French and Spanish characters (é, ñ, ü) survive.
- Character fields are padded with trailing blanks. Trim them.
- Codes often only make sense through a separate code file. Find it before you map the field.
- Opening an extract in Excel drops leading zeros and turns long numbers into scientific notation. Load extracts into SQL, or import CSV with the columns set to Text.

## Template

### Part 1: Header

| Field | Entry |
|---|---|
| Spec ID and version | [DM-RES-01 v0.1] |
| Object | [Product classification master, tariff rates, USMCA qualification, landed-cost components, broker entry data, item cost interface] |
| Source system | [AS400 trade system: COMPANY library and file; Oracle; SQL Server or warehouse table; Excel file; external source] |
| Target system | [e2open GTM: COMPANY e2open object or load template; Oracle interface; broker file] |
| Type | [One-time migration load, recurring interface, report feed] |
| Direction and frequency | [Source to target; once at cutover, daily, per cost cycle] |
| Record scope (filter) | [For example: active items, countries US, CA, MX] |
| Key | [Unique identifier, for example item number + country] |
| Expected volume | [Rows; from profiling] |
| Data owner | [COMPANY: business data owner] |
| Maker and checker | [Hire A or B; Senior or Manager] |
| Related documents | [Requirements, as-is map, UAT plan, change requests] |

### Part 2: Mapping tables

Table A: field mapping

| Map ID | Source file/table | Source field (type) | Target field (type, required?) | Transform rule |
|---|---|---|---|---|
| [XX-01] | [File or table] | [Field name and description (type, length)] | [Target field (type, Y/N)] | [Rule, using the vocabulary below] |

Table B: data quality and open questions (same Map IDs)

| Map ID | Data quality rule | Open question | Owner | Status |
|---|---|---|---|---|
| [XX-01] | [What a valid value looks like; what happens to invalid ones] | [Question, or "none"] | [Name] | [Draft, Open question, Agreed] |

Transform rule vocabulary (use these words so rules are read the same way by everyone):

| Rule | Meaning | Example |
|---|---|---|
| Direct | Copy as is | Origin country code to origin country code |
| Trim | Remove leading or trailing blanks | Item number padded to 15 characters |
| Pad | Left-pad with zeros to a fixed length | US HTS 9 digits to 10 digits |
| Format | Change the presentation only | Remove the periods from 8471.30.0100 |
| Convert | Change type, unit or date format | CYYMMDD to YYYY-MM-DD |
| Lookup | Translate a code through a value map (Part 3) | AS400 status code to e2open status |
| Derive | Calculate from other fields | Effective-to date = next row's effective-from minus 1 day |
| Default | Constant value when the source is empty (data owner must approve) | Classification status = "Active" |
| Not migrated | Deliberately left behind, with the reason and the archive plan | Obsolete legacy note field |

### Part 3: Value cross-reference

| Value map ID | Source value | Target value | Meaning | Notes |
|---|---|---|---|---|
| [VM-01] | [Code found in profiling] | [Target code] | [Plain-words meaning] | [Who confirmed; date] |

List every distinct source value found in profiling, including blanks and oddities. A value with no row here is an open question.

### Part 4: Interface details (Oracle and broker interfaces)

Fill this part for any recurring interface, not for a one-time load.

| Item | Entry |
|---|---|
| Trigger and schedule | [Time, event, or manual run] |
| Format and layout | [CSV, fixed width, EDI, API; layout version; COMPANY: layout document] |
| Delivery | [SFTP, email, portal, API; COMPANY: location] |
| Control records | [Header or trailer with record count and totals] |
| Error handling | [Reject file, who is alerted, how fast, who fixes] |
| Monitoring | [Who checks that it ran and the counts make sense] |
| Change notice to the receiver | [Lead time; for brokers, agree a test file before any layout change] |

Points to confirm for each interface:

- **Oracle item and cost data.** Which system is the master for item number, description and unit of measure ([COMPANY: confirm Oracle is the item master]). Which cost elements receive duty, freight and fees ([COMPANY: Oracle EBS or Fusion cost elements and sub-elements]). Finance owns the cost load; the BSA prepares and checks the input.
- **Broker classification or parts files (data out).** Per country and per broker: item, description, HTS number, country of origin, preference claim data, unit of measure ([COMPANY: broker file layout for each broker]).
- **Broker entry data (data back).** Entry number and line, HTS number, entered value, duty, fees, preference claimed, origin. Used to audit broker filings and as actual duty for PPV.

### Starter object list for the day-90 data maps

The e2open concepts below are generic. Confirm each against the project's scope and data model ([COMPANY: e2open scope document]).

| Track | Data object | Source today | e2open concept (confirm) | Watch for |
|---|---|---|---|---|
| Research | Product classification (HTS per country) | AS400 classification master | Product classification | History and effective dates; leading zeros; expired numbers |
| Research | Tariff rates and additional duties (for example HTSUS Chapter 99) | National tariff schedules, Tariff-Impact Briefs, Excel | Trade content and duty rates ([COMPANY: in scope?]) | Effective and end dates; stacking rules |
| Research | USMCA qualification and supplier certifications | AS400 flags, certification files, bills of material | Trade agreement qualification | Blanket periods; missing certifications |
| Standard Cost | Duty rates used in standard cost | [COMPANY: name of std-cost tool] | Landed cost or duty calculation ([COMPANY: in scope?]) | Rates without dates; hard-coded rates |
| Standard Cost | Landed-cost components (freight, fees, brokerage factors) | [COMPANY: name of std-cost tool], Oracle | Landed cost | Allocation basis; currency |
| Standard Cost | Broker entry data (actual duty) | Broker files, data warehouse | Import declaration history | Line-level matching to items |
| Both | Parties (suppliers, producers, brokers, importer of record) | Oracle supplier master, AS400 | Party master | Duplicates; addresses for certifications |

### Part 5: Data profiling checklist

Run on the full extract, save the queries and results with the date, and repeat on each new extract.

- [ ] Row count matches the source system's own count for the same filter and date.
- [ ] The key is unique (no duplicate item + country); duplicates are listed.
- [ ] Blank and null counts per field; no blanks in fields the target requires.
- [ ] HTS length by country: US 10 digits (8-digit subheading + 2-digit statistical suffix), Canada 10 digits (8-digit tariff item + 2-digit statistical suffix), Mexico 10 digits (8-digit fracción + 2-digit NICO).
- [ ] Leading zeros are intact for chapters 01 to 09; no periods, spaces or scientific notation.
- [ ] Each HTS number exists in the current national schedule for its country (HTSUS, Canada Customs Tariff, TIGIE with NICO). Expired numbers are listed for Research.
- [ ] The first 6 digits agree across US, CA and MX for the same item. Differences are usually errors but not always; list them for Research review.
- [ ] Country codes are valid ISO 3166 alpha-2; units of measure and status codes all appear in the value map.
- [ ] Dates are valid and in range; "no date" values (0, 9999999) are identified.
- [ ] Every item exists in the item master ([COMPANY: Oracle]); orphans are listed.
- [ ] Active and inactive records are counted; the scope decision is written down.
- [ ] Coded fields contain no free text; special characters and encoding are checked.
- [ ] USMCA data: every item flagged as qualifying has a qualification record and a certification whose blanket period is 12 months or less and still current.
- [ ] Numeric fields: decimal places confirmed; negatives and outliers checked (a duty rate above 100% can be real with stacked additional duties; verify it against the brief).

A starting query for SQL Server (replace stg_classification and the column names with your staging table):

```sql
-- Rows, distinct keys and duplicates
SELECT COUNT(*) AS row_count,
       COUNT(DISTINCT CONCAT(item_no, '|', country)) AS distinct_keys
FROM stg_classification;

SELECT item_no, country, COUNT(*) AS n
FROM stg_classification
GROUP BY item_no, country
HAVING COUNT(*) > 1;

-- HTS length by country (LEN ignores trailing blanks; use DATALENGTH to see them)
SELECT country, LEN(hts) AS hts_len, COUNT(*) AS n
FROM stg_classification
GROUP BY country, LEN(hts)
ORDER BY country, hts_len;
```

### Part 6: Cleansing log

| Issue ID | Map ID | Issue and record count | Decision | Owner | Status and date |
|---|---|---|---|---|---|
| [DQ-01] | [XX-03] | [What is wrong; how many rows] | [Fix at source, Fix in transform, Accept, Exclude] | [Name] | [Open, In progress, Done; date] |

Decision rules:

- **Fix at source** is the default. It keeps the AS400 data, the broker feeds and e2open in agreement during any parallel run.
- **Fix in transform** only for mechanical, rule-based fixes (for example zero-padding), written into table A.
- **Accept** only with a written reason from the data owner.
- **Exclude** only with data-owner approval and an archive plan for the excluded records.
- A correction to classification, value or origin data is a compliance change. Research is maker, the Senior is checker, and it goes through a change request (`docs/templates/bsa/06-change-request.md`). If past entries may have used the wrong data, tell the Manager; any correction of a past entry is filed by the broker on [COMPANY: trade compliance lead]'s decision.

### Part 7: Reconciliation

| Check | Source result | Target result | Difference | Tolerance | Pass/Fail |
|---|---|---|---|---|---|
| Total records (same filter) | [n] | [n] | [n] | 0, or explained by excluded records in the cleansing log | [ ] |
| Records by country | [n per country] | [n per country] | [ ] | Same | [ ] |
| Distinct keys | [ ] | [ ] | [ ] | 0 | [ ] |
| Control total (sum of a numeric field, or of HTS numbers as a hash total) | [ ] | [ ] | [ ] | 0, or [COMPANY: tolerance] for amounts | [ ] |
| Blanks in required target fields | n/a | [n] | [ ] | 0 | [ ] |
| Sample check, field by field | [25 random + all edge cases] | [Matches] | [Mismatches] | 0 | [ ] |

Edge cases to include in every sample: HTS chapters 01 to 09; descriptions with accented characters; the longest descriptions (truncation); items classified in all three countries; USMCA-flagged items; classifications changed in the last 90 days; the earliest and latest dates.

Re-run every check after each test load and at cutover. Keep the queries, results, date and load ID together; they are UAT and audit evidence.

### Part 8: Sign-off

| Role | Name | Decision | Date | Version reviewed |
|---|---|---|---|---|
| Data owner (business) | [COMPANY: data owner] | [Approved, Approved with conditions, Rejected] | [ ] | [ ] |
| BSA maker | [ ] | Submitted | [ ] | [ ] |
| Checker | [Senior] | [Review complete; findings closed] | [ ] | [ ] |
| e2open data or integration lead | [COMPANY: name] | [ ] | [ ] | [ ] |
| Manager | [ ] | [ ] | [ ] | [ ] |

## Filled example (illustrative)

Product classification master, AS400 to e2open. Field and file names stay as [COMPANY: ...] until the AS400 data dictionary and the e2open load template are in hand. Counts are illustrative.

| Field | Entry |
|---|---|
| Spec ID and version | DM-RES-01 v0.3 |
| Object | Product classification master |
| Source system | AS400 trade system: [COMPANY: item classification file] |
| Target system | e2open GTM: [COMPANY: product classification load template] |
| Type | One-time migration load, then e2open becomes the master |
| Record scope (filter) | Active items; countries US, CA, MX |
| Key | Item number + country |
| Maker and checker | Hire A; Senior |

Table A: field mapping

| Map ID | Source file/table | Source field (type) | Target field (type, required?) | Transform rule |
|---|---|---|---|---|
| CL-01 | [COMPANY: item classification file] | [COMPANY: item number field] (CHAR 15) | Product ID (text, Y) | Trim |
| CL-02 | Same | [COMPANY: country field] (CHAR 2) | Classification country (code, Y) | Lookup VM-01 |
| CL-03 | Same | [COMPANY: HTS field] (numeric, 10 digits, 0 decimals) | Tariff number (text 10, Y) | Convert to text; Pad to 10 digits |
| CL-04 | Same | [COMPANY: classification date field] (numeric 7, CYYMMDD) | Effective-from date (date, N) | Convert CYYMMDD to YYYY-MM-DD; 0 becomes blank |
| CL-05 | [COMPANY: item master file] | [COMPANY: origin field] (CHAR 2) | Country of origin (code, Y) | Direct |
| CL-06 | Same | [COMPANY: USMCA flag] (CHAR 1, Y or N) | Trade agreement qualification (separate object) | Not migrated as a flag; see VM-02 and open question |

Table B: data quality and open questions

| Map ID | Data quality rule | Open question | Owner | Status |
|---|---|---|---|---|
| CL-01 | Unique with country; must exist in the Oracle item master | None | Hire A | Agreed |
| CL-02 | Only US, CA, MX | None (profiling found only those three) | Hire A | Agreed |
| CL-03 | 10 digits after padding; exists in the current schedule for that country | Is HTS numeric for all three countries, or only for US? | [COMPANY: AS400 system owner] | Open question |
| CL-04 | Valid date, not in the future | Does 0 mean "never set" or "set before the field existed"? | [COMPANY: data owner] | Open question |
| CL-05 | Valid ISO code; not blank for active items | None | [COMPANY: item data owner] | Agreed |
| CL-06 | Every Y needs a qualification record and a current certification | Does the e2open scope include USMCA qualification and supplier certification collection? | [COMPANY: e2open project lead] | Open question |

Value map VM-02 shows why a single Y/N flag cannot move as is: the same claim is coded differently in each country.

| Value map ID | Source value | Target value | Meaning | Notes |
|---|---|---|---|---|
| VM-02 | Y | US: SPI "S", or "S+" where the HTSUS gives different treatment by partner country | USMCA claim on the US entry | HTSUS General Note 3(c)(i); the broker enters it |
| VM-02 | Y | CA: tariff treatment code 10 (UST) or 11 (MXT) | CUSMA claim on the Canadian accounting declaration | UST or MXT depends on the CUSMA Tariff Preference Regulations |
| VM-02 | Y | MX: [COMPANY: pedimento coding, confirmed with the agente aduanal by the Senior] | T-MEC claim on the pedimento | Not confirmed here. Before day 60, the hire asks the Senior, not the agente aduanal |
| VM-02 | N or blank | No preference | Pay the non-preferential rate | Blank needs a source fix |

Cleansing log

| Issue ID | Map ID | Issue and record count | Decision | Owner | Status and date |
|---|---|---|---|---|---|
| DQ-01 | CL-03 | 312 US rows with 9 digits (leading zero lost, chapters 01 to 09) | Fix in transform (Pad); also fix the source | Hire A; [COMPANY: AS400 system owner] | In progress |
| DQ-02 | CL-03 | 47 rows whose HTS number is not in the current schedule | Fix at source: Research reclassifies (Hire A maker, Senior checker, change request) | Hire A | In progress |
| DQ-03 | CL-05 | 18 active items with blank origin | Fix at source | [COMPANY: item data owner] | Open |
| DQ-04 | CL-01 | 6 items (18 rows) not in the Oracle item master | Exclude; list archived with the spec | [COMPANY: data owner] | Done, approved |

Reconciliation after test load 1

| Check | Source result | Target result | Difference | Tolerance | Pass/Fail |
|---|---|---|---|---|---|
| Total records (active, 3 countries) | 41,250 | 41,232 | 18 | Explained by DQ-04 | Pass |
| Records for US | 13,750 | 13,744 | 6 | Explained by DQ-04 | Pass |
| Blanks in required target fields | n/a | 0 | 0 | 0 | Pass |
| Sample: 25 random + 15 edge cases | 40 | 39 match | 1 | 0 | Fail: a 1990s date loaded as 2090s (century digit misread). Logged as DQ-05 |

## Quality checklist before you send

- [ ] One object and one direction per spec; header complete, including key, scope and data owner.
- [ ] Target field names come from the e2open data dictionary or load template, or are marked TBC.
- [ ] The source was profiled before mapping, and the profiling results are saved with their date.
- [ ] Every target field has a row (mapped, derived, defaulted or not migrated, with a reason).
- [ ] Transform rules use the standard vocabulary and are specific enough to code from.
- [ ] Every coded field has a complete value map, including blanks.
- [ ] Every Map ID has a data quality rule; open questions have an owner.
- [ ] HTS numbers are text, the right length per country, with leading zeros kept.
- [ ] Classification, value and origin corrections are routed through Research, a checker and a change request.
- [ ] The reconciliation covers counts, a control total and a sample with edge cases, and every difference is explained.
- [ ] The Senior's review is recorded and the data owner has signed the current version.
