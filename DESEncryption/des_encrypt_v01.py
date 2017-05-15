
def main():
    plaintext = list('COMPUTER')
    key = '133457799BBCDFF1'

    # bin_plaintext = ' '.join(format(ord(x), '08b') for x in plaintext)
    # print bin_plaintext

    data_plain_text = []
    for z in plaintext:
        data_plain_text.append(format(ord(z), '08b'))
    print data_plain_text

    split_key = split(key, 2)
    z = 0
    data_temp = []
    for y in split_key:
        z = z + 1
        data_temp.append(y)
    print data_temp

    bin_key = map(lambda x: "{0:08b}".format(int(x, 16)), data_temp)
    print bin_key

def split(s, chunk_size):
    a = zip(*[s[i::chunk_size] for i in range(chunk_size)])
    return [''.join(t) for t in a]

main()