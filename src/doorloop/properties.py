from .base import DoorLoopBase


class DoorLoopProperty(DoorLoopBase):
    endpoint_base = '/properties'

    def list(self, **kwargs):
        '''
        List all Properties
        https://api.doorloop.com/reference/get-properties
        '''
        response = self.connector.get(f'{self.endpoint_base}', **kwargs)
        return self.validator(response).validate()

    def retrieve(self, property_id, **kwargs):
        '''
        Retrieve a Property
        https://api.doorloop.com/reference/get-property
        '''
        response = self.connector.get(f'{self.endpoint_base}/{property_id}', **kwargs)
        return self.validator(response).validate()
