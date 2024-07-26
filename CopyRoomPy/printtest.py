data_dict = {}
str = "a: 1; b: 2; c: 3; d: 4;"
data_list = str.split(";")
print(len(data_list))
for item in data_list:
    if not item == "":
        print(item)
        key, value = item.split(":")
        data_dict[key.strip()] = value.strip()
print(data_dict["c"])