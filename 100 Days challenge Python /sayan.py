# keys = ['Name', 'Age',"Roll"]
# values = ["Sayan",30, 1]
# combined_dict = dict(zip(keys,values))
# print("Combined Dictionary")
# print(combined_dict)

input_string = "Sayan, 05/12/2004; Dhrubojyoti, 09/12/2003; Ankur, 01/07/2003"
name_birthday_list = input_string.split('; ')
birthday_dict = {}
for join in name_birthday_list:
    name, birthday  = join.split(', ')
    birthday_dict[name] = birthday
print("join Name and Birthday")
print(birthday_dict)
search_name  = input("Enter the name: ")
if search_name in birthday_dict:
    print(f"{search_name}'s birthday is on {birthday_dict[search_name]}")
else:
    print("f {search_name}'s not found")