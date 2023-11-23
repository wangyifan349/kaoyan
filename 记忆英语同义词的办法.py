from nltk.corpus import wordnet as wn

# 定义一个常用形容词列表
common_adjectives = ["happy"]

# 遍历列表，获取每个形容词的同义词集、定义、例句和相似词语
for adj in common_adjectives:
    # 获取形容词的同义词集，注意使用pos='a'来指定词性为形容词
    adj_synsets = wn.synsets(adj, pos=wn.ADJ)
    
    for synset in adj_synsets:
        # 打印形容词及其定义和例句
        print(f"形容词: {synset.name().split('.')[0]}")
        print(f"定义: {synset.definition()}")
        if synset.examples():
            print(f"例句: {'; '.join(synset.examples())}")
        else:
            print("例句: 无")
        
        # 打印同义词集中的同义词
        synonyms = [lemma.name() for lemma in synset.lemmas()]
        print(f"同义词: {', '.join(synonyms)}")
        
        # 打印近义词
        #similar_tos = synset.similar_tos()
        #if similar_tos:
            #similar_words = [similar_synset.lemmas()[0].name() for similar_synset in similar_tos]
            #print(f"！！近义词: {', '.join(similar_words)}")
        #else:
            #print("近义词: 无")

        print()  # 输出更美观
