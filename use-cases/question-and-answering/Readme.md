## Question and Answering

Using transformer architecture, we store a corpus (array of strings) as a vector embedding then send a human-native question also via a vector embedding to our similarity calculation.

1. Answers: Corpus (array of "answers") -> vector embedding -> store in database
2. Question: Question (as a string) -> vector embedding -> similarity calculation to find answers based on answers in database (dot product, )


### To-Do

- Uses Dot-Product for now, need to experiment with other similarity calculations like cosine and euclidian.
