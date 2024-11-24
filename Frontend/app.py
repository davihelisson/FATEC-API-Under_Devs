# Code for executing flask
from flask import Flask, render_template, request, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Chave secreta para segurança das sessões

# main routes
# these routes redirect to the main pages

def initialize_session():
    for variable_name in ['score_scrum_generics', 'score_product_owner', 'score_scrum_master', 'score_dev_team', 'score_final_exam']:
        session.setdefault(variable_name, 0)

@app.route('/')
def index():
    initialize_session()
    return render_template('index.html')

@app.route('/modules')
def modules():
    def check_progress(score):
        return ('checked', '') if int(score) >= 6 else ('', 'hidden')

    initialize_session()

    scrum_checked, scrum_show = check_progress(session['score_scrum_generics'])
    po_checked, po_show = check_progress(session['score_product_owner'])
    sm_checked, sm_show = check_progress(session['score_scrum_master'])
    dt_checked, dt_show = check_progress(session['score_dev_team'])
    fx_show = 'hidden'
    
    c1 = int(session['score_scrum_generics']) >= 6
    c2 = int(session['score_product_owner']) >= 6
    c3 = int(session['score_scrum_master']) >= 6
    c4 = int(session['score_dev_team']) >= 6

    if c1 and c2 and c3 and c4:
        btn_fx = ''
        if int(session['score_final_exam']) > 0:
            fx_show = ''
    else:
        btn_fx = 'display:none'

    return render_template(
        'Modulos.html',
        score_scrum_generics=scrum_checked,
        score_product_owner=po_checked,
        score_scrum_master=sm_checked,
        score_dev_team=dt_checked,
        sc_show=scrum_show,
        po_show=po_show,
        sm_show=sm_show,
        dt_show=dt_show,
        fx_show=fx_show,
        sc_points=session['score_scrum_generics'],
        po_points=session['score_product_owner'],
        sm_points=session['score_scrum_master'],
        dt_points=session['score_dev_team'],
        fx_points=session['score_final_exam'],
        sc_total=10,
        po_total=10,
        sm_total=10,
        dt_total=10,
        fx_total=20,
        btn_fx = btn_fx
    )

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
    return render_template('/evaluations/FinalExamQuestions.html')

@app.route('/SobreNos')
def SobreNos():
    return render_template('SobreNos.html')

# Review dos resultados das avaliações

@app.route('/review', methods=['POST'])
def ReviewScore():
    total = ''
    current = ''
    if request.method == 'POST':
        if request.form['module'] == 'sc':
            session['score_scrum_generics'] = request.form['score']
            current = 'score_scrum_generics'
            
        elif request.form['module'] == 'po':
            session['score_product_owner'] = request.form['score']
            current = 'score_product_owner'
            
        elif request.form['module'] == 'sm':
            session['score_scrum_master'] = request.form['score']
            current = 'score_scrum_master'
            
        elif request.form['module'] == 'dt':
            session['score_dev_team'] = request.form['score']
            current = 'score_dev_team'

        elif request.form['module'] == 'fx':
            session['score_final_exam'] = request.form['score']
            current = 'score_final_exam'
            
        total = request.form['total']
    return render_template('/evaluations/Redirect.html', result = f'{session[current]} de {total}')