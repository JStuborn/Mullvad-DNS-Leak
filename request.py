import requests
import time
import random
import string
import threading

session = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
iteration = 0
fetch_iterations = 0
success_iterations = 0
failed_iterations = 0

def create_url():
    global iteration
    iteration += 1
    date = time.strftime("%H-%M-%S-%f").replace('.', '-')
    return f"https://{session}-{iteration}-{date}.mullvad.test/"

def update_text():
    print("Fetch:", fetch_iterations)
    print("Success:", success_iterations)
    print("Failed:", failed_iterations)

def make_request():
    global fetch_iterations, success_iterations, failed_iterations
    url = create_url()
    try:
        response = requests.get(url)
        if response.status_code == 200:
            success_iterations += 1
        else:
            failed_iterations += 1
    except requests.exceptions.RequestException as e:
        failed_iterations += 1
    fetch_iterations += 1
    update_text()

def start():
    update_text()
    while True:
        threading.Thread(target=make_request).start()
        time.sleep(30)

if __name__ == "__main__":
    start()
