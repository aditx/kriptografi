import binascii

string = list('0123456789ABCDEF')
result01 = bin(int(binascii.hexlify('string'), 16))
result02 = ' '.join(format(ord(x), 'b') for x in string)
print result01
print result02