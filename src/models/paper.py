from pydantic import BaseModel, HttpUrl
from typing import List, Optional
from datetime import datetime


class Paper(BaseModel):
    title: str
    authors: List[str]
    summary: str
    published_date: Optional[datetime] = None
    journal: Optional[str] = None
    doi: Optional[str] = None
    arxiv_id: Optional[str] = None
    semantic_scholar_id: Optional[str] = None
    url: Optional[HttpUrl] = None
    pdf_url: Optional[HttpUrl] = None
    categories: List[str] = []
    keywords: List[str] = []
    citation_count: Optional[int] = None
