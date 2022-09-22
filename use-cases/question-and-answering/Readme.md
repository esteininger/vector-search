
## Question and Answering

Using transformer architecture, we store a corpus (array of strings) as a vector embedding then send a human-native question also via a vector embedding to our similarity calculation.

[<img src="qa-preview.png" width="700">](https://www.youtube.com/watch?v=aiye4QDaf6g&ab_channel=ExplainLikeI%27m5)


### 1. Import Dependencies
We'll be using a popular pre-trained sentence transformer model. You can alternatively train your own or re-train an existing one.

``` python
from sentence_transformers import SentenceTransformer, util
model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
```
### 2. Prepare Corpus
Convert the corpus into an array of sentences. We do this to ensure our engine returns the most relevant independent thought.
``` python
corpus = "Japan is an island country in East Asia. It spans an archipelago of 6852 islands."
docs = corpus.split('.')
corpus_vector = model.encode(docs)
```
### 3. Prepare Question
Just like above, we convert the question into a vector.
``` python
query = "How many islands are comprised of Japan?"
query_vector = model.encode(query)
```
### 4. Calculate Similarity
The heart of vector search is in the similarity calculation. Here we use [cosine similarity](https://www.sbert.net/docs/package_reference/util.html#sentence_transformers.util.cos_sim) but you can experiment with others.
```python
scores = util.cos_sim(query_vector, corpus_vector)[0].cpu().tolist()
```
```text
It spans an archipelago of 6852 islands.
```

## Next Steps

1. Store your corpus vector embeddings in one of the many [Vector Search Engines](https://github.com/esteininger/vector-search/tree/master/foundations/vector-search-comparisons) out there.
2. Experiment with other similarity calculations (`euclidian` and `dot-product` to name a few)
3. [Store, version and scale](https://github.com/esteininger/vector-search#architecture) your embedding model

## Other Q&A Use Cases

- Chat Bot
- Support Agent
- FAQ Guidance
- Website Search Engine
