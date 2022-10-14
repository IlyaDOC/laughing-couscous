def my_substr(string, len_of_substr):
    index=0
    part_of_string=''
    while index<len_of_substr:
        current_char=string[index]
        part_of_string=part_of_string+current_char
        index=index+1
    return part_of_string
