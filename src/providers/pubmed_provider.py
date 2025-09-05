from pubmed_sdk import PubMed
from datetime import datetime
from typing import List
from models.paper import Paper


def map_pubmed_to_paper(pubmed_response: dict) -> Paper:
    """
    Maps a PubMed API response to a Paper object.
    """
    citation = pubmed_response.get('MedlineCitation', {})
    article = citation.get('Article', {})

    # Extract title
    title = article.get('ArticleTitle', '').strip()

    # Extract authors
    authors = []
    author_list = article.get('AuthorList', {}).get('Author', [])
    if not isinstance(author_list, list):
        author_list = [author_list]

    for author in author_list:
        if isinstance(author, dict):
            last_name = author.get('LastName', '')
            fore_name = author.get('ForeName', '')
            if last_name and fore_name:
                authors.append(f"{last_name}, {fore_name}")
            elif last_name:
                authors.append(last_name)

    # Extract abstract/summary
    abstract = article.get('Abstract', {})
    summary = ""
    if isinstance(abstract, dict):
        abstract_text = abstract.get('AbstractText', '')
        if isinstance(abstract_text, str):
            summary = abstract_text
        elif isinstance(abstract_text, list):
            # Handle list of strings or dictionaries
            text_parts = []
            for item in abstract_text:
                if isinstance(item, str):
                    text_parts.append(item)
                elif isinstance(item, dict):
                    # Extract text from dictionary (could be '#text' or direct value)
                    text_value = item.get('#text', '') or item.get('text', '') or str(item.get('value', ''))
                    if text_value:
                        text_parts.append(text_value)
            summary = ' '.join(text_parts)

    # Extract publication date
    pub_date = None
    article_date = article.get('ArticleDate', {})
    if article_date:
        try:
            year = int(article_date.get('Year', 0))
            month = int(article_date.get('Month', 1))
            day = int(article_date.get('Day', 1))
            if year > 0:
                pub_date = datetime(year, month, day)
        except (ValueError, TypeError):
            pass

    # Extract journal
    journal = article.get('Journal', {}).get('Title', '')

    # Extract DOI
    doi = None
    elocation_id = article.get('ELocationID', {})
    if isinstance(elocation_id, dict) and elocation_id.get('@EIdType') == 'doi':
        doi = elocation_id.get('#text', '')
    elif isinstance(elocation_id, list):
        for eid in elocation_id:
            if isinstance(eid, dict) and eid.get('@EIdType') == 'doi':
                doi = eid.get('#text', '')
                break

    # Extract PubMed ID
    pubmed_id = citation.get('PMID', {})
    if isinstance(pubmed_id, dict):
        pubmed_id = pubmed_id.get('#text', '')

    # Extract keywords
    keywords = []
    keyword_list = citation.get('KeywordList', {}).get('Keyword', [])
    if not isinstance(keyword_list, list):
        keyword_list = [keyword_list]

    for keyword in keyword_list:
        if isinstance(keyword, dict):
            kw_text = keyword.get('#text', '')
            if kw_text:
                keywords.append(kw_text)
        elif isinstance(keyword, str):
            keywords.append(keyword)

    url = f"https://pubmed.ncbi.nlm.nih.gov/{pubmed_id}/"

    # Create Paper object
    return Paper(
        title=title,
        authors=authors,
        summary=summary,
        published_date=pub_date,
        journal=journal,
        doi=doi,
        pubmed_id=pubmed_id,
        keywords=keywords,
        url=url
    )


class PubMedProvider:
    def __init__(self):
        self.pubmed = PubMed()

    def search_pubmed(self, query, limit=10) -> List[Paper]:
        """Search pubmed for papers."""
        results = self.pubmed.search(query)
        id_list = results['id_list']
        details = self.pubmed.fetch_details(id_list[:limit]).get('PubmedArticle')

        papers = []
        for detail in details:
            paper = map_pubmed_to_paper(detail)
            papers.append(paper)
        return papers

if __name__ == '__main__':
    p = PubMedProvider()
    res = p.search_pubmed('covid-19')
    print(len(res))
    for paper in res:
        print(paper)
        break
