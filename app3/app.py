from flask import Flask, request
import socket

app = Flask(__name__)

@app.route('/')
def index():
    # 클라이언트 IP 주소 추출
    client_ip = request.remote_addr
    xff_header = request.headers.get('X-Forwarded-For', None)
    if xff_header:
        # X-Forwarded-For 헤더에서 첫 번째 IP 주소 추출
        client_ip = xff_header.split(',')[0].strip()

    client_user_agent = request.headers.get('User-Agent')

    # 서버 정보
    server_ip = socket.gethostbyname(socket.gethostname())
    server_name = socket.gethostname()

    return f"""
    <html>
    <head>
        <style>
            .client-info {{
                color: blue;
            }}
            .server-info {{
                color: green;
            }}
        </style>
    </head>
    <body>
        <h1> - 접속 정보 Version 3 - </h1>

        <h2 class="client-info">1. 클라이언트 정보</h2>
        <p class="client-info">IP 주소: {client_ip}</p>
        <p class="client-info">X-Forwarded-For: {xff_header if xff_header else '없음'}</p>
        <p class="client-info">User-Agent: {client_user_agent}</p>

        <h2 class="server-info">2. 서버 정보</h2>
        <p class="server-info">IP 주소: {server_ip}</p>
        <p class="server-info">이름: {server_name}</p>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)