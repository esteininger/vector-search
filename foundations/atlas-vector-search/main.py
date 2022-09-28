from sentence_transformers import SentenceTransformer
import pymongo
from pprint import pprint

# import the embedding model
# https://huggingface.co/obrizum/all-MiniLM-L6-v2
model = SentenceTransformer('obrizum/all-MiniLM-L6-v2')

# mongo
mongo_uri = ""
# connection object
connection = pymongo.MongoClient(mongo_uri)
vector_collection = connection['eap']['vector']

# strings as an array that we will
products = [
    {"name": "Mozzarella"},
    {"name": "Parmesan"},
    {"name": "Cheddar"},
    {"name": "Brie"},
    {"name": "Swiss"},
    {"name": "Gruyere"},
    {"name": "Feta"},
    {"name": "Gouda"},
    {"name": "Provolone"},
    {"name": "Monterey Jack"}
]

# create a new embedding field for each product object
for product in products:
  # convert to embedding, then to array
    embeddings = model.encode(product['name']).tolist()
    product['embedding'] = embeddings
    vector_collection.insert(product)


query = "cheese"
vector_query = model.encode(query).tolist()

pipeline = [
    {
        "$search": {
            "knnBeta": {
                "vector": vector_query,
                "path": "embedding",
                "k": 10
            }
        }
    },
    {
        "$project": {
            "embedding": 0,
            "_id": 0,
            'score': {
                '$meta': 'searchScore'
            }
        }
    }
]

results = list(connection[database][collection].aggregate(pipeline))
print(results)
