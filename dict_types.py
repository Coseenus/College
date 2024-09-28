  doter = {
    "name": "Max",
    "age": 30,
    "address": {
        "city": "Kivertsi",
        "street": "5th Avenue",
        "house_number": 10,
        "apartment": 6,
        "zip_code": "45200"},
     "weight_kg": 121 }
type_items = {}
for k, v in doter.items():
    if type(v) == dict:
        for k1, v1 in v.items():
            type_items[k1] = type(v1)
    else:
        type_items[k] = type(v)
print(type_items)
