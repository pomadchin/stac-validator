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
 
    click.echo(click.style('stac-validator-cli', blink=True, bold=True))
    click.echo(click.style('Stac_item: %s' % stac_item, bg='black', fg='green', bold=True))
    
    # pystac validation
    item = Item.from_file(stac_item)
    item.validate()
    print(item.validate())
    # print(item.bbox)

    # # stac-validator validation
    # stac_spec_dirs=None
    # version="master"
    # log_level="DEBUG"
    # follow=False
    
    # stac = stac_validator.StacValidate(stac_item, stac_spec_dirs, version, log_level, follow)
    # result = stac.run()
    # click.echo(click.style(result, bg='black', fg='white', bold=True))
    
    # write to text file
    # click.echo(stac.run(), file=out)

def stac_validator(stac_item):
    pass
    
if __name__ == '__main__':
    validate_item()