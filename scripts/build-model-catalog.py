# from schemas.dataset_schema import Creator
from typing import List, Optional
from pydantic import BaseModel, Field, HttpUrl, EmailStr
import yaml
import json
from pathlib import Path


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


FILES = (Path(__file__).resolve().parent.parent / "inputs" / "models").glob("*.yaml")

list_of_objects = []

for file in FILES:
    with open(file) as stream:
        try:
            data = yaml.safe_load(stream)
            list_of_objects.append(data)
        except yaml.YAMLError as exc:
            print(exc)

output_path = Path(__file__).resolve().parent.parent / "catalogs" / "model-catalog.json"

with open(output_path, "w") as f:
    json.dump(list_of_objects, f, indent=4, default=str)

print(json.dumps(list_of_objects, indent=4, default=str))
