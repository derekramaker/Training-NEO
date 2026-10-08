# Trade Systems, GTM and e2open Primer

Last updated: 2026-10-08 · Owner: BSA Manager

- **Purpose:** the self-study backbone for M2 (trade systems and GTM) and the preparation for M10 (the e2open project). It explains what a Global Trade Management (GTM) system does, the data objects behind it, how trade data flows between Oracle, the trade system, brokers, customs and reporting, how legacy AS400 (IBM i) trade systems are usually built and how to explore ours safely, what e2open publicly offers, and the migration concepts you will use from January 2027. It is not screen-by-screen AS400 training: the AS400 is being replaced.
- **Who uses it:** Hire A and Hire B for self-study (about 7 hours including the exercise). The Manager, who teaches M2 and is the only trainer for the AS400 and the custom tools, uses Sections 4, 7 and 8 for the Tue 10/20 landscape session and the Tue 10/27 data-flow walkthrough. The Senior uses Sections 2 and 6 for the W9 GTM data domains session.
- **When:** follow the study plan below. Re-read Section 6 before the e2open kickoff (expected W12) and Section 2 before drafting your data map (W10 to W13).

## How to use this primer

| Session | When (see `docs/02-weeks-1-2-schedule.md`) | Sections | Focused time | Output |
|---|---|---|---|---|
| 1 | W1 Tue 10/20, 14:30 (after the landscape session) | 1 to 3: GTM functions, data objects, data flows | 1.5 h | Landscape diagram v1: system, data and owner on each box |
| 2 | W1 Fri 10/23 (Hire A); W2 Fri 10/30 13:00–13:45 (Hire B) | 5: e2open | 0.5 h | 3 Anki cards |
| 3 | W2 Tue 10/27 (before and after the AS400 walkthrough) | 4, then Exercise 1 (Section 7) | 1.5 h | Data-flow v1 and a 5-row mini data map |
| 4 | W3 | 3.3 and 3.4 (Oracle touchpoints, broker exchange) again; Section 8 questions | 0.75 h | Questions sent to the Manager, batched |
| 5 | W4 to W5 | Finish Exercise 1; Section 9 self-check | 1 h | Day-30 evidence for A30-4 / B30-4: diagram and notes |
| 6 | W8 to W9 | 6: migration concepts and W9 preparation | 1 h | W9 checklist done; list of your process's data elements |
| 7 | W12 (before kickoff) | 5.3 and 6 again | 0.5 h | Kickoff questions |

Tailoring:

- **Hire A (Research):** focus on classification, trade content and duty-rate data (Sections 1.2, 1.9 and 2). Your e2open data map covers HTS codes, rates, countries, programs, effective dates and sources (A60-8, A90-3). If you script, use Python only against extracts, never against production (Section 4.7).
- **Hire B (Standard Cost):** focus on landed cost, broker entry data and Oracle touchpoints (Sections 1.4, 3.3 and 3.4). Your data map covers duty rates, landed-cost components, broker entry data for actual duty, and the Oracle item cost interface (B90-3). You already know the business, so go deeper on data early: in W3, profile a sanitized broker entry data extract against item master data (match rate, unmatched lines, unit-of-measure mismatches).

Rules: [COMPANY: ...] marks a company fact the Manager must confirm. Never invent a program, file, report or interface name; leave the placeholder and log the question. Definitions are in `data/trackers/glossary.csv`.

## 1. What a GTM system does

A Global Trade Management (GTM) system holds trade compliance master data and runs trade processes: what an item is for customs purposes in each country, where it comes from, whether it qualifies for a trade agreement, what duty it will pay, whether it can be exported, and what was actually declared. Today these functions are spread across the AS400 trade system, our custom tools, spreadsheets, the brokers and Oracle [COMPANY: confirm]. The e2open project will move some of them into one system.

### 1.1 The functions at a glance

| Function | What it does | Key data | Typical outputs | Where it happens today |
|---|---|---|---|---|
| Product classification master | Stores tariff codes per item per country with history; runs the request, decide, review and approve workflow; handles mass changes when tariff schedules change | Item, description, attributes, code per country, effective dates, rationale, status | Codes to brokers and ERP; audit trail | [COMPANY: AS400 classification file or screen] |
| Trade agreement qualification | Decides whether items qualify for USMCA (and other agreements); runs supplier solicitation; tests bills of material against product-specific rules; manages certificates | BOM, component origin and value, rules of origin, certificates | Qualification result per item, agreement and period; certifications | [COMPANY: AS400 flags, spreadsheets, custom tool] |
| Landed cost and duty calculation | Calculates duty, additional duties and fees per item, origin and route; models scenarios | Classification, origin, rates, fees, freight, value | Duty and landed cost per item; scenario comparisons | [COMPANY: name of std-cost tool], Tariff-Impact Model |
| Customs filing integration and broker data exchange | Sends product and shipment data to brokers (or files directly); receives declaration data back; validates and reconciles | Item codes, origin, preference flags, invoice data; entry lines | Broker files; entry history; audit exceptions | [COMPANY: broker interfaces, data warehouse] |
| Restricted party screening (awareness only) | Screens customers, suppliers and other parties against government restricted lists; holds possible matches | Party names and addresses; list content | Screening results, holds, audit trail | [COMPANY: screening tool or process] |
| Export compliance and license determination | Stores export classifications (ECCN, Schedule B); determines whether a license is needed for a destination, end user and end use; manages licenses; supports export filing | ECCN, destination, parties, license details | License determinations; shipment holds; export filing data | [COMPANY: exports process, Senior] |
| Special programs | Tracks inventory and balances for duty programs: Mexico IMMEX temporary imports (Anexo 24), US duty drawback (matching imports to exports) | Import declarations, inventory movements, exports, BOM consumption | Program inventory, claims, reports to authorities | [COMPANY: IMMEX system; drawback with the Senior] |
| Trade content | Supplies tariff schedules, duty rates, rules of origin, regulations, rulings and restricted lists, kept current by the vendor | Vendor content feeds, versioned by date | Rates and rules used by every other function | [COMPANY: today maintained by hand from official sources?] |
| Reporting and audit | Reports on duty spend, savings, exceptions and audit trails; extracts to BI | Everything above | Dashboards, audit evidence, data for Power BI | SQL Server, data warehouse, Power BI, Excel |

