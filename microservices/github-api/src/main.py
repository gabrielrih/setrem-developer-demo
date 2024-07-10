from flask import Flask, jsonify, request

from .github import get_user, get_user_repos
from .queue import QueueManager
import env as envs


queue = QueueManager()
app = Flask(__name__)


INDEX_HTML = """
    <h1>GitHub API</h1>
    <h3>Version: {version}</h3>
"""


@app.route("/")
def index():
    return INDEX_HTML.format(version=envs.GITHUB_API_VERSION)


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


@app.route("/clone-repo", methods=["GET"])
def clone_repo():
    repo_url = request.args.get("repo_url")
    if not repo_url:
        return jsonify({"error": "Missing repo_url"}), 400
    response = queue.send_message(
        data = {
            'repo_url': repo_url
        }
    )
    return jsonify({"message": "Repository clone scheduled.", "sqs_response": response})


if __name__ == "__main__":
    app.run(port = envs.FLASK_PORT, debug=True)
