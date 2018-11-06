no_rows = 3

a = "*"

for i in range(round(no_rows/2)+1):
    print(a * i)
for i in range(round(no_rows/2), no_rows):
    print(a * (no_rows-i))
