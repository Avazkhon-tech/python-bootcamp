with open("file1.txt") as file:
    file1 = file.readlines()
    file1 = [n.replace('\n', '') for n in file1]


with open("file2.txt") as file:
    file2 = file.readlines()
    file2 = [n.replace('\n', '') for n in file2]

result = [int(n) for n in file2 if n in file1]
print(result)
