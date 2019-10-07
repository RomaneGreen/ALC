
def divide_byte(x):

    low_byte = x & 0x00FF
    high_byte = x >> 8
    return high_byte, low_byte



def decode(high_byte, low_byte):

    high_byte = high_byte << 7
    decoded = (high_byte | low_byte) - 8192
    return decoded



def encode(x):

    encoded_int = x + 8192
    low_byte = encoded_int & 0x007F  
    high_byte = ((encoded_int & 0x3F80) << 1)  
    encoded = hex(low_byte + high_byte)
    return encoded


