from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Production Grade GitOps CI/CD on AWS EKS 🚀"

app.run(host='0.0.0.0', port=5000)
