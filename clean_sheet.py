def clean_sheet(*kwargs):
    final_array = []
    number = len(kwargs[0])
    arg_length = len(kwargs)
    kwargs[0].sort()
    for item in kwargs:
        array = []
        longest = item[0]
        length = len(item[0])
        i = 0 
        j = 1
        while j < len(item):
            if len(item[j]) > len(item[i]):
                length = len(item[j])
            i += 1
            j += 1
        for elements in item:
            if len(elements) < length+1:
                add = (length+1) - len(elements) 
                elements = elements+" "*add
            array.append(elements)
        final_array.append(array)
    for i in range(number):
        j = 0
        while j < arg_length:
            print(final_array[j][i], end = " ")
            j += 1
        print()


if __name__ == "__main__": 
    first_names = ["Adhityan","Adwaith","Arjun","Arun","Athmaja","Athul","Bobby","Don"]
    last_names = ["M","S Kumar","VK","K Paul","M Nair","PV","Shaju","George"]
    marks = ["43","38","48","39","49","45","40","40"]
    clean_sheet(first_names,last_names,marks)


    





# full_name = first_names[i]+" "+last_names[i] 
# file.write(row)
# file.write("\n")
# file.close()
