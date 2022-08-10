from .base import DoorLoopBase


class DoorLoopNote(DoorLoopBase):
    endpoint_base = '/notes'

    def list(self, **kwargs):
        '''
        List all Notes
        https://api.doorloop.com/reference/get-notes
        '''
        response = self.connector.get(f'{self.endpoint_base}', **kwargs)
        return self.validator(response).validate()

    def create(self, data, **kwargs):
        '''
        Create a Note
        https://api.doorloop.com/reference/post-notes
        '''
        response = self.connector.post(f'{self.endpoint_base}', data, **kwargs)
        return self.validator(response).validate()

    def retrieve(self, note_id, **kwargs):
        '''
        Retrieve a Note
        https://api.doorloop.com/reference/get-note
        '''
        response = self.connector.get(f'{self.endpoint_base}/{note_id}', **kwargs)
        return self.validator(response).validate()

    def update(self, note_id, data, **kwargs):
        '''
        Update a Note
        https://api.doorloop.com/reference/put-note
        '''
        response = self.connector.put(f'{self.endpoint_base}/{note_id}', data, **kwargs)
        return self.validator(response).validate()

    def delete(self, note_id, **kwargs):
        '''
        Delete a Note
        https://api.doorloop.com/reference/delete-note
        '''
        response = self.connector.delete(f'{self.endpoint_base}/{note_id}', **kwargs)
        return self.validator(response).validate()
