from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

@app.route('/', methods = ["GET"])
def home():
    return render_template ("index.html")


@app.route('/predict', methods =["POST"])
def predict():
    if request.method == "POST":
        Tablename = request.form.get("Tablename")
        
        data = {'Tablename': Tablename,
        }
  
        r = requests.request("POST",url = 'https://web-production-20ea.up.railway.app/predict', data=data)
        
        res = r.text
                 
    return render_template ("index.html", prediction_text = res)


if __name__ == '__main__':
    app.run(debug=True)
    