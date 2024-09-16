from flask import Flask

app = Flask(__name__)

@app.route('/trigger', methods=['GET'])
def trigger():
    print("Motion detected!")
    # Call your function or run any script here
    run_script()
    return "OK", 200

def run_script():
    # Code to run your Python script
    print("HELLO GAJA BOAAAAAAAAAAAAAAAAAAAA :)")
    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000) #host='0.0.0.0' if all hosts can send the http request
