from tastypie.api import Api
from api.resources import (ConvenioResource)
                           # BusLineTerminalResource)

v1_api = Api(api_name='v1')
v1_api.register(ConvenioResource())
