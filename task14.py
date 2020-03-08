def anagrams(word, words):
    finish = []
    lens = 0
    for i in words:
        lens = 0
        for w in word:
            if word.count(w) == i.count(w):
                continue
            else:
                break
        else:
            if len(word) == len(i):
                finish.append(i)
    return finish


print(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']))
print(anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']))

