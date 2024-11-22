# Code for executing flask
from flask import Flask, render_template, request

app = Flask(__name__)

# main routes
# these routes redirect to the main pages

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/modules')
def modules():
    return render_template('Modulos.html')

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