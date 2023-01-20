from .base import DoorLoopBase


class DoorLoopFile(DoorLoopBase):
    endpoint_base = '/files'
    RESOURCE_TYPES = [
        'TENANT',
        'OWNER',
        'VENDOR',
        'PROPERTY',
        'UNIT',
        'LEASE',
        'LEASE_DRAFT',
        'TASK',
        'RENTAL_APPLICATION',
    ]

    def list(self, **kwargs):
        '''
        List all Files
        https://api.doorloop.com/reference/get-files
        '''
        response = self.connector.get(f'{self.endpoint_base}', **kwargs)
        return self.validator(response).validate()

    def upload(self, data, **kwargs):
        '''
        Upload a File
        https://api.doorloop.com/reference/post-files
        '''
        # TODO convert file to string / binary file
        response = self.connector.post(f'{self.endpoint_base}', data, **kwargs)
        return self.validator(response).validate()

    def retrieve(self, file_id, **kwargs):
        '''
        Retrieve a File
        https://api.doorloop.com/reference/get-file
        '''
        response = self.connector.get(f'{self.endpoint_base}/{file_id}', **kwargs)
        return self.validator(response).validate()

    def update(self, file_id, data, **kwargs):
        '''
        Update a File
        https://api.doorloop.com/reference/put-file
        '''
        response = self.connector.put(f'{self.endpoint_base}/{file_id}', data, **kwargs)
        return self.validator(response).validate()

    def delete(self, file_id, **kwargs):
        '''
        Delete a File
        https://api.doorloop.com/reference/delete-file
        '''
        response = self.connector.delete(f'{self.endpoint_base}/{file_id}', **kwargs)
        return self.validator(response).validate()

    def download(self, file_id, **kwargs):
        '''
        Download a File
        https://api.doorloop.com/reference/download-file
        '''
        response = self.connector.get(f'{self.endpoint_base}/{file_id}/download', **kwargs)
        return self.validator(response).validate()
