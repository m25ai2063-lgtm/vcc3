from flask import Flask
import multiprocessing
import time

app = Flask(__name__)

def stress_cpu():
    timeout = time.time() + 30  # Run for 30 seconds
    while time.time() < timeout:
        _ = 1000 * 1000

@app.route('/status')
def status():
    return {"server": "Local Ubuntu VM", "status": "Active"}

@app.route('/trigger-load')
def load():
    # Launches processes to spike CPU usage
    for _ in range(multiprocessing.cpu_count()):
        multiprocessing.Process(target=stress_cpu).start()
    return "CPU Load spike initiated..."

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