### 1.2 Product classification master

- **How it works:** each item gets one tariff code per import (and export) country, valid from a date. A change creates a new version with a new effective date; the old one is kept. Good systems capture the rationale (rule applied, rulings cited), the preparer and the approver.
- **What goes wrong:** codes overwritten with no history, so nobody can say what was declared last year; codes valid in one country copied into another; expired codes left on active items after a tariff schedule change; no record of why a code was chosen.
- **BSA questions:** who can change a code, how is it reviewed, and how fast does a change reach each broker?

### 1.3 Trade agreement qualification (origin)

- **Supplier solicitation:** the system sends suppliers requests for certifications or component origin data, tracks responses and expiry dates, and stores the documents.
- **BOM qualification:** for items we (or our suppliers) produce, the system takes the bill of materials, each component's classification, origin and value, and tests it against the product-specific rule: tariff shift first, then de minimis and regional value content where the rule allows (see Section 10 of `docs/primers/customs-trade-compliance-primer.md`).
- **Result:** a qualification record per item, agreement, import country and period, linked to the BOM version and certificates that support it. The broker's preference claim should come from this record.
- **What goes wrong:** qualification flags with no supporting record; certifications that expired while the flag stayed "Y"; BOM changes that never trigger requalification.

### 1.4 Landed cost and duty calculation

- **How it works:** for an item, an origin, an import country and a date, the system finds the classification, the base duty rate, any preference (if qualified), additional duties and their stacking rules, and fees, and applies them to the right duty base (FOB-like in the US and Canada, CIF-like in Mexico). Add freight, insurance, brokerage and inland costs and you have landed cost.
- **Why it matters here:** this is the input to Standard Cost (Hire B) and the engine of the Tariff-Impact Model. The boundary rule still applies: Research decides the WHAT of a new action (scope, rates, dates, stacking) in the Tariff-Impact Brief; Standard Cost owns the $.
- **What goes wrong:** rates with no effective dates; hard-coded rates in spreadsheets; freight added to the US duty base; an additional duty applied to the wrong origin.

### 1.5 Customs filing integration and broker data exchange

- **Data out:** product data (item, codes per country, origin, preference flags) and sometimes shipment data (invoice lines) go to each broker.
- **Data back:** the broker's declarations at line level (US entry summary, Canadian CAD, Mexican pedimento), used for audits, actual duty and PPV, and drawback.
- **What goes wrong:** the file stops arriving and nobody notices; a layout change breaks the load; lines cannot be matched to items; the broker overrides our code without telling us.

### 1.6 Restricted party screening (awareness)

Screening compares party names and addresses against lists such as the US Consolidated Screening List. A possible match is put on hold and escalated to [COMPANY: screening owner]. The hires never clear a match.

### 1.7 Export compliance and license determination

The system stores each item's export classification (ECCN or EAR99, Schedule B), applies country and party rules, records licenses with their limits and expiry, and holds shipments that need review. License determinations stay with the Senior.

### 1.8 Special programs

- **IMMEX (Mexico):** an automated inventory control system (Anexo 24) tracks each temporarily imported input from its pedimento to consumption, export, transfer or change of regime, with time limits per input. SAT's credit and guarantee account system (the SCCCyG: RGCE Anexo 30, formerly Anexo 31, a name the trade still uses) must reconcile with it.
- **US duty drawback:** the system matches import entries (duty paid) to exports or destruction within the time limits and prepares claim data. Drawback stays with the Senior.
- Whether e2open will handle either for us is a project scope question (Section 5.3).

### 1.9 Trade content

Trade content is the reference data behind everything: tariff schedules and rates, rules of origin, regulations, rulings, restricted lists. A vendor maintains it and pushes updates. Two cautions:

- Vendor content can lag a new tariff action, or interpret it differently from us. Until the content is confirmed, the Tariff-Impact Brief (sources cited) governs. Research checks vendor content against the primary sources in `docs/primers/current-tariff-landscape.md`.
- Content changes must be dated. A rate that changed on a date must be stored with that date, or historical landed cost and audits break.

### 1.10 Reporting and audit

Typical reports: duty paid by country, origin and program; preference savings; items without classification; expiring certifications; broker filing exceptions; screening holds. Many of ours live in SQL Server, the data warehouse and Power BI today (M3, M8) [COMPANY: report inventory].

## 2. Data objects and relationships

### 2.1 The main objects

