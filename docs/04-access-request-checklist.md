# Access Request Checklist

Last updated: 2026-10-17 · Owner: BSA Manager

- **Purpose:** one list of every system the two new BSAs need: why, at what level (least privilege), how to request it, and by when. It also covers the approval, tracking and escalation rules, the one account the hires never get (the service account), and what the hires do in Week 1 if access is late.
- **Who uses it:** the Manager submits and chases requests. On Day 1, Mon 10/19, 14:15-15:00, each hire copies the tracking table into an "Access tracker" page in their own OneNote section and checks each system; the Manager reviews it in the weekly 1:1. System owners approve.
- **When:** submit Day-1 and Week-1 items by Mon 10/12 at the latest (earlier is better, since many IT teams quote 5-10 business days; confirm [COMPANY: IT service-level target]). The sandbox grant in AR-07 and rows AR-22 to AR-24 were added on 10/17: submit them by Mon 10/19. Review access again at day 30 (Wed 11/18), day 60 (Fri 12/18) and day 90 (Fri 1/15/2027), using "Milestone access reviews" below.

## Rules

1. **Least privilege.** Read-only or inquiry access by default, scoped to named databases, workspaces, folders and accounts. Ask for the narrowest role that supports the work in `docs/02-weeks-1-2-schedule.md` and `docs/01-30-60-90-plan.md`, not "the same as the Senior".
2. **No production write access before day 60 (Fri 12/18/2026).** That covers Oracle, the AS400 trade system, SQL Server, the data warehouse, production Power BI workspaces, production Power Apps and flows, tool folders, and broker or government portals. There are two exceptions, and neither is production. (a) The hire's own tables in [COMPANY: sandbox or staging schema in the team database]: the AR-07 sandbox grant lets them create, load and drop their own tables there. Sandbox tables are not production, and nothing a report, flow, app or tool relies on may read from one (`docs/primers/data-platform-primer.md` 1.1, rule 4). (b) A test or dev copy of the hire's own tool: edit rights on that copy are requested at the day-30 review and work from W6 (AR-12, AR-13, AR-15).
3. **From the day-60 review, write access covers only the custom tool the hire owns (M6), and only through change control.** The Manager grants it at the review if the hire meets the "owns one tool" definition in `docs/01-30-60-90-plan.md` Section 4. Make and test the change in a dev or test copy, log a change request (`docs/templates/bsa/06-change-request.md`), get a documented second-person review (maker-checker), have the Manager approve the release, and keep the record in Jira. No other production write access inside the first 90 days.
4. **Oracle cost updates are not a tool.** Hire B prepares and checks the standard cost inputs. Whoever posts them today [COMPANY: who executes the Oracle cost update] keeps doing it in the first 90 days. Any exception needs written approval from the Manager, [COMPANY: Finance controller] and [COMPANY: ERP security], is scoped to the cost-update function only, and must pass [COMPANY: segregation-of-duties or internal-control check]. Maker-checker applies either way.
5. **Government portals (CBP ACE, CBSA CARM) are restricted.** Request them only if the company already uses that portal for this purpose and the account owner agrees. Read-only roles only. For anything else, the Senior or [COMPANY: report owner] runs the report and shares it.
6. **Never share logins.** No borrowed credentials, no shared accounts, no "just use mine to look". If a hire needs to see something before access arrives, the account holder shares their screen. This includes the team's service account: the hires never sign in with it or see its password ("The service account" below).
7. **No company data on personal devices or accounts.** That includes personal email, personal cloud drives and personal AnkiWeb accounts.
8. **Track every request** with a ticket number and status. Before Day 1 the Manager records each ticket number in the tracking table at the end of this page (the OneNote copy). On Day 1 each hire copies that table into an editable "Access tracker" page in their own OneNote section and keeps their own status current: daily in Week 1, then whenever something changes. The Manager reviews each hire's Access tracker in the weekly 1:1.
9. **Review access at each milestone.** At day 30, 60 and 90 the Manager compares each hire's access with this list and removes anything that is no longer needed, using the checks in "Milestone access reviews" below.

