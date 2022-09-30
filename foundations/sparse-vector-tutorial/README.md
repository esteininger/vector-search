# Sparse Vector Tutorial

Search engines today work by converting text into numerical representations. Lucene, the most popular search engine calculates text into features known as sparse vectors. It does this by taking the frequency of terms (TF) and dividing it by the inverse of the frequency of the documents in the collection (IDF).

This walkthrough showcases how you can build a feature extraction engine (using the bag-of-words approach) that stores tokens as 1's and 0's to then become searchable. 

## Reference
[https://stackabuse.com/python-for-nlp-creating-bag-of-words-model-from-scratch/](https://stackabuse.com/python-for-nlp-creating-bag-of-words-model-from-scratch/)
