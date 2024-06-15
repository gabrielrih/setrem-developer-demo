import os
from flask import Flask, jsonify, request
from github import get_user, get_user_repos

app = Flask(__name__)

INDEX_HTML = """
    <h1>GitHub API</h1>
    <h3>Version: {version}</h3>
"""


@app.route("/")
def index():
    return INDEX_HTML.format(version=os.getenv("GITHUB_API_VERSION", "-"))


@app.route("/_health")
def health():
    return jsonify({"status": "healthy"})


@app.route("/github-user", methods=["GET"])
def github_user():
    username = request.args.get("username")
    if not username:
        return jsonify({"error": "Missing username"}), 400

    user = get_user(username)
    return jsonify({"user": user})


@app.route("/github-user-repos", methods=["GET"])
def github_user_repos():
    username = request.args.get("username")
    if not username:
        return jsonify({"error": "Missing username"}), 400

    user_repos = get_user_repos(username)
    return jsonify({"user_repos": user_repos})


if __name__ == "__main__":
    app.run(port=3000, debug=True)
