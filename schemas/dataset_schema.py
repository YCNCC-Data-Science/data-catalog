from typing import List, Optional
from pydantic import BaseModel, Field, HttpUrl, EmailStr
import yaml
import json
from pathlib import Path


class Creator(BaseModel):
    name: str
    affiliation: Optional[str] = None
    orcid: Optional[str] = None


class Maintainer(BaseModel):
    name: str
    email: Optional[EmailStr] = None
    affiliation: Optional[str] = None
    github: Optional[str] = None


class Identifier(BaseModel):
    doi: Optional[str] = None
    url: Optional[HttpUrl] = None


class Access(BaseModel):
    landing_page: Optional[HttpUrl] = None
    download_link: Optional[HttpUrl] = None
    license: Optional[str] = None
    github_repo: Optional[HttpUrl] = None


class Publication(BaseModel):
    title: str
    doi: Optional[str] = None
    url: Optional[HttpUrl] = None


class GeoCoverage(BaseModel):
    description: str
    bbox: Optional[List[float]] = Field(
        None, description="Bounding box: [minLon, minLat, maxLon, maxLat]"
    )


class TemporalCoverage(BaseModel):
    start_date: Optional[str] = None  # could refine to date if always YYYY-MM-DD
    end_date: Optional[str] = None


class Dataset(BaseModel):
    id: str
    title: str
    description: str

    creators: List[Creator]
    maintainers: List[Maintainer]

    publication_date: Optional[str] = None
    version: Optional[str] = None
    keywords: Optional[List[str]] = None
    tags: Optional[List[str]] = None  # ✅ extra tags

    identifiers: Optional[Identifier] = None
    access: Optional[Access] = None
    related_publications: Optional[List[Publication]] = None

    geospatial_coverage: Optional[GeoCoverage] = None
    temporal_coverage: Optional[TemporalCoverage] = None

    formats: Optional[List[str]] = None
    size: Optional[str] = None
    provenance: Optional[str] = None
    notes: Optional[str] = None

    @classmethod
    def from_yaml(cls, path: str | Path) -> "Dataset":
        """Load dataset from YAML file"""
        with open(path, "r") as f:
            content = yaml.safe_load(f)
        return cls.model_validate(content)

    def to_json(self, path: Optional[str | Path] = None) -> str:
        """Dump dataset to JSON (file or string)"""
        json_str = self.model_dump_json(indent=2)
        if path:
            Path(path).write_text(json_str)
        return json_str