| Object | Key (what one row is) | Important attributes | Related to | Source today |
|---|---|---|---|---|
| Item (product) | Item number | Description, trade description, unit of measure, weight, material composition, status | Classifications, supplier items, BOMs, entry lines | [COMPANY: Oracle item master and/or AS400] |
| Classification | Item + country + effective-from date | Tariff code, status, rationale, preparer, approver, effective-to date | Item; trade content (rates) | [COMPANY: AS400] |
| Country of origin | Item + supplier (or ship-from site) + effective date | Non-preferential origin, basis, marking | Item, party | [COMPANY] |
| Party | Party ID + address | Name, role (supplier, producer, customer, broker, importer), identifiers (US MID, BN15, RFC, tax IDs), related-party flag, screening status | Supplier items, certificates, entries | [COMPANY: Oracle supplier master, AS400] |
| Supplier item (sourcing) | Item + supplier + site | Price, currency, Incoterm, origin | Item, party, purchase orders | [COMPANY: Oracle] |
| Bill of materials (BOM) | Parent item + component + effective date | Quantity per, component cost, component origin and classification | Items (parent and components), qualification | [COMPANY: Oracle BOM, AS400, spreadsheets] |
| Trade agreement qualification result | Item + agreement + import country + period | Qualified (Y/N), origin criterion, method (tariff shift, RVC), RVC percent, producer, BOM version used | Item, BOM, certificates | [COMPANY] |
| Certificate (origin certification or supplier declaration) | Certificate ID | Certifier, items covered, blanket period, received date, status, document link | Party, items, qualification | [COMPANY: certificate repository] |
| Duty rate (trade content) | Tariff code + country + rate type + effective dates | Rate (ad valorem, specific, compound), unit, conditions, legal source | Classification | [COMPANY: AS400 rate table, custom tool, Excel] |
| Additional duty measure | Measure ID (for example a Chapter 99 number) + effective dates | Scope (codes, origins), rate, stacking rules, exclusions, source | Duty rates; items via classification and origin | Tariff-Impact Briefs; [COMPANY] |
| Entry (declaration header) | Entry, CAD or pedimento number + country | Importer, broker, port, entry, release and liquidation dates, totals | Entry lines | [COMPANY: broker files, warehouse] |
| Entry line | Entry + line number | Item (once matched), tariff code, origin, value, quantity, unit, preference claimed, rates, duty, fees | Entry, item, PO and receipt | [COMPANY: broker files, warehouse] |
| Purchase order and receipt | PO line; receipt line | Quantity, price, currency, dates | Item, entry lines (by matching) | [COMPANY: Oracle] |
| Landed-cost component | Item + cost type + period | Duty, freight, fees, brokerage factors | Item; Oracle standard cost | [COMPANY: name of std-cost tool], Oracle |
| Export classification and license | Item (+ jurisdiction); license number | ECCN, Schedule B; license limits and expiry | Item, party, shipments | [COMPANY] |
| IMMEX inventory record | Temporary import pedimento line + item | Quantity in, quantity discharged, balance, due date | Entries (pedimentos), BOM consumption | [COMPANY] |

### 2.2 How they connect

- An **item** has many **classifications** (one per country per effective period).
- An item has many **supplier items**, each with a **country of origin**.
- An item can be the parent of a **BOM**; its components are also items, each with its own classification and origin.
- An item has many **qualification results** (per agreement, import country and period), each supported by a BOM version and one or more **certificates**.
- A **classification code** links to **trade content**: base duty rates, **additional duty measures**, other-agency requirements.
- A **party** links to supplier items, certificates and entries (as importer, broker or manufacturer).
- An **entry** has many **entry lines**. Each line is matched to an item and to a PO or receipt. The duty on the line is the actual duty that feeds PPV, audits and drawback.

### 2.3 Grain, dates and history

- **Grain** is what one row represents. Classification is item + country + date, not item. Joining an item table to a classification table without filtering country and date multiplies rows (join fan-out; see the glossary and the M3 practice pack).
- **Effective dating:** codes, rates, qualifications and certificates are all valid for a period. Queries must ask "as of which date?". A system that overwrites values loses the ability to explain past filings and costs.
- **Codes are text, not numbers:** keep leading zeros (chapters 01 to 09) and store codes without periods. Excel will damage them if you let it.
- **HS 2028:** on 1 January 2028 the next HS edition takes effect, and every classification in every country gets a new version. The e2open data model must handle this mass change with dates and history (Section 6.4).

## 3. How trade data flows

### 3.1 End to end

The flow below is generic. In Exercise 1 you replace each [COMPANY] with how it works here.

| Step | From and to | What moves | Trigger and frequency | What to check |
|---|---|---|---|---|
| 1 | Oracle to trade system | New or changed items: number, description, unit of measure, supplier | Item creation or change; [COMPANY: interface and schedule] | New items with no classification after [COMPANY: N] days |
| 2 | Within the trade system | Classification per country, by the team, with maker-checker review | Item request or tariff change | Items imported with no code or an expired code |
| 3 | Suppliers to trade system | Origin data, USMCA certifications, BOM data | Supplier solicitation cycle | Expired or missing certifications on claimed items |
| 4 | Oracle (purchasing) | PO: price, currency, Incoterm, supplier, ship-to country | PO creation | PO terms that differ from the invoice |
| 5 | Trade system to brokers | Product file: item, codes per country, origin, preference flags | [COMPANY: batch job, full or delta, schedule, delivery] | File sent; record counts; rejects returned |
| 6 | Supplier and forwarder to broker | Commercial invoice, packing list, transport documents | Each shipment | Invoice versus PO |
| 7 | Broker to customs | US entry and entry summary; Canadian CAD; Mexican pedimento | Each shipment | Not our system, but our data |
| 8 | Customs to broker to us | Release, questions (CBP Forms 28 and 29), liquidation | Event-driven | Who receives them [COMPANY] |
| 9 | Brokers to us | Declaration data at line level | [COMPANY: file or report, schedule] | Arrival, counts, unmatched lines |
| 10 | Brokers to Oracle (AP) | Broker invoices: duty, fees, brokerage | Each shipment | [COMPANY: how duty is coded in AP] |
| 11 | Oracle (receiving and cost) | Receipt at standard cost (including duty); PPV against actual | Each receipt | PPV driven by duty differences |
| 12 | Standard Cost process to Oracle | New duty rates and landed-cost factors in the cost update, with Finance | Cost cycle [COMPANY: calendar] | Maker-checker sign-off (`docs/templates/domain/standard-cost-update-checklist.md`) |
| 13 | Systems to warehouse to BI | AS400, Oracle and broker data to SQL Server and the warehouse; reports in Power BI and Excel | [COMPANY: ETL schedule] | Refresh failures; numbers that do not tie to the source |
| 14 | Research to everything | A new tariff action: Tariff-Impact Brief, then the Tariff-Impact Model, then codes, rates, broker instructions and cost updates | Action published | Maker-checker on the brief and the model |

