# Data Platform Primer

Last updated: 2026-10-17 · Owner: BSA Manager

- **Purpose:** the self-study backbone for M12 (the team's data platform). It teaches you to use the platform safely and to see how its pieces connect: the team database (SQL Server, in SSMS), Oracle EBS production (read-only, in DBeaver), the Power BI premium workspace and its gateway, Power Automate and Power Apps on our databases, and the remote server where scheduled jobs run. By day 60 you own a tool that depends on some of these pieces, so you must be able to trace its path end to end and troubleshoot it read-only when something breaks. Scope until day 90 is **use only**: you query and load data; you do not change the platform.
- **Who uses it:** Hire A and Hire B for self-study (about 5.5 hours in W1–W6, taken from the existing self-study budget) and three labs (Part 10). The Senior uses Parts 1 and 2 in the W1 data landscape tour and reviews the SSMS lab in the W4 SQL review. The Manager uses Parts 2, 3, 6, 7 and 8 in the W2 data platform walkthrough, owns the service-account decision (3.3) and keeps the filled platform map (`docs/templates/knowledge/data-platform-map.md`).
- **When:** Part 1 in W1, before your first SSMS or DBeaver session. Then follow the study plan below. Re-read Part 1 before each milestone review and whenever your access changes.

## How to use this primer

| Session | When | Parts | Focused time | Output |
|---|---|---|---|---|
| 1 | W1, before your first SSMS or DBeaver session. The Senior's data landscape tour (Thu 10/22, 13:45) covers the map and these rules | 1, then skim 2.1 | 0.75 h | "Part 1 read" and the date in your Access tracker page; questions in your question log |
| 2 | W2, before and after the Manager's data platform walkthrough (45 min, both hires; day and time in `docs/02-weeks-1-2-schedule.md`) | 2 and 3 | 1.0 h | Your one-page sketch of the data path (2.2), with every [COMPANY] gap listed as a question |
| 3 | W3, when your SQL Server access arrives (AR-07, needed by Mon 11/2) | 4 and 5; SSMS lab steps 1–4 (10.1) | 1.0 h | Lab steps 1–4 saved |
| 4 | W4, by the end of Wed 11/11 | SSMS lab steps 5–8 | 1.0 h | Lab posted for the Senior's SQL review (Thu 11/12, 13:00) |
| 5 | W5, after the day-30 review (Wed 11/18) | 6 and 7; Power Platform lab (10.2) | 0.75 h | Two trace notes; proposed rows for the platform map |
| 6 | W6 (Mon 11/23 to Wed 11/25) | 8 and 9; server lab (10.3); self-check (Part 11) | 1.0 h | Tour note; your owned tool's doc, Sections 2, 5 and 8, updated |

Evidence: following the safe-use rules (Part 1) and finishing the SSMS lab are a day-30 Must for both hires. At day 60, your owned tool's doc names its platform path: the database objects it uses, its connections, the account it runs as, its schedule and its server location (`docs/01-30-60-90-plan.md` Section 4; `docs/primers/sdlc-primer.md` 5.4).

Tailoring:

- **Hire A (Research):** your data is mostly trade data: HTS codes, origin, rates and entry lines, which reach the team database from the AS400 trade system and broker files [COMPANY: confirm]. You can script, so Parts 1 (rules 7 and 11), 8.4 and 8.5 matter most: a Python script never holds a password, and nothing you script writes to production or runs on a schedule until your checker has reviewed it. If your owned tool is a Python job on the server, do the server lab with special care.
- **Hire B (Standard Cost):** your data is cost data from Oracle EBS. If your DBeaver connection to EBS arrives before W3, read Part 5 before you use it, in W2 time. Use the team database's copy of EBS data first and go to EBS only for what the copy lacks (2.2). Cost and supplier price data is sensitive: rule 8 applies to every extract.

Conventions: [COMPANY: ...] marks a company fact the Manager or Senior confirms. KIT-100, PART-A and object names such as `rpt.v_item_trade` are fictional and marked "(example name)". Product facts (licensing, limits, names) carry "as of Oct 2026" and a link: check the link before you rely on one, and trust what you see in our tenant over this page. Terms are in the Glossary tab of the trackers workbook.

## 1. Safe-use rules

Read this page before you open SSMS or DBeaver for the first time. The rules apply from Day 1 and do not relax at day 60 or day 90 unless the Manager changes them in writing. They add to the access rules in `docs/04-access-request-checklist.md`; they never replace them.

### 1.1 The rules

1. **Your personal login for all interactive work.** SSMS, DBeaver, Power BI, Power Automate, Power Apps and Remote Desktop: you sign in as yourself, every time, so every action can be traced to you (3.2).
2. **Never the service account.** Never sign in with it, never ask for or accept its password, never type it into anything. It lives only in saved, unattended connections that the Manager or IT sets up (3.2, 3.3).
3. **Oracle EBS production is read-only.** Your DBeaver account on EBS can only read, and you write only SELECT queries: filtered by organization, row-limited, short. Heavy queries run only in [COMPANY: off-peak window for EBS queries] and only after the Manager agrees. You never run DML (INSERT, UPDATE, DELETE, MERGE: statements that change data) or DDL (CREATE, ALTER, DROP: statements that change structure). If DBeaver asks you to confirm a statement on EBS, the answer is No: it asks because the statement would change data (5.1).
4. **Loads go only into [COMPANY: sandbox or staging schema in the team database]:** only your own tables, named by the convention in 4.5, dropped when you are done. Nothing that a report, flow, app or tool relies on may ever read from a sandbox table.
5. **Use, don't change, the team database.** Outside the sandbox you never create, alter or drop tables, views, procedures or jobs. Those change through the Senior. If your owned tool needs a change to team-database objects, it goes through a change request with the Senior as checker (4.6).
6. **No production write before the day-60 review (Fri 12/18)** except what `docs/04-access-request-checklist.md` rule 2 allows: from W6, the test copy of your own tool. Your own sandbox tables (rule 4) are not production. No INSERT, UPDATE or DELETE outside the sandbox, and never "Edit Top 200 Rows" on a shared table (4.2).
7. **No credentials in scripts, flows or files.** No passwords, keys or connection strings with passwords in code, config files, Excel cells, OneNote, Jira, email, Teams, screenshots or Copilot prompts. If you find one, do not copy or use it; tell the Manager the same day (8.5).
8. **Export only what you need, and keep it in [COMPANY: approved location for data extracts].** Only the rows and columns the task needs. Never on personal devices, personal email or personal cloud drives (`docs/04-access-request-checklist.md` rule 7). Delete it when the task closes ([COMPANY: retention rule for extracts]).
9. **Hands off the server's setup.** On the remote server you never restart or shut it down, install or update software (Python packages included), or create, change, run or disable scheduled tasks or services. Sign out when you finish (8.2).
10. **Hands off production connections.** Never edit, re-sign, share or delete a gateway connection, a flow connection, a production flow or app, or a semantic model's settings. Never share a report or add people to a workspace.
11. **Unreviewed code never runs on production, and Copilot's code is a draft.** Read and explain every line of any script or query you did not write yourself, and test it in the sandbox or on the practice data first. A SELECT you understand may then run on the views your login can read. Anything that writes, sends output or runs on a schedule is reviewed by your checker and reaches production only through its owner (rule 6). Copilot-written code never goes straight from the chat to EBS or to production objects, and never into an EBS session (`docs/primers/copilot-chat-guide.md` 2.4).
12. **When unsure, stop and ask.** Ask before you run it. If something has already happened, do not try to fix it yourself: follow 1.3.

### 1.2 What "use only" means

| Area | You may (before the day-60 review) | You may not |
|---|---|---|
| Team database (SQL Server) | Read the views and tables your login can see; save your queries | Create, alter or drop objects; INSERT, UPDATE or DELETE; Edit Top 200 Rows |
| Sandbox [COMPANY] | Create, load, query and drop your own tables | Touch other people's tables; let anything in production depend on yours |
| Oracle EBS production (DBeaver) | Small, filtered SELECT queries; export your own result | Any DML or DDL; "show all rows" on large tables; long queries in business hours |
| Power BI | View reports (Viewer, AR-09); Contributor only in a personal or dev workspace | Publish to production workspaces; change refresh, credentials or gateway settings; share |
| Power Automate and Power Apps | Use apps; read run history with the owner; from W6, a test copy of your owned tool in [COMPANY: dev or sandbox environment] (AR-13) | Edit production flows or apps; change, re-sign or delete connections |
| Remote server | Sign in as yourself; read Task Scheduler, logs and folders on the tour | Restart, install, change tasks or services; leave sessions running |

From the day-60 review the Manager may grant production change rights for your owned tool only, through change control (`docs/04-access-request-checklist.md` rule 3). The rest of this table stays as it is until day 90. Team-database objects (tables, views, procedures, jobs) still change only through the Senior, even when your owned tool uses them (4.6).

### 1.3 If something goes wrong

- [ ] Stop. Run nothing else on that system and do not try to undo it. The only exception is a ROLLBACK of your own open transaction: in the sandbox (4.4), or a pending transaction DBeaver shows on EBS (5.1).
- [ ] Write down the time, the system, the exact text you ran, the message you saw, and take a screenshot.
- [ ] Tell the Senior (team database, Power BI) or the Manager (EBS, flows, apps, the server, anything else) within the hour, by Teams call or in person, not only in chat. Log a Jira bug if the Manager asks (`docs/primers/sdlc-primer.md` 8.3). Saying "I think I changed something" early turns a small problem into a quick fix; waiting turns it into an incident.

### 1.4 Checklist before your first session

- [ ] Part 1 read; date noted in your Access tracker page (`docs/04-access-request-checklist.md` rule 8).
- [ ] SSMS installed from [COMPANY: software portal or IT ticket] with your SQL Server access (AR-07). DBeaver and your personal EBS database account come through [COMPANY: access request for DBeaver and a read-only EBS database account]; AR-05 covers EBS screens (inquiry), not database access. The Senior has told you what your SQL Server login can do: read on [COMPANY: team database]; create, load and drop only in [COMPANY: sandbox or staging schema in the team database] ([COMPANY: DBA confirms the sandbox grant]).
- [ ] **The Manager has confirmed with [COMPANY: ERP security] that your DBeaver EBS account is read-only** at the database. That account is the real control; the DBeaver settings in 5.1 are a safety net.
- [ ] Your DBeaver EBS connection uses the Production connection type and the Read-only connection setting, checked on your screen by the Manager (5.1).
- [ ] You know who to call for each system (the "Who to call" table in the platform map).

**How this applies to our work:** Research and Standard Cost both depend on data other people trust, so a careless write or a runaway query hurts more than your own work. For your owned tool, these rules decide what you may do before day 60: run it supervised or on a test copy, never change production. On e2open, the same habits carry over to the project sandbox (AR-20).

## 2. The map: how the pieces connect

The platform is a chain. Data starts in Oracle EBS (and in the AS400 trade system and broker files), is copied into the team database, is shaped by views, is pulled into Power BI through the gateway, and is read and written by flows, apps and scheduled jobs. When a number looks wrong at the end of the chain, walk back along it one link at a time. The filled map with our real names lives in [COMPANY: location of the filled data platform map], kept by the Manager or the Senior from the template `docs/templates/knowledge/data-platform-map.md`. Real names are never copied into the training repository.

### 2.1 The components

| Component | What it is for | Who owns it | How you connect | What you may do |
|---|---|---|---|---|
| Oracle EBS production database | The ERP: items, item costs, purchase orders, receipts | [COMPANY: ERP team] | DBeaver, your personal read-only database account | Small, filtered SELECT queries (Part 5) |
| Team database (SQL Server) | The team's working copy of EBS, trade and broker data, with views for reports and tools | Objects: the Senior. Server and backups: [COMPANY: DBA or IT] | SSMS, Windows Authentication with your own login | Read; views first (Part 4) |
| Sandbox [COMPANY: sandbox or staging schema in the team database] | Your loads and scratch tables | The Senior | SSMS | Create, load, query and drop your own tables (4.5) |
| Data warehouse [COMPANY: name, if separate] | Curated history for analysis and reporting | [COMPANY: data owner] | SSMS | Read curated views (AR-08) |
| On-premises data gateway | The bridge that lets Power BI, Power Automate and Power Apps reach the on-premises SQL Server | Gateway admins [COMPANY: IT or Power Platform admin] | You don't; the services use it | Nothing; report failures (6.5) |
| Power BI premium workspace | Semantic models (data and measures) and the reports built on them | Workspace admin [COMPANY] | Browser; Power BI Desktop | View (AR-09); no publishing to production before day 60 |
| Power Automate flows and Power Apps | Automation and apps that read or write the team database | Each flow's or app's owner [COMPANY] | make.powerautomate.com, make.powerapps.com | Use apps; read run history with the owner; test copy from W6 (Part 7) |
| Remote server [COMPANY: server name] | Scheduled jobs (Python and other tools) and [COMPANY: other services, for example the gateway] | [COMPANY: IT server owner]; each job: its tool owner | Remote Desktop with your own account | Look and read logs on the tour (Part 8) |
| Password vault [COMPANY: password vault] | Holds the service account's password | The Manager (or IT) | You don't | Nothing |

### 2.2 The data path, step by step

1. **Oracle EBS records the business:** items, item costs, POs and receipts are created there by Purchasing, Receiving and Finance. EBS is always the most current, and the most expensive place to query.
2. **Data reaches the team database** by [COMPANY: how EBS data gets to the team database: scheduled extract job, ETL (extract, transform, load) tool, linked server, file drop or the warehouse feed], on [COMPANY: schedule], running as [COMPANY: account]. AS400 trade data and broker entry files arrive the same way [COMPANY: how and when]. The team database is a copy: it is as fresh as its last successful load.
3. **Views in the team database shape the data** for reports and tools: they join, filter and rename so that every report uses the same logic [COMPANY: which schemas hold reporting views]. A change to a view changes every report and tool that reads it, which is why views change only through the Senior.
4. **The Power BI semantic model refreshes from those views through the gateway** on a schedule. The gateway connection holds one stored credential, the service account under the recommended model, and every refresh runs as that account (6.5).
5. **Reports show the semantic model's data as of its last successful refresh.** A report can look normal while showing data that is days old (6.4).
6. **Flows and apps use connections:** each connection stores a credential and, for the on-premises SQL Server, goes through the gateway. A flow acts as whoever's credentials sit in its connections (7.1).
7. **Scheduled jobs on the remote server** run Python scripts and other tools against the team database and file shares, as the account the task is set to run as (8.3).
8. **Outputs leave the platform:** files to brokers, inputs to Finance and the Oracle cost update [COMPANY]. These always pass through a tool owner and maker-checker; Standard Cost inputs also need Finance sign-off before any Oracle load (`docs/01-30-60-90-plan.md` Section 1).

Three things follow from the path:

- **Every hop is a copy with a schedule.** Always ask "as of when?". A report is no newer than its last refresh, the refresh is no newer than the last load into the team database, and that load is older than EBS.
- **Every connection runs as an account.** Whoever's credentials sit in a gateway connection, a flow connection, an app connection or a scheduled task is who the data source sees. That is why the account model matters (Part 3).
- **Every hop has an owner.** When a link breaks, the owner of that link fixes it. Your job is to find which link broke and tell the right person (Part 9).

**How this applies to our work:** Research follows the path from the AS400 and broker files to the views behind trade reports. Standard Cost follows it from EBS cost and receipt data to the PPV (purchase price variance) and landed-cost views and models. For your owned tool, the day-60 platform path is this chain drawn for one tool. On e2open, the filled map is the start of the interface inventory: which feeds the new system replaces, and which new feeds the team database will need [COMPANY: confirm with the e2open project].

## 3. Accounts: personal and service

### 3.1 Two kinds of account

- **Your personal account** is you: your Windows and Microsoft Entra ID (work) account, plus your personal read-only EBS database account. You use it for everything you do yourself.
- **A service account** is not a person. It is used by a service, a job or a saved connection. The team has one with the same access as the team [COMPANY: its label in the platform map's Accounts table]. Because it can do whatever the team can do, anyone who uses it can do all of that without leaving their own name behind.

### 3.2 The recommended model, and why attribution matters

- The service account is used **only by saved, unattended connections:** Power BI gateway data-source credentials, Power Automate connections, and scheduled jobs on the server.
- **Nobody signs in with it interactively.** Hires never see its password, which lives in [COMPANY: password vault], held by the Manager (or IT).
- **All interactive work uses your personal account,** so every query, load, export and change is attributable to a person. This matches `docs/04-access-request-checklist.md` rule 6 ("Never share logins").

Why it matters: maker-checker only works if the record shows who made what. When someone leaves, their personal account is disabled and that is the end of their access; a shared password stays known until it is changed. Microsoft says the same about flows: "Shared credentials are a security risk and make it difficult to track who changed a flow. If you do use a service account, grant it only the permissions the task requires and limit who has access to it" (as of Oct 2026; check https://learn.microsoft.com/en-us/power-automate/service-principal-support). For SQL Server it recommends Windows (Active Directory) authentication over SQL Server logins wherever possible (check https://learn.microsoft.com/en-us/sql/relational-databases/security/sql-server-security-best-practices).

### 3.3 Manager decision

> **Manager decision (open): [COMPANY: confirm the service-account model before access requests go out].**
>
> Recommended: the service account is used only inside saved, unattended connections (gateway data-source credentials, Power Automate connections, scheduled tasks on the server). Nobody signs in with it. Its password is in [COMPANY: password vault], held by the Manager (or IT). Hires use their personal accounts for all interactive work.
>
> Also decide: (1) who rotates the password, how often, and who updates every connection that uses it the same day; (2) whether each connection really needs the whole team's access, or a narrower grant (Microsoft's least-privilege advice); (3) for business-critical flows, whether to use a Microsoft Entra service principal, which Microsoft prefers to a shared service account for unattended flows and which "isn't tied to a user that could leave"; (4) whether any scheduled task should run as a group Managed Service Account, whose password Windows rotates itself; (5) licensing if the service account would own flows rather than only hold their connections: Microsoft treats one Premium license on a shared service account as multiplexing, while flows that use a service account only as a connection are not affected (as of Oct 2026; check https://learn.microsoft.com/en-us/power-platform/admin/power-automate-licensing/faqs).

### 3.4 Which account, where

| Activity | Account | Why |
|---|---|---|
| Querying the team database in SSMS; loading into the sandbox | Your personal login | Attributable; your grant is your limit |
| Querying EBS in DBeaver | Your personal read-only EBS account | The read-only grant is the real control (5.1) |
| Power BI, Power Automate, Power Apps and Remote Desktop, when you use them | Your personal account | Roles and licenses are per person; attributable |
| Saved, unattended connections: gateway refresh credentials, flow connections, scheduled tasks on the server | The service account under the recommended model (or a service principal or gMSA, if the Manager decides so in 3.3) | Runs when nobody is signed in; must not stop when a person leaves |

### 3.5 If anyone offers you a shared login

People mean well: "just use mine to look", "here's the service account password, it's quicker". Say no, every time:

> "Thanks, but I can't use another person's login or the service account. Could you share your screen instead?"

Then tell the Manager the same day. If you saw or heard a password, say so, so it can be changed; never write it down. Until your own access arrives, the account holder shares their screen (`docs/04-access-request-checklist.md` rule 6).

**How this applies to our work:** every tool you document records the account each connection and job runs as (tool doc Sections 2, 5 and 8). Hire B: a cost tool that runs as a person's account stops when that person leaves. Hire A: a Python job that reads a password from a file breaks rule 7; flag it in the tool doc's open questions. On e2open, interfaces will need their own non-person identities; the map shows which of ours they replace.

## 4. The team database in SSMS

### 4.1 Connecting

- **Install:** SSMS 22 is the current line (as of Oct 2026; check https://learn.microsoft.com/en-us/ssms/install/install). Install it only from [COMPANY: software portal or IT ticket for SSMS].
- **Connect:** server type Database Engine; server name [COMPANY: team database server]; authentication **Windows Authentication**, which Microsoft calls "much more secure than SQL Server Authentication" (check https://learn.microsoft.com/en-us/sql/relational-databases/security/choose-an-authentication-mode). Never SQL Server Authentication with a shared login.
- **Check where you are** in every new query window before you run anything:

```sql
SELECT SUSER_SNAME() AS my_login, DB_NAME() AS my_database;
```

If `my_login` is not you, or `my_database` is not the database you meant, stop and fix the connection or the database drop-down first.

### 4.2 Object Explorer and schemas

- **Object Explorer** is the tree on the left. Under Databases > [COMPANY: team database] you find Tables, Views, Programmability (stored procedures, functions) and Security. You may not see SQL Server Agent jobs; the Senior can show them ([COMPANY: who monitors team database jobs]).
- **Schemas** group objects: always use two-part names, `schema.object`. Ours are [COMPANY: schemas in the team database and what each holds], for example `stg` for raw loads, `rpt` for reporting views and `sbx` for the sandbox (example names).
- **Right-click menus:** Select Top 1000 Rows is a quick look, not a query to save. **Edit Top 200 Rows opens an editable grid: changing or deleting a row there changes the table.** Treat it as a write tool and never use it outside your own sandbox tables (rule 6).

### 4.3 Finding things: views first

Start from views, not tables. A reporting view already holds the agreed joins and filters, and it is what the reports use, so your numbers will match theirs. Read a table directly only when the Senior tells you no view fits.

```sql
-- Which views have a column that looks like an HTS code?
SELECT c.TABLE_SCHEMA, c.TABLE_NAME, c.COLUMN_NAME, c.DATA_TYPE
FROM INFORMATION_SCHEMA.COLUMNS AS c
JOIN INFORMATION_SCHEMA.TABLES AS t
  ON t.TABLE_SCHEMA = c.TABLE_SCHEMA AND t.TABLE_NAME = c.TABLE_NAME
WHERE t.TABLE_TYPE = 'VIEW' AND c.COLUMN_NAME LIKE '%hts%'
ORDER BY c.TABLE_SCHEMA, c.TABLE_NAME;
-- A view's definition: read it, never run it as a CREATE
SELECT OBJECT_DEFINITION(OBJECT_ID(N'rpt.v_item_trade'));  -- (example name)
```

INFORMATION_SCHEMA.COLUMNS returns "one row for each column that can be accessed by the current user" (check https://learn.microsoft.com/en-us/sql/relational-databases/system-information-schema-views/columns-transact-sql), so it also shows you what your login can see. For each view you use, write down its grain (what one row is) and its owner.

### 4.4 Query habits

- **Header comment** on every saved query: purpose, source objects, author, date, row-count checks (the format in `docs/analytics/practice-exercises.md`, "SQL habits for this pack").
- **Explicit columns, never `SELECT *`.** Microsoft's own code-analysis rule says the columns returned "might change if the underlying table or view changes" (check https://learn.microsoft.com/en-us/sql/tools/sql-database-projects/concepts/sql-code-analysis/t-sql-design-issues).
- **`WHERE` first, and `TOP` always with `ORDER BY`.** Filter by date, status or item set before you look at results. For TOP, ORDER BY "is the only way to predictably indicate which rows are affected" (check https://learn.microsoft.com/en-us/sql/t-sql/queries/top-transact-sql).
- **No `WITH (NOLOCK)`.** It allows dirty reads: "data that was never committed", or "records twice (or not at all)" (check https://learn.microsoft.com/en-us/sql/t-sql/queries/hints-transact-sql-table).
- **Save every script** to [COMPANY: script location for team queries], named so others can find it (for example `M12-lab-HireA-step4.sql`, example name). A query that matters is never only in an unsaved tab.
- **Writes happen only in the sandbox,** in a short transaction that you check before you commit. An open transaction holds locks that can block other people, so never leave one open.

```sql
-- Purpose: active items in HTS chapter 85, by origin (SSMS lab step 4)
-- Source:  rpt.v_item_trade (example name)    Author: Hire A    Date: 2026-11-03
-- Checks:  rows returned = ____ ; active items in the view = ____
SELECT TOP (100) item_no, hts10_us, origin_country, item_status
FROM rpt.v_item_trade                          -- (example name)
WHERE item_status = 'Active' AND LEFT(hts10_us, 2) = '85'
ORDER BY item_no;

-- Sandbox only: the safe-write pattern
SET XACT_ABORT ON;   -- any error rolls back the whole transaction
BEGIN TRAN;
UPDATE sbx.hirea_suppliers_20261104            -- (example name: your own table)
SET supplier_type = 'Distributor' WHERE supplier_id = 'SUP-105';
SELECT @@ROWCOUNT AS rows_changed;             -- expect exactly 1
ROLLBACK;            -- change to COMMIT only after the count is right
```

### 4.5 Loading data into the sandbox

Use the **Import Flat File** wizard for a CSV or text file: right-click the database > Tasks > Import Flat File. It copies the file "to a new table"; the table name must be unique, so it creates tables and does not append (check https://learn.microsoft.com/en-us/sql/relational-databases/import-export/import-flat-file-wizard).

1. **Name the table** by [COMPANY: sandbox naming convention], for example `sbx.hirea_suppliers_20261104` (example name: sandbox schema, your hire letter or initials, content, load date). Put it in the sandbox schema, never in `dbo` or any shared schema. If the wizard does not offer the sandbox schema, stop and ask the Senior.
2. **Preview** shows the first 50 rows. Check headers, delimiters and leading zeros.
3. **Modify Columns:** set codes (item numbers, HTS, supplier and country codes) to text (`nvarchar`), dates to `date`, money and rates to `decimal`, and allow nulls. The wizard guesses types from the first 200 rows, so a later odd value can fail the import; widen the column and run it again.
4. **Check after loading:** the row count equals the file's rows; blanks became NULL; codes kept their leading zeros. The wizard reads the file using the computer's active code page, so check accented names (for example Mexican supplier names) as well.
5. **Clean up** when the task closes: `DROP TABLE IF EXISTS sbx.hirea_suppliers_20261104;` (example name). Drop only your own tables. [COMPANY: sandbox clean-up rule, for example tables older than 30 days are removed].

### 4.6 Asking for a schema change

A new or changed table, view, procedure or job in the team database is a schema change, and it goes through the Senior. You may need one when your owned tool or a report needs a new column or a corrected view.

- [ ] Write the need as a Jira story with the business reason, agree it with the Senior, then open a change request (`docs/templates/bsa/06-change-request.md`; Technology: "configuration (team database object)"). Before: the current definition, saved with `OBJECT_DEFINITION` (4.3); it is also your rollback script. After: the new definition.
- [ ] Impact: every report, semantic model, flow, app and tool that reads the object, from the platform map and the tool docs. A renamed column breaks every one of them (6.6).
- [ ] Test in the sandbox: build your version there under your own name (for example `sbx.hirea_v_item_trade_test`, example name) and compare old and new results on the same data.
- [ ] Checker: the Senior. Approver: the Manager. The Senior makes the production change (`docs/primers/sdlc-primer.md` 4.2); through day 90 you never do, even for your owned tool (rule 5). Afterwards, check the next refresh and run of everything on the impact list.

### 4.7 Backups and restores

Backups and restores are [COMPANY: DBA or IT backup owner]'s job, never yours. Two facts help you ask the right question. A database in the full recovery model can be restored "to a specific point in time", provided its log backups are complete; the simple recovery model can only go back to the end of a backup (check https://learn.microsoft.com/en-us/sql/relational-databases/backup-restore/recovery-models-sql-server). The team database uses [COMPANY: recovery model and backup schedule]; whether the sandbox is backed up at all is [COMPANY: confirm]. If data is lost or wrong, tell the Senior the object name and the last time it was known to be right; the Senior raises the restore request.

**How this applies to our work:** Research: your small real analysis (A30-5) and your HTS list comparisons run as saved, read-only queries on views. Standard Cost: your landed-cost and PPV work (B30-5, B30-9) starts from the cost views; when a view does not have what you need, that is a schema change request, not a sandbox copy that a report quietly starts using. Owned tool: list every object it reads or writes in its tool doc (Section 5). e2open: the views you document are a map of today's business rules, and data mapping will need them.

## 5. Oracle EBS production in DBeaver (read-only)

### 5.1 Connection settings

| Setting | Use | Why |
|---|---|---|
| Account | Your personal EBS database account, confirmed read-only by [COMPANY: ERP security] (1.4) | This is the control that protects EBS |
| Connection type (General page) | **Production** | DBeaver then turns auto-commit off, asks before running INSERT, UPDATE or DELETE, colours the connection brick red, rolls back idle transactions after 10 minutes and disconnects after 1 hour idle (defaults; as of Oct 2026, check https://github.com/dbeaver/dbeaver/wiki/Connection-Types) |
| Read-only connection (Security section) | **On, and never switched off** | DBeaver refuses data-changing statements on this connection. It is a client-side setting anyone can toggle, which is why the read-only account matters more (check https://github.com/dbeaver/dbeaver/wiki/Managing-security-restrictions-for-database-connection) |
| Commit mode | Leave it as the Production type sets it (manual commit) | With a read-only account you have nothing to commit. If the toolbar ever shows a pending transaction on EBS, choose Rollback and tell the Manager |
| Role | Normal | SYSDBA and SYSOPER are administrative roles |
| Save password | Off, unless [COMPANY: password policy for client tools] allows it | DBeaver stores a saved password in its local configuration (check https://github.com/dbeaver/dbeaver/wiki/Connecting-to-Oracle-databases) |
| Connection name | [COMPANY: naming], including "EBS PROD READ-ONLY" | You see at a glance where you are |

How to tell you are read-only: in the data editor, editing buttons are disabled and a read-only icon marks the table (check https://github.com/dbeaver/dbeaver/wiki/Data-Editor).

### 5.2 Query habits on EBS

- **Ask first whether the team database already has the data** (2.2). EBS is the last resort, not the first stop.
- **Limit rows:** end every exploratory query with a row limit. The examples here use `FETCH FIRST n ROWS ONLY` (Oracle's row-limiting clause), which older Oracle versions do not support: [COMPANY: confirm the EBS database version and the row-limit syntax with the ERP or DBA team] in your first EBS session, before you rely on it. Use `ORDER BY` with it when you need predictable rows.
- **Filter by organization** every time, and by date or item set ([COMPANY: our operating units and inventory organizations, and their codes]; 5.3).
- **No `SELECT *` on large tables.** List only the columns you need: less work for the production database, and a saved query that does not break when columns change.
- **The grid is not the result.** DBeaver fetches 200 rows at a time by default and loads more as you scroll; "select and show all rows" removes that limit and is exactly the costly pattern to avoid (check https://github.com/dbeaver/dbeaver/wiki/Data-Editor-preferences).
- **Heavy queries off-peak** in [COMPANY: off-peak window for EBS queries], with the Manager's agreement, or ask [COMPANY: ERP team] for a report instead. A long query on a busy database can also fail with "ORA-01555: Snapshot too old" (as described by Microsoft for Oracle sources; check https://learn.microsoft.com/en-us/sql/relational-databases/replication/non-sql/troubleshooting-oracle-publishers).
- **Cancel a runaway query** from the Background Tasks view with Cancel Operation (check https://github.com/dbeaver/dbeaver/wiki/Background-Tasks), then tell the Manager what you ran.
- **Disconnect when done** (Disconnect on the toolbar) and never set a keep-alive to hold an EBS session open. Never paste Copilot-written SQL into an EBS session (rule 11).

```sql
-- Purpose: current standard cost for two items in one organization (Hire B)
-- Source:  [COMPANY: approved EBS item cost view]    Author: Hire B    Date: 2026-11-05
SELECT item_number, organization_code, cost_type, item_cost
FROM item_cost_v                               -- (example name; get the real one from the ERP team)
WHERE organization_code = 'ORG1'               -- (example value)
  AND item_number IN ('KIT-100', 'PART-A')
ORDER BY item_number
FETCH FIRST 50 ROWS ONLY;
```

### 5.3 EBS data basics: confirm before you query

The right table or view depends on how our company set EBS up. None of the names or structures below has been checked against Oracle documentation for this primer, so **use no EBS table or view name until [COMPANY: ERP team] gives it to you.** Ask these questions in your first EBS session with the Manager and record the answers in the platform map.

| Data area | What you need it for | Table or view to use | One row is | Always filter by |
|---|---|---|---|---|
| Items | Item number, description, unit of measure, status | [COMPANY: confirm EBS table or view name with the ERP team] | [COMPANY: for example one item per inventory organization] | [COMPANY: organization] |
| Item costs | Standard cost and its cost elements (where duty, freight and fees sit) | [COMPANY: confirm EBS table or view name with the ERP team] | [COMPANY] | [COMPANY: organization and the cost type that holds the standard in use] |
| Purchase orders | PO price, currency, supplier, terms | [COMPANY: confirm EBS table or view name with the ERP team] | [COMPANY: header or line] | [COMPANY: operating unit] |
| Receipts | Receipt quantity and date; the link to PO lines | [COMPANY: confirm EBS table or view name with the ERP team] | [COMPANY] | [COMPANY: organization and date] |

Terms you will hear, which the ERP team should explain for our setup: "the APPS schema", "multi-org", "operating unit" versus "inventory organization", "cost type", and "flexfields" (company-defined fields whose meaning is not in the column name) [COMPANY: flexfield map for the fields we use].

### 5.4 Exporting results safely

- Export **from your filtered query result** (right-click the grid > Export data), not by right-clicking a table in the connection tree: exporting from the tree "always" reads the data directly from the database, which on EBS means the whole table. From a result grid you can choose **Use fetched rows** or **Selected rows only** (check https://github.com/dbeaver/dbeaver/wiki/Data-export). Use fetched rows exports only the rows already loaded in the grid (200 by default, 5.2), so compare the file's row count with what you expected; Query the database re-runs your filtered query instead.
- Choose only the columns you need. CSV for data, XLSX only when someone will read it in Excel; keep codes as text.
- Save to [COMPANY: approved location for data extracts], name the file with the date and the query's purpose, and delete it when the task closes (rule 8).

**How this applies to our work:** Hire B uses EBS for item cost and cost-element data (B30-9) and PO and receipt data for PPV (B60-3); a filtered query on the approved view, saved with a header, is the evidence. Hire A rarely needs EBS directly: item and PO data for an investigation should come from the team database first. Owned tools: if a tool reads EBS, record the account it uses and when it runs. e2open: the EBS item and PO data elements you confirm here go straight into your data map (`docs/templates/bsa/04-data-mapping-spec.md`).

## 6. Power BI: the premium workspace and the gateway

### 6.1 What "premium" means for you

Microsoft is retiring Power BI Premium per-capacity (P) SKUs (a SKU is a product size Microsoft sells, such as P1): new customers could not buy them after 1 July 2024, and Microsoft directs customers to Microsoft Fabric capacity (F SKUs; F64 is the P1 equivalent). Premium Per User (PPU) is a per-user license, not a capacity, and is not being retired. So "our premium workspace" is most likely a workspace on a Fabric F capacity or a PPU workspace (as of Oct 2026; check https://learn.microsoft.com/en-us/fabric/enterprise/licenses). [COMPANY: confirm the workspace type (Fabric F SKU, PPU, or P on an Enterprise Agreement) and the capacity size]. What changes for you:

- **Refreshes:** up to 48 scheduled refreshes a day in Premium, PPU or Fabric capacity, against 8 in shared (Pro) capacity.
- **Viewing:** on F64 or larger (or P), people with a free license and the Viewer role can view content; on smaller F SKUs every viewer needs Pro or PPU, and a PPU workspace is open only to PPU users. Your own license is [COMPANY: confirm] (AR-09).
- **Deployment pipelines** work in PPU, Premium and Fabric workspaces, not in Pro workspaces (`docs/primers/sdlc-primer.md` 4.4).

### 6.2 Workspace roles

| Role | What it can do | You, before day 60 |
|---|---|---|
| Admin | Everything, including deleting the workspace and adding or removing other admins | Never |
| Member | Add people with the same or lower roles; publish the workspace app; everything a Contributor can do | Never |
| Contributor | Create, edit and delete content; schedule refreshes through the gateway (with separate gateway permissions) | Only in a personal or dev workspace (AR-09) |
| Viewer | View and interact with content | Your role on production workspaces |

A person gets the highest role from all their groups (check https://learn.microsoft.com/en-us/fabric/fundamentals/roles-workspaces). A Viewer without build permission cannot access the semantic model itself.

**Sharing rules:** before day 60 you share nothing: no sharing reports, no adding people, no publishing the app, no "publish to web". Send people the existing report or app link. Do not export report data to send around; if someone needs data, ask the report owner. [COMPANY: sharing policy, sensitivity labels and external sharing rules for Power BI].

### 6.3 Semantic model and report

The **semantic model** (formerly "dataset") holds the data, the relationships and the measures; it is what refreshes. A **report** is the pages and visuals on top of it. Many reports can share one model, so a change to the model, or to the view it reads, reaches every report on it. When a number is wrong, first decide which one you are looking at: wrong data or logic in the model, or a wrong filter on the report page.

### 6.4 Scheduled refresh and refresh history

- The schedule is set on the semantic model by its owner [COMPANY: who owns each model]. The report shows data as of the last **successful** refresh.
- **Refresh history** on the semantic model lists scheduled and on-demand refreshes with start and end times and the error text. Read the error text: it usually names the cause.
- Power BI turns a schedule off after repeated failures (Microsoft says four in a row) or when credentials are invalid, and pauses it when nobody has opened a report on the model for two months; long refreshes also time out (Microsoft lists 2 hours in shared capacity and 5 hours in Premium) (as of Oct 2026; check https://learn.microsoft.com/en-us/power-bi/connect-data/refresh-scheduled-refresh and https://learn.microsoft.com/en-us/power-bi/connect-data/refresh-data). [COMPANY: who receives refresh-failure emails].

### 6.5 The gateway and its connections

- The **on-premises data gateway** (standard mode) lets Power BI, Power Automate and Power Apps reach on-premises sources such as the team database; the **personal mode** gateway serves one user and Power BI only (check https://learn.microsoft.com/en-us/power-automate/gateway-reference). Team solutions should use the standard gateway [COMPANY: where ours runs, and who its admins are].
- A **gateway connection** stores one set of credentials, and every refresh through it uses them, not the viewer's (unless single sign-on is set up). Under the recommended model that is the service account (3.3).
- **Gateway admins** manage the gateway and its connections (check https://learn.microsoft.com/en-us/power-platform/admin/onpremises-data-gateway-management); **connection users** can use a connection but cannot see or change its credentials (as of Oct 2026; check https://learn.microsoft.com/en-us/power-bi/connect-data/service-gateway-data-sources). Microsoft recommends more than one gateway admin. Hires hold no gateway role before day 60 [COMPANY: confirm].
- Removing a data source breaks "any items that depend on it" (check https://learn.microsoft.com/en-us/fabric/data-factory/data-source-management).

### 6.6 Common refresh failures and who fixes each

| Failure | What you usually see | First check (read-only) | Who fixes it |
|---|---|---|---|
| Expired or changed credentials (for example the service account password was rotated) | Credential error in refresh history; the schedule may be off | Did other models on the same connection fail at the same time? | Gateway connection owner [COMPANY: Manager or IT] |
| Gateway offline | Every refresh, flow and app using the gateway fails at once | The time of the first failure; whether the server was restarted (Part 8) | Gateway admin [COMPANY: IT] |
| Source changed (view, column, server or database renamed or removed) | An error naming a column, table or object | Query the view in SSMS: does the named column still exist? | The Senior (object) with the model owner |
| Timeout or very long refresh | Refresh runs long, then fails | Duration trend in refresh history | Model owner, with the Senior for slow views |
| Schedule off or paused | No new entries in refresh history | When the last entry was | Model owner |

**How this applies to our work:** Research and Standard Cost both read Power BI reports built on team-database views. Before you quote a number from a report, check the model's last refresh time. Owned tool: if it feeds a report, the refresh is part of its platform path. Reporting backlog items from W10 (M8) start here. e2open: reports fed by AS400 data will need new sources after cutover [COMPANY].

## 7. Power Automate and Power Apps on our databases

### 7.1 Connections and who owns them

- A **connection** is a stored credential for a connector. A flow acts with the credentials of the connections inside it, and owners of a flow "can't modify the credentials for a connection that another owner created" (check https://learn.microsoft.com/en-us/power-automate/create-team-flows).
- **SQL Server is a premium connector,** and reaching our on-premises SQL Server needs the gateway, which is also a premium feature. A scheduled or automated flow uses its owner's license; an app's users each need a premium entitlement (as of Oct 2026; check https://learn.microsoft.com/en-us/power-platform/admin/power-automate-licensing/faqs). [COMPANY: confirm which Power Automate and Power Apps licenses we hold].
- Each connection's owner and account go in the platform map's Connections table.

### 7.2 Run history

Each flow keeps a run history: every run and its status; open a run to see which action failed and its error. It is kept for about 28 to 30 days (as of Oct 2026; check https://learn.microsoft.com/en-us/power-automate/limits-and-config), so save screenshots or exports of anything you need as evidence. A 401 error usually means the connection's token expired or its password changed (check https://learn.microsoft.com/en-us/power-automate/fix-connection-failures). A flow that fails continuously for 14 days is turned off (same limits page).

### 7.3 Environments and solutions

- The **default environment** is shared by everyone in the tenant and is meant for personal productivity, not production. Our environments are [COMPANY: our environment names and which one is production] (check https://learn.microsoft.com/en-us/power-platform/admin/environments-overview).
- **Solutions** package apps and flows to move between environments: unmanaged in development, managed in test and production. **Connection references** let a solution use a different connection in each environment (check https://learn.microsoft.com/en-us/power-apps/maker/data-platform/create-connection-reference). More in `docs/primers/sdlc-primer.md` 4.3.

### 7.4 What breaks when an owner leaves

- If a flow uses connections that belong to someone who left, those steps fail until someone updates the credentials, and a flow whose original owner leaves "reverts to the Low performance profile".
- Only solution-aware flows can change owner in place; other flows must be copied. If the new owner lacks a premium license for a premium flow, it runs for 30 days and is then turned off (as of Oct 2026; check https://learn.microsoft.com/en-us/power-automate/change-cloud-flow-owner).
- Prevention: co-owners, connections under the agreed account model (3.3), flows in solutions, and the owner and connections recorded in the tool doc and the map. When anyone leaves the team, the Manager runs the map's leaver check.

### 7.5 Power Apps on SQL Server

- **Delegation:** when a formula cannot be delegated to SQL Server, Power Apps "gets the first 500 records" (up to 2,000 if the Data row limit is raised) and works only on those. Results can be silently incomplete; Power Apps marks such formulas with a delegation warning (blue underline) (as of Oct 2026; check https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/delegation-overview). An app that "loses" records on a large table is often this.
- **Identity:** with Microsoft Entra integrated authentication each user acts as themselves. With SQL Server Authentication, or with Windows Authentication on a shared connection, every user acts as the account the maker connected with, so the app's real permissions are that account's permissions (check https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/connections/sql-server-security). Record which one each app uses.
- **Sharing an app does not share its data:** the data sources, flows and gateway connections need their own permissions (check https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/share-app).

### 7.6 What you may change

Before the day-60 review: nothing in production. From W6, for your owned tool only: Environment Maker in [COMPANY: dev or sandbox environment] and co-owner of its test copy (AR-13). Switch off any schedule on the test copy so it cannot run twice. Changes go through a change request with the Manager as checker (`docs/templates/bsa/06-change-request.md`, Power Apps and Power Automate checklists). Never "fix" a broken production flow by signing its connection in with your own account: the flow would then run as you, lose attribution to the agreed account, and break again when your password changes.

**How this applies to our work:** several custom tools are apps or flows; the Tool Inventory says which. Hire A: a flow that collects tariff notices or sends a broker file must name its connections and account. Hire B: a cost app on a large table can hit delegation limits; check counts against SSMS. e2open: flows that move trade data today are interface candidates for the project's interface list.

## 8. The remote server

### 8.1 What runs there

[COMPANY: what runs on the team server: scheduled Python jobs, other tools, file drops, and whether the on-premises data gateway is installed there]. The platform map's Scheduled jobs table lists each job, its schedule, the account it runs as and who is told when it fails. Because several things share this server, one careless action affects all of them: a restart stops every job and every session, and stops any service on it, such as a gateway, which then makes refreshes and flows fail.

### 8.2 Remote Desktop etiquette

- Sign in with your **personal account**, never the service account.
- **Sign out when you finish.** Signing out ends your programs and deletes your session. **Disconnecting** (closing the window) leaves everything you started running "with no loss of data", held in memory (check https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/tsdiscon and https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/logoff). A forgotten session uses memory and can keep files open. [COMPANY: the server's disconnected-session time limit].
- Disconnect only if the Manager or the tool owner asks you to keep something running; anything that must run on its own belongs in a scheduled task. Close any tool file you opened (workbook, Access file) first: a file left open in your session can block a scheduled run that needs it.
- Never restart, shut down, install, or change tasks, services or settings (rule 9). Save nothing on the server's desktop.

### 8.3 Reading Task Scheduler and its logs

- Open Task Scheduler and go to [COMPANY: the folder in the Task Scheduler Library that holds the team's tasks]. For each task read **Status** (Ready means it can run; a task stuck in Running usually means its program did not exit), **Triggers**, **Next Run Time**, **Last Run Time** and **Last Run Result**. Compare the result with one from a run you know was good.
- The **History** tab shows each run's events. The full log is in Event Viewer > Applications and Services Logs > Microsoft > Windows > TaskScheduler > Operational (check https://learn.microsoft.com/en-us/troubleshoot/windows-server/system-management-components/troubleshoot-scheduled-tasks-not-running). If History is empty, ask whether task history is turned on [COMPANY].
- A task that runs while nobody is signed in uses a stored credential or a service identity, so its scripts never need a password in them. The task's properties show which account it runs as: write that down, never the password.
- Read only. You do not run, end, enable, disable or edit a task; in the server lab the Manager or the tool owner does anything that changes state. Your tool's own log files are in [COMPANY: log folder for each job]. Read them; never edit or delete them.

### 8.4 The Python environment

The server's scheduled Python jobs run with [COMPANY: Python version, the virtual environment's location, and how tasks call it]. A task's action names the program it starts (for example a `python.exe` inside a virtual environment) and the script with its arguments; record both in the tool doc (Sections 2 and 8). Never install or upgrade packages there: one upgrade can break every job that shares the environment. The source code lives in [COMPANY: code repository] (AR-15), not only on the server; if the server copy is the only copy, flag it to the Manager.

### 8.5 Where credentials live

Credentials live only in places built to hold them: gateway connections (encrypted before they are stored), Power Automate and Power Apps connections, Task Scheduler's stored credential for a task, Windows Credential Manager on the server [COMPANY: confirm whether jobs use it], and [COMPANY: password vault]. They never live in a script, a config file in the repository, a flow's text, a workbook, OneNote, Jira, email, chat or Copilot. Microsoft warns that applications that store a SQL password on the client are "additional attack points" (check https://learn.microsoft.com/en-us/sql/relational-databases/security/choose-an-authentication-mode). If you find a password in a file: do not copy it, do not use it, do not paste it into your notes; tell the Manager the same day so it can be changed and moved.

**How this applies to our work:** if your owned tool runs on the server, its schedule, account, program and log location are the core of its tool doc (Sections 2, 5, 7 and 8) and of its day-60 platform path. Hire A: if you script, this is where your scripts would one day run, so learn its rules now. Hire B: if the standard cost tool runs here, a failed overnight job shows up later as missing inputs. e2open: jobs that feed brokers or Oracle today are candidates for replacement; record them in the tool's e2open disposition.

## 9. When something breaks: triage

You own a tool, so you are often the first to notice. Your job in the first hour is to find which link broke, using only read-only checks, and get the right owner on it with good notes. You do not fix production (rule 6; `docs/primers/sdlc-primer.md` 8.3).

| Symptom | First checks you can do (read-only) | Who fixes it | What to write down |
|---|---|---|---|
| A report shows old or missing data | The semantic model's refresh history: last success and error text (6.4, 6.6) | Model owner; credentials: gateway connection owner; gateway: gateway admin | Model, last good refresh, error text, time noticed |
| A flow failed or did not run | Run history: the failing action and its error code; is the flow on? (7.2) | Flow owner; a 401: the connection owner | Flow, run time, action, error code; screenshot |
| An app shows fewer rows than expected | Count the same rows in SSMS; is there a delegation warning? (7.5) | App owner | App, screen, filter, both counts |
| A scheduled job's output is missing | Task Scheduler Last Run Result and History; Event Viewer; the job's log (8.3) | Tool owner; the server: [COMPANY: server owner] | Task, expected and actual run time, result, log lines |
| A view returns an error or odd numbers | Your query on its source; `OBJECT_DEFINITION`; did the load run? (2.2, 4.3) | The Senior | View, query text, row counts, when it last looked right |
| "Login failed" in SSMS or DBeaver | Right server, right database, your own account; did your password change? | [COMPANY: IT service desk]; database rights: [COMPANY: DBA] | Exact message, server, time |
| Your EBS query runs for minutes | Cancel it (5.2); disconnect | Nobody, if you cancelled; tell the Manager. Repeated slowness: [COMPANY: ERP or DBA team] | Query text, start and cancel time |
| Many things fail at once | Did they all start at the same time? Is the server reachable? | Gateway admin or [COMPANY: IT] | First failure time; list of what failed |

Never while triaging: restart anything, re-run a job or flow, re-enter credentials, edit a connection, or "test" a fix in production. Re-running a job that sends a broker file can send it twice.

## 10. Labs

Each lab is read-only outside the sandbox. Post your output in your OneNote section with your practice-pack posts (07 Analytics) unless the Manager names another page.

### 10.1 SSMS lab (W3–W4)

Reviewed in the Senior's small-analysis SQL review (Thu 11/12, 13:00–14:00). Post it by the end of Wed 11/11. Needs AR-07 and the sandbox grant; if either is late, do steps 1–5 on the Senior's screen and steps 6–8 in the practice scratch database if you have one (`docs/analytics/practice-exercises.md`, Setup, Option B), and tell the Manager.

1. Connect to [COMPANY: team database] with Windows Authentication and run the check in 4.1. Screenshot the result.
2. In Object Explorer, list the schemas and, with the Senior's help, one line on what each holds. Mark the sandbox schema.
3. Find three views relevant to your track with the INFORMATION_SCHEMA query in 4.3 (Hire A: HTS, origin or entry columns; Hire B: cost, PO or receipt columns). For each, write its grain and its owner.
4. Write one read query on one of those views with a header comment, explicit columns, a WHERE clause, and TOP with ORDER BY (4.4). Record the row counts. Save it to [COMPANY: script location for team queries].
5. Write one aggregate query (for example active items by origin country, or receipts by month) and tie its total to a control total the Senior gives you or to a report. Explain any difference.
6. Load suppliers.csv from the practice-data folder in the onboarding folder into the sandbox with the Import Flat File wizard, named by the convention (4.5). Set supplier_id and supplier_country to text. Check: 31 rows, and the codes are stored as text.
7. On your sandbox table only, run the safe-write pattern in 4.4 once with ROLLBACK, and record the count it showed. Then count rows per supplier_country and confirm the total is still 31.
8. Drop your sandbox table and show that it is gone. Write a 5-line lab note: what you did, the row counts, one thing that surprised you, one question, and confirmation that every query you ran outside the sandbox was a SELECT.

Output: the saved scripts (steps 4, 5 and 7), the screenshots and the lab note. It is day-30 evidence for the safe-use Must.

### 10.2 Power Platform lab (W5, read-only)

Trace one semantic model refresh and one flow run end to end. Book 20 minutes with each owner [COMPANY: who owns the model and the flow you trace], who shares their screen; you do not need extra access (AR-09, AR-13). If your owned tool has a model or a flow, trace that one, inside the W5 tool-ownership coaching. Use the time from the W5 self-study line (0.75 h).

- [ ] **Refresh:** workspace and its type (6.1); semantic model; schedule; last 5 entries in refresh history with times and results; the data source and gateway connection name, and which account type it uses (never the password); the views it reads. Then in SSMS, check the newest date in one of those views against what the report shows.
- [ ] **Flow:** trigger and schedule; last 5 runs; for one run, each action with status and duration; each connection and the account it uses; what it read or wrote in the team database. Then in SSMS, find the data that run touched (read-only) and confirm it matches.
- [ ] Note which step of the data path (2.2) each item belongs to, and what would break if each account's password changed tomorrow.

Output: two trace notes with screenshots, and proposed rows for the platform map's Connections and Gateway data sources tables, sent to the Manager. The Manager or the Senior enters confirmed rows in the map.

### 10.3 Server lab (W6, read-only tour)

A 30-minute tour with the Manager or your owned tool's knowledge holder present [COMPANY: confirm who escorts the tour], during the W6 supervised run if your tool runs on the server (Wed 11/25), otherwise booked with the knowledge holder. Needs [COMPANY: Remote Desktop access to the server, requested with docs/04].

- [ ] Connect with Remote Desktop as yourself. Note the server's name as the map records it.
- [ ] In Task Scheduler, for each team task: name, trigger, next run, last run time and result, the account it runs as, and the program and script it starts (8.3, 8.4).
- [ ] For one task, read its History tab and the TaskScheduler Operational log entries for its last run, and find its log file.
- [ ] Find the Python environment the jobs use and note its version and location. Change nothing.
- [ ] Close everything you opened, then sign out (not disconnect).

Output: a tour note, proposed rows for the map's Scheduled jobs table, and your owned tool's doc updated: Section 2 (trigger and schedule), Section 5 (connections) and Section 8 (infrastructure).

## 11. Self-check questions

| No. | Question | Where to check |
|---|---|---|
| 1 | State the twelve safe-use rules in your own words. Which three would hurt the most if broken, and why? | 1.1 |
| 2 | DBeaver asks you to confirm a statement on the EBS connection. What does that tell you, and what do you do? | 1.1 rule 3, 5.1 |
| 3 | You think a statement you ran changed data. List your next steps. | 1.3 |
| 4 | Walk the data path from an EBS receipt to a number on a Power BI report. At which hops can the number be out of date? | 2.2 |
| 5 | What is the recommended service-account model, and why does attribution matter for maker-checker? | 3.2 |
| 6 | A colleague offers you the service account password "to save time". What do you say and do? | 3.5 |
| 7 | Why start from views rather than tables, and how do you find the views that hold a given column? | 4.3 |
| 8 | Why must TOP come with ORDER BY, and why is NOLOCK not a safe way to speed up a query? | 4.4 |
| 9 | Load a CSV into the sandbox: name the steps, the checks after loading and the clean-up. What may you do in the sandbox that you may not do elsewhere? | 1.2, 4.5 |
| 10 | Your owned tool needs a new column in a team view. Who builds it, who checks it, and what goes in the change request? | 4.6 |
| 11 | Which DBeaver settings do you use for EBS, and why is the read-only database account still the real control? Why is the 200-row grid not the whole result? | 5.1, 5.2 |
| 12 | What does "premium workspace" most likely mean today, and what does it change for refreshes and viewers? | 6.1 |
| 13 | A report shows last Tuesday's data. Where do you look first, and who fixes each of the common causes? Whose credentials does a gateway refresh use? | 6.4 to 6.6 |
| 14 | The maker of a flow leaves the company. What breaks, and what would have prevented it? Why does an app on a large SQL table sometimes show only 500 rows? | 7.4, 7.5 |
| 15 | When do you sign out of Remote Desktop and when do you disconnect? Why does it matter on a shared server? | 8.2 |
| 16 | You find a password in a script on the server. What do you do? | 8.5 |

## 12. Sources and further reading

Repo documents: `docs/04-access-request-checklist.md` (rules 2, 3, 6 and 7; AR-05, AR-07 to AR-09, AR-13, AR-15); `docs/templates/knowledge/data-platform-map.md`; `docs/templates/knowledge/tool-doc.md` (Sections 2, 5 and 8 hold your tool's platform path); `docs/templates/bsa/06-change-request.md`; `docs/primers/sdlc-primer.md` (Parts 4, 7 and 8); `docs/primers/copilot-chat-guide.md` 2.4; `docs/analytics/practice-exercises.md` (SQL habits, practice data).

External (product facts as of Oct 2026; check before relying on them):

| Topic | Link |
|---|---|
| SSMS install; SQL Server security best practices | https://learn.microsoft.com/en-us/ssms/install/install; https://learn.microsoft.com/en-us/sql/relational-databases/security/sql-server-security-best-practices |
| DBeaver connection types and read-only restrictions | https://github.com/dbeaver/dbeaver/wiki/Connection-Types; https://github.com/dbeaver/dbeaver/wiki/Managing-security-restrictions-for-database-connection |
| Power BI and Fabric licenses; workspace roles | https://learn.microsoft.com/en-us/fabric/enterprise/licenses; https://learn.microsoft.com/en-us/fabric/fundamentals/roles-workspaces |
| On-premises data gateway management | https://learn.microsoft.com/en-us/power-platform/admin/onpremises-data-gateway-management |
| Power Automate limits; changing a flow's owner | https://learn.microsoft.com/en-us/power-automate/limits-and-config; https://learn.microsoft.com/en-us/power-automate/change-cloud-flow-owner |
| Power Apps delegation | https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/delegation-overview |
| Scheduled tasks that don't run | https://learn.microsoft.com/en-us/troubleshoot/windows-server/system-management-components/troubleshoot-scheduled-tasks-not-running |
| Oracle EBS | docs.oracle.com (E-Business Suite 12.2 library) and [COMPANY: the ERP team's own documentation] |
