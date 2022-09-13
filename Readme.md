## Vector Search

Vector Search provides the capability for developers to **store** dense vectors, structured around certain algorithms (i.e. KNN), and an engine to **compute** similar vectors (i.e. euclidean distance) for relevance score calculation.

This repository provides a comprehensive overview of the vector search landscape inclusive of tutorials, guides, best-practices, and extended learning. Please review the [Education](https://github.com/esteininger/vector-search#education) section to learn more.

Here is how you may use a Vector Search engine within your application search engine architecture:

<center><img src="/assets/diagram.png"></center>

## Topics

🧑‍🏫 **Introduction** - Learn the core concepts of vector-based information retrieval.

🥝 **Foundation** - Implement Vector Searching to retrieve contextually similar content.

🎬 **Use Cases** - Understand where it makes sense to use vector search.

💵 **Architecture** - Guides on how to use vector search in your architecture.

## Foundations

| #   | Label                                 | Description                                                                                                               |
| --- | ------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| 1   | [Word vs Vector Search](#)            | The difference between standard (TF-IDF) word search and vector search and when to use each.                              |
| 2   | [DIY Word Embeddings](#)              | An educational walkthrough of building your own word embedding vector model.                                              |
| 3   | [TBD Vector Search](#)                | Guides that showcase TBD's vector search implementation.                                                                  |
| 4   | [Vector Model Comparisons](#)         | A comparison of the most popular vector models and trade-offs between each.                                               |
| 5   | [Vector Search Engine Comparisons](#) | A comparison of the most popular vector search engines comparing query syntax, index definitions and document structures. |

## Use Cases

| #   | Label                                                       | Description                                           |
| --- | ----------------------------------------------------------- | ----------------------------------------------------- |
| 1   | [Sentence Similarity](#)                                    | Determination of how similar to texts are.            |
| 2   | [Named Entity Recognition](#)                               | Classification of text into pre-defined categories.   |
| 3   | [Question and Answering](/use-cases/question-and-answering) | Building systems that automatically answer questions. |
| 4   | [Personalization](#)                                        | Using client data to personalize query results.       |
| 5   | [Automated Synonym Creation](#)                             | Lorem ipsum.                                          |
| 6   | [Content Creation](#)                                       | Lorem ipsum.                                          |

## Architecture

| #   | Source                      | Description                                                                   |
| --- | --------------------------- | ----------------------------------------------------------------------------- |
| 1   | [Reference Architecture](#) | Common best-practices for deploying vector search architecture in production. |
| 2   | [Model Hosting](#)          | Suggestions on how to host your vector models.                                |
| 3   | [Model Versioning](#)       | Common best-practices for versioning your models as they evolve.              |
| 4   | [Feedback Loops](#)         | Lorem ipsum.                                                                  |

## Education

Although a challenging topic to grasp, there's a myriad of educational resources at your disposal.

- [Attention Is All You Need Research Paper](https://arxiv.org/pdf/1706.03762.pdf)
- [Google Vector Search](https://cloud.google.com/blog/topics/developers-practitioners/find-anything-blazingly-fast-googles-vector-search-technology)
- [Lucene KNN Discussion](https://issues.apache.org/jira/browse/LUCENE-9004)
- [Transformers by Pinecone](https://www.pinecone.io/learn/transformers/)
- [BERT Research Paper](https://arxiv.org/pdf/1810.04805.pdf)
- [Transformers by Huggingface](https://aclanthology.org/2020.emnlp-demos.6.pdf)

## Gratitude

This repository wouldn't be possible without several key individuals:

- [Nick Gogan](https://github.com/nickgogan)
