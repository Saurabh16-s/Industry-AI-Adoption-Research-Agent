from tavily import TavilyClient
from config import TAVILY_API_KEY

client = TavilyClient(api_key=TAVILY_API_KEY)

def search_industry_ai_training(industry: str):
    """
    Searches the web for how a given industry trains employees on AI.
    Returns a list of result snippets (title + content).
    """
    query = f"how {industry} companies train employees on AI tools 2026"
    response = client.search(
        query=query,
        max_results=8,
        search_depth="advanced"
    )

    results = []
    for r in response.get("results", []):
        results.append({
            "title": r.get("title", ""),
            "content": r.get("content", ""),
            "url": r.get("url", "")
        })
    return results