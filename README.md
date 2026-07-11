# AI Bharat Value

An India-first, AI-assisted public-equity research framework for Codex and Claude Code.

AI Bharat Value turns an open-ended company question into a repeatable, source-backed research process built for the Indian market. It is designed around business quality, capital allocation, governance, forensic accounting, valuation, and thesis falsification.

> Research and education only. This project does not provide personalized investment advice, portfolio recommendations, or assured returns. Verify every material fact with primary sources before relying on it.

## Why an India-specific framework?

Indian public markets require checks that generic global templates often miss:

- promoter ownership, pledging, dilution, warrants, and preferential allotments;
- related-party transactions and group-company dependencies;
- standalone versus consolidated financial statements;
- working-capital intensity, contingent liabilities, and capital-work-in-progress;
- auditor qualifications, resignations, and key audit matters;
- NSE/BSE announcements, SEBI disclosures, credit-rating rationales, and annual reports;
- cyclicality, commodity exposure, government policy, and PSU-specific capital allocation;
- point-in-time data discipline to prevent look-ahead and survivorship bias.

## Architecture

| Layer | Purpose |
|---|---|
| Skills | Seven consistent workflows for company research, screening, forensics, earnings, industries, thesis tracking, and portfolio risk review |
| Evidence | Primary-source hierarchy, citation rules, as-of dates, and explicit confidence labels |
| Tools | Exact-decimal calculations, cross-source comparison, report checks, and reproducible tests |

## Included workflows

| Skill | Use it for |
|---|---|
| `india-company-research` | Full company initiation with business, moat, governance, financials, forensics, and valuation |
| `india-quality-screen` | Fast elimination screen using sector-aware quality and governance tests |
| `india-forensic-accounting` | Accounting-quality, promoter, auditor, working-capital, and related-party review |
| `india-earnings-review` | Quarterly or annual result review against the prior thesis and disclosed expectations |
| `india-industry-funnel` | Map an Indian industry, screen the listed universe, and identify candidates for further diligence |
| `india-thesis-tracker` | Maintain prove/kill conditions and detect thesis drift after investment research |
| `india-portfolio-risk-review` | Educational concentration, correlation, liquidity, and thesis-risk review without personalized allocation advice |

## Evidence hierarchy

Use the highest available source and preserve the document date:

1. NSE/BSE corporate announcement or SEBI filing
2. Company annual report, audited results, investor presentation, or earnings-call transcript
3. Credit-rating rationale and statutory disclosures
4. Government, regulator, or industry-body publication
5. Reputable financial database or newswire
6. Other secondary commentary, clearly labelled

Material numbers should have two sources where practicable. When sources conflict, retain both values, explain the accounting perimeter or timing difference, and prefer the primary filing.

## Quick start

```bash
git clone https://github.com/SoumyaAnand2219/ai-bharat-value.git
cd ai-bharat-value
./scripts/install-codex-skills.sh
```

Restart Codex, then ask:

```text
Use india-company-research to research Asian Paints as of 31 March 2026.
Use india-quality-screen to screen the Nifty Midcap 100 using point-in-time data.
Use india-forensic-accounting to review the latest five annual reports of a listed company.
Use india-earnings-review to analyse the latest quarterly results against the previous thesis.
```

For Claude Code, the canonical workflow files are available under `skills/`.

## Research output standard

Every substantive report must state:

- company name, NSE/BSE symbol, reporting perimeter, currency, and as-of date;
- sources beside material claims;
- reported, adjusted, estimated, and inferred figures separately;
- data gaps and confidence levels;
- bull/base/bear assumptions and the variables that matter most;
- thesis-proving and thesis-killing evidence;
- a clear research verdict: `Pass`, `Watch`, `Needs verification`, or `Reject for further work`.

Verdicts describe research priority, not a direction to buy, sell, or hold.

## Validation tools

```bash
python3 tools/financial_rigor.py market-cap --price 2500 --shares 95.9e7 --reported 2.3975e12
python3 tools/financial_rigor.py ratio --numerator 1500 --denominator 10000 --scale 100
python3 tools/financial_rigor.py cross-validate --field revenue --values '{"annual_report":"10000","exchange_results":"10020"}'
python3 tools/report_check.py reports/example.md
python3 -m unittest discover -s tests
```

The calculator verifies arithmetic, not accounting meaning. The researcher remains responsible for checking units, financial-statement perimeter, exceptional items, and source dates.

## What this project deliberately does not claim

- No historical or future return claim is made.
- A good research score is not evidence of future outperformance.
- AI agents are not independent human analysts and can share correlated errors.
- Exact arithmetic cannot correct an incorrect accounting input.
- Backtests are invalid unless they use point-in-time constituents and information available on each historical date.

## Roadmap

- Point-in-time Nifty 500 universe snapshots
- Sector-specific modules for banks, NBFCs, insurers, REITs, utilities, and commodity businesses
- Filing-to-source audit trail
- Walk-forward research validation with transaction costs and delisted companies
- Example reports that show both successful and failed theses

## License

MIT. See [LICENSE](LICENSE).

