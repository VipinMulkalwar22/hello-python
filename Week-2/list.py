# List
# Syntax : []
# Heterogenious
# Ordered
# Index
# Data Mutable
# List Mutable
# Duplicate Allowed

data = [10,90.67,"Hello",40,True]

print("Data Type is : ",type(data))
print("Length is ", len(data))
print(data)

print(data[0])
print(data[1])
print(data[2])
print(data[3])
print(data[4])

data[0]=11

print(data[0])
print(data[1])
print(data[2])
print(data[3])
print(data[4])

data.append(40)

print(data[0])
print(data[1])
print(data[2])
print(data[3])
print(data[4])
print(data[5])

print("Data Display using loop")
for value in data:
    print(value)