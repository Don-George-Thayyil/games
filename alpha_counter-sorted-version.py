#read_file = open("test.txt", "rt")
read_file = "There is nothing to right here 9843--$$@# is my mobile number??? "
dictionary = {}
alphabets_tuple = tuple()
for line in read_file:
    for character in line.lower():
        if character not in dictionary:
            dictionary[character] = 1
            alphabets_tuple += (character,)
        else:
            dictionary[character] += 1
alphabets = list(alphabets_tuple)
alphabets.sort()
for key in alphabets:
    for item in dictionary.keys():
        if item == key and item.isalnum():
            print(key, "-->", dictionary[key])