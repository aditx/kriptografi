###################################################
#   Created by : Aditya Putra Indrayanto          #
#   Program Enkripsi dengan metode Caesar Chiper  #
###################################################

alphabet = list('abcdefghijklmnopqrstuvwxyz')

def main():

    var_kata = list(raw_input("Input Kata yang ingin di Enkripsi : "))

    encrypt(var_kata)

def encrypt(var_kata):
    cipher = ''
    k = 3
    for c in var_kata:
        if c in alphabet:
            cipher += alphabet[(alphabet.index(c) + k) % len(alphabet)]

    print cipher

main()