import argparse
import sys
from tabulate import tabulate

from services.data_loader import load_data
from reports.average_gdp import AverageGDPReport


REPORTS = {
    "average-gdp": AverageGDPReport,
}


def parse_args():
    parser = argparse.ArgumentParser(description="Macroeconomic data reports")
    parser.add_argument("--files", nargs="+", required=True)
    parser.add_argument("--report", required=True)
    return parser.parse_args()


def main():
    args = parse_args()

    if args.report not in REPORTS:
        print(f"Unknown report: {args.report}")
        sys.exit(1)

    try:
        data = load_data(args.files)
    except FileNotFoundError as e:
        print(str(e))
        sys.exit(1)

    report_class = REPORTS[args.report]
    report = report_class(data)

    result = report.generate()

    print(tabulate(result, headers="keys", tablefmt="grid"))


if __name__ == "__main__":
    main()
