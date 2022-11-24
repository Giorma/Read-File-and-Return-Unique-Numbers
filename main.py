file = "./file/txt"


def numbers_in_file(filename):
    with open(filename, "r") as f:
        data = {int(x) for x in f.readlines()}
    return data


with open(file, "w") as f:
    for i in range(10):
        num = input("Enter Number: ")
        f.writelines(num + "\n")

num = numbers_in_file(file)

print(num)