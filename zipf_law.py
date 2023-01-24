import string
import math
import operator
import matplotlib.pyplot as plt

# Read text from file
with open("book.txt", encoding='utf-8') as file:
    text = file.read().lower()

# Remove punctuation
text = text.translate(text.maketrans("", "", string.punctuation))

# Split text into words
words = text.split()

# Count word frequencies
word_freq = {}
for word in words:
    if word in word_freq:
        word_freq[word] += 1
    else:
        word_freq[word] = 1

# Sort words by frequency
sorted_words = sorted(word_freq.items(), key=operator.itemgetter(1), reverse=True)

# Print log f and log r for each word
log_f = []
log_r = []
for i, (word, freq) in enumerate(sorted_words):
    log_f.append(math.log10(freq))
    log_r.append(math.log10(i + 1))
    print(f"{word}: log f = {log_f[-1]}, log r = {log_r[-1]}")

# Plot log f vs log r
plt.plot(log_r, log_f)
plt.xlabel("log r")
plt.ylabel("log f")
plt.show()