### 3.2 Where data quality breaks

| Break point | Symptom | Control that should catch it |
|---|---|---|
| Item set up without trade data | Broker classifies on its own; first entries use a guessed code | Report of active items with no classification per import country |
| Classification changed but brokers not updated | Filed code differs from our master | Broker filing audit (customs primer, Section 7.3) |
| Origin or certification out of date | Preference claimed without support | Expiring-certification report; claim versus certificate check |
| Rate tables not dated or not updated for a new action | Wrong landed cost; wrong standard cost | Rate table with effective dates; checker review of the cost update |
| Broker entry file missing or changed layout | Gaps in actual duty; PPV unexplained | Arrival monitoring with record counts and control totals |
| Entry lines not matched to items | Audits and PPV by item impossible | Match-rate metric; exception queue |
| Unit of measure mismatch | Wrong specific duty; wrong per-unit cost | Conversion table, profiled |

### 3.3 Oracle touchpoints

Oracle is the ERP; whether it is E-Business Suite or Fusion matters for table and screen names [COMPANY: Oracle EBS or Fusion]. Keep the concepts below and fill in the names in M2.

| Oracle area | Trade-relevant data | Direction | Notes |
|---|---|---|---|
| Item master | Item number, description, unit of measure, status; possibly some trade fields | Oracle to trade system | [COMPANY: which system is the master for each field] |
| Supplier master | Supplier names, sites, addresses; related-party indicator | Oracle to trade system | Addresses feed certifications and MIDs |
| Purchasing | PO price, currency, terms (Incoterm), ship-from and ship-to | Oracle to brokers (via documents) and models | The price is the start of transaction value |
| Receiving | Receipt quantity and date | Within Oracle | Receipt at standard cost creates PPV |
| Costing | Standard cost by cost element; where duty, freight and fees sit | Standard Cost process to Oracle | [COMPANY: Oracle EBS or Fusion cost elements and sub-elements] |
| Payables | Broker and carrier invoices: duty, fees, freight | Brokers to Oracle | Actual duty for PPV |
| BOMs (if used) | Kit and assembly structures | Oracle to trade system (if integrated) | [COMPANY: where kit structures live] |

### 3.4 Broker data exchange patterns

| Pattern | How it works | Typical formats | What fails |
|---|---|---|---|
| Product (parts) file, data out | Periodic full or delta file of items with codes per country, origin and preference flags, one per broker | Fixed-width or delimited flat file, Excel; SFTP, email or broker portal | Deltas missed; stale codes; wrong country's file; leading zeros lost |
| Shipment data, data out | Invoice or PO line data per shipment, so the broker can build entry lines | Flat file, EDI, PDF invoices | Lines that cannot be matched to the product file |
| Declaration data, data back | Line-level entry, CAD or pedimento data | Flat file, Excel, EDI; broker portal downloads | File stops arriving; layout changes; unmatched lines |
| Government portal reports | ACE Portal reports (US); CARM Client Portal statements and declarations (Canada) | CSV or Excel downloads | Manual; access lapses when people leave |
| Broker invoices | Duty, fees and brokerage billed | PDF or EDI to AP | Duty coded to the wrong account |

Controls every interface needs: a header or trailer with record counts and totals; a reject file and who gets it; someone who checks that it ran; and advance notice and a test file before any layout change. Record them in Part 4 of `docs/templates/bsa/04-data-mapping-spec.md`. [COMPANY: broker interface specifications].

## 4. Legacy AS400 (IBM i) trade systems

"AS400" is the everyday name for IBM's midrange platform. AS/400 was the original name (later iSeries and System i); the operating system today is **IBM i**, and its built-in database is **Db2 for i**. Many trade systems were built on it in-house or bought as packages and customized. This section explains the common patterns so the Manager's walkthrough makes sense. It is generic: our actual libraries, files and programs are [COMPANY: ...] until the Manager shows them.

### 4.1 Vocabulary translation

| IBM i term | What it is | Nearest SQL Server or Windows idea | Why it matters to you |
|---|---|---|---|
| Library | A container for objects (files, programs) | Schema or database | Trade data may sit in several libraries: production, test, history [COMPANY] |
| Physical file (PF) | An object that holds data in records | Table | The real data |
| Logical file (LF) | A keyed or filtered view over one or more physical files | View or index | Same data in another order or subset; never add it to its physical file and double count |
| Member | A partition inside a file | Partition | SQL reads the first member unless an alias is created; multi-member files can hide data |
| Record format and field | Row layout and column | Row and column | System names are 10 characters or fewer and cryptic; use the field text descriptions |
| DDS or SQL DDL | Two ways files are defined: older Data Description Specifications, or SQL | Table definition scripts | Tells you types, lengths and decimal places |
| Db2 for i | The integrated relational database | SQL Server | It can be queried with SQL (ODBC, JDBC) if access is granted |
| Program (RPG, COBOL, CL) | Business logic (RPG or COBOL) and job control (CL, Control Language) | Stored procedures, scripts | Business rules live in code, not in tables. Ask the owner, do not guess |
| Batch job, job queue, job scheduler | Background processing, often scheduled (the IBM i job scheduler or a third-party scheduler) | SQL Agent jobs, Task Scheduler | Broker files, rate updates and extracts usually run as nightly jobs |
| Spooled file and output queue | Report output waiting to print or be viewed | Report files | Many "reports" are spooled files that someone exports to Excel |
| 5250 "green screen" | The terminal interface, used through IBM i Access Client Solutions (ACS) | Application screens | Inquiry screens show the data the way the business sees it |
| IFS (Integrated File System) | Directory-style storage for stream files | File share | Flat files to and from brokers often land here |
| Journal | A log of changes to files, if journaling is switched on | Change data capture or audit log | Can show who changed a code and when; ask whether it exists |
| CCSID and EBCDIC | Character encoding on the server | Code page | Accented characters (é, ñ) can break in extracts |