## Who approves

| Request | Business approver | System approver or provisioner |
|---|---|---|
| Every request (business need and level) | Manager | See rows below |
| Network, email, Teams, Microsoft 365 apps, software installs (Python, Access runtime, Anki, SSMS, DBeaver, Power BI Desktop) | Manager | [COMPANY: IT service desk] |
| Microsoft 365 Copilot Chat | Manager | [COMPANY: Microsoft 365 administrator] |
| Oracle EBS inquiry (screens) | Manager | [COMPANY: ERP security or Oracle application owner]; [COMPANY: Finance] for cost data |
| Oracle EBS database account for DBeaver (read-only) | Manager | [COMPANY: ERP security], who also confirms to the Manager that the account is read-only |
| AS400 trade system inquiry | Manager | [COMPANY: IBM i security administrator or AS400 system owner] |
| SQL Server and data warehouse, including the sandbox grant | Manager | [COMPANY: data owner or DBA] |
| Power BI (including the premium workspace) and Power Platform environments | Manager | [COMPANY: Power BI or Power Platform administrator] |
| Remote Desktop to the team server | Manager | [COMPANY: IT server owner] |
| Shared drives, SharePoint, code repository | Manager | [COMPANY: site or repository owner] |
| Broker portals | Manager and [COMPANY: trade compliance lead or broker relationship owner] | [COMPANY: broker account representative] |
| CBP ACE Portal | Manager and [COMPANY: ACE Trade Account Owner] | The Trade Account Owner creates the user |
| CBSA CARM Client Portal | Manager and [COMPANY: CARM Business Account Manager] | The Business Account Manager (or Program Account Manager) approves the employee's request |
| e2open project sandbox | Manager and [COMPANY: e2open project lead] | [COMPANY: e2open project administrator] |
| Test-copy edit rights for the owned tool (from W6); production change rights for it (from the day-60 review) | Manager, plus the system owner, plus a change request for production | System owner |

## Access matrix

"Needed by" dates come from the Weeks 1-2 schedule and, for later weeks, the plan. Each date is the first planned use. "Hire A" or "Hire B" means only that hire needs it by that date.

