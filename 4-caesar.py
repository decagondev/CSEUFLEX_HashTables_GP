# lets write up a transposition table to encode and decode ROT 13 (Caesar's Cipher)
# This is a varient of ROT-13 but the same idea applies 
# it uses a hash table to store the encode table

encode_table = {
    'A': 'H',
    'B': 'Z',
    'C': 'Y',
    'D': 'W',
    'E': 'O',
    'F': 'R',
    'G': 'J',
    'H': 'D',
    'I': 'P',
    'J': 'T',
    'K': 'I',
    'L': 'G',
    'M': 'L',
    'N': 'C',
    'O': 'E',
    'P': 'X',
    'Q': 'K',
    'R': 'U',
    'S': 'N',
    'T': 'F',
    'U': 'A',
    'V': 'M',
    'W': 'B',
    'X': 'Q',
    'Y': 'V',
    'Z': 'S'
}

# now lets plan what we need next



# Tests
if __name__ == "__main__":
    plaintext = "HELLOWORLD"

    ciphertext = encode(plaintext)

    print(f"Ciphertext: {ciphertext}")

    plaintext2 = decode(ciphertext)

    print(f"Plaintext:  {plaintext}")