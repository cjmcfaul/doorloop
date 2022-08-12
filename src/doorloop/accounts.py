from .base import DoorLoopBase, DoorLoopValidator


class DoorLoopAccount(DoorLoopBase):
    endpoint_base = '/accounts'
    # TODO create function to get verbose account type
    ACCOUNT_TYPES = (
        ("Asset", (
                ('Other Current Assets', 'ASSET_OTHER_CURRENT_ASSETS'),
                ('Bank', 'ASSET_BANK'),
                ('Fixed Assets', 'ASSET_FIXED_ASSETS'),
                ('Other Assets', 'ASSET_OTHER_ASSETS')
            )
        ),
        ("Liability", (
                ('Accounts Payable', 'LIABILITY_ACCOUNTS_PAYABLE'),
                ('Credit Card', 'LIABILITY_CREDIT_CARD'),
                ('Other Current Liability', 'LIABILITY_OTHER_CURRENT_LIABILIY'),
                ('Long Term Liability', 'LIABILITY_LONG_TERM_LIABILITY')
            )
        ),
        ('Equity', 'EQUITY_EQUITY'),
        ("Revenue", (
                ('Income', 'REVENUE_INCOME'),
                ('Other Income', 'REVENUE_OTHER_INCOME')
            )
        ),
        ("Expense", (
                ('Expense', 'EXPENSE_EXPENSE'),
                ('Other Expense', 'EXPENSE_OTHER_EXPENSE'),
                ('Cost of Goods Sold', 'EXPENSE_COGS'),
            )
        )
    )

    def init(self, connector, validator):
        validator = DoorLoopAccountValidator()
        super(DoorLoopAccount).__init__(connector, validator)

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


class DoorLoopAccountValidator(DoorLoopValidator):

    class Meta:
        fields = {
            "name": {
                "type": str,
                "required": True,
            },
            "active": {
                "type": bool,
                "required": True,
            },
        }
