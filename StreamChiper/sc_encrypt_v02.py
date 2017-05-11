######################################################
#   Created by : Aditya Putra Indrayanto             #
#   Program Enkrip dgn metode Stream Chiper Modern   #
######################################################

def main():
    #Define data variable
    S = [0, 1, 2, 3]
    K = [1, 7, 1, 7]
    z = 0
    char = list('hi')

    #Pengacakan S-Box
    for i in range(len(S)):
        z = (z + S[i] + K[i]) % 4
        S[i], S[z] = S[z], S[i]
        print "Iterasi ke", (i+1), S

    #Pseudo Random Byte
    for c in range(len(char)):
        i = (c + 1) % 4
        #print "Ini i:", i, S[c]
        z = (z + S[c]) % 4
        #print "Ini z:", z
        S[i], S[z] = S[z], S[i]
        print "Pseudo Random ke", i, S
        t = (S[i] +S[z]) % 4
        k = S[t]
    print "K :", k

    # j = (2 + 1) % 4
    # print j

main()