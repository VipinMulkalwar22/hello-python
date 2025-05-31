# Tuple
# syntax : ()
# Heterogenious
# ordered
# Index
# data immutable
# Tuple immutable
# Duplicate Allowed

data = (10, 10, 70.67,"Hello",True)

print("Data type is :", type(data))
print("Length is :",len(data))
print(data)

print(data[0])
print(data[1])

# data[0] = 11

print("Data using loop")
for value in data:
    print(value)


for i in range(len(data)):
    print(data[i])