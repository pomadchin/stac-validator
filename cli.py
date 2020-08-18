import click
import pystac
import json
from pystac import Item, Catalog
from stac_validator import stac_validator

@click.command()
@click.option('--stac_item', default='sentinel2-sample.json', help="Local stac item to validate")
def validate_item(stac_item):
    """A simple program that validates a local STAC item."""
    
    # pystac validation
    click.echo('Stac_item: %s' % stac_item)
    item = Item.from_file(stac_item)
    print(item.validate())
    print(item.bbox)

    # pystac validation
    stac = stac_validator.StacValidate(stac_item)
    print(stac.run())


if __name__ == '__main__':
    validate_item()