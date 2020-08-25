import click 
import pystac
from pystac import Item, Catalog, Collection
import json
import requests
from json.decoder import JSONDecodeError
from typing import Tuple
from urllib.parse import urljoin, urlparse

def fix_version(version: str ) -> str:
    if version[0] not in ['m','d','v']:
        version = 'v' + version
    return version

def fix_stac_missing(stac_content: dict) -> dict:
    # # # add stac version field if there isn't one # # # 
    if not 'stac_version' in stac_content:
        stac_content['stac_version'] = 'v0.9.0'
        click.echo("added stac version field to pass validation")

    # # # add id field if there isn't one # # #
    if not 'id' in stac_content:
        stac_content['id'] = 'missing'
        click.echo("added stac id field to pass validation")

    return stac_content

def create_err_msg(err_type: str, err_msg: str) -> dict:
    return {"valid_stac": False, "error_type": err_type, "error_message": err_msg}

def is_valid_url(url: str) -> bool:
    try:
        result = urlparse(url)
        if result.scheme in ("http", "https"):
            return True
        else:
            return False
    except Exception as e:
        return False

def fetch_and_parse_file(input_path: str) -> Tuple[dict, dict]:
    err_message = {}
    data = None

    try:
        if is_valid_url(input_path):
            # logger.info("Loading STAC from URL")
            resp = requests.get(input_path)
            data = resp.json()
        else:
            with open(input_path) as f:
                # logger.info("Loading STAC from filesystem")
                data = json.load(f)

    except JSONDecodeError as e:
        # logger.exception("JSON Decode Error")
        err_message = create_err_msg("InvalidJSON", f"{input_path} is not Valid JSON")

    except FileNotFoundError as e:
        # logger.exception("STAC File Not Found")
        err_message = create_err_msg("FileNotFoundError", f"{input_path} cannot be found")

    return data, err_message

def validate(file, version):
    click.echo(click.style('stacTools', blink=True, bold=True))
    try:
        stac_content, err_message = fetch_and_parse_file(file)
        if bool(err_message): 
            click.echo(err_message)
        stac_content = fix_stac_missing(stac_content)
        version = fix_version(stac_content['stac_version'])
        result = pystac.validation.validate_dict(stac_content, stac_version=version)
        
        # # print(json.dumps(itemdict, indent=4))
      
    except KeyError as e:
        print("Missing Key: ", e)
    except pystac.validation.STACValidationError as e:
        print(e)

def create_validate_command(cli):
    """Validates a STAC object."""
    @cli.command('validate', short_help='Validate a STAC object')
    @click.option('--file', '-f', default='sentinel2-sample.json', help='File to validate')
    @click.option('--version', '-f', default='1.0.0-beta.2', help='STAC version')
    def validate_command(file, version):
        validate(file, version)

    return validate_command