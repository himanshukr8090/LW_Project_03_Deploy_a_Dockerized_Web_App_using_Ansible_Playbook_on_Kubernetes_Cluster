from flask import Flask
app = Flask(__name__)
@app.route('/')
def home():
    return "Hello I am Himanshu Singh, Using Ansible to deploy my flask app on EKS.. !"
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

