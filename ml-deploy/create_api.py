import  os

def create_api():
    """this builds the api file"""
    api_constant = """
from flask import Flask, request, jsonify
import score

app = Flask(__name__)

@app.route("/score/", methods=['POST'])
def score():
    _json = request.json
    score_results = score.score(_json)
    return jsonify(score_results)

if __name__ == '__main__':
    #run the app
    app.run(host='0.0.0.0', debug=False)"""

    with open("app.txt", 'w') as f:
        f.write(api_constant)
    os.rename("app.txt", "app.py")
