a = "Hello World"
name = "Dmytro"
surname = "Kosynets"
age = 16
weight = 63.44
Group_of_blood = 2
lst = [a, name, age, weight]
type_lst = []
value_lst = []
string = 0
integer = 0
floatt = 0
other = 0
for i in lst:
    x = type(i)
    y = i
    type_lst.append(x)
    value_lst.append(y)
    if isinstance(y, str):
        string += 1
    elif isinstance(y, int):
        integer += 1
    elif isinstance(y, float):
        floatt += 1
    else:
        other += 1
if string > integer and string > floatt and string > other:
    print("the most frequency type is 'str'")
elif integer > string and integer > floatt and integer > other:
    print("the most frequency type is 'int'")
elif floatt > string and floatt > integer and floatt > other:
    print("the most frequency type is 'float'")
else:
    print("we don't have a winner")