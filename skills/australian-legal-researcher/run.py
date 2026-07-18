#!/usr/bin/env python3
import argparse
import json
from hermes_tools import web_search

def main() -> None:
    parser = argparse.ArgumentParser(description="Australian Legal Researcher")
    parser.add_argument("--query", required=True, help="Search query for law topics")
    parser.add_argument(
        "--jurisdiction",
        default="Commonwealth",
        help="Jurisdiction (state or territory) – defaults to Commonwealth.",
    )
    args = parser.parse_args()

    statute_results = web_search(
        query=args.query,
        domain_filters=["legislation.gov.au", "legislation.nsw.gov.au", "legislation.vic.gov.au"],
        max_results=5,
    )
    case_results = web_search(
        query=f"{args.query} High Court",
        domain_filters=["cases.slaw.com.au"],
        max_results=3,
    )

    output = {
        "jurisdiction": args.jurisdiction,
        "query": args.query,
        "statutes": statute_results[:3],   # take top three statute snippets
        "case_law": case_results[:2],
        "note": "This is a placeholder – replace with full research logic and citations.",
    }
    print(json.dumps(output, indent=2))

if __name__ == "__main__":
    main()
