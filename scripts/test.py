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

FILES = (Path(__file__).resolve().parent.parent / "inputs" / "datasets").glob("*.yaml")

list_of_objects = []

for file in FILES:
    with open(file) as stream:
        try:
            data = yaml.safe_load(stream)
            list_of_objects.append(data)
        except yaml.YAMLError as exc:
            print(exc)

output_path = (
    Path(__file__).resolve().parent.parent / "catalogs" / "dataset-catalog.json"
)

with open(output_path, "w") as f:
    json.dump(list_of_objects, f, indent=4, default=str)

print(json.dumps(list_of_objects, indent=4, default=str))
