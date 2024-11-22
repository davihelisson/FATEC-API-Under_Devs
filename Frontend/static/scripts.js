// Script para a verificação dos acertos.
function hiddenBox(){
    document.getElementById('result-panel').hidden = true;
}

function SubmitResults(correct, total){
    const form = document.getElementById('frm_sq');
    document.getElementById('score').value = correct;
    document.getElementById('total').value = total;
    form.submit();
}

function ScrumQuestions (){
    let contador = 0;
    const quest1 = document.getElementById('a3');
    const quest2 = document.getElementById('b2');
    const quest3 = document.getElementById('c2');
    const quest4 = document.getElementById('d3');
    const quest5 = document.getElementById('e3');
    const quest6 = document.getElementById('f2');
    const quest7 = document.getElementById('g1');
    const quest8 = document.getElementById('h2');
    const quest9 = document.getElementById('i2');
    const quest10 = document.getElementById('j1');
    if(quest1.checked){
        contador += 1;
    }
    if(quest2.checked){
        contador += 1;
    }
    if(quest3.checked){
        contador += 1;
    }
    if(quest4.checked){
        contador += 1;
    }
    if(quest5.checked){
        contador += 1;
    }
    if(quest6.checked){
        contador += 1;
    }
    if(quest7.checked){
        contador += 1;
    }
    if(quest8.checked){
        contador += 1;
    }
    if(quest9.checked){
        contador += 1;
    }
    if(quest10.checked){
        contador += 1;
    }
    SubmitResults(contador, 10);
}
function PoQuestions (){
    let contador = 0;
    const quest1 = document.getElementById('a2');
    const quest2 = document.getElementById('b2');
    const quest3 = document.getElementById('c3');
    const quest4 = document.getElementById('d1');
    const quest5 = document.getElementById('e3');
    const quest6 = document.getElementById('f1');
    const quest7 = document.getElementById('g3');
    const quest8 = document.getElementById('h2');
    const quest9 = document.getElementById('i4');
    const quest10 = document.getElementById('j2');
    if(quest1.checked){
        contador += 1;
    }
    if(quest2.checked){
        contador += 1;
    }
    if(quest3.checked){
        contador += 1;
    }
    if(quest4.checked){
        contador += 1;
    }
    if(quest5.checked){
        contador += 1;
    }
    if(quest6.checked){
        contador += 1;
    }
    if(quest7.checked){
        contador += 1;
    }
    if(quest8.checked){
        contador += 1;
    }
    if(quest9.checked){
        contador += 1;
    }
    if(quest10.checked){
        contador += 1;
    }
    SubmitResults(contador, 10);
}

function ScrumMasterQuestions (){
    let contador = 0;
    const quest1 = document.getElementById('a1');
    const quest2 = document.getElementById('b2');
    const quest3 = document.getElementById('c4');
    const quest4 = document.getElementById('d1');
    const quest5 = document.getElementById('e2');
    const quest6 = document.getElementById('f2');
    const quest7 = document.getElementById('g3');
    const quest8 = document.getElementById('h3');
    const quest9 = document.getElementById('i2');
    const quest10 = document.getElementById('j2');
    if(quest1.checked){
        contador += 1;
    }
    if(quest2.checked){
        contador += 1;
    }
    if(quest3.checked){
        contador += 1;
    }
    if(quest4.checked){
        contador += 1;
    }
    if(quest5.checked){
        contador += 1;
    }
    if(quest6.checked){
        contador += 1;
    }
    if(quest7.checked){
        contador += 1;
    }
    if(quest8.checked){
        contador += 1;
    }
    if(quest9.checked){
        contador += 1;
    }
    if(quest10.checked){
        contador += 1;
    }
    SubmitResults(contador, 10);
}

function DevTeamQuestions (){
    let contador = 0;
    const quest1 = document.getElementById('a2');
    const quest2 = document.getElementById('b1');
    const quest3 = document.getElementById('c3');
    const quest4 = document.getElementById('d2');
    const quest5 = document.getElementById('e3');
    const quest6 = document.getElementById('f2');
    const quest7 = document.getElementById('g4');
    const quest8 = document.getElementById('h3');
    const quest9 = document.getElementById('i3');
    const quest10 = document.getElementById('j2');
    if(quest1.checked){
        contador += 1;
    }
    if(quest2.checked){
        contador += 1;
    }
    if(quest3.checked){
        contador += 1;
    }
    if(quest4.checked){
        contador += 1;
    }
    if(quest5.checked){
        contador += 1;
    }
    if(quest6.checked){
        contador += 1;
    }
    if(quest7.checked){
        contador += 1;
    }
    if(quest8.checked){
        contador += 1;
    }
    if(quest9.checked){
        contador += 1;
    }
    if(quest10.checked){
        contador += 1;
    }
    SubmitResults(contador, 10);
}