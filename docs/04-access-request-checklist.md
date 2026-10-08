# Access Request Checklist

Last updated: 2026-10-08 · Owner: BSA Manager

- **Purpose:** one list of every system the two new BSAs need: why, at what level (least privilege), how to request it, and by when. It also covers the approval, tracking and escalation rules, and what the hires do in Week 1 if access is late.
- **Who uses it:** the Manager submits and chases requests. The hires check and update the status on Day 1, Mon 10/19, 14:15-15:00. System owners approve.
- **When:** submit Day-1 and Week-1 items by Mon 10/12 at the latest (earlier is better, since many IT teams quote 5-10 business days; confirm [COMPANY: IT service-level target]). Review it again at day 30 (Wed 11/18), day 60 (Fri 12/18) and day 90 (Fri 1/15/2027).

## Rules

1. **Least privilege.** Read-only or inquiry access by default, scoped to named databases, workspaces, folders and accounts. Ask for the narrowest role that supports the work in `docs/02-weeks-1-2-schedule.md` and `docs/01-30-60-90-plan.md`, not "the same as the Senior".
2. **No production write access before day 60 (Fri 12/18/2026).** That covers Oracle, the AS400 trade system, SQL Server, the data warehouse, production Power BI workspaces, production Power Apps and flows, tool folders, and broker or government portals.
3. **After day 60, write access covers only the custom tool the hire owns (M6), and only through change control.** Make and test the change in a dev or test copy, log a change request (`docs/templates/bsa/06-change-request.md`), get a documented second-person review (maker-checker), have the Manager approve the release, and keep the record in Jira. No other production write access inside the first 90 days.
4. **Oracle cost updates are not a tool.** Hire B prepares and checks the standard cost inputs. Whoever posts them today [COMPANY: who executes the Oracle cost update] keeps doing it in the first 90 days. Any exception needs written approval from the Manager, [COMPANY: Finance controller] and [COMPANY: ERP security], is scoped to the cost-update function only, and must pass [COMPANY: segregation-of-duties or internal-control check]. Maker-checker applies either way.
5. **Government portals (CBP ACE, CBSA CARM) are restricted.** Request them only if the company already uses that portal for this purpose and the account owner agrees. Read-only roles only. For anything else, the Senior or [COMPANY: report owner] runs the report and shares it.
6. **Never share logins.** No borrowed credentials, no shared accounts, no "just use mine to look". If a hire needs to see something before access arrives, the account holder shares their screen.
7. **No company data on personal devices or accounts.** That includes personal email, personal cloud drives and personal AnkiWeb accounts.
8. **Track every request** in the tracking table at the end of this page, with a ticket number and status. In Week 1 the hires update it daily; after that, the Manager reviews it weekly.
9. **Review access at each milestone.** At day 30, 60 and 90 the Manager compares each hire's access with this list and removes anything that is no longer needed.

## Who approves

| Request | Business approver | System approver or provisioner |
|---|---|---|
| Every request (business need and level) | Manager | See rows below |
| Network, email, Teams, Microsoft 365 apps, software installs (Python, Access runtime, Anki, SQL client, Power BI Desktop) | Manager | [COMPANY: IT service desk] |
| Oracle ERP inquiry | Manager | [COMPANY: ERP security or Oracle application owner]; [COMPANY: Finance] for cost data |
| AS400 trade system inquiry | Manager | [COMPANY: IBM i security administrator or AS400 system owner] |
| SQL Server and data warehouse | Manager | [COMPANY: data owner or DBA] |
| Power BI and Power Platform | Manager | [COMPANY: Power BI or Power Platform administrator] |
| Shared drives, SharePoint, code repository | Manager | [COMPANY: site or repository owner] |
| Broker portals | Manager and [COMPANY: trade compliance lead or broker relationship owner] | [COMPANY: broker account representative] |
| CBP ACE Portal | Manager and [COMPANY: ACE Trade Account Owner] | The Trade Account Owner creates the user |
| CBSA CARM Client Portal | Manager and [COMPANY: CARM Business Account Manager] | The Business Account Manager (or Program Account Manager) approves the employee's request |
| e2open project sandbox | Manager and [COMPANY: e2open project lead] | [COMPANY: e2open project administrator] |
| Any write access after day 60 | Manager, plus the system owner, plus a change request | System owner |

## Access matrix

"Needed by" dates come from the Weeks 1-2 schedule. "Hire A" or "Hire B" means only that hire needs it by that date.

