from flask import Flask
import subprocess
import socket

app = Flask(__name__)

@app.route('/', methods=['POST'])
def stress_cpu():
    # Run 'stress_cpu.py' in a separate process
    subprocess.Popen(["python", "stress_cpu.py"])
    return "CPU stress process started", 200

@app.route('/', methods=['GET'])
def get_private_ip():
    # Get the private IP address of the EC2 instance
    ip_address = socket.gethostbyname(socket.gethostname())
    return ip_address

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
