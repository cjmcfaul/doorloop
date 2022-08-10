from .base import DoorLoopBase


class DoorLoopPortfolio(DoorLoopBase):
    endpoint_base = '/property-groups'

    def list(self, **kwargs):
        '''
        List all Portfolios
        https://api.doorloop.com/reference/get-property-groups
        '''
        response = self.connector.get(f'{self.endpoint_base}', **kwargs)
        return self.validator(response).validate()

    def retrieve(self, portfolio_id, **kwargs):
        '''
        Retrieve a Portfolio
        https://api.doorloop.com/reference/get-property-group
        '''
        response = self.connector.get(f'{self.endpoint_base}/{portfolio_id}', **kwargs)
        return self.validator(response).validate()
