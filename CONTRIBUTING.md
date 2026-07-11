# Contributing

Contributions are welcome when they improve evidence quality, reproducibility, or India-market coverage.

## Requirements

- Do not publish personal data, confidential research, brokerage statements, or paid research without permission.
- Do not claim assured returns or describe a research verdict as personalized investment advice.
- Cite primary filings for material facts and include an as-of date.
- Keep reported, adjusted, estimated, and inferred figures distinct.
- Add or update tests for deterministic tools.
- Do not add historical performance claims without a complete, independently reproducible methodology.

Run before opening a pull request:

```bash
python3 -m unittest discover -s tests
python3 tools/report_check.py reports/example.md
```

