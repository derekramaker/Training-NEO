# How trade data flows, and what changes with e2open

Narration script (107 s). Edit video/v2-trade-data-flow/script.yaml and rebuild.

## title

- Trade data makes a round trip: out to the brokers, and back to us as entries.
- Here is that trip, and what e2open changes.

## oracle

- It starts in Oracle, our main business system for items, purchase orders and standard costs.
- New and changed items flow on to the trade system.

## as400

- The AS400 trade system adds what customs needs to know.
- Each item gets a tariff code per country, its origin, and flags for the US-Mexico-Canada Agreement.
- Codes and origin get maker-checker review: one person prepares, a second person checks.

## product-file

- A scheduled batch job, often nightly, builds a product file for each broker.
- The brokers use it to declare our goods to customs.
- The last row, the trailer, holds counts and totals that prove the file is complete.
- But failures are usually silent: if it does not run, brokers file with yesterday's codes.

## entries

- After filing, the brokers send back entry data, line by line.
- Each line is matched to one of our items.
- It then feeds broker audits, the actual duty paid, and Power BI reports.

## e2open

- In a project expected to start in January, e2open replaces the AS400.
- The same data moves into e2open's Global Trade Management system.
- For your own process, you write the as-is doc: how it really works today.
- And the data map: where each field goes in e2open.
- Then you help clean the data and test, so nothing is lost in the move.

## remember

- Remember: every filing and every report is only as good as this chain.
- Next, read sections three to five of the Trade systems primer.
- In Anki: Units one and two now, and Unit seven from week ten.
