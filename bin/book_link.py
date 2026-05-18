#!/usr/bin/env python3

import argparse
import requests
import urllib.parse
import json
import subprocess

HEADERS = {
    "User-Agent": "book_link.py (jms@schof.org)"
}

def debug_print(debug, label, content):
    if debug:
        print(f"\n🔍 {label}")
        if isinstance(content, str):
            print(content)
        else:
            print(json.dumps(content, indent=2))

def get_first_work_data(title, debug=False):
    debug_print(debug, "get_first_work_data() called with", {"title": title})

    query = urllib.parse.quote_plus(title)
    url = f"https://openlibrary.org/search.json?title={query}"
    debug_print(debug, "OpenLibrary Search URL", url)

    resp = requests.get(url, headers=HEADERS)
    resp.raise_for_status()
    data = resp.json()

    debug_print(debug, "Search API result (first 3)", data.get("docs", [])[:3])

    docs = data.get("docs", [])
    if not docs:
        debug_print(debug, "get_first_work_data() returning", None)
        return None

    result = docs[0]
    debug_print(debug, "get_first_work_data() returning", result)
    return result

def get_english_editions(work_key, debug=False):
    debug_print(debug, "get_english_editions() called with", {"work_key": work_key})

    work_id = work_key.strip("/").split("/")[-1]
    url = f"https://openlibrary.org/works/{work_id}/editions.json?limit=50"
    debug_print(debug, "Editions API URL", url)

    resp = requests.get(url, headers=HEADERS)
    resp.raise_for_status()
    data = resp.json()
    editions = data.get("entries", [])

    debug_print(debug, "Raw Editions API response (first 3)", editions[:3])

    english_editions = []
    for ed in editions:
        langs = ed.get("languages", [])
        if isinstance(langs, list) and len(langs) == 1:
            lang_key = langs[0].get("key", "")
            if lang_key.endswith("/eng"):
                english_editions.append({
                    "key": ed.get("key"),
                    "title": ed.get("title", "Unknown Title"),
                    "publish_date": ed.get("publish_date", "Unknown Date"),
                    "publishers": ed.get("publishers", []),
                })

    debug_print(debug, "Filtered English editions", english_editions[:3])
    return english_editions

def choose_edition(editions):
    print("\n📚 English-only Editions:\n")
    for i, ed in enumerate(editions, start=1):
        pubs = ", ".join(ed["publishers"]) if ed["publishers"] else "Unknown publisher"
        print(f"{i}. {ed['title']} ({ed['publish_date']}) - {pubs}")
    print()

    while True:
        choice = input("Select an edition by number: ").strip()
        if choice.isdigit():
            index = int(choice) - 1
            if 0 <= index < len(editions):
                return editions[index]
        print("Invalid choice. Please try again.")

def get_wikipedia_url(author_name, debug=False):
    debug_print(debug, "get_wikipedia_url() called with", {"author_name": author_name})

    url = "https://en.wikipedia.org/w/api.php"
    params = {
        "action": "opensearch",
        "search": author_name,
        "limit": 5,
        "namespace": 0,
        "format": "json"
    }

    resp = requests.get(url, params=params)
    resp.raise_for_status()
    data = resp.json()
    debug_print(debug, "Wikipedia response", data)

    urls = data[3]
    if urls:
        return urls[0]
    else:
        return f"https://en.wikipedia.org/wiki/Special:Search?search={urllib.parse.quote_plus(author_name)}"

def copy_to_clipboard(text):
    try:
        subprocess.run("pbcopy", text=True, input=text, check=True)
        print("✅ Markdown copied to clipboard.")
    except Exception as e:
        print(f"⚠️ Clipboard copy failed: {e}")

def main():
    parser = argparse.ArgumentParser(description="Markdown + Wikipedia + Clipboard for OpenLibrary book links.")
    parser.add_argument("--title", required=True, help="Book title to search for")
    parser.add_argument("--debug", action="store_true", help="Show debug output")
    args = parser.parse_args()

    debug_print(args.debug, "main() received arguments", vars(args))

    work_data = get_first_work_data(args.title, debug=args.debug)
    if not work_data:
        print("❌ No work found for that title.")
        return

    work_key = work_data.get("key")
    author = work_data.get("author_name", ["Unknown"])[0]
    title = work_data.get("title", "Unknown Title")

    english_editions = get_english_editions(work_key, debug=args.debug)
    if not english_editions:
        print("❌ No English-only editions found.")
        return

    selected = choose_edition(english_editions)
    edition_url = f"https://openlibrary.org{selected['key']}"
    wiki_url = get_wikipedia_url(author, debug=args.debug)
    print("\n\n\n\n")
    markdown = f"[{title}]({edition_url}) by [{author}]({wiki_url})"
    print(markdown)
    print("\n\n\n\n")
    copy_to_clipboard(markdown)

if __name__ == "__main__":
    main()
