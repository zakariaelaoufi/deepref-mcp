from models.paper import Paper
from typing import List, Optional
from providers.arXiv_provider import ArxivProvider
from providers.semantic_scholar_provider import SemanticScholarProvider
from providers.pubmed_provider import PubMedProvider

async def search_papers(query: str, max_results: int = 10, sources: List[str]=None) -> List[Paper]:
    results = []
    """
    Search for academic papers across multiple databases.

    Args:
        query: The user query.
        max_results: The maximum number of papers to return from each database.
        sources: The databases to fetch papers from. Defaults to arXiv, Semantic Scholar, and PubMed.
    """
    if sources is None:
        sources = ['arxiv', 'semantic scholar', 'pubmed']
    else:
        sources = [word.lower() for word in sources]

    for source in sources:
        print('hello')
        if source == 'arxiv':
            arxiv_provider = ArxivProvider()
            results.extend(arxiv_provider.search_arxiv(query=query, max_results=max_results))
        elif source == 'semantic scholar':
            scholar_provider = SemanticScholarProvider()
            results.extend(scholar_provider.search_sch(query=query, limit=max_results))
        elif source == 'pubmed':
            pubmed_provider = PubMedProvider()
            results.extend(pubmed_provider.search_pubmed(query=query, limit=max_results))
        else:
            raise Exception(f"Unknown source: {source}")
    return results

def register_tools(mcp_instance):
    mcp_instance.tool(description="Search for academic papers across multiple databases (e.g: arXiv, Semantic scholar...).")(search_papers)