from flask import Flask, request, jsonify
from service import storeEmbeddings , searchEmbeddings

# Initialize Flask app
app = Flask(__name__)


@app.route("/store_embedding", methods=["POST"])
def store_embedding():
    try:
        print(request.json)
        storeEmbeddings(request.json)
        return jsonify({"message": "Embedding stored successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500



@app.route("/search", methods=["GET"])
def search_embeddings():
    try:
        searchEmbeddings(request.json.get("query"))
    except Exception as e:
        return jsonify({"error": str(e)}), 500



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