| System | Why a BSA needs it | Access level (least privilege) | How to request | Needed by |
|---|---|---|---|---|
| AR-01 Network, email, Teams, VPN, MFA | Everything else depends on it; sessions, chat and calendar | Standard user account; member of [COMPANY: BSA team distribution list and Teams channel] | [COMPANY: IT new-hire request], submitted by the Manager | Day 1, Mon 10/19 08:00 |
| AR-02 OneNote team notebook | Where the hires read the program and write notes, question logs, tool docs and SOPs | Edit on their own section group plus Question Log, Tool Docs and Process SOPs. Read on everything else. No access to the answer-key section | Manager shares the notebook from [COMPANY: SharePoint or Teams location] | Day 1, Mon 10/19 13:00 |
| AR-03 Jira | Logging intake, onboarding stories, and later real work items and change records | Project member who can create and edit issues in [COMPANY: Jira project]; no project admin | [COMPANY: Jira admin request] | Wed 10/21 10:00 |
| AR-04 Planner | Weekly learning tasks and plans that the Manager can see | Member of the "BSA Onboarding" plan | Manager adds them (Microsoft 365 group membership) | Wed 10/21 10:00 |
| AR-05 Oracle ERP, read-only inquiry [COMPANY: Oracle EBS or Fusion] | Items, item costs and cost elements, POs and receipts: the raw material for landed cost, PPV and the data-flow work | Inquiry-only [COMPANY: Oracle responsibility or role name] covering items, item costs, purchasing and receiving inquiry and [COMPANY: cost reports]. No item, cost, PO or receipt entry; no cost-update function | [COMPANY: ERP access request form], approved by the ERP security owner | Hire B: Tue 10/20. Hire A: Tue 10/27 |
| AR-06 AS400 trade system, inquiry [COMPANY: system name] | Item trade data (HTS per country, origin, USMCA indicator), broker data flows, as-is documentation for e2open | Inquiry-only user profile limited to trade inquiry screens and reports [COMPANY]; no update menus, no special authorities such as `*ALLOBJ`, no direct file or ODBC access unless separately approved | [COMPANY: IBM i access request] | Tue 10/27 13:00 (data-flow walkthrough); W1 is better |
| AR-07 SQL Server, read-only on named databases | Queries for the first real analysis before day 30; checking tool data sources | `db_datareader` (or a read-only AD group) on [COMPANY: database names] only; no write roles; no access to production transactional databases if the warehouse has the data. Client: SQL Server Management Studio or VS Code with the MSSQL extension (Azure Data Studio was retired on 2/28/2026, so don't install it) | [COMPANY: database access request] plus a software install ticket for the client | Mon 11/2 (W3) |
| AR-08 Data warehouse [COMPANY: name] | Trade and cost history for analysis and reporting backlog items (W10+) | Read on curated schemas or views [COMPANY]; no staging or ETL write | [COMPANY: data access request] | Mon 11/2 (W3) |
| AR-09 Power BI (license and workspace) | Reading existing trade and cost reports; later reporting backlog items | Viewer on [COMPANY: named workspaces]. A Pro (or PPU) license is needed unless the content sits on Premium or Fabric F64+ capacity, where free users can view with the Viewer role. Contributor only in a personal or dev workspace; no publishing to production workspaces before day 60. Install Power BI Desktop (free) | [COMPANY: license request] plus the workspace admin adding them | Viewer by Thu 10/22 (data tour); license by Mon 11/2 |
| AR-10 Excel and Power Query | Analytics practice pack, extracts, the Tariff-Impact Model, most Excel-based tools | Standard Microsoft 365 desktop Excel (Power Query is built into Excel for Windows). Macros run only from trusted locations per [COMPANY: macro policy] | Part of the laptop image; confirm with IT | Tue 10/20 16:00 |
| AR-11 Python (install and IDE per IT policy) | Several custom tools are Python; Hire A can script; data cleansing for e2open | Python from the IT-approved source, VS Code (or the IDE IT approves), packages from the approved index (for example pandas, openpyxl, pyodbc). No admin rights unless IT requires them for the install. If IT suggests a commercial distribution, check its license terms first | [COMPANY: software request] | Mon 11/2 (W3). The practice data is pre-built in `dist/`, so W1-W2 need no Python |
| AR-12 Microsoft Access runtime | Opening the Access-based tools during the inventory | Microsoft 365 Access Runtime (free from Microsoft) runs Access apps but has no Design view. Full Access only for the hire who owns an Access tool, after day 60, in a dev copy [COMPANY: confirm license] | [COMPANY: software request] | Thu 10/29 (tool inventory) |
| AR-13 Power Apps and Power Automate environment | Some custom tools are apps or flows; inventory now, ownership after day 60 | Now: user of the production apps they need to see. Flow details come from the knowledge holder's screen-share or export. After day 60, for the owned tool only: Environment Maker in [COMPANY: dev or sandbox environment] and co-owner of the dev copy. Production changes only through change control | [COMPANY: Power Platform admin request] | User access by Thu 10/29; dev environment by W9 (12/14) for the owner |
| AR-14 Shared drives and SharePoint where custom tools live | The inventory needs to see each tool's files, inputs and outputs; training samples | Read (Visitors) on tool folders [COMPANY: paths]. Edit (Members) only on the BSA training folder and the OneNote location | Site owner or [COMPANY: file-share request] | Training folder Day 1; tool folders Thu 10/29 |
| AR-15 Code repository for Python tools, if any [COMPANY: GitHub, Azure DevOps, GitLab or none] | Reading tool code for the inventory and tool docs; changes after day 60 | Read (clone and view) now. After day 60: push to feature branches for the owned tool only, with branch protection and a required pull-request review (maker-checker). If the code is in no repository, flag it to the Manager now; the tool docs need a source of truth | Repository owner | Read by Thu 10/29 |
| AR-16 Broker portals (read-only) [COMPANY: broker names] | Seeing what each broker filed (entry summaries, CADs, pedimentos, statements) to audit against our data; Research investigations | View-only user for our importer accounts; cannot submit instructions, approve entries or change billing | Manager and [COMPANY: trade compliance lead] ask each broker's account representative | W4 (Mon 11/9). W1-W2 use the sanitized packets |
| AR-17 CBSA CARM Client Portal (only if the company uses delegated employee access) | Viewing Canadian CAD and statement data directly, rather than through the broker | Reader role (view transactions, no create or edit) on [COMPANY: RM program accounts]. Each user creates their own portal account (GCKey or sign-in partner) and requests access; the company's Business Account Manager or Program Account Manager approves | Manager asks [COMPANY: CARM Business Account Manager] | Not before W4; skip it if the broker provides the data |
| AR-18 CBP ACE Portal reports (usually restricted; only if approved) | Import history by HTS, country and duty paid for Research and cost work; data checks for drawback exposure | Account user with permission to run reports only, created by [COMPANY: ACE Trade Account Owner]; no account-management rights | Manager asks the Trade Account Owner, with a written reason | Only if approved; not needed for days 1-30 |
| AR-19 IMMEX / Anexo 24 inventory-control reports (only if the company runs IMMEX and the team has access) | Understanding how IMMEX data uses item, classification and origin data | Read-only reports [COMPANY: Anexo 24 system or provider]; no data entry | Manager asks [COMPANY: Mexico trade compliance contact] | W5 (Mon 11/16) or later; optional |
| AR-20 e2open (project sandbox, later) | Core project BSA work: as-is to to-be, data mapping and cleansing, UAT | Project sandbox or test tenant user per the project role design; no production tenant access during the build | Manager requests through [COMPANY: e2open project lead] in W9 | Project kickoff, expected W12 (Mon 1/4/2027) [COMPANY: confirm date] |
| AR-21 Anki desktop | 15 minutes a day on the onboarding deck and the hires' own cards | Standard install from apps.ankiweb.net via IT. AnkiWeb sync off for company-specific cards unless IT approves | [COMPANY: software request] | Day 1, Mon 10/19 15:45 |

## Tracking table

Status values: Not requested, Requested, Approved, Provisioned, Verified (the hire has signed in and seen the right data), Blocked (with reason). The hires update the "Verified" status themselves on Day 1 and as items arrive.

| ID | System | Hire A status | Hire B status | Ticket numbers | Notes or escalation |
|---|---|---|---|---|---|
| AR-01 | Network, email, Teams, VPN, MFA | | | | |
| AR-02 | OneNote team notebook | | | | |
| AR-03 | Jira | | | | |
| AR-04 | Planner | | | | |
| AR-05 | Oracle ERP inquiry | | | | |
| AR-06 | AS400 trade system inquiry | | | | |
| AR-07 | SQL Server read-only and client | | | | |
| AR-08 | Data warehouse | | | | |
| AR-09 | Power BI license and workspace | | | | |
| AR-10 | Excel and Power Query | | | | |
| AR-11 | Python and IDE | | | | |
| AR-12 | Access runtime | | | | |
| AR-13 | Power Apps and Power Automate | | | | |
| AR-14 | Shared drives and SharePoint | | | | |
| AR-15 | Code repository | | | | |
| AR-16 | Broker portals | | | | |
| AR-17 | CBSA CARM Client Portal (if used) | | | | |
| AR-18 | CBP ACE Portal reports (if approved) | | | | |
| AR-19 | IMMEX / Anexo 24 reports (if applicable) | | | | |
| AR-20 | e2open sandbox | | | | |
| AR-21 | Anki desktop | | | | |

## Escalation

| When | Check | Action |
|---|---|---|
| Wed 10/14 | Every Day-1 and Week-1 item has a ticket that is moving | Chase any ticket with no update through [COMPANY: IT service desk] |
| Fri 10/16 12:00 | AR-01 to AR-04, AR-10, AR-21 provisioned | Escalate anything missing to [COMPANY: IT service desk lead], giving the start date and what breaks without it |
| Mon 10/19 15:00 | The hires' Day-1 access check (schedule block 14:15-15:00) | The Manager escalates every gap that same afternoon and starts the fallback plan below |
| Needed-by date missed for AR-05 Oracle or AR-06 AS400 | Is there a firm provisioning date? | Escalate the same day to the system owner and [COMPANY: IT manager]. These two drive the day-30 goals |
| Still missing on Fri 10/30 | Any item due by W2 | Escalate to [COMPANY: Manager's manager or IT director] and note the risk in both hires' day-30 scorecards (`docs/03-check-ins-and-scorecards.md`) |

Copy-paste escalation note:

> Subject: Access for new BSA - [system] not provisioned (ticket [number])
>
> [New hire] started on Mon 10/19 as a Business Systems Analyst. Ticket [number], raised on [date] for [system and access level], is still [status]. It is needed for [activity] on [date]; without it, [impact].
>
> Can you confirm a provisioning date by [time today]? The business approval from the BSA Manager is on the ticket.

## Fallback plan for Week 1 if access is late

The training does not stop for missing access. Each gap below has a substitute that keeps the block's output the same.

| If this is missing | Do this instead | Who arranges it |
|---|---|---|
| Laptop, network or sign-in (AR-01) | Work from the printed backup pack (Week 1 schedule, US sections of the customs primer, time management). Attend every Manager and Senior session in a meeting room on the trainer's screen. Take paper notes and type them into OneNote later. Do the shadow sessions as planned | Manager prints the pack on Fri 10/16 |
| OneNote (AR-02) | Read the Word files in `dist/docs/` or `dist/BSA-Onboarding-Handbook.docx` from the shared folder. Keep notes and the question log in one Word file, then paste it in when OneNote is live | Manager |
| Jira or Planner (AR-03, AR-04) | Run the Wed 10/21 session on the Manager's screen. Keep the intake practice and weekly plan in the templates from `docs/05-time-management.md` in Word or Excel; enter them into Jira and Planner on the day access arrives | Manager |
| Oracle (AR-05) | Hire B uses the sanitized standard cost extract and the PPV example instead of live inquiry. Log the questions that need live data | Manager provides the extracts before Day 1 |
| AS400 (AR-06) | The Tue 10/27 data-flow walkthrough runs on the Manager's screen, and the sanitized AS400 item extract is used for the mini data map | Manager |
| SQL Server, data warehouse, Power BI (AR-07 to AR-09) | Not needed for W1-W2 exercises. Practice data is in `dist/Practice-Data.xlsx` and `dist/practice-data/*.csv` and runs in Excel and Power Query. The Senior gives the Thu 10/22 data tour on their own screen | Senior |
| Python (AR-11) | Not needed in W1-W2; the practice data is pre-built | None |
| Access runtime, Power Platform, tool folders, code repository (AR-12 to AR-15) | During the Thu 10/29 inventory, fill in what you can from the knowledge holder's screen-share and the Manager's list, and mark the other fields "pending access" | Manager |
| Anki (AR-21) | Open `dist/anki/BSA-Onboarding-cards.csv` in Excel, hide the answer column, and self-quiz for 15 minutes. Draft new cards in the same layout. Do not use a personal AnkiWeb account | Hires |

Public sources need no access request and work from day 1. Use them for every customs and research self-study block:

- US: hts.usitc.gov (HTSUS), rulings.cbp.gov (CROSS rulings), cbp.gov (including CSMS messages), ecfr.gov (19 CFR), federalregister.gov.
- Canada: cbsa-asfc.gc.ca (Customs Tariff, D-Memoranda, CARM guidance).
- Mexico: dof.gob.mx (Diario Oficial, where TIGIE changes are published), anam.gob.mx, sat.gob.mx.
- USMCA: ustr.gov (agreement text, including Chapter 4 rules of origin and Chapter 5 origin procedures).