| System | Why a BSA needs it | Access level (least privilege) | How to request | Needed by |
|---|---|---|---|---|
| AR-01 Network, email, Teams, VPN, MFA | Everything else depends on it; sessions, chat and calendar | Standard user account; member of [COMPANY: BSA team distribution list and Teams channel] | [COMPANY: IT new-hire request], submitted by the Manager | Day 1, Mon 10/19 08:00 |
| AR-02 OneNote team notebook | Where the hires read the program and write notes, question logs, tool docs and SOPs | Edit on their own section group (including their Access tracker page) plus Question Log, Tool Docs and Process SOPs. Read on everything else. The analytics answer key is never in the notebook; it stays in [COMPANY: trainer-only location] | Manager shares the notebook from [COMPANY: SharePoint or Teams location] | Day 1, Mon 10/19 13:00 |
| AR-03 Jira | Logging intake, onboarding stories, and later real work items and change records | Project member who can create and edit issues in [COMPANY: Jira project]; no project admin | [COMPANY: Jira admin request] | Wed 10/21 10:00 |
| AR-04 Planner | Weekly learning tasks and plans that the Manager can see | Member of the "BSA Onboarding" plan | Manager adds them (Microsoft 365 group membership) | Wed 10/21 10:00 |
| AR-05 Oracle EBS, read-only inquiry (screens) | Items, item costs and cost elements, POs and receipts: the raw material for landed cost, PPV and the data-flow work | Inquiry-only [COMPANY: Oracle responsibility or role name] covering items, item costs, purchasing and receiving inquiry and [COMPANY: cost reports]. No item, cost, PO or receipt entry; no cost-update function. Database access through DBeaver is AR-23, not this row | [COMPANY: ERP access request form], approved by the ERP security owner | Hire B: Tue 10/20. Hire A: Tue 10/27 |
| AR-06 AS400 trade system, inquiry [COMPANY: system name] | Item trade data (HTS per country, origin, USMCA indicator), broker data flows, as-is documentation for e2open | Inquiry-only user profile limited to trade inquiry screens and reports [COMPANY]; no update menus, no special authorities such as `*ALLOBJ`, no direct file or ODBC access unless separately approved | [COMPANY: IBM i access request] | Tue 10/27 13:00 (data-flow walkthrough); W1 is better |
| AR-07 SQL Server: read on named databases, plus the sandbox grant | Queries for the first real analysis before day 30; checking tool data sources; the SSMS lab and sandbox loads (`docs/primers/data-platform-primer.md` Part 4 and 10.1) | `db_datareader` (or a read-only AD group) on [COMPANY: database names] only, with Windows Authentication and the hire's own login. One write grant only: create, load and drop the hire's own tables in [COMPANY: sandbox or staging schema in the team database] ([COMPANY: DBA confirms the sandbox grant]). No other write roles; no access to production transactional databases if the warehouse has the data. Client: SQL Server Management Studio (SSMS) or VS Code with the MSSQL extension (Azure Data Studio was retired on 2/28/2026, so don't install it) | [COMPANY: database access request] plus a software install ticket for the client; submitted with the Week-1 items | SSMS, the login and the sandbox grant in W1 (by Thu 10/22, the data landscape tour; only after platform primer Part 1 on Tue 10/20). Mon 11/2 (W3, SSMS lab) at the latest |
| AR-08 Data warehouse [COMPANY: name] | Trade and cost history for analysis and reporting backlog items (W10+) | Read on curated schemas or views [COMPANY]; no staging or ETL write | [COMPANY: data access request] | Mon 11/2 (W3) |
| AR-09 Power BI (license and workspace) | Reading existing trade and cost reports; later reporting backlog items | Viewer on [COMPANY: named workspaces], including the team's Power BI premium workspace [COMPANY: workspace name and type]; never Member or Admin, and no gateway role before day 60 (`docs/primers/data-platform-primer.md` 6.2 and 6.5). A Pro (or PPU) license is needed unless the content sits on Premium or Fabric F64+ capacity, where free users can view with the Viewer role. Contributor only in a personal or dev workspace; no publishing to production workspaces before day 60. Install Power BI Desktop (free) | [COMPANY: license request] plus the workspace admin adding them | Viewer by Thu 10/22 (data tour); license by Mon 11/2 |
| AR-10 Excel and Power Query | Analytics practice pack, extracts, the Tariff-Impact Model, most Excel-based tools | Standard Microsoft 365 desktop Excel (Power Query is built into Excel for Windows). Macros run only from trusted locations per [COMPANY: macro policy] | Part of the laptop image; confirm with IT | Tue 10/20 16:00 |
| AR-11 Python (install and IDE per IT policy) | Several custom tools are Python; Hire A can script; data cleansing for e2open | Python from the IT-approved source, VS Code (or the IDE IT approves), packages from the approved index (for example pandas, openpyxl, pyodbc). No admin rights unless IT requires them for the install. If IT suggests a commercial distribution, check its license terms first | [COMPANY: software request] | Mon 11/2 (W3). The practice data is pre-built (Practice-Data.xlsx in the onboarding folder), so W1-W2 need no Python |
| AR-12 Microsoft Access runtime | Opening the Access-based tools during the inventory | Microsoft 365 Access Runtime (free from Microsoft) runs Access apps but has no Design view. Full Access only for the hire who owns an Access tool, on a test copy from W6; the production copy only after the day-60 review [COMPANY: confirm license] | [COMPANY: software request] | Runtime by Thu 10/29 (tool inventory); Full Access by Wed 11/25 (W6 tool coaching) for an Access-tool owner, requested at the day-30 review |
| AR-13 Power Apps and Power Automate environment | Some custom tools are apps or flows; inventory now, test-copy work from W6, ownership from day 60 | Now: user of the production apps they need to see, with no environment role beyond what running them needs [COMPANY: environment security role]; never Environment Admin or System Administrator. Flow details come from the knowledge holder's screen-share or export. From W6, for the owned tool only: Environment Maker in [COMPANY: dev or sandbox environment] and co-owner of the test copy; before day 60 the hire works on test copies only. Production changes only after the day-60 review, through change control | [COMPANY: Power Platform admin request], raised at the day-30 review | User access by Thu 10/29; dev environment by Wed 11/25 (W6 tool coaching) for the owner, requested at the day-30 review |
| AR-14 Shared drives and SharePoint where custom tools live, and the onboarding folder | The inventory needs to see each tool's files, inputs and outputs; the onboarding folder holds the Anki deck, practice data, model template, trackers workbook and samples | Read (Visitors) on tool folders [COMPANY: paths] and on the onboarding folder ([COMPANY: team onboarding folder on SharePoint/Teams]). Edit only on the trackers workbook and the OneNote location. No access to [COMPANY: trainer-only location] | Site owner or [COMPANY: file-share request] | Onboarding folder Day 1; tool folders Thu 10/29 |
| AR-15 Code repository for Python tools, if any [COMPANY: GitHub, Azure DevOps, GitLab or none] | Reading tool code for the inventory and tool docs; test-copy changes from W6 | Read (clone and view) now. From W6: push to feature branches for the owned tool only, with branch protection and a required pull-request review (maker-checker); merges that reach production only after the day-60 review. If the code is in no repository, flag it to the Manager now; the tool docs need a source of truth | Repository owner | Read by Thu 10/29; feature-branch push by Wed 11/25 (W6 tool coaching) for the owner, requested at the day-30 review |
| AR-16 Broker portals (read-only) [COMPANY: broker names] | Seeing what each broker filed (entry summaries, CADs, pedimentos, statements) to audit against our data; Research investigations. Portal access is not a contact channel: until the day-60 review, questions to a broker go through the Senior | View-only user for our importer accounts; cannot submit instructions, approve entries or change billing | Manager and [COMPANY: trade compliance lead] ask each broker's account representative | W4 (Mon 11/9). W1-W2 use the sanitized packets |
| AR-17 CBSA CARM Client Portal (only if the company uses delegated employee access) | Viewing Canadian CAD and statement data directly, rather than through the broker | Reader role (view transactions, no create or edit) on [COMPANY: RM program accounts]. Each user creates their own portal account (GCKey or sign-in partner) and requests access; the company's Business Account Manager or Program Account Manager approves | Manager asks [COMPANY: CARM Business Account Manager] | Not before W4; skip it if the broker provides the data |
| AR-18 CBP ACE Portal reports (usually restricted; only if approved) | Import history by HTS, country and duty paid for Research and cost work; data checks for drawback exposure | Account user with permission to run reports only, created by [COMPANY: ACE Trade Account Owner]; no account-management rights | Manager asks the Trade Account Owner, with a written reason | Only if approved; not needed for days 1-30 |
| AR-19 IMMEX / Anexo 24 inventory-control reports (only if the company runs IMMEX and the team has access) | Understanding how IMMEX data uses item, classification and origin data | Read-only reports [COMPANY: Anexo 24 system or provider]; no data entry | Manager asks [COMPANY: Mexico trade compliance contact] | W5 (Mon 11/16) or later; optional |
| AR-20 e2open (project sandbox, later) | Core project BSA work: as-is to to-be, data mapping and cleansing, UAT | Project sandbox or test tenant user per the project role design; no production tenant access during the build | Manager requests through [COMPANY: e2open project lead] in W9 | Project kickoff, expected W12 (Mon 1/4/2027) [COMPANY: confirm date] |
| AR-21 Anki desktop | 15 minutes a day on the onboarding deck and the hires' own cards | Standard install from apps.ankiweb.net via IT. AnkiWeb sync off for company-specific cards unless IT approves | [COMPANY: software request] | Day 1, Mon 10/19 15:45 |
| AR-22 Microsoft 365 Copilot Chat | Drafting, summarizing and explaining within the rules of `docs/primers/copilot-chat-guide.md` (M11); the use log and the team prompt library | Copilot Chat signed in with the work (Microsoft Entra ID) account, under enterprise data protection. No paid Microsoft 365 Copilot license assumed; no agents unless the Manager confirms; never the consumer Copilot or another AI tool for work data [COMPANY: confirm our Microsoft 365 plan includes Copilot Chat and what the AI acceptable-use policy allows] | Usually comes with the work account (AR-01); the Manager confirms with [COMPANY: Microsoft 365 administrator] that it is enabled for the hires | Day-1 check, Mon 10/19 14:15 (Copilot guide 1.6). Used for work only from the rules session, Fri 10/23 15:00 |
| AR-23 DBeaver and a read-only Oracle EBS database account | Small, filtered SELECT queries on Oracle EBS production for data the team database's copy lacks (`docs/primers/data-platform-primer.md` Part 5). AR-05 covers EBS screens, not database access | DBeaver from [COMPANY: software portal or IT ticket]. A personal EBS database account that can only read [COMPANY: approved EBS views or tables]: no DML, no DDL, no administrative role. Steps: (1) [COMPANY: ERP security] creates the account; (2) **the Manager confirms with [COMPANY: ERP security] that the account is read-only**, before the first query; (3) the Manager checks on the hire's screen that the connection uses the Production connection type and the Read-only connection setting (primer 5.1) | [COMPANY: access request for DBeaver and a read-only EBS database account], approved by the ERP security owner | Before the first EBS query: Mon 11/2 (W3) for both. Hire B earlier only if a W2 cost-data task needs it, after reading primer Part 5 |
| AR-24 Remote Desktop to the team server [COMPANY: server name] | The read-only server lab and the owned tool's scheduled jobs (`docs/primers/data-platform-primer.md` Part 8 and 10.3) | Member of Remote Desktop Users on that server only, signed in with the hire's personal account; no local administrator, no rights to change scheduled tasks or services; never the service account | [COMPANY: Remote Desktop access request], approved by [COMPANY: IT server owner]; submit by Mon 10/19 with the other 10/17 additions, and by Mon 11/9 (W4) at the latest | Mon 11/23 (W6 server lab; supervised run Wed 11/25) |

## The service account: no access for the hires

The team's service account [COMPANY: its label in the platform map's Accounts table] has the same access as the team. Under the recommended model it is used only by saved, unattended connections: Power BI gateway data-source credentials, Power Automate connections and scheduled tasks on the server. It is never requested for the hires and has no row in the tracking table.

