from .base import DoorLoopBase


class DoorLoopReport(DoorLoopBase):
    endpoint_base = '/reports'

    def rent_roll(self, **kwargs):
        '''
        Rent Roll
        https://api.doorloop.com/reference/get-reports-rent-roll
        '''
        response = self.connector.get(f'{self.endpoint_base}/rent-roll', **kwargs)
        return self.validator(response).validate()

    def profit_and_loss(self, **kwargs):
        '''
        Profit & Loss
        https://api.doorloop.com/reference/get-reports-profit-and-loss
        '''
        response = self.connector.get(f'{self.endpoint_base}/profit-and-loss-summary', **kwargs)
        return self.validator(response).validate()

    def cash_flow_statement(self, **kwargs):
        '''
        Cash Flow Statement
        https://api.doorloop.com/reference/get-reports-cash-flow-statement
        '''
        response = self.connector.get(f'{self.endpoint_base}/cash-flow-statement', **kwargs)
        return self.validator(response).validate()

    def balance_sheet(self, **kwargs):
        '''
        Balance Sheet
        https://api.doorloop.com/reference/get-reports-balance-sheet
        '''
        response = self.connector.get(f'{self.endpoint_base}/balance-sheet-summary', **kwargs)
        return self.validator(response).validate()
