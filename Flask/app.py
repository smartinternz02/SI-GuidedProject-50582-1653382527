from flask import Flask, render_template, request
import pickle

app = Flask(__name__)   #interfaace between web server and app 

model = pickle.load(open("model.pkl", "rb"))

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/login', methods = ['POST'])
def user():
    p = request.form["rd"]
    q = request.form["ad"]
    r = request.form["mkt"]
    s = request.form["s"]
    if(s == "cal"):
        s1,s2,s3 = 1,0,0
    if(s == "flo"):
        s1,s2,s3 = 0,1,0
    if(s == "ny"):
        s1,s2,s3 = 0,0,1
    t = [[int(s1), int(s2), int(s3), int(p), int(q), int(r)]]
    y = model.predict(t)    
    return render_template('index.html', y="The profit is "+str(y[0][0]))

if __name__ == '__main__':
    app.run(debug= True)