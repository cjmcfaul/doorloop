from .base import DoorLoopBase


class DoorLoopAccount(DoorLoopBase):
    endpoint_base = '/accounts'
    # TODO finish setting up account types
    # TODO create function to get verbose account type
    ACCOUNT_TYPES = (
        ('Asset > Other Current Assets', 'ASSET_OTHER_CURRENT_ASSETS'),
        ('Asset > Bank', 'ASSET_BANK'),
    )
    '''
    'ASSET_FIXED_ASSETS',
            'ASSET_OTHER_ASSETS',
            'LIABILITY_ACCOUNTS_PAYABLE',
            'LIABILITY_CREDIT_CARD',
            'LIABILITY_OTHER_CURRENT_LIABILIY',
            'LIABILITY_LONG_TERM_LIABILITY',
            'EQUITY_EQUITY',
            'REVENUE_INCOME',
            'REVENUE_OTHER_INCOME',
            'EXPENSE_EXPENSE',
            'EXPENSE_OTHER_EXPENSE',
            'EXPENSE_COGS'
    '''

    def list(self, **kwargs):
        '''
        List all Accounts
        https://api.doorloop.com/reference/get-accounts
        '''
        response = self.connector.get(f'{self.endpoint_base}', **kwargs)
        return self.validator(response).validate()

    def create(self, data, **kwargs):
        '''
        Create an Account
        https://api.doorloop.com/reference/post-account
        '''
        response = self.connector.post(f'{self.endpoint_base}', data, **kwargs)
        return self.validator(response).validate()

    def retrieve(self, account_id, **kwargs):
        '''
        Retrieve an Account
        https://api.doorloop.com/reference/get-account
        '''
        response = self.connector.get(f'{self.endpoint_base}/{account_id}', **kwargs)
        return self.validator(response).validate()

    def update(self, account_id, data, **kwargs):
        '''
        Update an Account
        https://api.doorloop.com/reference/put-account
        '''
        response = self.connector.put(f'{self.endpoint_base}/{account_id}', data, **kwargs)
        return self.validator(response).validate()

    def delete(self, account_id, **kwargs):
        '''
        Delete an Account
        https://api.doorloop.com/reference/delete-account
        '''
        response = self.connector.delete(f'{self.endpoint_base}/{account_id}', **kwargs)
        return self.validator(response).validate()
