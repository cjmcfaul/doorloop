from .base import DoorLoopBase


class DoorLoopCommunication(DoorLoopBase):
    endpoint_base = '/communications'

    def list(self, **kwargs):
        '''
        List all Communication Logs
        https://api.doorloop.com/reference/get-communications
        '''
        response = self.connector.get(f'{self.endpoint_base}', **kwargs)
        return self.validator(response).validate()

    def create(self, data, **kwargs):
        '''
        Create a Communication Log
        https://api.doorloop.com/reference/post-communication
        '''
        response = self.connector.post(f'{self.endpoint_base}', data, **kwargs)
        return self.validator(response).validate()

    def retrieve(self, communication_id, **kwargs):
        '''
        Retrieve a Communication
        https://api.doorloop.com/reference/get-communication
        '''
        response = self.connector.get(f'{self.endpoint_base}/{communication_id}', **kwargs)
        return self.validator(response).validate()

    def update(self, communication_id, data, **kwargs):
        '''
        Update a Communication
        https://api.doorloop.com/reference/put-communication
        '''
        response = self.connector.put(f'{self.endpoint_base}/{communication_id}', data, **kwargs)
        return self.validator(response).validate()

    def delete(self, communication_id, **kwargs):
        '''
        Delete a Communication
        https://api.doorloop.com/reference/delete-communication
        '''
        response = self.connector.delete(f'{self.endpoint_base}/{communication_id}', **kwargs)
        return self.validator(response).validate()