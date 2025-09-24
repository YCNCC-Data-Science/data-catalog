# YCNCC Data Catalog

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) [![Ruff](https://img.shields.io/badge/lint-ruff-FFFF00?labelColor=808080&style=flat)](https://docs.astral.sh/ruff/)

The **YCNCC Data Catalog** provides a frontend for browsing datasets and model metadata related to YCNCC research. This repository stores the data and model catalogs.

## Setup

1. **Install uv**  
   Follow the [installation guide](https://docs.astral.sh/uv/getting-started/installation/) if you haven't already.

2. **Install dependencies**

   ```bash
   uv install
   ```

   This installs all packages listed in uv.lock.

## Contributing

1. **Add metadata**

   - Place dataset metadata (YAML format) in `/inputs/datasets`
   - Place model metadata (YAML format) in `/inputs/models`

2. **Build the catalog**

   Convert YAML files to JSON for the catalog by running:

```bash
uv run -m scripts.build-model-catalog
uv run -m scripts.build-model-catalog
```

3. **Open pull request**

   After you add your dataset open a [pull request](https://github.com/YCNCC-Data-Science/data-catalog/pulls)

## Improvements and Bugs

- **Bugs**: Please report issues through [GitHub Issues](https://github.com/YCNCC-Data-Science/data-catalog/issues)
- **Ideas / Feedback**: Start a [Discussion](https://github.com/YCNCC-Data-Science/data-catalog/discussions) to suggest improvements. You can use discussions if you need help contributing metadata
- **Documentation**: See the [Wiki](https://github.com/YCNCC-Data-Science/data-catalog/wiki) for developer guides and additional resources.
