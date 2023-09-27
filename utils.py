import openai


def getEmbeddings(text_chunk):
    # calculate embeddings
    EMBEDDING_MODEL = "text-embedding-ada-002"
    embeddings = []
    response = openai.Embedding.create(model=EMBEDDING_MODEL, input=text_chunk)

    for i, be in enumerate(response["data"]):
        assert i == be["index"]  
    batch_embeddings = [e["embedding"] for e in response["data"]]
    embeddings.extend(batch_embeddings)
    return embeddings;

