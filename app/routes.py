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
    index_list = []
    if request.args.get('icd10'):
        index_list.append('icd10')
    if request.args.get('msh'):
        index_list.append('msh')
    if request.args.get('doid'):
        index_list.append('doid')
    if request.args.get('umls'):
        index_list.append('umls')
    
    print(index_list)

    hits = search(query,index_list)
    return render_template(
        'result.html',
        hits=hits
    )