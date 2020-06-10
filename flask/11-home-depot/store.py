from flask import Flask, render_template, request, redirect
from datetime import datetime
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    endings = {
        '1': 'st',
        '2': 'nd',
        '3': 'rd',
        'other': 'th'
    }

    current_date = datetime.today().strftime('%B %-d')
    if int(current_date[-1]) >= 4 or int(current_date[-1]) == 0:
        current_date += endings['other']
    else:
        current_date += endings[current_date - 1]

    current_date += datetime.today().strftime(' %Y %-I:%M:%S %p')
    
    sum = int(request.form['bitset']) + int(request.form['saw']) + int(request.form['sander']) + int(request.form['nailgun'])
    print(f'\033[1;37;40m Each time you refresh page I\'m charging {request.form["first_name"]} {request.form["last_name"]} for {sum} tools on {current_date} \033[0;37;40m \n')
    
    return render_template("checkout.html", 
        quantity_b=request.form['bitset'], 
        quantity_c=request.form['saw'], 
        quantity_o=request.form['sander'], 
        quantity_n=request.form['nailgun'], 
        first_name=request.form['first_name'], 
        last_name=request.form['last_name'], 
        discount_id=request.form['discount_id'], total=sum, date=current_date)

@app.route('/tools')         
def tools():
    return render_template("tools.html")

if __name__=="__main__":   
    app.run(debug=True)    