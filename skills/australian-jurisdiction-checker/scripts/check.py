#!/usr/bin/env python3
import argparse,json

def main():
    parser = argparse.ArgumentParser(description="Jurisdiction checker")
    parser.add_argument("--question", required=True)
    args = parser.parse_args()
    q=args.question.lower()
    if "corporate" in q or "company" in q:
        j=["CTH"]
    elif "employment" in q:
        j=["NSW","VIC"]
    else:
        j=[]
    print(json.dumps({"jurisdictions":j,"certainty":"high"}))

if __name__=="__main__": main()
