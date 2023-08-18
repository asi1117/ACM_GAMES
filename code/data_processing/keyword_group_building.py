import pandas as pd
from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence


csv_file = '.csv'
data = pd.read_csv(csv_file)


sentences = data['review'].tolist()


temp_file = 'temp_corpus.txt'
with open(temp_file, 'w', encoding='utf-8') as f:
    for sentence in sentences:
        f.write(sentence + '\n')


corpus_sentences = LineSentence(temp_file)


model = Word2Vec(corpus_sentences, vector_size=100, window=5, min_count=5, sg=0)  # 根据需要调整参数


model.save('word2vec_model.model')


model = Word2Vec.load('word2vec_model.model')


keyword = 'controller' 
if keyword in model.wv:
    vector = model.wv[keyword]
    print(f'向量表示: {vector}')
else:
    print(f'controller "{keyword}" 不在词汇表中。')


similar_words = model.wv.most_similar(keyword, topn=5)
print(f'与"{keyword}"相似的词语:')
for word, score in similar_words:
    print(f'{word}: {score}')


