from flask import Flask, jsonify, request
from algorithms import create_algorithm

app = Flask(__name__)

@app.route("/api/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"})
@app.route("/api/algorithms", methods=["GET"])
def get_algorithms():
    return jsonify({"algorithms": ["bubble", "selection", "quick"]})
@app.route("/api/sort", methods=["POST"])
def sort():
    data = request.get_json()
    arr  = data.get("data", [])
    algo = data.get("algorithm", "bubble")

    instance = create_algorithm(algo, arr)
    return jsonify({
        "algorithm":   algo,
        "sorted_data": instance.sort()
    })

@app.route("/", methods=["GET"])
def index():
    return jsonify({
        "message": "Flask API работает",
        "endpoints": [
            "/api/health",
            "/api/algorithms",
            "/api/sort",
            "/api/tree",
            "/api/tree/traverse",
            "/api/graph/dfs",
            "/api/graph/bfs"
        ]
    })
from tree import BST

@app.route("/api/tree", methods=["POST"])
def build_tree():
    data   = request.get_json()
    values = data.get("values", [])
    if not values:
        raise EmptyDataError()

    bst = BST()
    for v in values:
        bst.insert(v)

    return jsonify({
        "tree":   bst.to_dict(),
        "count":  bst.count,
        "height": bst.get_height()
    })
if __name__ == "__main__":
    app.run(port=5000, debug=True)