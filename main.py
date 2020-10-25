from flask import Flask, request, jsonify
from underthesea import word_tokenize, pos_tag, ner, classify
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "hello word"

@app.route("/tokenize", methods=['POST'])
def tokenize():
    text = request.data
    tokenized = word_tokenize(text)
    return jsonify(tokenized)
 
@app.route("/pos", methods=['POST'])
def pos_tagging():
    text = request.data
    tagged = pos_tag(text)
    return jsonify(tagged)

@app.route("/ner", methods=['POST'])
def ner_tagging():
    text = request.data
    tagged = ner(text)
    return jsonify(tagged)

@app.route('/classify', methods=['POST'])
def category_classify():
    text = request.data
    tagged = classify(text)
    return jsonify(tagged)

if __name__ == '__main__':
    app.run(port=5000,debug=True)
