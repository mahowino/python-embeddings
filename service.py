from flask import jsonify
import openai
from utils import getEmbeddings
import pinecone
import numpy as np


limit = 3750
pinecone.init(api_key="2673672d-c5fd-4f95-b597-3bb651997a40", environment="gcp-starter")
metadata_config = {
    "indexed": ["chunks"]
}
# pinecone.create_index("example-index", dimension=1536, metadata_config=metadata_config)
# Initialize Pinecone client
# get api key from platform.openai.com
openai.api_key ='openaiKey'

embed_model = "text-embedding-ada-002"

def storeEmbeddings(data):
    try: 
        index = pinecone.GRPCIndex("example-index")
       
     # Convert the JSON data into the desired format
        vector = [(item['name'], item['values'], item['metadata']) for item in data]
        

        upsert_response = index.upsert(
           vector
        )

        embeddingFromOpenAi = data.get("data_chunk")
       
        if embeddingFromOpenAi is None:
            return jsonify({"error": "No 'data_chunk' key in the request data"}), 400
    

        return jsonify({"message": "Embedding stored successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500 




def searchEmbeddings(data):
    try:
        query_variable = data["query"]
        query_with_contexts = retrieve(query_variable)
        # then we complete the context-infused query
        
        result=complete(query_with_contexts,query_variable)
        return result
    except Exception as e:
        print(str(e))
        return jsonify({"error":str(e)}),500


def complete(prompt,query):
    # Query text-davinci-003
    res = openai.ChatCompletion.create(
        model='ft:gpt-3.5-turbo-0613:consumer-law-secrets-llc:cl-expert:83mrgZ5A',
         messages=[
             {"role": "system", "content": "You are an assistant and want to help the user. Use the following context to build your answer. Give the most emphasis on the user query"},
             {"role": "user", "content": "use the following context, ensure you include some items in the context. Here is the context:"+prompt},
             {"role": "assistant", "content": "Thank you for the context, now provide me with the prompt or question"},
             {"role": "user", "content": "this is the prompt,:"+query}
        ],
        temperature=0.6,
        max_tokens=2000,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        stop=None
    )
    return res.choices[0]["message"]["content"]

def retrieve(query):
    index = pinecone.GRPCIndex("example-index")
    res = openai.Embedding.create(
        input=[query],
        engine="text-embedding-ada-002"  # Define your OpenAI engine
    )

    # Retrieve from Pinecone
    xq = res['data'][0]['embedding']

    # Get relevant contexts
    res = index.query(xq, top_k=50, include_metadata=True)
    contexts = [
        x['metadata']['chunks'] for x in res['matches']
    ]
    print(contexts[1])
    # Build our prompt with the retrieved contexts included
    prompt_start = (
        
        "Context:\n"
    )
    prompt_end = (
        "\n\n"
    )
    
    # Define your context limit
    limit = 1000  # Set your desired context limit here

    # Append contexts until hitting the limit
    for i in range(1, len(contexts)):
        if len("\n\n---\n\n".join(contexts[:i])) >= limit:
            prompt = (
                prompt_start +
                "\n\n---\n\n".join(contexts[:i-1]) +
                prompt_end
            )
            break
        elif i == len(contexts)-1:
            prompt = (
                prompt_start +
                "\n\n---\n\n".join(contexts) +
                prompt_end
            )
    return prompt
