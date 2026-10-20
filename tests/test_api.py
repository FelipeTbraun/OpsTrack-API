def test_status_retorna_ok(client):
    resposta = client.get('/status')
    assert resposta.status_code == 200
    assert resposta.get_json()['status'] == 'ok'

def test_usuarios_retorna_dois_usuarios(client):
    resposta = client.get('/usuarios')
    assert resposta.status_code == 200
    assert len(resposta.get_json()['usuarios']) == 2

def test_rota_inexistente_retorna_404(client):
    resposta = client.get('/nao-existe')
    assert resposta.status_code == 404