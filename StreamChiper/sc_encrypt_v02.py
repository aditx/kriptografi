
def main():
    S = [0, 1, 2, 3]
    K = [1, 7, 1, 7]
    z = 0

    for i in range(len(S)):
        z = (z + S[i] + K[i]) % 4
        S[i], S[z] = S[z], S[i]
        print S

main()