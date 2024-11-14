# Code for executing flask
from flask import Flask, render_template

app = Flask(__name__)

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
    return render_template('ScrumTail.html')

# Submodulos routes

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