# Program to check if a given word is palindrome or not

word = 'never odd or even'

new_word = ""  # not considering solution spaces that's why new word

for ch in word:
    if ch != " ":
        new_word += ch

length = len(new_word)

flag = True
for i in range(length // 2):

    if new_word[i] != new_word[length - i - 1]:
        flag = False
        break

if flag:
    print(f"{word} is a palindrome")
else:
    print(f"{word} is not a palindrome")

print()
print("------------------------------------")
print("Another solution")
print()

word = 'racecar'

word_to_list = list(word)
word_to_list.reverse()

if list(word) == word_to_list:
    print(f"{word} is a palindrome")
else:
    print(f"{word} is not a palindrome")
