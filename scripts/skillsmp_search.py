#!/usr/bin/env python3
"""
Search SkillsMP and print results for selection.
"""

import argparse
import json
import os
import sys
import urllib.parse
import urllib.request

API_URL = "https://skillsmp.com/api/v1/skills/ai-search"
DEFAULT_HEADERS = {
    "Accept": "application/json, text/plain, */*",
    "Origin": "https://skillsmp.com",
    "Referer": "https://skillsmp.com/",
    "User-Agent": "skillsmp-installer/1.0",
}


def build_request(query, api_key):
    params = urllib.parse.urlencode({"q": query})
    url = "{}?{}".format(API_URL, params)
    headers = dict(DEFAULT_HEADERS)
    headers["Authorization"] = "Bearer {}".format(api_key)
    return urllib.request.Request(url, headers=headers)


def fetch(query, api_key, timeout):
    request = build_request(query, api_key)
    with urllib.request.urlopen(request, timeout=timeout) as response:
        return response.read()


def simplify_results(payload):
    results = []
    items = payload.get("data", {}).get("data", [])
    for item in items:
        skill = item.get("skill") or {}
        results.append(
            {
                "name": skill.get("name"),
                "author": skill.get("author"),
                "description": skill.get("description"),
                "githubUrl": skill.get("githubUrl"),
                "skillUrl": skill.get("skillUrl"),
                "score": item.get("score"),
                "id": skill.get("id"),
            }
        )
    return results


def print_text(results):
    for index, item in enumerate(results, 1):
        name = item.get("name") or "<unknown>"
        author = item.get("author") or "<unknown>"
        description = (item.get("description") or "").strip().replace("\n", " ")
        score = item.get("score")
        github = item.get("githubUrl") or ""
        skill_url = item.get("skillUrl") or ""
        print("{}. {} by {}".format(index, name, author))
        if score is not None:
            print("   score: {}".format(score))
        if description:
            print("   description: {}".format(description))
        if github:
            print("   github: {}".format(github))
        if skill_url:
            print("   skill: {}".format(skill_url))
        print("")


def main():
    parser = argparse.ArgumentParser(description="Search SkillsMP skills by keyword.")
    parser.add_argument("--query", required=True, help="Search query string.")
    parser.add_argument(
        "--format",
        choices=["text", "json"],
        default="text",
        help="Output format for results.",
    )
    parser.add_argument("--timeout", type=int, default=30, help="Request timeout (s).")
    args = parser.parse_args()

    api_key = os.getenv("SKILL_MAP_API_KEY", "").strip()
    if not api_key:
        print("ERROR: SKILL_MAP_API_KEY is not set.", file=sys.stderr)
        sys.exit(2)

    try:
        raw = fetch(args.query, api_key, args.timeout)
    except Exception as exc:
        print("ERROR: request failed: {}".format(exc), file=sys.stderr)
        sys.exit(1)

    try:
        payload = json.loads(raw.decode("utf-8"))
    except Exception as exc:
        print("ERROR: failed to parse JSON: {}".format(exc), file=sys.stderr)
        sys.exit(1)

    if not payload.get("success"):
        if args.format == "json":
            print(json.dumps(payload, ensure_ascii=True, indent=2))
        else:
            print("SUCCESS: false. No results or request failed.")
        sys.exit(3)

    results = simplify_results(payload)
    if not results:
        if args.format == "json":
            print(json.dumps({"success": True, "results": []}, ensure_ascii=True, indent=2))
        else:
            print("No results.")
        sys.exit(4)

    if args.format == "json":
        output = {"success": True, "query": args.query, "results": results}
        print(json.dumps(output, ensure_ascii=True, indent=2))
    else:
        print_text(results)


if __name__ == "__main__":
    main()
