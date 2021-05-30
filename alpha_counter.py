read_file = open("test.txt", "rt")
dictionary = {}
for line in read_file:
    for character in line.lower():
        if character not in dictionary:
            dictionary[character] = 1
        else:
            dictionary[character] += 1
for key, value in dictionary.items():
    if key.isalnum():
        print(key,"-->",value)