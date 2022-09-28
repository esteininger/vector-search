## Vector Search

Vector Search engines provide the capability for developers to `store` vectors structured around certain algorithms (i.e. KNN), and an engine to `compute` similar vectors (like cosine distance) to determine which vectors are related. 

This repository provides a comprehensive overview of the vector search landscape inclusive of tutorials, guides, best-practices, and extended learning. Please review the [Education](https://github.com/esteininger/vector-search#education) section to learn more.

Here is how you may use a Vector Search engine within your application search architecture:

<center><img src="/assets/diagram.png"></center>

## Topics

🧑‍🏫 **Foundation** - Learn the core concepts of vector-based information retrieval.

🎬 **Use Cases** - Understand where it makes sense to use vector search.

💵 **Architecture** - Guides on how to use vector search in your architecture.

## Foundations

| # | Label                                                               | Description |
|:--|:--------------------------------------------------------------------|:---|
| 1 | Keyword vs Vector Search                                            | The difference between standard (TF-IDF) text search and vector search and when to use each. |
| 2 | DIY Word Embeddings                                                 | An educational walkthrough of building your own word embedding vector model. |
| 3 | [Atlas Vector Search Engine](/foundations/atlas-vector-search)                 | Guides that showcase MongoDB Atlas' vector search implementation. |
| 4 | [Vector Search Comparisons](/foundations/vector-search-comparisons) | A comparison of the most popular vector search engines. |

## Use Cases

| # | Label                                                       | Description |
|:--|:------------------------------------------------------------|:-----------|
| 1 | Sentence Similarity                                         | Determination of how similar to texts are. |
| 2 | Token Classification                                        | Classification of text into pre-defined categories. |
| 3 | [Question and Answering](/use-cases/question-and-answering) | Building systems that automatically answer questions. |
| 4 | Personalization                                             | Using client data to personalize query results. |
| 5 | Automated Synonym Creation                                  | Enriching synonyms collection automatically. |
| 6 | Summarization                                               | Reconstruction of a corpus into less words. |
| 7 | Conversational                                              | Dialogue response generation. |
| 8 | [File Search](/use-cases/file-search)                       | Searching the contents of files. |

## Architecture

| # | Source                 | Description                                     |
|:--|:-----------------------|:------------------------------------------------|
| 1 | Reference Architecture | Common best-practices for deploying vector search architecture in production. |
| 2 | Model Hosting          | Suggestions on how to host your vector models.  |
| 3 | Model Versioning       | Common best-practices for versioning your models as they evolve. |
| 4 | Feedback Loops         | Lorem ipsum.                                    |

## Education

Although a challenging topic to grasp, there's a myriad of educational resources at your disposal.

### Information Retrieval

Overarching field of education.

- [A Primer on Neural Network Models for Natural Language Processing](https://u.cs.biu.ac.il/~yogo/nnlp.pdf)
- [Speech and Language Processing](https://web.stanford.edu/~jurafsky/slp3/)
- [Introduction to Information Retrieval](https://nlp.stanford.edu/IR-book/)

### Transformer Architecture

Latest breakthrough in the area of converting human content (text, images, etc.) into vector representations.
Transformers are a deep learning model that utilize "self-attention", and differentially weigh the significance of each part of the input data.

-   [Transformers by Pinecone](https://www.pinecone.io/learn/transformers/)
-   [Transformers by Huggingface](https://aclanthology.org/2020.emnlp-demos.6.pdf)
-   [Attention Is All You Need Research Paper](https://arxiv.org/pdf/1706.03762.pdf)
-   [BERT Research Paper](https://arxiv.org/pdf/1810.04805.pdf)

### Similarity Search

In order to determine what is deemed relevant, computers need to measure the distance between points, in this case vectors.

-   [Lucene KNN MVP](https://issues.apache.org/jira/browse/LUCENE-9004) & [Follow-Up](https://issues.apache.org/jira/browse/LUCENE-10054)
-   [Google Vector Search](https://cloud.google.com/blog/topics/developers-practitioners/find-anything-blazingly-fast-googles-vector-search-technology)
- [HNSW Graphs Research Paper](https://arxiv.org/abs/1603.09320)

## Gratitude

This repository wouldn't be possible without several key individuals:

-   [Nick Gogan](https://github.com/nickgogan)
-   [Marcus Eagan](https://github.com/MarcusSorealheis)

## Watch for Changes

This is a living repository and will evolve as I learn and the landscape changes. Please subscribe to changes accordingly via:

<center><img src="/assets/watch.gif"></center>
