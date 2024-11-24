import requests, jsonpath

# headers = {'Authorization' : 'Token SEUTOKEN'}

# url = 'http://127.0.0.1:8000/empresa/'

# nova_empresa = {
#     'cnpj': '123456769876',
#     'name': 'tim',
#     'razao_social': 'TIM',
#     'sede': 'São Paulo',
#     'estado': 'SP',
#     'ranking': '9'
#     }


# resultado = requests.post(url = url, data = nova_empresa)
# print(resultado.json())



class TestEmpresas():
    url_empresa = 'http://127.0.0.1:8000/empresa/'
    
    nova_empresa = {
        'cnpj': '1234567866789',
        'name': 'CLARO',
        'razao_social': 'CLARO',
        'sede': 'São Paulo',
        'estado': 'SP',
        'ranking': '7'
        }
    
    def test_get_empresa(self):
        resposta = requests.get(url = self.url_empresa)
        assert resposta.status_code == 200
    
    def test_post_empresa(self):
        resultado = requests.post(url = self.url_empresa, data = self.nova_empresa)
        assert resultado.status_code == 201