# Spatial Temporal Asset Catalog (STAC) Validator

[![CircleCI](https://circleci.com/gh/sparkgeo/stac-validator.svg?style=svg)](https://circleci.com/gh/sparkgeo/stac-validator)

This utility allows users to validate STAC json files against the [STAC](https://github.com/radiantearth/stac-spec) spec.

It can be installed as command line utility and passed either a local file path or a url along with the STAC version to validate against. 
Example usages can be found below


## Requirements

* Python 3.6
    * Requests
    * Docopt
    * pytest

## Installation from repo

```bash
pip install .
or (for development)
pip install --editable .  
```

## Installation from PyPi  

```bash
pip install stac-validator  
```

## stac_validator --help
```
Description: Validate a STAC item or catalog against the STAC specification.

Usage:
    stac_validator <stac_file> [--version STAC_VERSION] [--timer] [--recursive] [--log_level LOGLEVEL] [--update] [--force] [--extension EXTENSION] [--core]

Arguments:
    stac_file  Fully qualified path or url to a STAC file.

Options:
    -v, --version STAC_VERSION   Version to validate against. [default: master]
    -h, --help                   Show this screen.
    --timer                      Reports time to validate the STAC. (seconds)
    --update                     Migrate to newest STAC version (1.0.0-beta.2) for testing
    --log_level LOGLEVEL         Standard level of logging to report. [default: CRITICAL]
    --force                      Add missing 'id' field or version='0.9.0' for older STAC objects to force validation
    --recursive                  Recursively validate an entire collection or catalog.
    --extension EXTENSION        Validate an extension
    --core                       Validate on core only
```
---
# CLI

Basic Usage  
```    
stac_validator https://raw.githubusercontent.com/radiantearth/stac-spec/master/catalog-spec/examples/catalog.json
```
```
[
    {
        "path": "https://raw.githubusercontent.com/radiantearth/stac-spec/master/catalog-spec/examples/catalog.json",
        "asset_type": "catalog",
        "version": "1.0.0-beta.2",
        "valid_stac": true
    }
]
```
--version  
```    
stac_validator https://raw.githubusercontent.com/radiantearth/stac-spec/master/catalog-spec/examples/catalog.json --version 0.9.0
```
```
[
    {
        "path": "https://raw.githubusercontent.com/radiantearth/stac-spec/master/catalog-spec/examples/catalog.json",
        "asset_type": "catalog",
        "valid_stac": false,
        "error_type": "STACValidationError",
        "error_message": "STAC Validation Error: Validation failed for CATALOG with ID NAIP against schema at https://raw.githubusercontent.com/radiantearth/stac-spec/v0.9.0/catalog-spec/json-schema/catalog.json"
    }
]
```




--extension
```
stac_validator https://raw.githubusercontent.com/radiantearth/stac-spec/master/item-spec/examples/sample-full.json --extension sat
```
```
[
    {
        "path": "https://raw.githubusercontent.com/radiantearth/stac-spec/master/item-spec/examples/sample-full.json",
        "asset_type": "item",
        "valid_stac": false,
        "error_type": "STACValidationError",
        "error_message": "STAC Validation Error: Validation failed for ITEM with ID CS3-20160503_132131_05 against schema at https://schemas.stacspec.org/v1.0.0-beta.2/extensions/sat/json-schema/schema.jsonfor STAC extension 'sat'"
    }
]
```


Testing
```bash
pytest -v
```
See the tests directory for examples on different usages.  
  
---
# Import stac-validator

```
from stac_validator import stac_validator
  
stac = stac_validator.StacValidate("https://raw.githubusercontent.com/radiantearth/stac-spec/master/item-spec/examples/sample-full.json")
stac.run()

print(stac.message)

if stac.message[0]["valid_stac"] == False:
    print("False")
```
```
from stac_validator import stac_validator
  
stac = stac_validator.StacValidate("tests/sample-full.json", extension='eo', update=True)
stac.run()

print(stac.message)
```