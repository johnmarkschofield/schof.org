#!/usr/bin/env python3

import requests
import argparse
import urllib.parse
import json
from bs4 import BeautifulSoup

def get_worldcat_results(title, debug=False):
    query = urllib.parse.quote_plus(title)
    url = f"https://www.worldcat.org/search?q={query}"

    if debug:
        print(f"\n🔍 WorldCat Search URL:\n{url}")

    headers = {"User-Agent": "Mozilla/5.0"}
    resp = requests.get(url, headers=headers)
    resp.raise_for_status()

    try:
        soup = BeautifulSoup(resp.text, "lxml")
    except Exception:
        soup = BeautifulSoup(resp.text, "html.parser")

    results = soup.select("div#searchResults div.result")
    if not results:
        print("❌ No search results found.")
        return []

    output = []

    if debug and results:
        print("\n🔍 First raw result HTML snippet:\n")
        print(results[0].prettify()[:2000])  # show first 2000 characters for brevity

    for result in results[:5]:  # Limit to top 5
        link_tag = result.select_one("a.title")
        author_tag = result.select_one(".author")
        format_tag = result.select_one(".type")
        lang_tag = result.select_one(".language")

        if not link_tag:
            continue

        title = link_tag.text.strip()
        author = author_tag.text.strip() if author_tag else "Unknown author"
        format_text = format_tag.text.strip() if format_tag else "Unknown format"
        lang_text = lang_tag.text.strip() if lang_tag else "Unknown language"
        result_url = urllib.parse.urljoin("https://www.worldcat.org", link_tag.get("href"))

        entry = {
            "title": title,
            "author": author,
            "format": format_text,
            "language": lang_text,
            "url": result_url
        }

        output.append(entry)

    if debug:
        print("\n🔍 Parsed results:")
        print(json.dumps(output, indent=2))

    return output

def print_results(results):
    if not results:
        print("No results to display.")
        return

    print("\n📚 Top WorldCat Matches:\n")
    for i, entry in enumerate(results, start=1):
        print(f"{i}. {entry['title']}")
        print(f"   Author:   {entry['author']}")
        print(f"   Format:   {entry['format']}")
        print(f"   Language: {entry['language']}")
        print(f"   Link:     {entry['url']}\n")

def main():
    parser = argparse.ArgumentParser(description="List WorldCat book matches by title.")
    parser.add_argument("--title", help="Book title to search for")
    parser.add_argument("--debug", action="store_true", help="Show search URL and raw HTML + parsed data")
    args = parser.parse_args()

    if args.title:
        results = get_worldcat_results(args.title, debug=args.debug)
    else:
        user_input = input("Enter book title: ").strip()
        results = get_worldcat_results(user_input, debug=args.debug)

    print_results(results)

if __name__ == "__main__":
    main()
