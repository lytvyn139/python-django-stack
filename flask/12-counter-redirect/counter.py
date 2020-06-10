from flask import Flask, render_template, redirect, session, request
app= Flask(__name__)

app.secret_key= "SHOWmeDEWay"

@app.route('/')
def count():
    try: 
        session['count'] += 1
    except: 
        session['count'] = 1 
    return render_template('index.html')

@app.route('/initialize_the_sequence', methods=['POST'])
def visits():
    session['count'] += 1
    return redirect('/')

@app.route('/destroy_session', methods=['POST'])
def reset():
    session['count'] =-1
    return redirect('/')

if __name__=="__main__":   
    app.run(debug=True)    