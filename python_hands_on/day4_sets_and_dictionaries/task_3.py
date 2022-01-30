word = 'banana'

s = set(word)

dict_word1 = {
}

for ch in s:
    dict_word1[ch] = 0

for ch in word:
    dict_word1[ch] += 1

for k, v in dict_word1.items():
    if v > 1:
        print(f"#{k} - {v}")


print()
print("-------------------------------")
print("Another solution:")
print()
word = 'missisippi'

for ch in set(word):
    count = word.count(ch)
    if count > 1:
        print(f"#{ch} - {count}")