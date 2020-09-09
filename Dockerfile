FROM python:3.7
WORKDIR /stac_validator
COPY ./stac_validator .
RUN python stac_validator.py