- The hires never sign in with it, never ask for or accept its password, and never type it into anything. The password lives in [COMPANY: password vault], held by the Manager (or IT).
- All interactive work uses the hire's personal account, so every query, load and change is attributable (rule 6).
- If anyone offers a hire the password or a shared login, the hire says no and tells the Manager the same day (`docs/primers/data-platform-primer.md` 3.5).

> **Manager decision (open): [COMPANY: confirm the service-account model before access requests go out].** The recommended model, and the related choices (who rotates the password, narrower grants, a service principal or a gMSA for some connections), are in Part 3 of `docs/primers/data-platform-primer.md` (3.2 and 3.3).

## Tracking table

Status values: Not requested, Requested, Approved, Provisioned, Verified (the hire has signed in and seen the right data), Blocked (with reason). On Day 1 (14:15 block) each hire copies this table into an "Access tracker" page in their own OneNote section, where they have edit rights (AR-02), and keeps it current, including setting "Verified" themselves as items arrive. The Manager reviews each hire's Access tracker in the weekly 1:1 until every item is Verified or closed.

| ID | System | Hire A status | Hire B status | Ticket numbers | Notes or escalation |
|---|---|---|---|---|---|
| AR-01 | Network, email, Teams, VPN, MFA | | | | |
| AR-02 | OneNote team notebook | | | | |
| AR-03 | Jira | | | | |
| AR-04 | Planner | | | | |
| AR-05 | Oracle EBS inquiry (screens) | | | | |
| AR-06 | AS400 trade system inquiry | | | | |
| AR-07 | SQL Server read, sandbox grant and SSMS | | | | |
| AR-08 | Data warehouse | | | | |
| AR-09 | Power BI license and workspace | | | | |
| AR-10 | Excel and Power Query | | | | |
| AR-11 | Python and IDE | | | | |
| AR-12 | Access runtime | | | | |
| AR-13 | Power Apps and Power Automate | | | | |
| AR-14 | Shared drives, SharePoint and onboarding folder | | | | |
| AR-15 | Code repository | | | | |
| AR-16 | Broker portals | | | | |
| AR-17 | CBSA CARM Client Portal (if used) | | | | |
| AR-18 | CBP ACE Portal reports (if approved) | | | | |
| AR-19 | IMMEX / Anexo 24 reports (if applicable) | | | | |
| AR-20 | e2open sandbox | | | | |
| AR-21 | Anki desktop | | | | |
| AR-22 | Copilot Chat (work account) | | | | |
| AR-23 | DBeaver and read-only EBS database account | | | | |
| AR-24 | Remote Desktop to the team server | | | | |

