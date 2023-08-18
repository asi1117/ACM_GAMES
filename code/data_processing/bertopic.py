from bertopic import BERTopic
import csv
import os
from flair.embeddings import TransformerDocumentEmbeddings


# topic_model = BERTopic(embedding_model=roberta)


os.environ["TOKENIZERS_PARALLELISM"] = "false"

url = 'stop/'
docs = []
with open(url, 'r', encoding='UTF-8') as f:
    reader = csv.reader(f)
    for row in reader:
        if row:
            docs.append(row[0])

docs = docs[1:]
# models: all-MiniLM-L6-v2, all-mpnet-base-v2
# roberta = TransformerDocumentEmbeddings('roberta-base')

# embedding_model="all-mpnet-base-v2",
# calculate_probabilities=True
num_topics = 10
model = BERTopic(embedding_model="all-mpnet-base-v2",
                 nr_topics=num_topics,
                 diversity=0.1,
                 top_n_words=15,
                verbose=True)
topics, probabilities = model.fit_transform(docs)
model.get_topic_info()[1:num_topics]
print(model.get_topic_freq().head())
for i in range(num_topics):
    print(model.get_topic(i))
model.visualize_barchart(top_n_topics=num_topics)
