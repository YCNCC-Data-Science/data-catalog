from pathlib import Path
from typing import List

def build_catalog(yaml_dir: str, output: str = "catalog.json") -> None:
    """Load all YAMLs in a directory and build consolidated catalog"""
    datasets: List[] = []

for path in Path(yaml_dir).glob("*.yaml"):
        ds = Dataset.from_yaml(path)
        datasets.append(ds)

    # Write consolidated JSON
    catalog = [ds.model_dump() for ds in datasets]
    Path(output).write_text(json.dumps(catalog, indent=2))
    print(f"✅ Catalog written to {output}")
