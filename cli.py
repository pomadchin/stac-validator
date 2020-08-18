import click
import pystac
import json
from pystac import Item, Catalog

@click.command()
@click.option('--stac_item', default='sentinel2-sample.json', help="Local stac item to validate")
def validate_item(stac_item):
    """A simple program that validates a local STAC item."""
    click.echo('Stac_item: %s' % stac_item)
    item = Item.from_file(stac_item)
    item.validate()
    print(item)

if __name__ == '__main__':
    validate_item()