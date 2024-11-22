# Code for executing flask
from flask import Flask, render_template, request, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Chave secreta para segurança das sessões

# main routes
# these routes redirect to the main pages

# initialize session
def InitializeSession():
    for variable_name in ['score_scrum_generics', 'score_product_owner', 'score_scrum_master', 'score_dev_team']:
        # Check if the variable exists in the session
        if variable_name not in session:
            # If not, initialize it to 0
            session[variable_name] = 0
# app all routes

@app.route('/')
def index():
    InitializeSession()
    return render_template('index.html')

@app.route('/modules')
def modules():
    chk_scrum = ''
    chk_po = ''
    chk_sm = ''
    chk_dvtm = ''
    InitializeSession()
    if int(session['score_scrum_generics']) >= 6:
        chk_scrum = 'checked'
    if int(session['score_product_owner']) >= 6:
        chk_po = 'checked'
    if int(session['score_scrum_master']) >= 6:
        chk_sm = 'checked'
    if int(session['score_dev_team']) >= 6:
        chk_dvtm = 'checked'
    return render_template('Modulos.html', score_scrum_generics = chk_scrum, score_product_owner  = chk_po, score_scrum_master = chk_sm, score_dev_team = chk_dvtm)

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
    total = ''
    if request.method == 'POST':
        if request.form['module'] == 'sc':
            session['score_scrum_generics'] = request.form['score']
        elif request.form['module'] == 'po':
            session['score_product_owner'] = request.form['score']
        elif request.form['module'] == 'sm':
            session['score_scrum_master'] = request.form['score']
        elif request.form['module'] == 'dt':
            session['score_dev_team'] = request.form['score']
        total = request.form['total']
    return render_template('/evaluations/Redirect.html', result = f'{session['score_scrum_generics']} de {total}')