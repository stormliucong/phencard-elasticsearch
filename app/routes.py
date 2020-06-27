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
    if not query:
        query = "Cleft Plate"
    index_list = ['icd10','msh','doid','umls']
    if not request.args.get('icd10'):
        index_list.remove('icd10')
    if not request.args.get('msh'):
        index_list.remove('msh')
    if not request.args.get('doid'):
        index_list.remove('doid')
    if not request.args.get('umls'):
        index_list.remove('umls')
    
    print(index_list)

    hits = search(query,index_list)
    return render_template(
        'result.html',
        hits=hits
    )