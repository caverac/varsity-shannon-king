from nltk.book import text1

print("=============")

# concordance = text1.concordance("whale")
similar = text1.similar("boat", num=10)


print(similar)
# positional arguments
# key-value arguments
