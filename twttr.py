str= input("text:")
new_text=""

vowels= ['a', 'e', 'i', 'o', 'u',  'A', 'E', 'I', 'O', 'U']

for i in range(len(str)):
    if str[i] not in vowels:
        new_text+=str[i]

print(new_text)