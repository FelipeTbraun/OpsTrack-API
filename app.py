from flask import Flask

app = Flask(__name__)

@app.route('/tickets')
def tickets():
    mocked_tickets = [
        {'id': 1, 'titulo': 'Impressora sem conexão', 'status': 'aberto'},
        {'id': 2, 'titulo': 'Erro ao acessar internet', 'status': 'em andamento'},
        {'id': 3, 'titulo': 'Solicitação de novo monitor', 'status': 'fechado'},
    ]
    
@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

@app.route('/')
def status():
    return {'status':'Ok'}


    return {'tickets': mocked_tickets}

if __name__ == '__main__':
    app.run()
