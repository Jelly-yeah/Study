cen = input("请输入一个英文句子：")
new_words = [l.lower() for l in cen]
ltr = '{}[]<>()*&^%$#@!,.:;"-=_+\|'
letters = sorted(list(set(new_words)))
for i in letters:
    if i.isalpha():
        print("字母 ”{}“ 和 “{}” 一共出现了 {} 次".format(chr(ord(i)-32), i, new_words.count(i)))

print("\n非字母字符共计出现了 {} 次".format(new_words.count(ltr)))



# words = input("请输入一个英文句子：")
# d = {}
# for letter in words:
#     letter = letter.lower()
#     if letter.isalpha():
#         d[letter] = (d[letter] if letter in d else 0) + 1
# letters = sorted(d)
# for letter in letters:
#     print(letters, d[letter])



