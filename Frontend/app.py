# Code for executing flask
from flask import Flask, render_template, request, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Chave secreta para segurança das sessões

# main routes
# these routes redirect to the main pages

# app all routes

@app.route('/')
def index():
    if 'score_scrum_generics' not in session:
        session['score_scrum_generics'] = 0
    if 'score_product_owner' not in session:
        session['score_product_owner'] = 0
    if 'score_scrum_master' not in session:
        session['score_scrum_master'] = 0
    if 'score_dev_team' not in session:
        session['score_dev_team'] = 0    
    return render_template('index.html')

@app.route('/modules')
def modules():
    return render_template('Modulos.html', checked = 'checked')

@app.route('/DevTeamTail')
def devTeamTail():
    return render_template('DevTeamTail.html')

@app.route('/ProductOwner')
def ProductOwner():
    return render_template('ProductOwner.html')

@app.route('/ScrumTail')
def ScrumTail():
    return render_template('ScrumTail.html')

@app.route('/ScrumMaster')
def ScrumMaster():
    return render_template('ScrumMaster.html')

# module routes
# these routes redirect to the scrum modules

@app.route('/DevTeamQuestions')
def DevTeam():
    return render_template('/evaluations/DevTeamQuestions.html')

@app.route('/ProductOwnerQuestions')
def Po():
    return render_template('/evaluations/PoQuestions.html')

@app.route('/ScrumMasterQuestions')
def ScrumM():
    return render_template('/evaluations/ScrumMasterQuestions.html')

@app.route('/ScrumQuestions')
def Scrum():
    return render_template('/evaluations/ScrumQuestions.html')

@app.route('/FinalExamQuestions')
def FinalExam():
    return render_template('/evaluations/FinalExam.html')

@app.route('/SobreNos')
def SobreNos():
    return render_template('SobreNos.html')

# Review dos resultados das avaliações

@app.route('/review', methods=['POST'])
def ReviewScore():
    corrects = ''
    total = ''
    if request.method == 'POST':
        corrects = request.form['score']
        total = request.form['total']
    return render_template('/evaluations/Redirect.html', result = f'{corrects} de {total}')