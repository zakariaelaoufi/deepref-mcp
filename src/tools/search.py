from ..models.paper import Paper
from typing import List
from ..server import mcp
from ..providers.arXiv_provider import ArxivProvider
from ..providers.semantic_scholar_provider import SemanticScholarProvider

@mcp.tool()
async def search(query: str, max_results: int = 10, sources: List[str]=None) -> List[Paper] | None:
    results = []
    """Search for academic papers across multiple databases."""
    if sources is None:
        sources = ['arXiv', 'semanticscholar']
    for source in sources:
        if source == 'arXiv':
            arxiv_provider = ArxivProvider()
            results.append(arxiv_provider.search_arxiv(query=query, max_results=max_results))
        elif source == 'semanticscholar':
            scholar_provider = SemanticScholarProvider()
            results.append(scholar_provider.search_sch("generative ai", limit=max_results))
        else:
            raise Exception(f"Unknown source: {source}")
    return results