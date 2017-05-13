######################################################
#   Created by : Aditya Putra Indrayanto             #
#   Program Enkrip dgn metode Stream Chiper Modern   #
######################################################

def main():

    S = [0, 1, 2, 3]
    K = [1, 7, 1, 7]
    z = 0
    character = list('hi')

    for i in range(len(S)):
        z = (z + S[i] + K[i]) % 4
        S[i], S[z] = S[z], S[i]
        print "Iterasi ke", (i+1), ":", S

    encrypt_rc4(S, character)

def random_pseudo_byte(S, character):
    j = 0
    d = 0
    for c in range(len(character)):
        i = (c + 1) % 4
        j = (j + S[d]) % 4
        S[i], S[j] = S[j], S[i]

        print "Pseudo Random ke", i, S
        t = (S[i] + S[j]) % 4
        k = S[t]
        yield k

def encrypt_rc4(S, character):
    cipher_chars = []
    random_byte_gen = random_pseudo_byte(S, character)
    for char in character:
        byte = ord(char)
        cipher_byte = byte ^ random_byte_gen.next()
        cipher_chars.append(chr(cipher_byte))
    print "Hasil Enkripsi :", ''.join(cipher_chars)

main()