### 4.2 Typical building blocks of an AS400 trade system

| Building block | Typical content | Ours |
|---|---|---|
| Item trade master file | Item, trade description, origin, program flags | [COMPANY: library/file] |
| Classification file | Item, country, tariff code, effective dates, status | [COMPANY: library/file] |
| Tariff rate table | Code, country, rate, effective dates (often maintained by hand) | [COMPANY: library/file or "not on AS400"] |
| Origin and USMCA files | Qualification flags, certificate references, expiry dates | [COMPANY] |
| Party cross-reference | Trade-system supplier ID to Oracle supplier; manufacturer IDs | [COMPANY] |
| Code tables | Country, unit of measure and status codes | [COMPANY] |
| Broker extract programs and jobs | Build the product file for each broker and send it | [COMPANY: program and job names, schedule] |
| Entry upload programs | Load the declaration data that brokers return | [COMPANY] |
| History or audit files | Before and after images of changes | [COMPANY: exists?] |
| Inquiry and maintenance screens | Menus to look up and change trade data | [COMPANY: menu path, inquiry-only options] |
| Reports and queries | Spooled reports, saved Query/400 queries | [COMPANY: report list] |

### 4.3 Batch jobs and schedules

For each job that matters to your process, find out: what it does, when it runs, what it depends on, who is alerted when it fails, how it is rerun, and who owns it. A trade system's failures are usually silent: a job that did not run means a broker filed with yesterday's codes. [COMPANY: job schedule list and owner].

### 4.4 Green-screen inquiry

- Screens are reached through menus. "Work with" list screens usually take option codes next to a line. A common convention is 5 = display, 2 = change, 4 = delete; function keys F3 = exit and F12 = cancel are also common. **Applications vary: confirm the options on every screen with the Manager before you use it.**
- Use only display options. Your access (AR-06 in `docs/04-access-request-checklist.md`) is meant to be inquiry-only; if a screen lets you change data, stop and tell the Manager.
- Inquiry screens are the fastest way to see one known item end to end: item, codes per country, origin, flags.

### 4.5 Flat-file and EDI exchanges

- **Fixed-width** files place each field at set positions; **delimited** files (CSV) separate fields with a character. Fixed-width layouts need a layout document; without one, the file is unreadable.
- Files are often built by a batch program, copied from a database file to a stream file (for example with the CPYTOIMPF command), placed on the IFS and sent by FTP or SFTP [COMPANY: method].
- **Control records:** a header or trailer with the record count and totals proves the file is complete.
- **EDI** (for example ANSI X12) needs a translator that maps the standard to the internal layout. Customs filing itself (ABI in the US, CARM in Canada, the pedimento in Mexico) is done by the broker's systems, not ours.
- Watch for: leading zeros lost, numbers with implied decimals, dates as CYYMMDD, accented characters, trailing blanks.

### 4.6 Query tools

| Tool | What it is | Notes |
|---|---|---|
| Query/400 (WRKQRY) | The classic IBM i query tool; saved queries produce reports or files | Many legacy reports are saved queries [COMPANY] |
| Run SQL Scripts in IBM i Access Client Solutions | An SQL editor against Db2 for i | Needs authority; read-only use only |
| ODBC from Excel, Power Query or SQL Server | Direct database connections | Not part of your inquiry profile (AR-06) unless separately approved |
| Warehouse or SQL Server copies | Data already extracted from the AS400 | **Use these first.** No load on production, and SQL you already know (M3) |

