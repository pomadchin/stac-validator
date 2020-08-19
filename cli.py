import click
import pystac
import json
from pystac import Item, Catalog
from stac_validator import stac_validator

@click.command()
@click.option('--stac_item', default='sentinel2-sample.json', help="Local stac item to validate")
@click.argument('out', type=click.File('w'), default='-', required=False)
def validate_item(stac_item, out):
    """A simple program that validates a local STAC item."""
 
    click.echo(click.style('stac-validator-api', blink=True, bold=True))
    click.echo(click.style('Stac_item: %s' % stac_item, bg='black', fg='green', bold=True))
    
    # pystac validation
    # item = Item.from_file(stac_item)
    # item.validate()
    # print(item.validate())
    # print(item.bbox)

    # stac-validator validation
    stac = stac_validator.StacValidate(stac_item)
    click.echo(click.style(stac.run(), bg='black', fg='white', bold=True))
    
    # write to text file
    click.echo(stac.run(), file=out)
    
if __name__ == '__main__':
    validate_item()