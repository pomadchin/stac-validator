FROM python:3.7
WORKDIR /stac_validator
COPY ./stac_validator .
RUN python stac_validator.py https://radarstac.s3.amazonaws.com/stac/catalog.json --version 0.7.0