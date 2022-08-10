from .base import DoorLoopBase


class DoorLoopUnit(DoorLoopBase):
    endpoint_base = '/units'

    def list(self, **kwargs):
        '''
        List all Units
        https://api.doorloop.com/reference/get-units
        '''
        response = self.connector.get(f'{self.endpoint_base}', **kwargs)
        return self.validator(response).validate()

    def retrieve(self, unit_id, **kwargs):
        '''
        Retrieve a Unit
        https://api.doorloop.com/reference/get-unit
        '''
        response = self.connector.get(f'{self.endpoint_base}/{unit_id}', **kwargs)
        return self.validator(response).validate()
