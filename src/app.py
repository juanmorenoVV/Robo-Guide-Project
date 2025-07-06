import socket
from flask import Flask, render_template, request


app = Flask(__name__)

ROBOT_IP = '192.168.1.10'
ROBOT_PORT = 5000

@app.route("/", methods=["GET", "POST"])

def home():
    return render_template("index.html")


def send_command(msg):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((ROBOT_IP, ROBOT_PORT))
            s.sendall(msg.encode())
            print(f"Comando enviado: {msg}")
    except Exception as e:
        print("Error:", e)

@app.route("/run_cuadrado")
def run_cuadrado():
    send_command("RUN_CUADRADO")
    return "OK"

@app.route("/run_circulo")
def run_circulo():
    send_command("RUN_CIRCULO")
    return "OK"



if __name__ == '__main__':
    
    app.run(debug=True, port=5000)
    app.run(host="0.0.0.0", port=8080)