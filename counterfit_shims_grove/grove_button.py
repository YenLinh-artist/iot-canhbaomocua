from counterfit_connection import CounterFitConnection
from counterfit_shims_grove.grove_input_device import GroveInputDevice

class GroveButton(GroveInputDevice):
    def __init__(self, pin):
        CounterFitConnection.init('127.0.0.1', 5000)
        super().__init__(pin)
