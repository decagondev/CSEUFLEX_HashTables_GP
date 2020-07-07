my_string = "DA"
my_string2 = "BOB"

class SomeClass:

    def __init__(self, size):
        self.storage = [None] * size

    def my_hash(self, s):
        """
            Input: String
            Output: Integer
            Operate on the individual bytes of the string (characters) -> number representation of the char
            byte can hold 0 - 255

            Algorithm:
                take each byte f the string
                sum up the total of the values of those bytes
                return the sum of the values
        """
        # sum up a total
        total = 0

        sb = s.encode() # encode the string in to a bunch of utf-8 bytes
        # loop over the bytes of the string
        for b in sb:
            # print byte
            total += b

            total &= 0xffffffff # constrain our number to a size of 32bits / 4 bytes
        
        return total
    
    def put(self, key, val):
        h = self.my_hash(key)

        i = h % len(self.storage)
        self.storage[i] = val


def my_hash(s):
    """
        Input: String
        Output: Integer
        Operate on the individual bytes of the string (characters) -> number representation of the char
        byte can hold 0 - 255

        Algorithm:
            take each byte f the string
            sum up the total of the values of those bytes
            return the sum of the values
    """
    # sum up a total
    total = 0

    sb = s.encode() # encode the string in to a bunch of utf-8 bytes
    # loop over the bytes of the string
    for b in sb:
        # print byte
        total += b

        total &= 0xffffffff  # constrain our number to a size of 32bits / 4 bytes
    
    return total



# print(my_hash(my_string))  # => 133
# print(my_hash(my_string))  # => 133
# print(my_hash(my_string))  # => 133
# print(my_hash(my_string2))  # => 211
# print(my_hash(my_string2))  # => 211

hash_table = [None] * 8 # 0, 1, 2, 3, 4, 5, 6, 7

# put
"""
1: put the key string through a hashing function to get a hash value -> h
2: Mod the hash value with the data structure size (arr) to get the index -> i
3: Store the value at the index
"""

def put(ht, key, val):
    h = my_hash(key)

    i = h % len(ht)
    ht[i] = val

put(hash_table, "DA", "DA Value")

# h = my_hash("DA")

# i = h % len(hash_table)
# print(i)

# hash_table[i] = "DA Value"


# h = my_hash("BOB")

# i = h % len(hash_table)

# hash_table[i] = "BOB Value"
put(hash_table, "BOB", "BOB Value")



print(hash_table)

# h = my_hash("BOB")

# i = h % len(hash_table)

# hash_table[i] = "BOB Value 2"
put(hash_table, "BOB", "BOB Value 2")


print(hash_table)

# get
"""
1: put the key string through a hashing function to get a hash value -> h
2: Mod the hash value with the data structure size (arr) to get the index -> i
3: Return the value at the index
"""
def get(ht, key):
    h = my_hash(key)

    i = h % len(ht)

    return ht[i]


# Delete
def delete(ht, key):
    h = my_hash(key)

    i = h % len(ht)

    ht[i] = None

# get the valuye at the bob key -> Bob Value 2
# h = my_hash("BOB")

# i = h % len(hash_table)

# v = hash_table[i]

v = get(hash_table, "BOB")

print(v)

# hash_table = [None] * 8 # 0, 1, 2, 3, 4, 5, 6, 7

# h = my_hash("DA")

# i = h % len(hash_table)
# print(i)

# if hash_table[i] == None:
#     hash_table[i] = "DA Value"
# else:
#     print("Collision!!!!!")

# h = my_hash("BOB")

# i = h % len(hash_table)

# if hash_table[i] == None:
#     hash_table[i] = "BOB Value"
# else:
#     print("Collision!!!!!")


# print(hash_table)

# h = my_hash("BOB")

# i = h % len(hash_table)

# if hash_table[i] == None:
#     hash_table[i] = "BOB Value 2"
# else:
#     print("Collision!!!!!")

# print(hash_table)

