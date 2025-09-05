from src.models.paper import Paper
from typing import List
from src.providers.arXiv_provider import ArxivProvider
from src.providers.semantic_scholar_provider import SemanticScholarProvider

async def search_papers(query: str, max_results: int = 10, sources: List[str]=None) -> List[Paper] | None:
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
            results.append(scholar_provider.search_sch(query=query, limit=max_results))
        else:
            raise Exception(f"Unknown source: {source}")
    return results

def register_tools(mcp_instance):
    mcp_instance.tool()(search_papers)