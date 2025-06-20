# app.py
from flask import Flask, render_template, request, jsonify
from scraper import scrape_truemeds

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scrape', methods=['POST'])
def scrape():
    query = request.form.get('query')
    if not query:
        return jsonify({"error": "No query provided"}), 400
    df = scrape_truemeds(query)
    return df.to_json(orient='records')

if __name__ == '__main__':
    app.run(debug=True)
