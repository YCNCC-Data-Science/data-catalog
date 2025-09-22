# from schemas.dataset_schema import Creator
from typing import List, Optional
from pydantic import BaseModel, Field, HttpUrl, EmailStr
import yaml
import json
from pathlib import Path


# need code to convert / to %2F
class License(BaseModel):
    name: str
    url: str


class Maintainer(BaseModel):
    name: str
    email: str
    image_url: Optional[str] = None


class DataAccess(BaseModel):
    doi: str
    url: str


class Publication(BaseModel):
    author: str
    publication_date: str
    title: str
    journal: str
    doi: str


class Dataset(BaseModel):
    id: str
    title: str
    description: str
    publication_date: str
    version: str
    tags: List[str]
    license: License
    maintainers: List[Maintainer]
    publications: List[Publication]


path = (
    Path(__file__).resolve().parent.parent
    / "inputs"
    / "datasets"
    / "kuebbing_etal_2025.yaml"
)

with open(path) as stream:
    try:
        data = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)

print(json.dumps(data, indent=4, default=str))
