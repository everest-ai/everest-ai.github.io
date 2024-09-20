import http.server
import socketserver

# 配置服务器端口和文件目录
PORT = 8000
DIRECTORY = "/Users/xmly/Documents/ximalaya-project/takin-demopage/FunAudioLLM.github.io/"

# 创建自定义的请求处理器类，以提供所需目录的功能
class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

# 启动服务器
with socketserver.TCPServer(("", PORT), CustomHTTPRequestHandler) as httpd:
    print(f"Serving at port {PORT}")
    httpd.serve_forever()