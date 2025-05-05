from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "secretkey"

@app.route("/")
def form():
    return render_template("form.html")

@app.route('/process', methods=['POST'])
def process():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']
    session['experience'] = request.form.get('experience')
    session['interests'] = request.form.getlist('interests')
    return redirect('/result')

@app.route('/result')
def result():
    return render_template('result.html')

if __name__=="__main__":
    app.run(debug=True)