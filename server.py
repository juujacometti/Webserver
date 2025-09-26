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
 
import os
from http.server import SimpleHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs
import json
  

class MyHandle(SimpleHTTPRequestHandler):
    def list_directory(self, path):
        try:
            f = open(os.path.join(path, 'index.html'), 'r')

            # Cabeçalho do header
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(f.read().encode('UTF-8'))
            f.close()
            return None
        except FileNotFoundError:
            pass
        return super().list_directory(path)

    # Verificação simples de usuário logado ou não logado
    def account_user(self, login, password):
        loga = "julya@gmail.com"
        senha = "12345"

        if login == loga and senha == password:
            return "Usuário logado"
        else:
            return "Usuário não existe "

    # Requisição do GET
    def do_GET(self):
        if self.path == "/login":
            try:
                with open(os.path.join(os.getcwd(), "login.html"), "r") as login:
                    content = login.read()
                self.send_response(200)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                self.wfile.write(content.encode('utf-8'))
            except FileNotFoundError:
                self.send_error(404, "File not found")
        elif self.path == "/cadastro":
            try:
                with open(os.path.join(os.getcwd(), "cadastro.html"), "r") as cadastro:
                    content = cadastro.read()
                self.send_response(200)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                self.wfile.write(content.encode('utf-8'))
            except FileNotFoundError:
                self.send_error(404, "File not found")
        elif self.path == "/listar_filmes":
            try:
                with open(os.path.join(os.getcwd(), "listar_filmes.html"), "r") as listar_filmes:
                    content = listar_filmes.read()
                self.send_response(200)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                self.wfile.write(content.encode('utf-8'))
            except FileNotFoundError:
                self.send_error(404, "File not found")
        elif self.path == "/index":
            try:
                with open(os.path.join(os.getcwd(), "index.html"), "r") as index:
                    content = index.read()
                self.send_response(200)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                self.wfile.write(content.encode('utf-8'))
            except FileNotFoundError:
                self.send_error(404, "File not found")
        else:
            super().do_GET()

    # Requisição do POST
    def do_POST(self):
        if self.path == '/send_login':
            # Tamanho da requisição que está sendo mandada
            content_length = int(self.headers['Content-length'])
            body = self.rfile.read(content_length).decode('utf-8')
            form_data = parse_qs(body)

            login = form_data.get('usuario', [""])[0]
            password = form_data.get('senha', [""])[0]
            logou = self.account_user(login, password)

            print("Data Form:")
            print("Usuario:", login)
            print("Senha:", password)

            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(logou.encode('utf-8'))

        elif self.path == '/send_cadastro':
            # Recebe dados do formulário
            content_length = int(self.headers['Content-length'])
            body = self.rfile.read(content_length).decode('utf-8')
            form_data = parse_qs(body)

            # Monta o dicionário do filme
            filme = {
                "titulo": form_data.get("titulo", [""])[0],
                "autores": form_data.get("autores", [""])[0],
                "diretores": form_data.get("diretores", [""])[0],
                "ano": form_data.get("ano", [""])[0],
                "genero": form_data.get("genero", [""])[0],
                "produtora": form_data.get("produtora", [""])[0],
                "sinopse": form_data.get("sinopse", [""])[0],
            }

            # Arquivo JSON
            json_file = "filmes.json"

            # Carrega dados existentes ou cria novo
            if os.path.exists(json_file):
                with open(json_file, "r", encoding="utf-8") as f:
                    try:
                        data = json.load(f)
                    except json.JSONDecodeError:
                        data = []
            else:
                data = []

            # Adiciona novo filme
            data.append(filme)

            # Salva de volta
            with open(json_file, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=4, ensure_ascii=False)

            # Resposta para o navegador
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(b"<h2>Filme cadastrado com sucesso!</h2>")

        else:
            super(MyHandle, self).do_POST()


def main():
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, MyHandle)
    print("Server running in http://localhost:8000")
    httpd.serve_forever()


main()
