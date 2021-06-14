croatia_alphabet = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

alphabet_input = input()
for char in croatia_alphabet:
    alphabet_input = alphabet_input.replace(char, '1')

print(len(alphabet_input))
