from flask import Flask, render_template, request
import pickle

app = Flask(__name__)   #interfaace between web server and app 

model = pickle.load(open("model.pkl","rb"))
sc = pickle.load(open("transform.pkl","rb"))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods = ['POST'])
def predict():
    a = request.form["cd"]
    b = request.form["ar"]
    c = request.form["jf"]
    d = request.form["mm"]
    e = request.form["js"]
    print(a)
    print(b)
    print(c)
    print(d)
    print(e)
    data = [[float(a),float(b), float(c), float(d), float(e)]]
    print(sc.transform(data))
    prediction = model.predict(sc.transform(data))
    y = prediction[0]
    return render_template('index.html', y="The possibility is "+str(y))

if __name__ == '__main__':
    app.run(debug= True)