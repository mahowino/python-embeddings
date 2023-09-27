from flask import jsonify
from utils import getEmbeddings
import random
import pinecone
import time
import numpy as np
import pandas


pinecone.init(api_key="2673672d-c5fd-4f95-b597-3bb651997a40", environment="gcp-starter")
metadata_config = {
    "indexed": ["color"]
}
pinecone.create_index("example-index", dimension=8, metadata_config=metadata_config)
# Initialize Pinecone client

def storeEmbeddings(data):
    try: 
        index = pinecone.GRPCIndex("example-index")

        upsert_response = index.upsert(
            vectors=[
                ("a", [0.1,0.2, 0.3, 0.4,0.5,0.6,0.7,0.8],{"color": "drama"}),
                ("b", [0.2,0.3, 0.4, 0.5,0.6,0.7,0.8,0.9,],{"color": "drama"}),
            ],
 )
        embeddingFromOpenAi = data.get("data_chunk")
       
        if embeddingFromOpenAi is None:
            return jsonify({"error": "No 'data_chunk' key in the request data"}), 400
    

        return jsonify({"message": "Embedding stored successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500 

def searchEmbeddings(query):
      
        query_vector=getEmbeddings(text_chunk=query);

        if query_vector is None:
            return jsonify({"error": "No 'query_vector' key in the request data"}), 400

        # Search Pinecone index by query_vector
        results = pinecone.query(queries=[query_vector], top_k=10)  

        # Extract the results
        search_results = []
        for result in results[0].matches:
            search_results.append({"id": result.id, "score": result.score})

        return jsonify({"results": search_results}), 200