## Milestone access reviews

The Manager runs these checks in the week of each milestone review (rule 9) and records the result in the Notes column of each hire's Access tracker.

| Review | Check | Action |
|---|---|---|
| Day 30 (Wed 11/18) | AR-07 is still read plus the sandbox grant only. AR-23 is still read-only (re-confirmed with [COMPANY: ERP security]). No hire holds a gateway, workspace Member or Admin, or environment admin role, or knows the service account's password. AR-24 is provisioned, or has a firm date, for W6. | Remove anything not needed. Request the owned tool's test-copy rights (AR-12, AR-13, AR-15) |
| Day 60 (Fri 12/18) | If the "owns one tool" definition is met: production change rights for the owned tool only, through change control (rule 3). Everything else stays as it was: EBS read-only, loads only into the sandbox, Viewer on production workspaces, no admin roles, no service-account access. | Grant or defer the owned-tool rights; record the decision in the plan change log |
| Day 90 (Fri 1/15) | The day-60 checks again. AR-20 matches the hire's e2open project role. Test copies, extracts and sandbox tables that are no longer needed are gone. | Remove what is no longer needed; agree access for days 91-180 |

## Escalation

| When | Check | Action |
|---|---|---|
| Wed 10/14 | Every Day-1 and Week-1 item has a ticket that is moving | Chase any ticket with no update through [COMPANY: IT service desk] |
| Fri 10/16 12:00 | AR-01 to AR-04, AR-10, AR-14 (onboarding folder), AR-21 provisioned | Escalate anything missing to [COMPANY: IT service desk lead], giving the start date and what breaks without it |
| Mon 10/19 15:00 | The hires' Day-1 access check (schedule block 14:15-15:00) | The Manager escalates every gap that same afternoon and starts the fallback plan below |
| Needed-by date missed for AR-05 Oracle or AR-06 AS400 | Is there a firm provisioning date? | Escalate the same day to the system owner and [COMPANY: IT manager]. These two drive the day-30 goals |
| Still missing on Fri 10/30 | Any item due by W2 | Escalate to [COMPANY: Manager's manager or IT director] and note the risk in both hires' day-30 scorecards (`docs/03-check-ins-and-scorecards.md`) |
| Before each hire's first EBS query (Mon 11/2 at the latest) | [COMPANY: ERP security] has confirmed that the AR-23 account is read-only | No confirmation, no EBS queries: the hire works from the team database's copy of EBS data, and the Manager escalates to the ERP security owner the same day |
| Mon 11/16 (W5) | AR-24 is provisioned for the W6 server lab | Escalate to [COMPANY: IT server owner]; if it is still missing in W6, the tour runs on the escort's screen |

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
| OneNote (AR-02) | Read the Word versions in the onboarding folder (BSA-Onboarding-Handbook.docx, or the single-page files in its docs folder). Keep notes and the question log in one Word file, then paste it in when OneNote is live | Manager |
| Jira or Planner (AR-03, AR-04) | Run the Wed 10/21 session on the Manager's screen. Keep the intake practice and weekly plan in the templates from `docs/05-time-management.md` in Word or Excel; enter them into Jira and Planner on the day access arrives | Manager |
| Oracle (AR-05) | Hire B uses the sanitized standard cost extract and the PPV example instead of live inquiry. Log the questions that need live data | Manager provides the extracts before Day 1 |
| AS400 (AR-06) | The Tue 10/27 data-flow walkthrough runs on the Manager's screen, and the sanitized AS400 item extract is used for the mini data map | Manager |
| SQL Server, data warehouse, Power BI (AR-07 to AR-09) | Not needed for W1-W2 exercises. Practice data is in Practice-Data.xlsx (and the CSV files in its practice-data folder) in the onboarding folder and runs in Excel and Power Query. The Senior gives the Thu 10/22 data tour on their own screen. If AR-07 or its sandbox grant is still missing in W3, the SSMS lab runs on the Senior's screen (steps 1-5) and in the practice scratch database (steps 6-8; `docs/primers/data-platform-primer.md` 10.1) | Senior |
| Python (AR-11) | Not needed in W1-W2; the practice data is pre-built | None |
| Access runtime, Power Platform, tool folders, code repository (AR-12 to AR-15) | During the Thu 10/29 inventory, fill in what you can from the knowledge holder's screen-share and the Manager's list, and mark the other fields "pending access" | Manager |
| Anki (AR-21) | Open BSA-Onboarding-cards.csv from the onboarding folder in Excel, hide the answer column, and self-quiz for 15 minutes. Draft new cards in the same layout. Do not use a personal AnkiWeb account | Hires |
| Copilot Chat (AR-22) | Work without it. Never use the consumer Copilot, a personal subscription or another AI tool for work data (`docs/primers/copilot-chat-guide.md` 1.6). The Fri 10/23 rules session still runs, with Copilot Chat on the Manager's screen | Manager |

Later items: if AR-23 (DBeaver on EBS) is late, the hire uses the team database's copy of EBS data in SSMS (`docs/primers/data-platform-primer.md` 2.2), logs the questions that need EBS itself, and the account holder shares their screen when it matters. If AR-24 (Remote Desktop) is late, the W6 server lab runs on the escort's screen.

Public sources need no access request and work from day 1. Use them for every customs and research self-study block:

- US: hts.usitc.gov (HTSUS), rulings.cbp.gov (CROSS rulings), cbp.gov (including CSMS messages), ecfr.gov (19 CFR), federalregister.gov.
- Canada: cbsa-asfc.gc.ca (Customs Tariff, D-Memoranda, CARM guidance).
- Mexico: dof.gob.mx (Diario Oficial, where TIGIE changes are published), anam.gob.mx, sat.gob.mx.
- USMCA: ustr.gov (agreement text, including Chapter 4 rules of origin and Chapter 5 origin procedures).
