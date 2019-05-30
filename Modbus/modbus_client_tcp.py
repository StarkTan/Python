from pymodbus.client.sync import ModbusTcpClient

client = ModbusTcpClient(host='127.0.0.1', port=5020)
result = client.read_discrete_inputs(1, 1)
print(result.bits[0])  # 位
client.write_coil(1, True)
result = client.read_coils(1, 1)
print(result.bits[0])  # 位
client.write_register(2, 0xFFFF)
result = client.read_holding_registers(2, 1)
print(result.registers[0])  # 两个字节
client.close()
