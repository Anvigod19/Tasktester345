# range 0 to 6
# print all no except 3 and 6
"""
for i in range(0,7,1):
    if i==3 or i==6:
        continue
    print(i)
"""
i = 0
while i <= 7:
    if (i != 3 and i != 6):
        print(i)
    i = i + 1
