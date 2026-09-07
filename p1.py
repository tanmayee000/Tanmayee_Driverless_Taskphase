n = int(input("Enter n: "))
words = []
for i in range(n):
 words.append(input("Enter string: "))
freq = {}
for word in words:
 word = word.lower()
 for ch in word:
 if ch.isalpha():
 if ch in freq:
 freq[ch] += 1
 else:
 freq[ch] = 1
print(freq)
