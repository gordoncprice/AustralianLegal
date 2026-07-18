#!/usr/bin/env python3
import argparse,json

def main():
    parser = argparse.ArgumentParser(description="Reviewer CLI")
    parser.add_argument("--input", required=True)
    args = parser.parse_args()
    with open(args.input) as f:
        data=json.load(f)
    # Very simple stub: add a warning if source URLs are not listed.
    warnings=["Missing source verification" if 'statutes' not in data else None]
    data['review']={"warnings":warnings}
    print(json.dumps(data, indent=2))

if __name__=="__main__": main()
