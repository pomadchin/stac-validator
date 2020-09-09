import json
import uuid
import stac_validator
# import trio

def handler(event, context):
    """
    Lambda Handler
    :param event: params passed to lambda
    :param context: AWS runtime params
    :return: dict message
    """

    # Find input params
    json_STAC = event.get('json')
    url_STAC = event.get('url')
    version = event.get('schemaVersion', None)
    print(f"STAC verison: {version}")
    if version == 'latest':
        version = 'master'

    # Check for JSON string
    if type(json_STAC) is dict:
        local_stac = f"/tmp/{str(uuid.uuid4())}.json"

        with open(local_stac, "w") as f:
            json.dump(json_STAC, f)

        stac_file = local_stac
    else:
        stac_file = url_STAC

    def _run_validate(url, version="missing"):
        stac = stac_validator.StacValidate(url, version)
        stac.run()
        return stac

    stac = _run_validate(stac_file.strip(), version)
    return stac.message[0]