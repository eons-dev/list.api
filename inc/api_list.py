import os
import logging
import requests
import json
import jsonpickle
import apie
from api_operation import operation

class list(operation):
    def __init__(this, name="list"):
        super().__init__(name)

        this.supportedMethods = ['GET']

        this.optionalKWArgs['page'] = 1
        this.optionalKWArgs['per_page'] = 100
        this.optionalKWArgs['fields'] = [] #all
        this.optionalKWArgs['make_list_of'] = None

    # Required Endpoint method. See that class for details.
    def GetHelpText(this):
        return f'''\
Get an overview of the available data in a resource.
This may or may not give any details for the listed resources.
If details are provided, they can be shaped per the 'fields' parameter.
If you get details and just want a simple list, use the 'make_list_of' parameter with a single field (e.g. .../resource/list?make_list_of='name').

{super().GetHelpText()}
'''