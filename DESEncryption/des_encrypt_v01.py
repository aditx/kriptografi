
from prettytable import PrettyTable

def main():
    plaintext = list('COMPUTER')
    key = '133457799BBCDFF1'

    data_plain_text = []
    for z in plaintext:
        data_plain_text.append(format(ord(z), '08b'))
    print "\nData PlainText: ", data_plain_text

    split_key = split(key, 2)
    z = 0
    data_temp = []
    for y in split_key:
        z = z + 1
        data_temp.append(y)
    print "Data Key: ", data_temp

    bin_key = map(lambda x: "{0:08b}".format(int(x, 16)), data_temp)
    print "Data Key (On Biner): ", bin_key

    p = PrettyTable()
    for row in data_plain_text:
        p.add_row(row)

    print "\nMatrix PlainText :\n"
    print p.get_string(header=False, border=False)

    plain_text_transpose = zip(*rev(data_plain_text))

    data_transform = []
    for x in range(len(plain_text_transpose)):
       data_transform.append("\n".join(map("".join,zip(*plain_text_transpose[x]))))

    pv = PrettyTable()
    for cols in data_transform:
        pv.add_row(cols)

    print "\nMatrix Invers PlainText :\n"
    print pv.get_string(header=False, border=False)

    data_transform_inv = list(data_transform)
    for xi in range(len(data_transform)):
        data_transform_inv[xi] = data_transform_inv[xi][:-1]

    px = PrettyTable()
    for colz in data_transform_inv:
        px.add_row(colz)

    print "\nMatrix Invers-1 PlainText :\n"
    print px.get_string(header=False, border=False)

def split(s, chunk_size):
    a = zip(*[s[i::chunk_size] for i in range(chunk_size)])
    return [''.join(t) for t in a]

def rev(l):
    return l and rev(l[1:]) + [l[0]]

main()