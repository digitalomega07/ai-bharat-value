import importlib.util
import unittest
from decimal import Decimal
from pathlib import Path

MODULE_PATH = Path(__file__).resolve().parents[1] / "tools" / "financial_rigor.py"
SPEC = importlib.util.spec_from_file_location("financial_rigor", MODULE_PATH)
financial_rigor = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(financial_rigor)


class FinancialRigorTests(unittest.TestCase):
    def test_decimal_expression(self):
        self.assertEqual(financial_rigor.exact_calc("0.1 + 0.2"), Decimal("0.3"))

    def test_market_cap_difference(self):
        self.assertEqual(financial_rigor.pct_difference("100", "100"), Decimal("0"))

    def test_rejects_code(self):
        with self.assertRaises(ValueError):
            financial_rigor.exact_calc("__import__('os')")


if __name__ == "__main__":
    unittest.main()

