from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "secretkey"

@app.route("/")
def nr_of_visits():
    if 'nr_of_visits' in session:
        session['nr_of_visits'] += 1
    else:
        session['nr_of_visits'] = 1

    if 'counter' not in session:
        session['counter'] = 0

    return render_template('nr_of_visits.html', nr_of_visits=session['nr_of_visits'], counter=session['counter'])


@app.route('/increment', methods=['POST'])
def increment():
    amount = int(request.form.get('amount', 1))
    session['counter'] += amount
    return redirect('/')


@app.route('/destroy_session')
def destroy_session():
    session.clear()
    return redirect('/')


@app.route('/plus2')
def plus2():
    session['counter'] += 2
    return redirect('/')


@app.route('/reset')
def reset():
    session['counter'] = 0
    return redirect('/')




if __name__== "__main__":
    app.run(debug=True)