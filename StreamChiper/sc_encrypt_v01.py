######################################################
#   Created by : Aditya Putra Indrayanto             #
#   Program Enkrip dgn metode Stream Chiper Klasik   #
######################################################

alphabet = list('abcdefghijklmnopqrstuvwxyz')
data_kata = {}
data_key = {}
data_tmp = {}

def main():
    kata = list('aditya')
    kunci = list('kuncik')

    encrypt(kata, kunci)

def encrypt(kata, kunci):
    for ri in range(len(kata)):
        data_kata = []
        for xi in kata:
            data_kata.append(alphabet.index(xi))
    print "Message:", data_kata

    for ki in range(len(kunci)):
        data_key = []
        for yi in kunci:
            data_key.append(alphabet.index(yi))
    print "Key:", data_key

    text = ''
    for tmp in range(len(data_kata)):
        data_tmp[tmp] = []
        temp_data = (data_kata[tmp] + data_key[tmp]) % len(alphabet)
        result = alphabet[temp_data]
        text += result
    print "Hasil Enkripsi dari {} adalah : {}".format(kata, text)

    #for ki in kunci:
    #     #print alphabet.index(ki)
    #     print ki
    #     for xi in enumerate(kata, start=0):
    #         print xi
    #         data_key.append(alphabet.index(ki))

main()