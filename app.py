from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "GitOps Application Running on AWS EKS with Istio"

app.run(host='0.0.0.0', port=5000)
