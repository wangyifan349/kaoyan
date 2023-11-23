from nltk.corpus import wordnet as wn

# 查询单词'dog'的所有同义词集
synsets = wn.synsets('dog')

# 遍历每个同义词集，打印出定义和例句
for synset in synsets:
    print(f"词义: {synset.name().split('.')[0]}")
    print(f"定义: {synset.definition()}")
    if synset.examples():
        print(f"例句: {'; '.join(synset.examples())}")
    else:
        print("例句: 无")
    print()  # 为了输出美观，增加空行

# 查询并打印第一个同义词集的上位词，这些词表示更一般的概念
print("上位词:")
for hypernym in synsets[0].hypernyms():
    print(f"{hypernym.name().split('.')[0]}")

# 查询并打印第一个同义词集的下位词，这些词表示更具体的分类或实例
print("\n下位词:")
for hyponym in synsets[0].hyponyms():
    print(f"{hyponym.name().split('.')[0]}")

# 查询并打印第一个同义词集中的所有词条，这些词条代表同义词集中的不同词
print("\n词条:")
for lemma in synsets[0].lemmas():
    print(f"{lemma.name()}")
