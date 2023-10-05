from owslib.csw import CatalogueServiceWeb
from owslib.ogcapi.records import Records
from owslib.opensearch import OpenSearch
from owslib.fes import And, Or, PropertyIsEqualTo, PropertyIsGreaterThanOrEqualTo, PropertyIsLessThanOrEqualTo, PropertyIsLike, BBox, SortBy, SortProperty
from geolinks import sniff_link
import json
import os
import sys
import logging


relative_paths = ["../utils", "../processing", "../resource_catalogue"]
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.extend(os.path.join(current_dir, rel_path) for rel_path in relative_paths)

from utils import config, rc_logger

def List_Records():
    '''
    Function to list records from the resource catalogue
    '''

    base_domain = config['base_domain']

    catalogue_endpoint = f'http://resource-catalogue-open.{base_domain}/csw'

    rc_logger.info(f'Connecting to catalogue endpoint: {catalogue_endpoint}')

    csw = CatalogueServiceWeb(catalogue_endpoint, timeout=30, skip_caps=True)

    rc_logger.info(f"Connected to catalogue endpoint: {catalogue_endpoint}")
    rc_logger.info(f'CSW version: {csw.version}')

