import argparse
import sys

parser = argparse.ArgumentParser(description="test")

parser.add_argument(
    "--strict",
    action="store_true"
)

args = parser.parse_args()

if args.strict:
    print("sys.exit(0)")
    sys.exit(0)