from flask import Flask, render_template, request, redirect, url_for
from servicesDB import servicesDB as db
import os

app = Flask(__name__)
conn = db()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/studentlogin')
def studentlogin():
    return render_template('studentportal.html')

@app.route('/addwaste',methods=['POST','GET'])
def addwaste():
    if request.method == "POST":
        quant = request.form['quant']
        food = request.form['food']
        conn.addWaste(quant,food)
    return render_template('foodWasteDetail.html')

@app.route('/postAttend',methods=['POST','GET'])
def postAttend():
    if request.method == "POST":
        present = request.form['present']
        total = request.form['total']
        conn.putAttend(present,total)
    return render_template('foodWasteDetail')

@app.route('/addfeed',methods=['POST','GET'])
def addfeed():
    if request.method == "POST":
        data = request.form['data']
        conn.addFeedback(data)
    return render_template('studentportal.html')

@app.route('/viewfeed')
def viewfeed():
    resp = conn.viewFeedback()
    out = "<html><head><title>Feedbacks</title></head><body><center><table><tr><th>No.</th><th>Feedback</th></tr>"
    for i in range(len(resp)):
        out += "<tr><td>%d</td><td>%s</td></tr>"%(i+1,resp[i][0])
    out += "</table></body></html>"
    return out

@app.route('/getwaste')
def getwaste():
    resp = conn.getWaste()
    out = ""
    outs = 0
    print(resp)
    for i in resp:
        out += "Total waste of %s on date %s is %s Kg's<br>"%(i[1],i[2],i[0])
        outs += int(i[0])
    out += "--------------------------------------------------------<br>"
    out += "Total waste on date is %s Kg's"%(str(outs))
    return out

@app.route('/manager')
def manager():
    return render_template('foodWasteDetail.html')

@app.route('/login',methods=['POST','GET'])
def login():
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']
        resp = conn.login(email,password)
        if(len(resp)>0):
            data = resp[0]
            if(data[-1]=='student'):
                return redirect(url_for('studentlogin'))
            return redirect(url_for('manager'))
    return render_template('login.html')

@app.route('/signup',methods=['POST','GET'])
def signup():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        eid = request.form['regname']
        typ = request.form['loggedAs']
        pwd = request.form['password']
        phone = request.form['pwd']
        conn.doSignUp(name,pwd,email,typ,phone,eid)
        return redirect(url_for('login'))
    else:
        return render_template('signup.html')

if __name__ == "__main__":
    port = int(os.environ.get("PORT",5000))
    app.run(host='0.0.0.0',port=port)