Db2 for i has catalog views that describe files and fields (for example `QSYS2.SYSTABLES` and `QSYS2.SYSCOLUMNS`, which include each field's text description). If the Manager or IT can run a query like `SELECT COLUMN_NAME, COLUMN_TEXT, DATA_TYPE, LENGTH, NUMERIC_SCALE FROM QSYS2.SYSCOLUMNS WHERE TABLE_SCHEMA = 'LIBNAME' AND TABLE_NAME = 'FILENAME'` for the trade files, you have most of a data dictionary.

### 4.7 How to explore an AS400 trade system safely

Rules:

1. **Read-only, always.** Inquiry screens and extracts only. Never use change or delete options, never run a menu option or job you do not fully understand (for example anything that sends files to brokers or updates rates), and never ask for more authority than inquiry.
2. **Prefer copies.** Query the warehouse or an extract, not production. Heavy queries on production during business hours can slow the system for everyone.
3. **Never script against production.** Python, Power Query and Excel work on extracts.
4. **Handle data properly.** Keep extracts in [COMPANY: approved team location], not on personal drives or email.
5. **Ask the owner** before drawing conclusions about business rules. The code, not the field name, decides what a field means.

Steps:

- [ ] Start with the business question and the recording of the Manager's walkthrough.
- [ ] Pick one known item and look it up on the inquiry screens: description, codes per country, origin, flags. Screenshot what you see.
- [ ] Ask which file is behind each screen and get the field descriptions (from `QSYS2.SYSCOLUMNS`, the DSPFFD command, or a layout document) [COMPANY: who can provide the AS400 data dictionary].
- [ ] Find related files: IT can show which logical files sit over a physical file (DSPDBR) and which files a program uses (DSPPGMREF). Ask; do not run commands you do not have authority for.
- [ ] Find the same item in the warehouse or extract and match field by field.
- [ ] Profile the extract with SQL: counts, blanks, distinct values, invalid codes, dates.
- [ ] Confirm what you found with the owner, then write it down: screen, file, field, meaning, owner. This becomes part of your tool doc (`docs/templates/knowledge/tool-doc.md`) and your data map.
- [ ] Log every open question in your question log, batched for the Manager.

### 4.8 Trade-specific data traps

The AS400 reading traps in `docs/templates/bsa/04-data-mapping-spec.md` (packed decimals, CYYMMDD dates, EBCDIC, trailing blanks, code files) all apply. Trade data adds these:

- Tariff codes stored as numbers, losing leading zeros, or with periods in some rows and not others.
- Codes stored at different lengths per country (8 versus 10 digits) in one field.
- Country codes that are internal codes rather than ISO 2-letter codes.
- Effective dates overwritten in place, so there is no history.
- Free-text origin ("CN", "China", "PRC").
- Yes/No flags that also contain blanks and other values, each meaning something different.
- First 6 digits that differ between the US, Canada and Mexico codes for the same item.
- Expired codes still on active items after a tariff schedule change.
- Units of measure that differ between Oracle, the trade system and the customs unit.

## 5. e2open Global Trade Management

This section describes e2open only at the level the vendor states publicly. It was compiled on 2026-10-08 from e2open's public website and press releases. Product names and packaging change; the project's contract and scope decide what we actually get.

### 5.1 The company

- **e2open** is a supply chain software vendor. Its GTM applications will replace our AS400 trade system; the project is expected to start in January 2027 [COMPANY: confirm kickoff date and scope].
- **Amber Road:** e2open acquired Amber Road, a GTM software and trade content vendor, through a cash tender offer and merger announced in May 2019 and completed in early July 2019. Amber Road's GTM applications and trade content became part of e2open.
- **WiseTech Global:** in August 2025 WiseTech Global completed its acquisition of e2open. e2open's 2026 press releases describe it as a WiseTech Global company. Ask at kickoff whether this changes product names, roadmap or support.

### 5.2 Publicly described GTM applications

| Application (as e2open names it publicly) | What e2open says it does | Relevance to us |
|---|---|---|
| Global Knowledge | Trade content: HS codes and national tariff lines, section and chapter notes, binding rulings, WCO Explanatory Notes, rules of origin, restricted party lists; it feeds the other GTM applications | Research still verifies new actions against primary sources (Section 1.9) |
| Product classification (part of the GTM suite; e2open markets AI-assisted classification) | Helps classify products to HS and national codes, using the trade content | Our classification master and its maker-checker workflow |
| Import Management | Import compliance: checking purchase order lines against import regulations, working with suppliers and brokers, visibility of entry stages | Broker data exchange and broker filing audits |
| Customs Filing | Direct (self) filing of customs declarations in a number of countries | We use brokers in all three countries; likely out of scope [COMPANY: confirm] |
| Duty Management | Using free trade agreements and duty programs: supplier solicitation, qualification and certificate management for trade agreements; duty drawback and duty deferral programs. Its help documentation describes BOM-based qualification and supplier campaigns | USMCA qualification and supplier solicitation; drawback (the Senior) |
| Export Management | Export compliance: export classification, license determination and management, export documents | Exports (M7) |
| Due Diligence Screening | Restricted and denied party screening against government lists | Awareness only |
| Landed cost and tariff modeling | e2open says its tariff and duty tables feed landed-cost calculations and scenario modeling | Standard Cost; the Tariff-Impact Model |

Vendor claims (number of lists, countries, accuracy) are marketing statements. Do not repeat them as facts; ask for them in writing if they matter.

### 5.3 What we do not know yet: questions for the project

Do not assume any of these. Each is a [COMPANY: confirm] until the project answers it.

- Which e2open applications and countries are licensed and in scope for the first release.
- Whether Mexico IMMEX and Anexo 24 inventory control are in scope, and in which system they will live.
- Whether landed cost and duty calculation are in scope, and whether results feed Oracle standard cost.
- How broker data exchange will work for each broker and country: who builds the interfaces, in what formats.
- How e2open will integrate with Oracle (items, suppliers, POs, costs) [COMPANY: Oracle EBS or Fusion].
- How much history will be migrated (classification versions, qualification results, entries).
- How the vendor's content is updated for a new tariff action, and how we override or supplement it.
- Whether e2open supports our maker-checker controls (approval workflow, audit trail) for classification and qualification.
- What reporting and data extracts will feed SQL Server, the warehouse and Power BI.
- Which environments (test, UAT, production) exist, and when.

### 5.4 Today's functions mapped to e2open concepts

This is the starting point for the day-30 mapping (A30-4) and the knowledge topic K-M2-07. Fill the "Today" column in M2; the "Status" column stays "confirm" until the project decides.

| Today's function | Where it happens today | e2open concept | Status |
|---|---|---|---|
| Item trade master and classification by country | [COMPANY: AS400 file or screen] | Product classification with Global Knowledge content | Likely replace; confirm |
| Tariff rate tables | [COMPANY: AS400, custom tool, Excel] | Global Knowledge content; duty calculation | Confirm; Research keeps verifying |
| USMCA qualification flags and certificates | [COMPANY] | Duty Management: trade agreement qualification, supplier solicitation, certificate management | Confirm |
| Product files to brokers | [COMPANY: AS400 batch jobs] | Import Management and integrations | Interface; confirm |
| Broker declaration data load | [COMPANY: upload program, warehouse] | Import Management (entry data), or stays in the warehouse | Unknown |
| Landed cost and duty rates for standard cost | [COMPANY: name of std-cost tool] | Landed cost calculation | Unknown |
| Export classification and license determination | [COMPANY] | Export Management | Unknown |
| Restricted party screening | [COMPANY] | Due Diligence Screening | Unknown |
| IMMEX Anexo 24 inventory | [COMPANY] | Not confirmed in public material | Unknown: do not assume |
| Drawback data | [COMPANY: Senior's process] | Duty Management (drawback) | Unknown |
| Trade reports | [COMPANY: AS400 reports, Power BI] | e2open reporting plus the warehouse and Power BI | Interface; confirm |
| Custom tools (10+) | [COMPANY: Tool Inventory tab] | Each needs a disposition: replace, interface, retire or keep | Owned-tool disposition note (day 60) |

## 6. Migration concepts

### 6.1 The phases

| Phase | What it is | BSA role | Deliverable | Common pitfall |
|---|---|---|---|---|
| As-is documentation | How the process and data work today, workarounds included | Interview, observe, map | As-is process doc (`docs/templates/bsa/03-process-map-as-is-to-be.md`) | Documenting the official process, not the real one |
| Future-state (to-be) design | How the process will work in the new system; fit and gap against the vendor's standard | Requirements, fit-gap, decisions log | To-be steps, gap list, requirements (`docs/templates/bsa/02-requirements.md`) | Rebuilding the AS400 inside e2open |
| Data mapping | Field-by-field rules from each source to the target | Map, define transforms, raise open questions | Data map (`docs/templates/bsa/04-data-mapping-spec.md`) | Guessing target field names |
| Data profiling and cleansing | Measuring data quality, then fixing it at the source with the data owner's decision | Profile with SQL, log issues, propose fixes | Profiling results and cleansing log (Parts 5 and 6 of the data-mapping template) | "Fixing" data only in the load file; no owner sign-off |
| Conversion and cutover | Loading data into the new system, reconciling it, then switching over | Reconcile counts and totals; run cutover tasks | Reconciliation evidence; cutover checklist | No rehearsal; no fallback plan |
| Parallel run | Running old and new side by side and comparing outputs | Define comparisons and tolerances; explain differences | Comparison reports | No time budgeted; no tolerance agreed in advance |
| UAT | Business users test the system against the requirements and sign off | Write and run test cases; log defects | UAT plan, results, sign-off (`docs/templates/bsa/05-uat-test-plan.md`) | Testing only the happy path; letting the vendor's tests replace ours |
| Hypercare | Intensive support right after go-live | Monitor, triage issues, fix data | Issue log; stabilization report | Key people on leave; nobody owns the issue list |

### 6.2 What you will do on the e2open project

| Deliverable | Hire A (Research) | Hire B (Standard Cost) | When | Day-90 criterion |
|---|---|---|---|---|
| As-is process doc | The Research process: from a tariff action to briefs, codes and rates | The duty and landed-cost inputs to standard cost | Draft W10, final W13 | A90-2, B90-2 |
| Data map and data-quality log | HTS codes, rates, countries, programs, effective dates, sources | Duty rates, landed-cost components, broker entry data for actual duty, the Oracle item cost interface | Draft W11, final W13 | A90-3, B90-3 |
| Cleansing | Fix the issues your profiling found, through the data owner's decisions | Same | From W12, continuing after day 90 | After day 90 |
| UAT | Test cases for Research scenarios | Test cases for landed cost and cost scenarios | Per the project plan, after day 90 | After day 90 |
| Owned-tool disposition note | For your owned tool | For your owned tool | Day 60 | A60 and B60 tool criteria |

The as-is doc and data map are your day-90 ownership evidence (`docs/01-30-60-90-plan.md`). The holiday weeks (W10 and W11) run at about half capacity, so start early.

### 6.3 Preparing in W9

- [ ] Re-read Sections 2, 3 and 6 of this primer.
- [ ] Walk through the as-is and data-mapping templates with the Manager (W9 session).
- [ ] Attend the Senior's GTM data domains session (product and classification, parties, trade agreements and origin, compliance, landed cost) with your list of data elements.
- [ ] List every data element your process uses, with its system of record, owner and consumers (start from your Exercise 1 worksheet).
- [ ] Profile your top three data elements from an extract: row counts, blanks, invalid codes, duplicates, dates.
- [ ] List the custom tools that touch your process and a first guess at each one's e2open disposition.
- [ ] Draft five kickoff questions from Section 5.3.
- [ ] Block time in W10 and W11 for the as-is draft and data map.

### 6.4 HS 2028 and the data model

HS 2028 takes effect on 1 January 2028, within the first year or so of e2open in production. Every item's classification in every country will be remapped. Ask the vendor how its content and classification tools handle a new HS edition, and make sure the data model keeps classification versions with effective dates, so that 2027 filings remain explainable after the change.

## 7. Exercise 1: map your current-state data flow

Do this after the Tue 10/27 walkthrough and refine it through W5. Together with your landscape diagram it is the evidence for the day-30 trade data-flow criterion (A30-4 and B30-4; Hire B also shows exactly where duty, freight and fees enter Oracle cost data). Post it in OneNote.

- **Hire A:** map "a new tariff action, from publication to updated codes, rates and broker instructions".
- **Hire B:** map "a duty rate, from its source to Oracle standard cost and back as actual duty in PPV".

### 7.1 Header

| Field | Entry |
|---|---|
| Process | [Name] |
| Trigger | [What starts it] |
| Frequency and volume | [How often; how many items] |
| Process owner | [COMPANY: name or role] |
| Systems involved | [AS400 trade system, Oracle, custom tools, Excel, broker portals] |
| Prepared by and date | [Hire A or B, date] |
| Reviewed by | [Manager] |

### 7.2 Steps

| Step | Who | System or file | Data in | Data out | Control |
|---|---|---|---|---|---|
| 1 | [Role] | [COMPANY: system, screen, file or tool] | [Fields] | [Fields] | [Maker-checker? Reconciliation? None?] |
| 2 | | | | | |
| 3 | | | | | |

### 7.3 Data elements

| Data element | System of record | Copied to | Owner | Known issues |
|---|---|---|---|---|
| [Example: US HTS number] | [COMPANY: AS400 classification file] | [COMPANY: broker file, warehouse, std-cost tool] | [COMPANY] | [Leading zeros lost in extract] |
| | | | | |

### 7.4 Interfaces

| Interface | From and to | Format and schedule | Monitoring | Failure signs |
|---|---|---|---|---|
| [Example: product file to US broker] | [AS400 to broker] | [COMPANY: format, nightly?] | [COMPANY: who checks] | [Filed codes differ from master] |
| | | | | |

### 7.5 Pain points and workarounds

| Pain point | How often | Impact | Idea for e2open |
|---|---|---|---|
| [Manual re-keying of rates from a brief] | [Each action] | [Errors, time] | [Rates with effective dates; approval workflow] |
| | | | |

Done when:

- [ ] Every step names a system or file, not just "the system".
- [ ] Every data element has a system of record and an owner, or an open question.
- [ ] Every interface has a format, schedule and monitoring owner, or an open question.
- [ ] At least three data-quality break points are named, with the control that should catch each.
- [ ] Each AS400 function in your flow is mapped to an e2open concept (Section 5.4).
- [ ] The Manager has reviewed it.

## 8. Questions to ask the Manager about the AS400 trade system

Batch these for 1:1s or the walkthrough; the Manager is the only trainer for the AS400. Record the answers in OneNote and in your tool docs.

1. Which libraries hold production trade data, and which hold test, history or archive copies?
2. Which files are the system of record for classification by country, country of origin and USMCA qualification? Is history kept, or are values overwritten?
3. Who may change classification or origin data, through which screens, and is there an approval step or a change log (journal)?
4. Which batch jobs build the broker files, when do they run, and who is alerted when one fails?
5. What exactly goes to each broker (fields, format, full or delta, delivery method), and what comes back?
6. Which Oracle interfaces feed the trade system (items, suppliers, POs), and which data goes back to Oracle?
7. Which AS400 data is copied to SQL Server or the data warehouse, how often, and which copy should we query?
8. Where are tariff rates maintained (AS400 table, custom tool, Excel), and who updates them when a new action takes effect?
9. Which custom tools read from or write to the AS400, and how (extracts, ODBC, manual upload)?
10. What are the known data-quality problems and workarounds, and which ones worry you most?
11. Which AS400 functions are planned to move to e2open, which will stay elsewhere, and which are undecided?
12. Who in IT supports the AS400 (programs, jobs, access), and how do we raise a request?
13. What documentation exists: file layouts, field descriptions, program lists, run books, past project documents?
14. Which reports come from the AS400 (spooled files, saved queries), who uses them, and what will replace them?
15. If the AS400 were unavailable for a day, what would stop, and what is the manual fallback?

## 9. Self-check questions

| No. | Question | Where to check |
|---|---|---|
| 1 | Name six GTM functions. For each, say where it happens today [COMPANY] and who uses the output. | 1.1 |
| 2 | Why is a classification keyed by item, country and effective date rather than by item alone? | 2.1, 2.3 |
| 3 | Describe how item, BOM, supplier, certificate and trade agreement qualification result relate to each other. | 2.2 |
| 4 | When an item's HTS code changes in the trade system, which downstream systems, files and reports change, and when? | 3.1 |
| 5 | A broker's returned entry file stops arriving. Who notices, how quickly, and what breaks downstream? | 3.1, 3.4 |
| 6 | Name three places where trade data quality breaks today and the control that should catch each. | 3.2 |
| 7 | In IBM i terms, what are a library, a physical file, a logical file and a member? Give the SQL Server equivalent of each. | 4.1 |
| 8 | Why might an SQL query on an AS400 file return only part of the data, or double it? | 4.1 |
| 9 | A date field holds 1261019. What date is it, and how do you confirm the convention for that field? | 4.8 and `docs/templates/bsa/04-data-mapping-spec.md` |
| 10 | List five rules for exploring a production AS400 trade system safely. | 4.7 |
| 11 | Why must Research still verify vendor trade content for a new tariff action, and which document governs until it is confirmed? | 1.9 |
| 12 | Which e2open applications are publicly described, which map to your process, and what must the project confirm? | 5.2, 5.3 |
| 13 | What is the difference between data mapping and data cleansing, and who decides how a dirty value is fixed? | 6.1 |
| 14 | What is a parallel run, and what tolerance would you propose for comparing landed cost between the old and new systems? | 6.1 |
| 15 | What are your two day-90 e2open deliverables, and which templates do you use for them? | 6.2 |
| 16 | Why does HS 2028 matter for the e2open data model? | 2.3, 6.4 |

## 10. Further reading

Repo documents:

- `docs/primers/customs-trade-compliance-primer.md`: the compliance meaning of every data element here (M1).
- `docs/primers/current-tariff-landscape.md`: current tariff actions and the primary sources Research monitors.
- `docs/templates/bsa/03-process-map-as-is-to-be.md`, `docs/templates/bsa/04-data-mapping-spec.md`, `docs/templates/bsa/05-uat-test-plan.md`: the project templates.
- `docs/templates/knowledge/tool-doc.md`: for documenting custom tools and AS400 functions as you learn them.
- `data/trackers/glossary.csv`: GTM, AS400, Db2 for i, data mapping, cutover, UAT and related terms.

External (vendor and IBM; vendor pages are marketing and change often):

| Topic | Source | Link |
|---|---|---|
| e2open GTM overview | e2open | https://www.e2open.com/global-trade/ |
| Trade content | e2open Global Knowledge | https://www.e2open.com/global-trade/global-knowledge/ |
| Trade agreements, drawback, duty programs | e2open Duty Management | https://www.e2open.com/global-trade/duty-management/ |
| Import compliance | e2open Import Management | https://www.e2open.com/global-trade/import-management/ |
| Export compliance | e2open Export Management | https://www.e2open.com/global-trade/export-management/ |
| Self-filing | e2open Customs Filing | https://www.e2open.com/global-trade/customs-filing/ |
| Screening | e2open Due Diligence Screening | https://www.e2open.com/global-trade/due-diligence-screening |
| Amber Road acquisition (2019) | Press release filed with the SEC | https://www.sec.gov/Archives/edgar/data/1314223/000119312519187992/d762026dex991.htm |
| IBM i documentation (Db2 for i, CL commands, catalog views) | IBM | https://www.ibm.com/docs/en/i |
| IBM i Access Client Solutions | IBM | https://www.ibm.com/support/pages/ibm-i-access-client-solutions |
