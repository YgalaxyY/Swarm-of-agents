#!/usr/bin/env python3
"""
🔍 Simple Web Search
"""
import sys
try:
    from duckduckgo_search import DDGS
    
    def search(query):
        print(f"🔍 Searching: {query}...")
        results = list(DDGS().text(query, max_results=5))
        if not results:
            print("❌ No results found.")
            return
        for i, r in enumerate(results, 1):
            print(f"\n{i}. {r['title']}\n   {r['href']}\n   {r['body'][:150]}...")

    if __name__ == "__main__":
        if len(sys.argv) > 1:
            search(" ".join(sys.argv[1:]))
        else:
            print("Usage: python web_search.py 'query'")
except ImportError:
    print("❌ Run: pip install duckduckgo-search")
