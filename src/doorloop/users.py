from .base import DoorLoopBase


class DoorLoopUser(DoorLoopBase):
    endpoint_base = '/users'

    def list(self, **kwargs):
        '''
        List all Users
        https://api.doorloop.com/reference/get-users
        '''
        response = self.connector.get(f'{self.endpoint_base}', **kwargs)
        return self.validator(response).validate()

    def retrieve(self, user_id, **kwargs):
        '''
        Retrieve a User
        https://api.doorloop.com/reference/get-user
        '''
        response = self.connector.get(
            f'{self.endpoint_base}/{user_id}',
            **kwargs
        )
        return self.validator(response).validate()

    def get_current(self, **kwargs):
        '''
        Get Current User
        https://api.doorloop.com/reference/get-current-user
        '''
        response = self.connector.get(f'{self.endpoint_base}/me', **kwargs)
        return self.validator(response).validate()
