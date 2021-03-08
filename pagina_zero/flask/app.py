from flask import Flask

app = Flask('teste')

@app.route('/flask/app')
def funcao_teste():
    return '<h1>É galera, o flask funciona!</h1>'

app.run() 
