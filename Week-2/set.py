# set
# syntax : {}
# Heterogenious
# Unordered
# Unindexed
# duplicate not allowed
# Set is Mutable
# data is immutable

data = {10,90.67,"Hello",True,10}
print("Data type is :",type(data))
print("Lenght is :",len(data))
print(data)
# print(data[0])
data.add(71)
print(data)
data.remove(10)
print(data)

print("Data using loop")

for value in data:
    print(value)