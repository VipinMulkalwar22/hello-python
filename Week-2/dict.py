# Dict
# Syntax : {Key : Value}
# heterogenious
# ordered
# Indexed (not numeric)
# key duplicate allowed but old gets overwritten
# Value duplicate allowed
# Data Mutable (Value)

data = {"Name": "Let us C", "Author":"Y kanetkar","Price":340,"Publication":"BPB Publication"}

print("Data Type is :", type(data))
print("Length is :", len(data))
print(data)

print(data["Author"])

data["Price"] = 400

print(data)