def mergeAlternately(word1, word2):
    mergedWord = []
    word2_cur = 0
    
    for i in word1:
        mergedWord.append(i)
        if word2_cur < len(word2):
            mergedWord.append(word2[word2_cur])
            word2_cur += 1


    mergedWord.extend(word2[word2_cur:])
    
    return ''.join(mergedWord)


print(mergeAlternately("be", "bab"))
