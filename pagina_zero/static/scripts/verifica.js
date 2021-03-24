const botao_submit = document.getElementById('bt-submit')
const botao_reset = document.getElementById('bt-reset')
const nome = document.getElementById('txt-nome')
const email = document.getElementById('txt-email')
const mensagem = document.getElementById('txt-mensagem')
const p_erros = document.getElementById('erros')
const assuntos = document.getElementById('sel-assunto')

//testando o acesso ao value do input nome:
//nome.value = "testando atribuição de nome pelo javascript 2"

/*ao apertar o botão submit, verifica antes se o campo nome está em branco*/
botao_submit.addEventListener('click', function(event){
    let erros = '';
    if (nome.value == '') {
        erros = erros + 'O nome não pode estar vazio! <br>';
        event.preventDefault();
    }
    if (email.value == '') {
        erros = erros + 'O e-mail não pode estar vazio! <br>';
        event.preventDefault();
    }
    if (mensagem.value == '') {
        erros = erros + 'A mensagem não pode estar vazia! <br>';
        event.preventDefault();
    }
    if (assuntos.value == 0) {
        erros = erros + 'Selecione um assunto!';
        event.preventDefault();
    }
    p_erros.innerHTML = erros;
});

/*
Posso escrever eventos de clicar botão e mudança
de eventos da seguinte forma:

botao_reset.addEventListener('click', function(event){
    p_erros.innerText = '';
});

//deixar nome em letras maiúsculas:
nome.addEventListener('change', function(event){
    nome.value = nome.value.toUpperCase();
})
*/

botao_reset.onclick = function(event){
    p_erros.innerText = '';
}

nome.onchange = function(event){
    nome.value = nome.value.toUpperCase();
}
