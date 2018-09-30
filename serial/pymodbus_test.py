#串口交互
from pymodbus.client.sync import ModbusSerialClient as ModbusClient
client= ModbusClient(method="rtu", baudrate=9600, port="COM2", parity='E')
#TCP 交互
#from pymodbus.client.sync import ModbusTcpClient as ModbusClient
#client = ModbusClient('127.0.0.1')

print(client.connect())
client.write_register(0x0000, 0x12F4, unit=0x01)#0x0000寄存器位置，写入值，从机位置
client.write_registers(0x0001, [0x5678, 0x9ABC], unit=0x01)
temp = client.read_holding_registers(0x0000, 0x01, unit=0x01)#起始位，读取个数，从机ID
print(temp.registers)
