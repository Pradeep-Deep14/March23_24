def extract_even_indices(lst):
    return [lst[i]for i in range(len(lst)) if i%2==0]

words=["hello","world","python","programming","is","fun"]
print(extract_even_indices(words))

#lst[i] - means it looks for the index position at 0,2,4
#only the index position goes into the even condition.