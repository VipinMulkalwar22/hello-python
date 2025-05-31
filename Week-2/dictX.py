data = {"Name": "Let us C", "Author":"Y kanetkar","Price":340,"Publication":"BPB Publication"}

print("Loop to Display Keys")
for X in data:
    print(X)

print("Loop to Display Values")

for X in data.values():
    print(X)

print("Loop to Display Key and Value")

for x,y in data.items():
    print(x,y)
