import json
import uuid
import stac_validator
# import trio

def _run_validate(url, version="missing"):
    stac = stac_validator.StacValidate(url, version)
    stac.run()
    return stac

#print("hello")
stac_file = 'https://raw.githubusercontent.com/radiantearth/stac-spec/master/catalog-spec/examples/catalog.json'
version = '0.9.0'
stac = _run_validate(stac_file, version)
#print(stac_file.strip())
print(json.dumps(stac.message, indent=4))
#return stac