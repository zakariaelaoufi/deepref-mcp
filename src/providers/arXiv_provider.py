import arxiv
from src.models.paper import Paper
from typing import List


class ArxivProvider:
  def __init__(self):
    self.client = arxiv.Client()

  def search_arxiv(self, query, max_results: int = 10) -> List[Paper]:
    """Search arXiv for papers."""
    search = arxiv.Search(
      query=query,
      max_results=max_results,
      sort_by=arxiv.SortCriterion.Relevance,
      sort_order = arxiv.SortOrder.Descending
    )

    papers = []
    results = self.client.results(search)

    for result in results:
      papers.append(
        Paper(
          title=result.title,
          authors=[author.name for author in result.authors],
          summary=result.summary,
          published_date=result.published,
          journal=result.journal_ref,
          doi=result.doi,
          arxiv_id=result.entry_id.split("/")[-1],
          pdf_url=result.pdf_url,
          categories=list(result.categories),
        )
      )
    return papers


if __name__ == "__main__":
  arxiv_provider = ArxivProvider()
  rs = arxiv_provider.search_arxiv("attention mechanism deepmind")

  for paper in rs:
    print(paper)
    print('----------------------')