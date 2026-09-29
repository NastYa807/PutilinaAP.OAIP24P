with open('data.txt', 'w', encoding='utf-8') as file:
    names = ['Hello', 'Hi', 'Bye']
    for name in names:
        file.write(name + '\n')

print("Данные записаны в файл data.txt")

with open('data.txt', 'r', encoding='utf-8') as file:
    content = file.readlines()

print("Содержимое файла:")
for line in content:
    print(line.strip())

