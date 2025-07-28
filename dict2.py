
str = "hello world"

dic = {}


for i in str:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1


print("Character Frequencies:")
for i, freq in dic.items():
    print(f"'{i}': {freq}")
