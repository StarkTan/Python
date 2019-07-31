
import binascii


def calculate_crc(data_bytes):
    if not isinstance(data_bytes, bytes):
        raise Exception('error data')
    temp = 0xFFFF
    for data in data_bytes:
        if not 0x00 <= data <= 0xFF:
            raise Exception((u'data: 0x{0:<02X}not[0x00-0xFF]'.format(data)).encode('utf-8'))
        low_byte = (data ^ temp) & 0x00FF
        result_crc = (temp & 0xFF00) | low_byte
        for index in range(8):
            if result_crc & 0x0001 == 1:
                result_crc >>= 1
                result_crc ^= 0xA001
            else:
                result_crc >>= 1
        temp = result_crc
    return temp


test_data = b'\xfe\x41\x00\x60\x01\xff'
result_data = calculate_crc(test_data)
print(binascii.b2a_hex(result_data.to_bytes(length=2, byteorder='little', signed=False)))
