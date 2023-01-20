import os
import unittest

from src.doorloop.main import DoorLoop


class DoorLoopTestCase(unittest.TestCase):
    dl = DoorLoop(api_key=os.environ['DOORLOOP_API_KEY'])

