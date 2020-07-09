from app import app
from app.esearch import search
from flask import Flask,render_template,request
from app.forms import PhenCardsForm
from app.config import Config




# @app.route('/')
# @app.route('/index')
# def index():
#     """
#     Search for products across a variety of terms, and show 9 results for each.
#     """
#     return render_template('index.html')
app.config.from_object(Config)


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

@app.route('/', methods=["GET", "POST"])
def phencards():
    form = PhenCardsForm()
    phen_name = "Cleft Plate"
    INDEX_LIST = ['icd10','msh','doid','umls']

    if form.validate_on_submit():
        phen_name = form.phenname.data.strip()
        hits = search(phen_name,INDEX_LIST)
        return render_template(
            'results.html',
            hits=hits
        )
    return render_template('index.html', form=form)