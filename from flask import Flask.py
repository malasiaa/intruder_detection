from flask import Flask, request, abort
import time
from model_function import run_script
import config

app = Flask(__name__)

# List of allowed IP addresses
ALLOWED_IPS = config.FLASK_ALLOWED_IPS  # Add your desired IPs here

# Option to limit the 
@app.before_request
def limit_remote_addr():
    if ALLOWED_IPS is not None:
        client_ip = request.remote_addr
        if client_ip not in ALLOWED_IPS:
            abort(403)  # Forbidden


# List to store the timestamps of incoming requests
request_times = []


@app.route('/trigger', methods=['GET'])
def trigger():
    global request_times
    
    # Current time in seconds
    current_time = time.time()
    
    # Append the current request time to the list
    request_times.append(current_time)
    
    # Remove timestamps older than 30 seconds
    request_times = [t for t in request_times if current_time - t <= 30]
    
    # Check if there are 3 or more requests in the last 20 seconds
    if len(request_times) >= 3:
        run_script()
        # Optionally clear the list to start fresh after triggering the script
        request_times = []
    
    return "Request received", 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

