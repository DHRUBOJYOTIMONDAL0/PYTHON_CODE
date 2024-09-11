info = {'name': 'Suman', 'age': 19, 'eligible': True}
# print(info)
# print(info['name'])
# print(info.get('name'))
# print(info.keys())
# print(info.values())
# for key in info.keys():
#     print(info[key])

print(info.items())
for key, value in info.items():
    print(f"The corresponding value to the key {key} is {value}")