import yaml
import json
from pathlib import Path


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
