import binascii

string = list('h')
result01 = bin(int(binascii.hexlify('string'), 16))
result02 = ' '.join(format(ord(x), 'b') for x in string)
print result01
print result02