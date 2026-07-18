#!/usr/bin/env python3
# simple CLI that prints a stub catalogue in JSON
import json
from pathlib import Path

def main():
    cat = {
        "commonwealth":{
            "legislation":[{"source":"https://www.legislation.gov.au/"}]
        },
        "state_nsw":{
            "legislation":[{"source":"https://www.legislation.nsw.gov.au/"}]
        }
    }
    print(json.dumps(cat, indent=2))

if __name__ == "__main__":
    main()
