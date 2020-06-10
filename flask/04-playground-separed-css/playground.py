from flask import Flask, render_template
app = Flask(__name__)    

@app.route('/')          
def index():
    return render_template('index.html')

    
@app.route('/plaground/<int:number>/<color>')
def playground(number, color):
    color_selection = ['steelblue' 'mediumspringgreen', 'chartreuse', 'darkorchid', 'lightsalmon']
    if color not in color_selection:
        color = 'white'
    return render_template('boxes.html', num = number, color = color)

if __name__=="__main__":
    app.run(debug=True)