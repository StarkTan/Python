"""
Pymodbus Synchronous Server Example
The synchronous server is implemented in pure python without any third
party libraries (unless you need to use the serial protocols which require
pyserial). This is helpful in constrained or old environments where using
twisted is just not feasible. What follows is an example of its use:
"""
# --------------------------------------------------------------------------- #
# import the various server implementations
# --------------------------------------------------------------------------- #
from pymodbus.server.sync import StartTcpServer

from pymodbus.device import ModbusDeviceIdentification
from pymodbus.datastore import ModbusSequentialDataBlock, ModbusSparseDataBlock
from pymodbus.datastore import ModbusSlaveContext, ModbusServerContext

import logging

FORMAT = ('%(asctime)-15s %(threadName)-15s'
          ' %(levelname)-8s %(module)-15s:%(lineno)-8s %(message)s')
logging.basicConfig(format=FORMAT)
log = logging.getLogger()
log.setLevel(logging.DEBUG)


def run_server():
    store = ModbusSlaveContext(
        di=ModbusSequentialDataBlock(0x0000, [0x0000] * 100),
        co=ModbusSequentialDataBlock(0x0000, [0x0000] * 100),
        hr=ModbusSequentialDataBlock(0x0000, [0x0000] * 100),
        ir=ModbusSequentialDataBlock(0x0000, [0x0000] * 100))

    context = ModbusServerContext(slaves=store, single=True)

    StartTcpServer(context, address=("localhost", 5020))


if __name__ == "__main__":
    run_server()
