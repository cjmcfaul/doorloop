from .base import DoorLoopBase


class DoorLoopExpense(DoorLoopBase):
    endpoint_base = '/expenses'

    def list(self, **kwargs):
        '''
        List all Expenses
        https://api.doorloop.com/reference/get-expenses
        '''
        response = self.connector.get(f'{self.endpoint_base}', **kwargs)
        return self.validator(response).validate()

    def create(self, data, **kwargs):
        '''
        Create an Expense
        https://api.doorloop.com/reference/post-expense
        '''
        response = self.connector.post(f'{self.endpoint_base}', data, **kwargs)
        return self.validator(response).validate()

    def retrieve(self, expense_id, **kwargs):
        '''
        Retrieve an Expense
        https://api.doorloop.com/reference/get-expense
        '''
        response = self.connector.get(f'{self.endpoint_base}/{expense_id}', **kwargs)
        return self.validator(response).validate()

    def update(self, expense_id, data, **kwargs):
        '''
        Update an Expense
        https://api.doorloop.com/reference/put-expense
        '''
        response = self.connector.put(f'{self.endpoint_base}/{expense_id}', data, **kwargs)
        return self.validator(response).validate()

    def delete(self, expense_id, **kwargs):
        '''
        Delete an Expense
        https://api.doorloop.com/reference/delete-expense
        '''
        response = self.connector.delete(f'{self.endpoint_base}/{expense_id}', **kwargs)
        return self.validator(response).validate()