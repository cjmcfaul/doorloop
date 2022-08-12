import os

from .base import DoorLoopConnector, DoorLoopValidator

from .accounts import DoorLoopAccount
from .users import DoorLoopUser
from .properties import DoorLoopProperty
from .units import DoorLoopUnit
from .leases import DoorLoopLease
from .tenants import DoorLoopTenant
from .lease_payments import DoorLoopLeasePayment
from .lease_returned_payments import DoorLoopLeaseReturnedPayments
from .lease_charges import DoorLoopLeaseCharge
from .lease_credits import DoorLoopLeaseCredit
from .portfolios import DoorLoopPortfolio
from .tasks import DoorLoopTask
from .owners import DoorLoopOwner
from .vendors import DoorLoopVendor
from .expenses import DoorLoopExpense
from .vendor_bills import DoorLoopVendorBill
from .vendor_credits import DoorLoopVendorCredit
from .reports import DoorLoopReport
from .communications import DoorLoopCommunication
from .notes import DoorLoopNote
from .files import DoorLoopFile


class DoorLoop:
    '''
    https://api.doorloop.com/reference/introduction
    '''

    def __init__(self, api_key=os.environ.get('DOORLOOP_API_KEY'), connector=None, validator=None):
        self.api_key = api_key
        self.connector = connector or DoorLoopConnector(api_key)
        self.validator = validator or DoorLoopValidator()

    @property
    def accounts(self):
        return DoorLoopAccount(self.connector, self.validator)

    @property
    def users(self):
        return DoorLoopUser(self.connector, self.validator)

    @property
    def properties(self):
        return DoorLoopProperty(self.connector, self.validator)

    @property
    def units(self):
        return DoorLoopUnit(self.connector, self.validator)

    @property
    def leases(self):
        return DoorLoopLease(self.connector, self.validator)

    @property
    def tenants(self):
        return DoorLoopTenant(self.connector, self.validator)

    @property
    def lease_payments(self):
        return DoorLoopLeasePayment(self.connector, self.validator)

    @property
    def lease_returned_payments(self):
        return DoorLoopLeaseReturnedPayments(self.connector, self.validator)

    @property
    def lease_charges(self):
        return DoorLoopLeaseCharge(self.connector, self.validator)

    @property
    def lease_credits(self):
        return DoorLoopLeaseCredit(self.connector, self.validator)

    @property
    def portfolios(self):
        return DoorLoopPortfolio(self.connector, self.validator)

    @property
    def tasks(self):
        return DoorLoopTask(self.connector, self.validator)

    @property
    def owners(self):
        return DoorLoopOwner(self.connector, self.validator)

    @property
    def vendors(self):
        return DoorLoopVendor(self.connector, self.validator)

    @property
    def expenses(self):
        return DoorLoopExpense(self.connector, self.validator)

    @property
    def vendor_bills(self):
        return DoorLoopVendorBill(self.connector, self.validator)

    @property
    def vendor_credits(self):
        return DoorLoopVendorCredit(self.connector, self.validator)

    @property
    def reports(self):
        return DoorLoopReport(self.connector, self.validator)

    @property
    def communications(self):
        return DoorLoopCommunication(self.connector, self.validator)

    @property
    def notes(self):
        return DoorLoopNote(self.connector, self.validator)

    @property
    def files(self):
        return DoorLoopFile(self.connector, self.validator)
