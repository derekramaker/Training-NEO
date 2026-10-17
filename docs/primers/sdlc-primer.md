# SDLC and Change Delivery Primer

Last updated: 2026-10-17 · Owner: BSA Manager

- **Purpose:** the self-study backbone for M13 (SDLC and change delivery). It explains how a change to a tool, a report, a database object or a system configuration moves from idea to production and support: the phases and the team template used at each, delivery models (including how a vendor GTM implementation runs), environments and test copies, version control, testing, change control and release, support, and how all of this works for each of our tool types. Part 10 walks one small change through every step. The templates in `docs/templates/bsa/` say what to fill in; this primer says why, and in what order.
- **Who uses it:** Hire A and Hire B for self-study (Parts 1–4 in W5, Parts 5–9 applied to the owned tool in W6, about 2.25 hours, taken from the existing self-study budget; short re-reads later). The Manager uses it in the W6 tool-ownership coaching (the supervised run) and the W8 change-request review. Both trainers can cite sections in review comments (for example "SDLC primer 7.5").
- **When:** follow the study plan below. Re-read Part 7 and Part 10 before your W8 change request, and 3.5 and Part 6 before the e2open kickoff (expected W12) and again before e2open testing starts (M10, after day 90).

## How to use this primer

| Session | When | Parts | Focused time | Output |
|---|---|---|---|---|
| 1 | W5, after the day-30 review (Wed 11/18) | 1 and 2 | 0.5 h | 3 Anki cards; the phases your owned tool's last change went through, or skipped |
| 2 | W5 | 3 and 4 | 0.75 h | Where your owned tool's production copy and data live, and where its test copy will live (first rows of the profile in 9.3) |
| 3 | W6, before tool coaching on Wed 11/25 | 5 to 9, closely for your tool's technology | 1.0 h | Owned-tool SDLC profile (9.3), brought to the supervised run |
| 4 | W7, before the Wed 12/2 session on data mapping and UAT basics | Part 6 again | 0.25 h | Two test cases for your planned W8 change, with exact expected results |
| 5 | W8, before the Wed 12/9 change-request review | 7 and 10, then the self-check (Part 11) | 0.5 h | Your change request (06) naming the environments, the test evidence and the rollback |
| 6 | W12, before the e2open kickoff | 3.5 and Part 6 again | 0.25 h | Questions on the project method and test phases, added to your kickoff list |

The rest of the 2.0 h of new self-study in each of W5 and W6 goes to the Power Platform lab (W5) and the server lab (W6), both in `docs/primers/data-platform-primer.md`. Sessions 4 to 6 are short re-reads inside that week's existing self-study.

Tailoring:

- **Hire A (Research):** your owned tool is [COMPANY: tool closest to Research]. If it is Python, spend extra time on 5.1 and the Python rows of Part 9: you can script, and a script that feeds a broker file or a rate table needs the same controls as any release. Research outputs are not software, but they follow the same pattern: version, check, release, tell people, re-issue when the action is amended.
- **Hire B (Standard Cost):** your owned tool is [COMPANY: name of std-cost tool]. Spend extra time on 4.6 (test data: costs and supplier prices are sensitive) and 7.5 (rollback and data clean-up): a wrong rate in a cost tool spreads into Oracle EBS standard cost and PPV (purchase price variance). Finance's cost calendar sets your release windows (06 Section 5).

Rules: [COMPANY: ...] marks a company fact the Manager confirms. PART-A, Country X, Action X-0, Action X-1 and the Duty Rate Lookup tool are fictional, and object names such as `rpt.v_duty_rate` are marked "(example name)". Product facts (licensing, limits, features) are dated and linked where they appear; check the link before you rely on one. Template numbers 01 to 08 refer to `docs/templates/bsa/`. Terms are in the Glossary tab of the trackers workbook.

## 1. What the SDLC is and why a BSA cares

### 1.1 The idea

