# put here the file with the scramble words(separated with new lines)
with open("scrambled.txt") as file:
	scrambled_words = [x.strip() for x in file.readlines() if x.strip() != ""]

# put here the file with the wordlist
with open("wordlist.txt") as file:
	dictionary = [x.strip() for x in file.readlines()]

# if they give you more than 10 words modify here
result = ["" for i in range(10)]

for i, word in enumerate(scrambled_words):
	for d in dictionary:
		if len(word) == len(d):
			mix = list(word)
			original = list(d)

			for k in mix:
				if k in original:
					original.remove(k)
			if len(original) == 0:
				result[i] = d

print("".join([x+"," for x in result]))
