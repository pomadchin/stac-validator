from setuptools import setup

setup(
    name="Stac-Validator-CLI",
    version="0.1.0",
    py_modules=['cli'],
    install_requires=[
        'click',
        'pystac[validation]',
        'stac-validator',
        'colorama',
    ],
    entry_points='''
        [console_scripts]
        cli=cli:validate_item
    ''',
)