The software development life cycle (SDLC) is the path a change takes from "someone needs something" to "it runs in production, is supported, and is eventually retired". NIST defines the system development life cycle as the "scope of activities associated with a system, encompassing the system's initiation, development and acquisition, implementation, operation and maintenance, and ultimately its disposal" (https://csrc.nist.gov/glossary/term/system_development_life_cycle). For teaching it is commonly described in eight phases: intake and plan, requirements, design, build, test, release, operate and support, retire (Part 2). It applies to anything that changes what a system does or produces: a Python script, an Excel workbook with macros, an Access database, a Power App, a flow, a Power BI report, a view in the team database, an e2open configuration. The size of a change decides how much paperwork it needs, never which steps it may skip.

### 1.2 Why a BSA cares

- **You are in every phase.** You write the intake and requirements, shape the design, test, prepare the release, support users and document the tool. On a vendor project such as e2open you do not build, but you write requirements, map data and run user acceptance testing (UAT).
- **Our tools carry real risk, and most have no documentation.** The team's 10+ custom tools feed brokers, Finance and Oracle EBS. One careless change can put a wrong HTS number on customs entries (06 filled example) or a wrong duty rate into standard cost, and without a record of what changed nobody can explain an old output or undo the change.
- **Controls depend on it.** Maker-checker, change requests and test evidence are the team's controls over tool changes. If the Sarbanes-Oxley Act (SOX) applies to the company, auditors test IT general controls and look for the same evidence (7.7).

### 1.3 Five rules that run through this primer

1. **Never change production directly.** Build and test in a development or test copy, then release the tested version.
2. **Maker-checker.** Every change gets a documented second-person review before release. Owning a tool never means approving your own change (`docs/01-30-60-90-plan.md` Section 4).
3. **No production write access before the day-60 review (Fri 12/18).** From W6 you build and test in a test copy of your owned tool. Before day 60 the Manager (or the current knowledge holder) carries out every production step (`docs/04-access-request-checklist.md` rules 2 and 3).
4. **Every change is reversible.** No release without a verified backup and a written rollback plan.
5. **Use, don't change, the team database.** Until day 90 you query data, and you load data only into [COMPANY: sandbox or staging schema in the team database]. Tables, views, procedures and jobs change through the Senior. If your owned tool depends on team database objects, a change to those objects goes through a change request with the Senior as checker, and rule 3 still applies.

**How this applies to our work:** the W6 supervised run and the W8 change request are your first full trips round the SDLC, and the day-60 "owns one tool" criteria (A60-4, B60-4) are the evidence that you can make the trip safely. Research briefs and Standard Cost input files follow the same pattern without code: drafted (build), checked (test and review), released, re-issued when something changes. On e2open you will see the same phases at project scale.

## 2. The phases and the template for each

### 2.1 Phase by phase

| Phase | What happens | The BSA's job | Team template | Done when |
|---|---|---|---|---|
| Intake and plan | A request arrives; it is routed, sized and prioritized | Clarify the need, route it, open the Jira issue | 01-intake-request; 07 epic or story | The issue meets the definition of ready (07) |
| Requirements | What the change must do, as testable statements | Elicit; write acceptance criteria in Given/When/Then; trace | 02-requirements; 07 acceptance criteria | The requester agrees the criteria |
| Design | How it will work: logic, data, screens, interfaces | Before and after; what is not changing; data mapping | 03 (to-be), 04-data-mapping-spec; 06 Section 2 | The checker could spot an unintended change from it |
| Build | The change is made, in a copy | Make it (tool owner) or confirm it (vendor or IT build) | 06 Section 7 technology checklist | Built in the test copy; production untouched |
| Test | Proof that it does what was agreed and breaks nothing | Test cases, evidence, defects, regression | 05-uat-test-plan; 06 Section 6 | Exit criteria met; checker reviewed the evidence |
| Release | The tested version goes to production, reversibly | Release checklist, rollback plan, user messages | 06 Sections 8 to 11 | Approved, deployed, users told |
| Operate and support | It runs; someone watches it and fixes what breaks | Run, monitor, log incidents and bugs, update docs | `docs/templates/knowledge/tool-doc.md` Sections 6, 7, 11; 07 bug | Post-release check passed; tool doc current |
| Retire | It is switched off or replaced | Disposition, archive, remove schedules and access | 08-project-closeout; Tool Inventory | Nothing still runs or depends on it |

### 2.2 Scaling to the size of the change

A one-cell fix and an e2open release go through the same phases; only the depth changes. For a small tool change (most of yours), a Jira story with acceptance criteria covers intake and requirements, the change request (06) covers design through release, and the tool doc's change history closes it. A larger change adds a requirements document (02), a UAT plan (05) and a closeout (08). The e2open project uses every template plus its own plans and gates (3.5). The risk rating in 06 Section 5 (Low, Medium, High) decides how much testing and approval a change needs. Never skip a phase because a change "is tiny": tiny changes to HTS or rate handling are where the worst errors start.

### 2.3 Retire is a phase too

Tools are retired when e2open replaces them, when their process ends or when a better tool exists. Retiring badly leaves a job running, a flow still emailing, or an old copy someone keeps using.

- [ ] The replacement is live and its first cycle reconciled with the old output; users know where to go, and old copies are removed or renamed "RETIRED - do not use".
- [ ] Schedules, flows, refreshes and service-account connections are switched off ([COMPANY: who removes server jobs and connections]).
- [ ] Code, the last version and its outputs are archived per [COMPANY: records retention policy], and the business rules hidden in the tool are in the replacement's requirements (tool doc Section 10).
- [ ] The Tool Inventory row and the tool doc are marked Retired with the date, and the closeout (08) is written.

**How this applies to our work:** for your owned tool, find the last real change and ask the knowledge holder which phases it went through. Gaps (no test, no backup, no record) go into the tool doc's open questions. Your day-60 e2open disposition for the tool (replace, interface, retire, keep) is a first retire-phase decision.

## 3. Delivery models

A delivery model is the order and rhythm in which the phases happen. The ISTQB Foundation syllabus (CTFL v4.0.1, https://www.istqb.org/certifications/certified-tester-foundation-level-ctfl-v4-0/) groups them as sequential (waterfall, V-model), iterative and incremental, and agile methods and practices (Scrum and Kanban among them).

### 3.1 Sequential models: waterfall and the V-model

In **waterfall**, phases run one after another, and test activities happen only after all development is done (ISTQB). It can work when requirements are stable and well understood. Its weakness: a misunderstood requirement surfaces at the end, when it is most expensive to fix.

The **V-model** keeps the sequence but integrates testing throughout development by pairing each development phase with a test level. It is usually drawn as: business requirements with acceptance testing; system requirements or functional design with system testing; architecture design with integration testing; detailed design with component (unit) testing. Labels vary by source; the pairs and our examples are in the table in 6.1. The habit to keep: write the test for each level when you write that level's requirement or design, not after the build.

### 3.2 Agile and Scrum basics

The Agile Manifesto (2001, https://agilemanifesto.org/) states four values: "Individuals and interactions over processes and tools; Working software over comprehensive documentation; Customer collaboration over contract negotiation; Responding to change over following a plan. That is, while there is value in the items on the right, we value the items on the left more." It values documentation less than working software; it does not say "no documentation".

Scrum is a common agile framework. From the 2020 Scrum Guide (https://scrumguides.org/scrum-guide.html):

- **One Scrum Team, three accountabilities.** The Product Owner (one person, not a committee) maximizes the product's value and manages the Product Backlog. The Scrum Master is accountable for establishing Scrum as the Guide defines it and for the team's effectiveness. The Developers create the Sprint Backlog and instill quality by adhering to the Definition of Done.
- **Five events.** The Sprint (fixed length, one month or less; the container for the other events), Sprint Planning, the Daily Scrum (15 minutes, for the Developers), the Sprint Review and the Sprint Retrospective.
- **Three artifacts, each with a commitment.** Product Backlog: the Product Goal. Sprint Backlog: the Sprint Goal. Increment: the Definition of Done. An item that does not meet the Definition of Done cannot be released or even presented at the Sprint Review; the team's definition of done for Jira issues (07) plays the same role.

### 3.3 Kanban

Kanban manages a continuous flow of work rather than fixed iterations (https://kanban.university/kanban-guide/). Its core practices: **visualize the work** on a board whose columns are steps; **limit work in progress** (WIP limits per column, person or whole system); **pull** new work only when there is room under the limit; and make the **policies explicit**. The team already works this way: the Jira board's columns ([COMPANY: workflow]; suggested in 07: Backlog, Ready, In progress, In review, Done) and the limit of 3 active items per hire (`docs/01-30-60-90-plan.md` Section 7).

### 3.4 Hybrid: what we actually do

ISTQB notes that models can be combined, and that is our normal case. Team work (tariff actions, cost cycles, backlog items) flows through Jira, Kanban-style, with the P1–P3 priorities in `docs/05-time-management.md`. A tool change runs like a small V-model: acceptance criteria first, build in a copy, test at each level, release through a change request. The e2open project follows the vendor's or partner's phased method (3.5), possibly with agile-style build iterations inside it: [COMPANY: confirm the e2open project method].

### 3.5 How a vendor GTM implementation usually runs

ERP and GTM implementations use broadly the same phases, though every vendor and partner names them differently. Microsoft's Dynamics 365 Implementation Guide describes them clearly and serves as a neutral reference. The e2open project's own names, gates and dates are [COMPANY: e2open/partner implementation phase names and current phase].

| Phase (generic name) | What happens | Your role as a core project BSA | Your template |
|---|---|---|---|
| Discovery and fit-gap | Fit-to-standard first: meet needs with standard features and configuration. Fit-gap then finds where the standard falls short and decides how to close each gap: configure, change the process, extend, or accept | As-is process and data; requirements; gap decisions | 03, 02, 04 |
| Build and configure | The partner configures the system (and extends it where approved) to the agreed design | Answer design questions; data mapping and cleansing | 04, including its cleansing log (Part 6) |
| SIT (system integration testing) | The solution tested with other applications and external systems, before UAT, at expected peak volumes | Interface test cases: Oracle EBS, broker files, the warehouse | 05 (scenarios TS-01, TS-09) |
| UAT (user acceptance testing) | Business users test in a dedicated environment with migrated data and realistic security roles; it ends in sign-off and is a prerequisite for go-live | Write and run cases, log defects, collect sign-off | 05 |
| Cutover | The last step before launch: a rehearsed plan (mock cutover), a rollback plan and a go/no-go decision | Cutover tasks; reconcile counts and totals after conversion | 04 Part 7 |
| Go-live | The new system becomes operational and moves to support | Run and check the first cycles | Tool doc and SOP updates |
| Hypercare | A short, intensive support period after go-live, with exit criteria and an end date set in advance | Triage issues, fix data, update SOPs | Issue log; 08 |

Sources (as of Oct 2026): https://learn.microsoft.com/en-us/dynamics365/guidance/implementation-guide/process-focused-solution-fit-to-standard-fit-gap-analysis and the same guide's pages on test types, cutover strategy and transition to support. The BSA migration activities (as-is, to-be, data mapping, cleansing, conversion, parallel run) are in `docs/primers/trade-systems-gtm-e2open-primer.md` Section 6; its Section 5.3 lists what the project must still confirm, including which environments exist and when.

**How this applies to our work:** your Research or Standard Cost work runs as Kanban, your owned-tool change as a small V-model, and e2open as a phased vendor project. Know which one you are in, because each tells you when a test should already exist. A vendor's own testing never replaces our UAT.

## 4. Environments

### 4.1 Why separate environments

An environment is a separate place where a version of a system runs with its own data, settings and access. The classic three are **development** (where you build), **test** (where you prove it, sometimes with a separate UAT stage) and **production** (what the business relies on). Microsoft's Power Platform guidance says lifecycle management needs at least separate development and production environments, and that "the ideal solution is to have three environments, one each for development, testing, and production" (as of Oct 2026; check https://learn.microsoft.com/en-us/power-platform/alm/basics-alm). Many of our custom tools have only production today. Your W6 test copy fixes that for one tool.

### 4.2 Our environments

- **Custom tools:** where you build and test each tool type is in 9.1. Your tool's production location ([COMPANY: tool library, server path or Power Platform environment]) goes in its tool doc. For Excel and Access tools the test environment is a test copy (4.5).
- **Team database (SQL Server):** changes to objects go through the Senior. You read with your personal login and load only into [COMPANY: sandbox or staging schema in the team database] (rule 5 in 1.3).
- **e2open:** the vendor or partner builds and configures; you work in the project sandbox or test tenant (AR-20), with no access to the production tenant during the build ([COMPANY: e2open environments and dates]).
- **Platform details** (the server, the gateway, connections and the safe-use rules) are in `docs/primers/data-platform-primer.md`; this Part covers only what matters for moving a change.

### 4.3 Power Platform environments and solutions

- **Environment types** (as of Oct 2026; check https://learn.microsoft.com/en-us/power-platform/admin/environments-overview): Production; Sandbox (non-production, can be copied and reset); Developer (single owner); Trial (expires after 30 days); Default (one per tenant; Microsoft says it is not for production workloads); Dataverse for Teams. Which ones the team uses is [COMPANY: Power Platform environments for the team's apps and flows].
- **Solutions** package apps, flows and their parts to move them between environments (https://learn.microsoft.com/en-us/power-platform/alm/solution-concepts-alm). Build in an **unmanaged** solution in development and treat it as your source; deploy it as a **managed** solution everywhere else. Managed components cannot be edited directly in the target, which stops "quick fixes" in production. **Environment variables** hold values that differ by environment (a site, a folder, a mailbox) and are set at deployment. Apps and flows built without this discipline often sit outside any solution; find out whether yours does, because it decides how you version it (5.3) and roll it back (Part 9).
- **Power Platform pipelines** deploy solutions from development to target environments inside the product. Targets must be Managed Environments, which need premium licensing (as of Oct 2026; check https://learn.microsoft.com/en-us/power-platform/alm/pipelines). [COMPANY: confirm Power Platform licensing and whether Managed Environments are enabled].

### 4.4 Power BI workspaces and deployment pipelines

- **The simple pattern:** develop in Power BI Desktop against test or sandbox data, publish to a development workspace, check it, then publish to the production workspace and update the app. Before day 60 you do not publish to production workspaces (AR-09).
- **Deployment pipelines** automate this: 2 to 10 stages (default three: Development, Test, Production), each its own workspace, with a stage comparison and **deployment rules** that switch data sources or parameters per stage. They work in Premium Per User, Premium-capacity and Fabric-capacity workspaces, not in Pro workspaces (as of Oct 2026; check https://learn.microsoft.com/en-us/fabric/cicd/deployment-pipelines/intro-to-deployment-pipelines). Whether our "Power BI premium workspace" supports them is [COMPANY: confirm our workspace's license mode].
- Refreshes from the team database run through the on-premises data gateway, with credentials set per data source (`docs/primers/data-platform-primer.md`). A report that refreshes in Desktop can still fail in the service because of the gateway connection.

### 4.5 Test copies for Excel and Access tools

A test copy is a separate, clearly labelled copy of the tool that cannot touch production outputs. Edit rights on it work from W6 (AR-12, AR-13, AR-15). Set one up like this:

- [ ] Copy the current production version to [COMPANY: test-copy location for the owned tool], add "_TEST" to the file name, and record which production version you copied. Mark it inside too: a banner cell, tab colour or form caption saying TEST COPY.
- [ ] Point every output at a test folder: no broker folder, no Finance share, no Oracle EBS interface, no emails to real distribution lists. For Access, link the test front-end to a test copy of the back-end (06 Section 7).
- [ ] If the tool writes to the team database, point it at [COMPANY: sandbox or staging schema in the team database]. A tool that only reads may read production views with your personal login.
- [ ] Switch off any schedule, auto-run macro or flow that could fire from the copy.
- [ ] Record the test copy's location and set-up in the tool doc (Section 8).

### 4.6 Test data: realistic, and masked where it must be

- **Realistic shapes.** A good test set has the awkward cases: HTS numbers starting with 0, codes per country, effective-date edges, blanks, unit-of-measure mismatches. Start from a production extract, then trim it.
- **Mask what you must.** Supplier prices, costs, margins, customer names and any personal data stay in access-controlled locations. Replace them with made-up values when the test does not need the real ones ([COMPANY: data classification policy]).
- **Keep evidence, then clean up.** Keep test inputs and outputs exactly as produced, named by the rule in 05 Section 10. Delete test data you no longer need, do not leave copies in email, and never put any on a personal device or account (`docs/04-access-request-checklist.md` rule 7).
- **Copilot Chat** can help draft test cases from acceptance criteria, within [COMPANY: AI acceptable-use policy] (`docs/primers/copilot-chat-guide.md`). You still work out every expected value yourself, and company data goes into it only as far as that policy allows.

### 4.7 Accounts and connections across environments

A change that works in test can fail in production because it runs under a different account. In test you run everything with your personal login; in production a scheduled job, a gateway data source or a flow connection may run as the team's service account. For every change, write down which account each connection uses in each environment, and check the production connection in the post-release check (7.6).

> **Manager decision (open):** the recommended model is that the team's service account is used only by saved, unattended connections: Power BI gateway data-source credentials, Power Automate connections and scheduled jobs on the server. Hires never sign in with it and never see its password, which lives in [COMPANY: password vault], held by the Manager (or IT). All interactive work, including all your testing, uses your personal account, so every action is attributable (`docs/04-access-request-checklist.md` rule 6). [COMPANY: confirm the service-account model before access requests go out]. Details: `docs/primers/data-platform-primer.md`.

**How this applies to our work:** your W6 test copy is your owned tool's test environment. Your W8 change request must name the environments (test copy and production, or dev, test and prod); that is part of the day-60 Must (A60-4, B60-4). Hire B: cost tools hold sensitive data, so mask it in any test copy others can open. On e2open, ask which environments exist and when; UAT needs its own environment with migrated data.

## 5. Version control and documentation

Version control answers three questions at any moment: what exactly is running, what changed since last time and who checked it, and how we get back. A tool without it is a tool nobody can safely change.

### 5.1 Git for Python tools

Python code lives in [COMPANY: repository] (AR-15); if a Python tool is in no repository, tell the Manager, because the tool doc needs a source of truth. Before the day-60 review you push only to feature branches of your owned tool and never merge anything that reaches production yourself (AR-15); until then the Manager or the knowledge holder does the merge and deploy steps. The everyday loop:

1. Create a branch for the change, named with the Jira key (for example `PROJ-171-hts-as-text`, example name).
2. Commit in small steps; each commit message starts with the Jira key.
3. Open a pull request. Branch protection requires a reviewer (the checker) before merge, so the tool enforces maker-checker.
4. After approval, merge and tag the release (for example `v1.5`). The previous tag is the rollback (06 Section 7).
5. Never commit credentials, connection strings with passwords, or data extracts. Settings that differ per environment go in a config file; secrets stay in [COMPANY: password vault].

### 5.2 SharePoint version history for Excel and Access files

SharePoint Online document libraries keep major versions by default, so you can view or restore an earlier version of a file from its version history (as of Oct 2026; check https://learn.microsoft.com/en-us/troubleshoot/sharepoint/lists-and-libraries/library-versioning-setting-changes). Treat it as a safety net, not as version control:

- It records saves, not releases, and has no review step. The change request and tool doc say which saved version is the release.
- The library's settings, and whether our tool files live in SharePoint or on a file share, are [COMPANY: confirm the tool library location and its versioning settings]. On a file share, rely on the dated backup copy that the change request requires.
- For VBA, also export the changed modules (.bas, .cls, .frm) before and after, so the checker can compare them as text (06 Section 7). For Access, back up the front-end and the back-end; restoring a back-end loses data entered since the backup. Name released copies with their version, for example `DutyRateLookup_v1.5.xlsm` (example name).

### 5.3 Power Platform and Power BI

- **Canvas apps** keep versions: Apps, select the app, Details, Versions. Restoring creates a new version, which you then publish (as of Oct 2026; check https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/restore-an-app). Save with version notes.
- **Cloud flows** have version history only when they are in a solution; a restored version becomes the latest draft and must be published. Flows outside a solution have none, so export a copy before every edit (as of Oct 2026; check https://learn.microsoft.com/en-us/power-automate/drafts-versioning). For flows and apps in a solution, the unmanaged solution exported from development is the source; Microsoft recommends keeping exported copies in source control (4.3).
- **Power BI:** a .pbix is a single file, so keep each released copy with its version in the name in [COMPANY: report source location]. Fabric Git integration can connect a workspace to a Git repository; Power BI reports and semantic models are listed as preview items (as of Oct 2026; check https://learn.microsoft.com/en-us/fabric/cicd/git-integration/intro-to-git-integration). [COMPANY: confirm whether the team uses it].

### 5.4 Version numbers and the change log in the tool doc

- Use one simple scheme and say in the tool doc which: for example v1.4 to v1.5 for a change that keeps inputs and outputs the same, v2.0 when inputs, outputs or layouts change in a way others depend on ([COMPANY: confirm the team's convention]). Every release gets a new number, visible where users look: a title cell, the app screen, the file name, the Git tag.
- The tool doc's change history (Section 11) gets one line per release: version, date, change, change request (CR) or Jira key, by, checked by. It must match the version table in the change request (06 Section 2).
- The tool doc also records the tool's **platform path**: the database objects it reads or writes, its connections, the account it runs as, its schedule and its server location (tool doc Sections 2, 5 and 8; `docs/templates/knowledge/data-platform-map.md`). This is part of the day-60 owned-tool evidence.

**How this applies to our work:** in W6, find where your owned tool's real current version lives and whether other copies exist ("which one is real?" is a tool-doc interview question). Research: version briefs the same way (v1.0, then v1.1 after an amendment) so Standard Cost always knows which version its model used. On e2open the vendor controls versions of the system; you control versions of requirements, data maps and test cases.

## 6. Testing

Test vocabulary here follows the ISTQB Foundation syllabus CTFL v4.0.1 and the ISTQB glossary (https://www.istqb.org/certifications/certified-tester-foundation-level-ctfl-v4-0/; https://glossary.istqb.org).

### 6.1 Test levels

| Test level | Focuses on | V-model pair | Owned-tool example (Part 10) | e2open example |
|---|---|---|---|---|
| Component testing (often called unit testing) | Individual components | Detailed design | The date filter in one VBA procedure | The partner's build tests |
| Component integration testing | Interfaces and interactions between components | Architecture design | The workbook and the database view it reads | Configured modules working together |
| System testing | The system as a whole meeting its specified requirements | System requirements or functional design | The whole tool against the story's acceptance criteria | The GTM configuration end to end |
| System integration testing | Interactions between systems | Architecture design | The tool's output read by the next tool, or a broker test file (sent through the Senior) | SIT with Oracle EBS, brokers, the warehouse |
| Acceptance testing | Deciding whether to accept the system | Business requirements | A Research user confirms the lookup answers Pricing's question | UAT and sign-off |

Builders usually run the first two levels, testers and BSAs the system levels, and business users acceptance. UAT is a form of acceptance testing, done by the intended users; ISTQB also lists operational, contractual and regulatory acceptance testing, and alpha and beta testing.

### 6.2 Test types

- **Functional and non-functional:** what it does (the right rows, the right rate) and how well it does it (performance, usability, security; for example "a normal user cannot edit the rate table").
- **Black-box and white-box:** tests derived from the requirements without looking at the code (most of yours), or from the code's structure (for example making sure each branch of an IF statement runs).
- **Change-related testing:** **confirmation testing** (re-testing) checks that a fixed defect no longer causes the failure; **regression testing** checks that a change has not broken unchanged areas. When both are needed, confirmation comes first. For a tool change the strongest regression test is the one in 06 Section 6: run the old and new versions on the same full input and confirm that the only differences are the intended ones.
- **Smoke test:** a quick check that the main functions work before planned testing starts. The same idea, run right after a release, opens the post-release check (7.6).

### 6.3 Test cases and evidence

A test case sets out the preconditions, inputs, actions, expected results and postconditions. The rules in 05 apply to every test you run:

- Write the expected result **before** you run the test, with exact values worked out independently: by hand, from the brief, from the model. "Works correctly" is not an expected result.
- Record the actual result in words and values, even on a pass. Save evidence named `[Test case ID]_[YYYY-MM-DD]_[initials]` in [COMPANY: UAT evidence folder], and keep output files unedited.
- "Test evidence" is our working term (it is not an ISTQB glossary term): the saved record that a test ran and what happened, meaning the case, the data used, expected and actual results, pass or fail, who ran it and when, plus the output files or screenshots.
- The checker reviews the test cases before you run them, and the evidence before release.

### 6.4 Defects, retest and regression

A defect is a flaw in a work product that means it does not meet its requirements. The change request's risk rating (06 Section 5) sets how much testing is enough. Every change has your tests, including an old-versus-new regression test, and the checker's review; Medium runs the regression on a full real input set; High adds a parallel run for one full cycle or a rollback rehearsal. When a test fails:

1. Log a defect the same day, linked to the test case, with a severity from 05 Section 9 (Critical, High, Medium, Low).
2. After the fix, re-run the failed case (confirmation), then the related cases and the old-versus-new comparison (regression).
3. Close the defect only when both pass, and record the root cause.

**How this applies to our work:** your W8 change request needs test evidence (A60-4, B60-4): at least the intended change, a boundary or error case, and the old-versus-new regression. Research tests a rate change on both sides of the effective date (05 TS-04); Standard Cost ties duty per unit to the model, and landed cost per unit to a hand calculation within $0.01 (05 TS-03). On e2open you will write and run UAT cases from the starter scenarios in 05 Section 7.

## 7. Change control and release

### 7.1 The change request

Every change to a tool, a configuration or production data goes through a change request (`docs/templates/bsa/06-change-request.md`), whatever its size. It holds the before and after, the impact assessment, the risk rating, the test evidence, the rollback plan, the implementation steps, the maker-checker approval and the communication. For day 60 (A60-4, B60-4) your W8 change request must name the environments, attach the test evidence and give the rollback.

### 7.2 Who does what

| Role | Who | Never |
|---|---|---|
| Maker | You, as tool owner or assigned learner | Checks or approves their own change |
| Checker | The Manager for tool changes; the Senior for data and report items in their area and for team database objects | Signs off without seeing the diff, the evidence and the rollback plan |
| Approver | The Manager, plus the system owner for a system the team does not own | Approves without a checker review |
| Implementer | Before day 60: the Manager or the current knowledge holder. After day 60, if granted: you, for your owned tool only | Deploys an unapproved or untested version |

Oracle EBS cost updates are not tool changes and stay outside your change rights in the first 90 days (`docs/04-access-request-checklist.md` rule 4).

### 7.3 Change types

ITIL 4 calls this practice change enablement (older material says change management or change control) and names three change types, which 06 uses. ITIL 4 is still offered alongside the newer ITIL (Version 5), released in 2026 (as of Oct 2026; check https://www.peoplecert.org/news-and-announcements/itil-version-5-explained).

- **Standard:** low risk, pre-authorized, well understood and fully documented. Ours: only changes on [COMPANY: standard change list], and maker-checker still applies every time.
- **Normal:** assessed, authorized and scheduled through the process. Most of your changes.
- **Emergency:** must be made as soon as possible, for example to stop wrong data reaching a broker or Finance now. The Manager gives a verbal go-ahead, the checker reviews the same day, and the change request is completed within 1 working day (06). A workaround that stops the damage often turns an emergency into an expedited normal change (06 filled example).

### 7.4 Release checklist

- [ ] The checker and approver have signed off on the Jira issue, and no Critical or High defects are open. The window is agreed (for Medium and High risk: not during a cost cycle, and not within [COMPANY: n] working days of a tariff effective date; 06 Section 5).
- [ ] A backup of the current production version exists, and its location is verified (by whom, when). The release is exactly the tested version (same file, tag or solution version), with environment settings switched to production values: paths, connections, environment variables, deployment rules.
- [ ] Users and downstream receivers have been told (06 Section 11).
- [ ] The rollback plan is written, with its trigger and decider; someone is named for the post-release check, and the maker is available for the first run.

### 7.5 The rollback plan

A rollback plan answers six questions (06 Section 8): what result triggers it, who decides, the steps, where the verified backup is, how long it takes, and how the outputs the faulty version already produced are found and corrected. The last question matters most in trade work: a wrong broker file or cost input does not disappear when you restore the old version. If a rollback is impossible (after a data conversion, for example), say so and plan a rehearsed fix-forward instead: a tested correcting change, ready before you release. Roll back first and investigate second; never debug in production.

### 7.6 Telling users and the post-release check

- **Before:** what changes, when, what users must do (often nothing), who to ask (wording in 06 Section 11).
- **After:** the new version is live, the first run was checked, and problems are reported quoting the CR ID.
- **Post-release check** (06 Section 12): the first production output matches the expected result and its counts tie to the input; the log or run history is clean; the production connection and account work; downstream receivers and users confirm; the tool doc, Tool Inventory and SOP are updated; the CR is closed with evidence. Before day 60 you do the read-only parts yourself.

### 7.7 ITGC and SOX awareness

Section 404 of the Sarbanes-Oxley Act (SOX) applies to companies that file annual reports with the SEC (issuers). Under the auditing standard for internal control over financial reporting, auditors consider IT general controls (ITGCs), including controls over program changes (PCAOB AS 2201, https://pcaobus.org/oversight/standards/auditing-standards/details/AS2201). Whether this applies to us, and to which tools, is [COMPANY: confirm whether SOX/ITGC applies] and [COMPANY: confirm with Internal Audit which tools are in ITGC scope]. A tool that feeds standard cost or financial reporting is the likeliest candidate.

In change management, auditors usually look for approval before the change, test evidence, approval before production, segregation of duties (whoever builds a change does not move it to production) and retained evidence, usually the change ticket. Segregation of duties is the hard part in a small team. Before day 60 the Manager approves and often also deploys; after day 60 you may deploy your own approved change to your owned tool (7.2). Where segregation is not possible, auditors may accept a compensating control, such as an independent review of what was deployed; for any tool in ITGC scope, ask Internal Audit what they accept and whether someone other than the maker must deploy ([COMPANY: deployment rule for ITGC-scope tools]). Practise the habits either way: the approval on the ticket (not only in a Teams chat), saved test evidence, a rollback plan, and a checker who sees the post-release check.

**How this applies to our work:** before day 60 your change requests stop after testing in the test copy, and the Manager implements (the note in 06's filled example). Hire B: a change to a cost tool touches standard cost, so expect Medium or High risk and a release window outside the cost cycle. On e2open the project runs its own change and release process; your part is to test and collect sign-off, not to deploy.

## 8. Support and operations

### 8.1 Incident, problem, change

ITIL 4 defines an **incident** as "an unplanned interruption to a service or reduction in the quality of a service" and a **problem** as "a cause, or potential cause, of one or more incidents". A problem that has been analysed but not resolved is a **known error**. Log incidents and problems as Jira bugs (07 bug template); the fix becomes a change request.

| Term | The question | Goal | Trade example |
|---|---|---|---|
| Incident | Something is broken or wrong now | Restore service and limit the damage | The broker file did not arrive this morning |
| Problem | Why does it keep happening? | Find and remove the cause | The file fails whenever the extract runs late |
| Change | We are adding, modifying or removing something | Assess, authorize, schedule, release safely | Move the job after the extract and add an arrival check |

### 8.2 Monitoring scheduled jobs

Our tools fail silently: a job that did not run means a broker files with yesterday's codes (`docs/primers/trade-systems-gtm-e2open-primer.md` 4.3). For each scheduled piece of your tool, the tool doc names where to look, what healthy looks like and who is told when it fails. Good monitoring compares a count or total with an expected value and tells a named person; "someone looks when they remember" is not monitoring.

| What runs | Where to look | Healthy looks like | Notes (as of Oct 2026; check the link before relying on it) |
|---|---|---|---|
| Python script run by Windows Task Scheduler on the server | The task's Last Run Result column and History tab | Ran on time; success result; output file with the expected row count | https://learn.microsoft.com/en-us/troubleshoot/windows-server/system-management-components/troubleshoot-scheduled-tasks-not-running |
| SQL Server Agent job | SSMS Job Activity Monitor and the job's history | Succeeded; normal duration | You may lack the rights to see it: ask the Senior ([COMPANY: who monitors team database jobs]); https://learn.microsoft.com/en-us/ssms/agent/monitor-job-activity |
| Power Automate cloud flow | The flow's run history | Every run succeeded; nothing skipped | Run history is kept about 28 to 30 days, so save the evidence you need; a flow that fails continuously for 14 days is turned off (as of Oct 2026; check https://learn.microsoft.com/en-us/power-automate/limits-and-config) |
| Power BI scheduled refresh | The semantic model's (dataset's) refresh history in the service | The last refresh succeeded on time | Failure alerts go to [COMPANY: who gets refresh-failure emails]; gateway checks in the data platform primer |
| Files from brokers or extracts | The landing folder and the load log | Arrived on time; header or trailer counts match | Every interface needs counts, totals and a named checker (GTM primer 3.4) |

**Runbooks.** A runbook is the step-by-step guide to running and recovering a tool. For our tools the tool doc is the runbook: Section 6 (how to run it), Section 7 (how it breaks and known fixes), Section 2 (trigger and schedule) and Section 8 (dependencies). It is good enough when the other hire can run the tool and fix its common failures from the page alone (the tool doc's peer test). Update it with every change request and after every incident.

### 8.3 When something breaks: the first hour

- [ ] If wrong data is going out, tell the Manager at once. The Manager or the knowledge holder pauses the job if the tool doc says that is safe. Before day 60 you never pause, re-run or fix anything in production yourself.
- [ ] Find out who received the bad output (broker, Finance, Oracle EBS, report users) and since when, and log a Jira bug with evidence: run date, version, error text, counts.
- [ ] The Manager decides the response (the tool doc's known fix, a rollback, a workaround or an emergency change) and who carries it out.
- [ ] Afterwards: root cause (`docs/primers/business-systems-analysis-primer.md` 6.3), a problem record if it can recur, and tool doc Section 7 updated.

**How this applies to our work:** in W6, find out for your owned tool what runs on a schedule, under which account, and who would notice a failure; gaps go into the tool doc and the tool's Jira backlog. Hire A: a failed rate or classification job can reach a broker. Hire B: a failed refresh or load shows up weeks later as unexplained PPV. At e2open go-live, hypercare is intense incident and problem work against an agreed issue list.

## 9. SDLC by tool type

### 9.1 Build and test

| Tool type | Where you build | Test copy or environment | How you test |
|---|---|---|---|
| Python on the server | Your laptop or a dev folder, on a branch | Test inputs and config; outputs to a test folder, never the broker SFTP or an Oracle EBS interface | Unit tests where they exist; old-versus-new comparison on a full real input; read the log |
| Excel VBA | A "_TEST" copy of the workbook | The same copy, outputs to a test folder | Debug, Compile VBAProject; test cases; old-versus-new comparison; open it the way users do (macro settings, trusted location) |
| Access | Copies of the front-end and the back-end | Test front-end linked to the test back-end | SQL of changed queries before and after; every form, report and linked file that uses a changed table |
| Power Apps | [COMPANY: dev environment] or a copy of the app | Test environment, or the copy with test data | Test as a normal-role user, not as the owner; check connections and permissions |
| Power Automate | Dev environment, or a copy of the flow kept off between tests | Test inputs and test recipients | Read each test run in the run history; switch the copy off afterwards so it cannot run twice |
| Power BI | Power BI Desktop, on a copy of the .pbix | Development or test workspace (or pipeline stage) | Totals tie to a SQL query on the same data; check filters, measures and row-level security as a viewer sees them |

### 9.2 Release and roll back

| Tool type | Versions kept in | How it is released | How you roll back | Watch for |
|---|---|---|---|---|
| Python on the server | Git tags in [COMPANY: repository] | Merge after review, tag, deploy to the server folder ([COMPANY: who deploys to the server]) | Redeploy the previous tag; re-run if needed | Pinned packages; config per environment; the account the scheduled task runs as |
| Excel VBA | SharePoint version history plus dated backups; exported modules | Replace the production file in the tool library | Restore the previous version or the backup | Users with the file open or with old copies saved locally; links to other workbooks |
| Access | Dated backups of the front-end and back-end | Copy the new front-end to production and relink it to the production back-end | Restore the old front-end; restoring the back-end loses newer data | Users with the database open; table design changes |
| Power Apps | App versions (or solution versions) | Publish, or import the managed solution | Restore the previous version, then publish | Production connections and permissions |
| Power Automate | Solution version history, or an exported copy | Import the solution or update the flow, then turn it on | Restore and publish the previous version, or import the exported copy | Whose account the connection uses; run-only users; a trigger firing on old items |
| Power BI | Versioned .pbix copies (or Git, if used) | Deploy through the pipeline, or publish to the production workspace and update the app | Republish the previous .pbix | Gateway data source and credentials; refresh schedule; app audience |

Team database objects (tables, views, procedures, jobs) are left out on purpose: until day 90 they change only through the Senior. If your owned tool depends on one, you draft the change request, the Senior is checker, and you never deploy it yourself (rule 5 in 1.3).

### 9.3 Your owned-tool SDLC profile (W6 output)

Copy this table into OneNote, fill it before the W6 supervised run, and carry each answer into the tool doc.

| Question | Your tool | Tool doc section |
|---|---|---|
| Technology and version; where the production version lives, and which copy is the real one | | 1, 8 |
| Where your test copy lives (from W6), and how it is isolated (4.5) | | 8 |
| Where versions are kept: Git, SharePoint history, backups, app versions | | 11 |
| How a release happens today and who does it; how to roll back, and how long it takes | | 7, 9 |
| Platform path: database objects, connections, the account it runs as, schedule, server location | | 2, 5, 8 |
| Where to look when it fails, and who is told | | 7 |
| Phases the last real change went through, and the gaps | | 12 |

## 10. Worked example: an as-of date for the Duty Rate Lookup

### 10.1 The tool and the request

Everything here is fictional: the tool, the object names, the rates and both actions; the dates show the day-60 rule at work in W8. The **Duty Rate Lookup** (Tool Inventory row T-99, example) is an Excel VBA workbook, `DutyRateLookup.xlsm` (example name), in [COMPANY: tool library on SharePoint]. A user enters an item and a country of origin; the workbook queries the team database view `rpt.v_duty_rate` (example name) through a read-only connection under the user's own login and lists the rate rows in effect today. Rate rows are loaded with effective dates from checked Tariff-Impact Briefs under their own change requests (07, the rewritten bad example). The tool lists rates; whether they stack comes from the brief. In this example Hire A owns the tool, and v1.4 is in production.

Mon 12/7: Pricing asks which rates will apply to PART-A from Country X once Action X-1 takes effect on 2027-03-01. The Action X-1 rows are already in the view, dated from 2027-03-01, but the tool only answers "as of today". The request: let the user choose an as-of date.

### 10.2 From intake to release

| Step | Phase | What happens | Template |
|---|---|---|---|
| 1 | Intake and requirements | Hire A logs a story, "Custom Tools: add an as-of date to the Duty Rate Lookup", linked to the Action X-1 epic: Normal change, P2, five acceptance criteria in Given/When/Then (10.3). The Manager confirms the definition of ready | 01, 07 |
| 2 | Design | Before: the query uses today's date. After: a new As-of date cell (named range `AsOfDate`, example name), today when left blank, used by the query. Not changing: the view, the output layout, the connection. No team database object changes, so the Senior is not involved; had the view needed a new column, that would be a separate change with the Senior as checker | 06 Sections 2 and 4 |
| 3 | Risk | Likelihood 2 x Impact 2 = 4, Medium: a wrong rate would reach Pricing's numbers, though internally and checked before use. Medium needs a full regression run, users told in advance, and a window outside any cost cycle and not within [COMPANY: n] working days of a tariff effective date: Hire A checks the cost calendar with Hire B | 06 Section 5 |
| 4 | Build | In `DutyRateLookup_TEST.xlsm` (example name) in [COMPANY: test-copy location for the owned tool]. It only reads, so it reads the production view with Hire A's personal login. Modules exported before and after; Option Explicit; compiles clean | 06 Section 7 |
| 5 | Test | The Manager reviews the test cases first; Hire A runs T1 to T5 (10.3) and saves the evidence under the naming rule | 05, 06 Section 6 |
| 6 | Review | Wed 12/9 tool coaching: the Manager checks the module diff, the evidence, the impact rows and the rollback plan, then approves on the Jira issue | 06 Section 10 |
| 7 | Release | Hire A has no production write access before day 60, so the Manager implements on Thu 12/10, after Hire A's "before" message on Wed 12/9: confirm v1.4 is in version history and a dated backup exists, replace the file with the tested v1.5, open it as a user | 06 Sections 8, 9, 11 |
| 8 | Post-release check | Hire A, read-only, runs T1 and T2 on the production file with a Research user, confirms the version cell says v1.5, and sends the "after" message | 06 Section 12 |
| 9 | Close | Tool doc v1.5: change-history line, the new input in Section 6, the as-of rule in Section 10 as a business rule for e2open; Tool Inventory row updated; one Anki card; CR closed | Tool doc; 08 at the end of the epic |

The query after the change (example names; `@as_of` is the as-of date, today when blank):

```sql
SELECT item_number, hts_number, origin_country, rate_type, rate_pct, effective_from, effective_to
FROM rpt.v_duty_rate
WHERE item_number = @item
  AND origin_country = @origin
  AND effective_from <= @as_of
  AND (effective_to IS NULL OR effective_to >= @as_of);  -- effective_to = last day the rate applies
```

### 10.3 Acceptance criteria and test evidence

Test data (fictional): PART-A from Country X has three rate rows: the base rate, 2.5% from 2020-01-01 with no end date; Action X-0, an additional 10% from 2025-04-01 to 2026-12-31; Action X-1, an additional 25% from 2027-03-01 with no end date. One criterion in full, 07 style: "AC2 Given PART-A from Country X and an as-of date of 2027-03-01, when the user runs the lookup, then it lists the base row and the Action X-1 row, each with its effective dates." The boundary tests T1 and T3 catch off-by-one date errors (a `<` where `<=` was meant) that a happy-path test misses. Actual results are written as values, even on a pass (05 Section 10).

| Test ID | What is tested | Input | Expected | Actual | Result |
|---|---|---|---|---|---|
| T1 | AC1 boundary: the day before Action X-1 | PART-A, Country X, as-of 2027-02-28 | 1 row: base 2.5% | 1 row: base 2.5% | Pass |
| T2 | AC2: the effective date itself | Same, as-of 2027-03-01 | 2 rows: base 2.5%, Action X-1 25% | 2 rows: base 2.5%, Action X-1 25% | Pass |
| T3 | AC3 boundary: an end date | Same, as-of 2026-12-31, then 2027-01-01 | 2 rows (base, Action X-0), then 1 row (base) | 2 rows (base 2.5%, Action X-0 10%), then 1 row (base 2.5%) | Pass |
| T4 | AC4 regression: blank as-of matches v1.4 | All 1,240 item and origin pairs in the view (example count), as-of blank, in v1.4 and v1.5 | Identical output files | 1,240 pairs in each file; 0 differences (file compare) | Pass |
| T5 | AC5 error case | As-of 2027-02-30 | Message "Enter a valid date"; no query runs | Message "Enter a valid date" shown; output area empty, no rows returned | Pass |

### 10.4 Rollback, and what changes after day 60

- **Rollback plan:** the trigger is any blank-as-of lookup that differs from v1.4, or a user reporting a wrong rate. The Manager decides. Steps: restore v1.4 from version history (or the dated backup), tell users, and ask them to redo any lookup they saved from v1.5. About 5 minutes. Not needed here: the post-release check passed.
- **After day 60:** if the Manager grants production change rights at the day-60 review, Hire A implements the next change to this tool; the Manager stays checker, and every other step is the same.
- **On e2open:** rate lookups may come from e2open's trade content and duty calculation [COMPANY: confirm]. The as-of rule is a business rule hidden in the tool, so it goes into the tool doc's e2open section and the project requirements, and a UAT case like TS-04 in 05 proves e2open handles it.

## 11. Self-check questions

| No. | Question | Where to check |
|---|---|---|
| 1 | Name the eight SDLC phases and the team template you use in each. | 2.1 |
| 2 | List the five rules that run through this primer. Which one changes at the day-60 review, and how? | 1.3, 7.2 |
| 3 | Pair each V-model development phase with its test level, using your W8 change as the example. | 3.1, 6.1 |
| 4 | Name the three Scrum accountabilities, the five events, and the commitment that goes with each artifact. | 3.2 |
| 5 | In a vendor implementation, what is the difference between SIT and UAT, and what is decided at cutover? | 3.5 |
| 6 | You set up a test copy of an Excel tool that writes a broker file. What must you change before you run it? | 4.5 |
| 7 | Your test needs supplier cost data. What do you mask, and where may the test data live? | 4.6 |
| 8 | A flow works in test but fails after release. Which account and connection questions do you ask first? | 4.7, 9.2 |
| 9 | Why is SharePoint version history a safety net and not version control? | 5.2 |
| 10 | What goes into the tool doc's change history and platform path for each release? | 5.4 |
| 11 | What is the difference between confirmation testing and regression testing, and which runs first? | 6.2, 6.4 |
| 12 | Who are the maker, checker, approver and implementer for your W8 change, before and after day 60? | 7.2 |
| 13 | A faulty version sent a broker file for two days before you rolled back. What must the rollback plan still cover? | 7.5 |
| 14 | Incident, problem or change: the cost refresh failed last night; it fails every month-end; you move its schedule. | 8.1 |
| 15 | For your owned tool, where do you look to know it ran last night, and who is told if it did not? | 8.2, 9.3 |
| 16 | In Part 10, why did the Manager implement the release, and what changes after day 60? | 10.2, 10.4 |
