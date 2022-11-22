from flask import Flask
app = Flask(__name__)

@app.route("/classify-image",methods=['GET','POST'])

def hello_world():
  return "Hello, World what to do"

if __name__ == '__main__':
  app.run(host = '0.0.0.0', debug= True)