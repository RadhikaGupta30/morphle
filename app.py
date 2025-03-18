from flask import Flask
import os
import subprocess
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route('/htop')
def htop_info():
    # Get system username
    username = os.getenv("USER", "codespace")

    # Get server time in IST
    ist = pytz.timezone("Asia/Kolkata")
    server_time = datetime.now(ist).strftime("%Y-%m-%d %H:%M:%S.%f")

    # Get top command output (first 10 lines)
    top_output = subprocess.getoutput("top -b -n 1 | head -10")

    # Format response
    response = f"""
    <h2>Name: Radhika Kumari Gupta</h2>
    <h3>User: {username}</h3>
    <h3>Server Time (IST): {server_time}</h3>
    <h3>TOP output:</h3>
    <pre>{top_output}</pre>
    """

    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)