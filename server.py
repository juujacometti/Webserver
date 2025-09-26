# from http.server import SimpleHTTPRequestHandler, HTTPServer 

# # Definindo a porta
# port = 8080

# # Definindo o gerenciador / manipulador de requisições
# handler = SimpleHTTPRequestHandler

# # Criando a instância servidor
# server = HTTPServer(("localhost", port), handler)

# # Imprimindo mensagem de ok
# print(f"Server runing in http://localhost:{port}")

# server.serve_forever()


"""
from http.server import SimpleHTTPRequestHandler, HTTPServer
 
#Definindo a porta
port = 8000
 
#Definindo o gerenciador/manipulador de requisições
handler = SimpleHTTPRequestHandler
 
#Criando a instância servidor
server = HTTPServer(("localhost", port), handler)
 
#Imprimindo mensagem
print(f"Server Initiated in http://localhost:{port}")
 
server.serve_forever()
"""
 
import os    # Import para manipular caminhos de arquivos
from http.server import SimpleHTTPRequestHandler, HTTPServer    # Import para lidar com requisições HTTP (GET/POST) e inicialização do servidor
from urllib.parse import parse_qs    # Transforma dados de formulário em dicionários de python
import json
  
# Classe que herda de 'SimpleHTTPRequestHandler', ajudando a adptar o servidor ao meu projeto
class MyHandle(SimpleHTTPRequestHandler):
    # Função para mostrar uma lista de arquivos
    def list_directory(self, path):
        try:
            # Abre o 'index.html' e mostra no lugar da "lista"
            f = open(os.path.join(path, 'index.html'), 'r')

            # Cabeçalho do header
            self.send_response(200)
            self.send_header("Content-type", "text/html")    # Define que a resposta é HTML
            self.end_headers()    # Finaliza o cabeçalho
            self.wfile.write(f.read().encode('UTF-8'))    # Escreve o conteúdo do arquivo no navegador
            f.close()
            return None
        
        # Caso não encontre o 'index.html', retorna um erro padrão HTML (404)
        except FileNotFoundError:
            pass
        return super().list_directory(path)

    # Verificação simples de usuário logado ou não logado
    # Definição de usuário / senha fixo
    def account_user(self, login, password):
        loga = "julya@gmail.com"
        senha = "12345"

        # Verifica se o login / senha correspondem ao definido
        if login == loga and senha == password:
            return "Usuário logado"
        else:
            return "Usuário não existe "


    # Requisição do GET
    def do_GET(self):
        # === Login === #
        if self.path == "/login":    # Abre o arquivo 'login.html'
            try:
                with open(os.path.join(os.getcwd(), "login.html"), "r") as login:
                    content = login.read()
                self.send_response(200)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                self.wfile.write(content.encode('utf-8'))

            # Caso não encontre a página de login, retorna um 404
            except FileNotFoundError:
                self.send_error(404, "File not found")

        # === Cadastro === #
        elif self.path == "/cadastro":    # Abre o arquivo 'cadastro.html'
            try:
                with open(os.path.join(os.getcwd(), "cadastro.html"), "r") as cadastro:
                    content = cadastro.read()
                self.send_response(200)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                self.wfile.write(content.encode('utf-8'))

            # Caso não encontre a página de cadastro, retorna um 404
            except FileNotFoundError:
                self.send_error(404, "File not found")

        # === Listar filmes === #
        elif self.path == "/listar_filmes":    # Abre o arquivo 'listar_filmes.html'
            try:
                with open(os.path.join(os.getcwd(), "listar_filmes.html"), "r") as listar_filmes:
                    content = listar_filmes.read()
                self.send_response(200)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                self.wfile.write(content.encode('utf-8'))

            # Caso não encontre a página de listar_filmes, retorna um 404    
            except FileNotFoundError:
                self.send_error(404, "File not found")

        # === Index === #
        elif self.path == "/index":    # Abre o arquivo 'index.html'
            try:
                with open(os.path.join(os.getcwd(), "index.html"), "r") as index:
                    content = index.read()
                self.send_response(200)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                self.wfile.write(content.encode('utf-8'))

            # Caso não encontre a página de index, retorna um 404
            except FileNotFoundError:
                self.send_error(404, "File not found")

        # Cai em um 404 caso nenhum dos arquivos seja encontrado  
        else:
            super().do_GET()


    # Requisição do POST
    # Função chamada quando um formulário é enviado com método POST
    def do_POST(self):

        # === Login === #
        if self.path == '/send_login':    
            # Tamanho da requisição que está sendo mandada
            content_length = int(self.headers['Content-length'])    # Tamanho do corpo
            body = self.rfile.read(content_length).decode('utf-8')    # Lê o corpo e decodifica
            form_data = parse_qs(body)    # Transforma em dicionário

            # Lê os dados do formulário (usuário/senha)
            login = form_data.get('usuario', [""])[0]
            password = form_data.get('senha', [""])[0]
            logou = self.account_user(login, password)    # Utiliza 'account_user' para verificar usuário/senha

            # Printa as informações enviadas
            print("Data Form:")
            print("Usuario:", login)
            print("Senha:", password)

            # Envia a mensagem de sucesso / erro
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(logou.encode('utf-8'))

        # === Cadastro === #
        elif self.path == '/send_cadastro':

            # Tamanho da requisição que está sendo mandada
            content_length = int(self.headers['Content-length'])
            body = self.rfile.read(content_length).decode('utf-8')
            form_data = parse_qs(body)

            # Lê os dados do formulário de cadastro e cria um dicionário
            filme = {
                "titulo": form_data.get("titulo", [""])[0],
                "autores": form_data.get("autores", [""])[0],
                "diretores": form_data.get("diretores", [""])[0],
                "ano": form_data.get("ano", [""])[0],
                "genero": form_data.get("genero", [""])[0],
                "produtora": form_data.get("produtora", [""])[0],
                "sinopse": form_data.get("sinopse", [""])[0],
            }

            # Define o nome do arquivo json que será/foi criado
            json_file = "filmes.json"

            # Carrega dados existentes ou cria novos
            if os.path.exists(json_file):
                with open(json_file, "r", encoding="utf-8") as f:
                    try:
                        data = json.load(f)    # Carrega os filmes existentes

                    except json.JSONDecodeError:
                        data = []    # Se arquivo estiver vazio/corrompido, cria lista nova
            else:
                data = []

            # Adiciona novo filme
            data.append(filme)

            # Atualiza a lista 
            with open(json_file, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=4, ensure_ascii=False)

            # Resposta de sucesso para o navegador
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(b"<h2>Filme cadastrado com sucesso!</h2>")

        else:
            super(MyHandle, self).do_POST()

# Função principal
def main():
    server_address = ('', 8000)    # IP vazio = aceita em qualquer interface / porta 8000
    httpd = HTTPServer(server_address, MyHandle)    # Cria servidor usando sua classe
    print("Server running in http://localhost:8000")
    httpd.serve_forever()     # Mantém o servidor rodando

# Executa a função principal
main()
