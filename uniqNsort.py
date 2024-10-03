input_list = [3, 1, 2, 3, 4, 5, 6, 3, 4, 5, 7, 6, 5, 4, 3, 4, 5, 4, 3, 'Привіт', 'анаконда']

def remove_dupl(input_list):
    result = []
    for item in input_list:
        if item not in result:
            result.append(item)
    return result

def sort_list(unique_list):
    numbers = []
    strings = []
    for i in unique_list:
        if type(i) == int:
            numbers.append(i)
        elif type(i) == str:
            strings.append(i)
    numbers.sort()
    strings.sort(key=lambda s: s.lower())
    return numbers + strings

unique_list = remove_dupl(input_list)
sorted_list = sort_list(unique_list)

print("List without duplicates:", unique_list)
print("List is sorted:", sorted_list )
