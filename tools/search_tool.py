from duckduckgo_search import DDGS

class SearchTool:
    @staticmethod
    def search(query):
        """Perform a live web search using DuckDuckGo."""
        with DDGS() as ddgs:
            results = [r['body'] for r in ddgs.text(query, max_results=3)]
            return "\n".join(results) if results else "No results found."