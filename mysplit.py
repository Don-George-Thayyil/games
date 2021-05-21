#clone for the split method available for strings

def mysplit(strng):
    array = []
    word = ""
    for i in strng:
        if i == " ":
            if word != "":
                array.append(word)
                word = ""            
        else:
            word += i
    if word != "":
        array.append(word)        
    return array

if __name__ == "__main__":
    print(mysplit("To be or not to be, that is the   question   "))
    print(mysplit("To be or not to be,that is the que       stion"))
    print(mysplit("   "))
    print(mysplit(" abc "))
    print(mysplit(""))
