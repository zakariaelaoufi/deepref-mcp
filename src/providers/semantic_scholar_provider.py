from semanticscholar import SemanticScholar
from typing import List
from src.models.paper import Paper
from datetime import datetime


class SemanticScholarProvider:
    def __init__(self):
        self.sch = SemanticScholar()

    def search_sch(self, query: str, limit: int = 5) -> List[Paper]:
        results = self.sch.search_paper(query=query, limit=1, open_access_pdf=True, bulk=True, )
        print(len(results))
        papers = []

        i = 1
        for result in results:
            papers.append(
                Paper(
                    title=result.title,
                    authors=[author.name for author in result.authors],
                    summary=result.abstract or "",
                    published_date=result.publicationDate,
                    journal=result.journal.name if result.journal else None,
                    doi=result.externalIds.get("DOI") if result.externalIds else None,
                    arxiv_id=result.externalIds.get("ArXiv") if result.externalIds else None,
                    semantic_scholar_id=result.paperId,
                    url=result.url,
                    pdf_url=result.openAccessPdf.get("url") if result.openAccessPdf else None,
                    categories=result.fieldsOfStudy or [],
                    citation_count=result.citationCount,
                )
            )
            # break
            if i == limit:
                break
            i+=1
        return papers


if __name__ == "__main__":
    sch_provider = SemanticScholarProvider()
    rs = sch_provider.search_sch("generative ai", limit=5)

    for paper in rs:
        print(paper)
        print("----------------------")
