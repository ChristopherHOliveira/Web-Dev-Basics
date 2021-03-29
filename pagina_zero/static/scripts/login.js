// requisição AJAX

// chamando os elementos de id 'txt-usuario' e 'msg-erros'
const txtUsuario = document.getElementById('txt-usuario');
const pErro = document.getElementById('msg-erros');


    // chamada AJAX utilizando o fetch API

// adicionando um evento na mudança do foco do campo de texto
txtUsuario.addEventListener('change', function(){

    // passando o conteudo (value) da constante txtUsuario para a variável 'usuario'
    let usuario = txtUsuario.value;

    pErro.innerText = '';

    // testando se a variavel 'usuario' não é uma sring vazia
    if (usuario){
        fetch('verifica_usuario/' + usuario).then(function(resposta){
            
            return resposta.json();

        }).then(function(json){

            console.log(json);

            let msg = json['msg2'];

            //verificando se a variável msg possui a substring 'não existe'
            if (msg.includes('não existe')){ 
                pErro.innerText = msg;
            }
        });
    }
});


// chamada AJAX utilizando XMLHttpRequest
// está com algum erro:
/* Uncaught TypeError: json is not a function
    at XMLHttpRequest.xhr.onreadystatechange (login.js:49)
xhr.onreadystatechange @ login.js:49
XMLHttpRequest.send (async)
(anonymous) @ login.js:56 

txtUsuario.addEventListener('change', function(){
    let usuario = txtUsuario.value;
    pErro.innerText = '';
    if (usuario){
        let xhr = new XMLHttpRequest();
        xhr.onreadystatechange = function(){
            if (xhr.readyState == XMLHttpRequest.DONE){
                let json = JSON.parse(xhr.responseText);
                let msg = json('msg2');
                if (msg.includes('não existe')){
                    pErro.innerText = msg;
                }
            }
        }
        xhr.open('GET', 'verifica_usuario/' + usuario, true);
        xhr.send(null);
    }
});  */