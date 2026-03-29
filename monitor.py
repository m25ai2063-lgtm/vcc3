import psutil
import subprocess
import time

THRESHOLD = 75.0
INSTANCE = "gcp-burst-node"
ZONE = "us-central1-a"

print("Monitoring started. Threshold: 75%")

while True:
    cpu = psutil.cpu_percent(interval=2)
    if cpu > THRESHOLD:
        print(f"CRITICAL: CPU at {cpu}%. Bursting to GCP...")
        subprocess.run(["gcloud", "compute", "instances", "start", INSTANCE, "--zone", ZONE])
        break # Burst triggered
    time.sleep(1)
