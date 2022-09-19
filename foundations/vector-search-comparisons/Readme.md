# Vector Search Comparisons

This repository will discuss the various criteria to use when evaluating the landscape of vector search technologies.

|                                         	| Pinecone   	| Weaviate 	| Google     	| Elastic 	| Algolia    	| Vespa  	| Milvus 	| Redis  	| Qdrant 	| OpenSearch 	|
|-----------------------------------------	|------------	|----------	|------------	|---------	|------------	|--------	|--------	|--------	|--------	|------------	|
| [Hosting](#Hosting)                     	| Cloud Only 	| Hybrid   	| Cloud Only 	| Hybrid  	| Cloud Only 	| Hybrid 	| Hybrid 	| Hybrid 	| Hybrid 	| Hybrid     	|
| [Performance](#Performance)             	|            	|          	|            	|         	|            	|        	|        	|        	|        	|            	|
| [MLOps](#MLOps)                         	|            	|          	|            	|         	|            	|        	|        	|        	|        	|            	|
| [Availability](#Availability)           	|            	|          	|            	|         	|            	|        	|        	|        	|        	|            	|
| [Security](#Security)                   	|            	|          	|            	|         	|            	|        	|        	|        	|        	|            	|
| [Cost](#Cost)                           	|            	|          	|            	|         	|            	|        	|        	|        	|        	|            	|
| [Community](#Community) 	|            	| 31       	|            	| 161     	|            	|        	| 194    	| 617    	| 28     	| 135        	|

# Criteria

## Hosting

Where is the search engine deployable?

- **Hybrid:** Can be deployed as a managed service in the cloud or self-managed on premise.
- **Cloud Only:** Can only be deployed as a managed service in the cloud.

## Performance

This gets challenging as some of the technologies are cloud exclusive and some are hybrid capable. We'll have to devise a benchmark that compares read/write SLAs against comparable hardware.
Ideally, we'll use [Locust.io](https://locust.io/) to simulate fixed throughput concurrency.

Proposed benchmarks below:

**Hardware Selection:**

-   Must select single node instances with comparable CPU, RAM, Disk, and IOPs

**Write:**

-   Insert 1,000,000 vectors with a fixed dimensionality (384) as an output from the most popular [sentence similarity transformer](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2)
-   Measure the time to completion/durability

**Read:**

-   Measure max reads/sec and query response latency
-   Fixed K value (10)
-   Will only be using cosine similarity to limit scope

## MLOps

## Availability

## Security

## Cost

## Community

With the caveat that some of these vector search engines are baked into a parent repository (i.e. Redis vector search within core Redis) we've taken the total number of contributors as of 9/19/2022.

# Database Details

### Pinecone

[Documentation](https://www.pinecone.io/docs/)

### Weaviate

[Documentation](https://weaviate.io/developers/weaviate/current/)

### Google

[Documentation](https://cloud.google.com/vertex-ai/docs/matching-engine/overview)

### Elastic

[Documentation](https://www.elastic.co/guide/en/elasticsearch/reference/current/dense-vector.html)

### Algolia

TBA

### Vespa

[Documentation](https://docs.vespa.ai/en/nearest-neighbor-search-guide.html#hybrid-sparse-and-dense-retrieval-methods-with-vespa)

### Milvus

[Documentation](https://milvus.io/docs)

### Redis

[Documentation](https://redis.io/docs/stack/search/reference/vectors/)

### Qdrant

[Documentation](https://qdrant.tech/documentation/)

### OpenSearch

[Documentation](https://opensearch.org/docs/latest/search-plugins/knn/approximate-knn/)

## References

-   [qdrant's open source benchmark](https://qdrant.tech/benchmarks/)
