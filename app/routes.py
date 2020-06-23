from app import app
from app.search import search
from flask import Flask
from flask import render_template
from flask import request


@app.route('/')
@app.route('/index')
def index():
    """
    Search for products across a variety of terms, and show 9 results for each.
    """
    return render_template('index.html')


@app.route('/search', methods=['GET', 'POST'])
def search_single_product():
    """
    Execute a search for a specific search term.
    Return the top 50 results.
    """
    query = request.args.get('search')
    hits = search(query)
    return render_template(
        'result.html',
        hits=hits
    )