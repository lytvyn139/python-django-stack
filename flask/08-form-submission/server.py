from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/create_user', methods=['POST'])
def create_user():
    name_from_form = request.form['username']
    email_from_form = request.form['email']
    print("!!!!     Got Post Info    !!!!")
    print('\033[1;32;40m')
    print(f'#########     name: {name_from_form}   ########')
    print(f'#########    email:{email_from_form}   ########')
    return render_template("show.html", name_on_template=name_from_form, email_on_template=email_from_form)

if __name__ == "__main__":
    app.run(debug=True)