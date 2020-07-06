my_string = "DA"
my_string2 = "BOB"


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
    
    return total


print(my_hash(my_string))  # => 133
print(my_hash(my_string))  # => 133
print(my_hash(my_string))  # => 133
print(my_hash(my_string2))  # => 211
print(my_hash(my_string2))  # => 211

