from typing import List, Optional
from pydantic import BaseModel


class License(BaseModel):
    name: str
    url: str


class Maintainer(BaseModel):
    name: str
    email: str
    image_url: Optional[str] = None
    github: Optional[str] = None


class DataAccess(BaseModel):
    doi: str
    url: str


class Publication(BaseModel):
    author: List[str]
    year: str
    title: str
    journal: str
    volume: Optional[str] = None
    article: Optional[str] = None
    doi: str


class Dataset(BaseModel):
    id: str
    title: str
    description: str
    publication_date: str
    version: str
    repository: str
    tags: Optional[List[str]] = None
    license: License
    maintainers: List[Maintainer]
    publications: List[Publication]
    thumbnail: Optional[str] = None
    color: Optional[str] = None
    slug: Optional[str] = None
