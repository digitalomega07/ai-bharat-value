#!/usr/bin/env python3
"""Deterministic arithmetic checks for AI Bharat Value."""

import argparse
import ast
import json
from decimal import Decimal, getcontext

getcontext().prec = 34


def dec(value):
    return value if isinstance(value, Decimal) else Decimal(str(value))


def pct_difference(value, reference):
    value, reference = dec(value), dec(reference)
    if reference == 0:
        return Decimal("0") if value == 0 else Decimal("Infinity")
    return abs(value - reference) / abs(reference) * Decimal("100")


def evaluate(node):
    if isinstance(node, ast.Expression):
        return evaluate(node.body)
    if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
        return dec(node.value)
    if isinstance(node, ast.UnaryOp) and isinstance(node.op, (ast.UAdd, ast.USub)):
        value = evaluate(node.operand)
        return value if isinstance(node.op, ast.UAdd) else -value
    if isinstance(node, ast.BinOp) and isinstance(node.op, (ast.Add, ast.Sub, ast.Mult, ast.Div)):
        left, right = evaluate(node.left), evaluate(node.right)
        if isinstance(node.op, ast.Add):
            return left + right
        if isinstance(node.op, ast.Sub):
            return left - right
        if isinstance(node.op, ast.Mult):
            return left * right
        return left / right
    raise ValueError("Only numeric literals and +, -, *, /, parentheses are allowed")


def exact_calc(expression):
    return evaluate(ast.parse(expression, mode="eval"))


def emit(payload):
    print(json.dumps(payload, indent=2, ensure_ascii=False, default=str))


def main():
    parser = argparse.ArgumentParser(description="Exact-decimal financial checks")
    subs = parser.add_subparsers(dest="command", required=True)

    market_cap = subs.add_parser("market-cap")
    market_cap.add_argument("--price", required=True)
    market_cap.add_argument("--shares", required=True)
    market_cap.add_argument("--reported", required=True)
    market_cap.add_argument("--tolerance", default="1")

    ratio = subs.add_parser("ratio")
    ratio.add_argument("--numerator", required=True)
    ratio.add_argument("--denominator", required=True)
    ratio.add_argument("--scale", default="1")

    cross = subs.add_parser("cross-validate")
    cross.add_argument("--field", required=True)
    cross.add_argument("--values", required=True)
    cross.add_argument("--tolerance", default="1")

    calc = subs.add_parser("calc")
    calc.add_argument("--expression", required=True)

    args = parser.parse_args()
    if args.command == "market-cap":
        calculated = dec(args.price) * dec(args.shares)
        difference = pct_difference(calculated, args.reported)
        emit({"calculated": calculated, "reported": dec(args.reported), "difference_pct": difference,
              "passes": difference <= dec(args.tolerance)})
    elif args.command == "ratio":
        denominator = dec(args.denominator)
        if denominator == 0:
            raise SystemExit("denominator cannot be zero")
        emit({"result": dec(args.numerator) / denominator * dec(args.scale)})
    elif args.command == "cross-validate":
        values = {key: dec(value) for key, value in json.loads(args.values).items()}
        if len(values) < 2:
            raise SystemExit("at least two sources are required")
        ordered = sorted(values.values())
        n = len(ordered)
        median = ordered[n // 2] if n % 2 else (ordered[n // 2 - 1] + ordered[n // 2]) / 2
        differences = {key: pct_difference(value, median) for key, value in values.items()}
        tolerance = dec(args.tolerance)
        emit({"field": args.field, "values": values, "median": median, "difference_pct": differences,
              "passes": all(value <= tolerance for value in differences.values())})
    else:
        emit({"result": exact_calc(args.expression)})


if __name__ == "__main__":
    main()

