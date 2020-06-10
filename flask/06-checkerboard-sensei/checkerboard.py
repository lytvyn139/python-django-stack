#############################
#       RUN
#       python3 checkerboard.py
#       http://127.0.0.1:5000/10/10/green/black/
#       (http:// .....       /x-size/y-size/color/color/)
    
from flask import Flask, render_template   
app = Flask(__name__)    

print(f'open: http://127.0.0.1:5000/10/10/green/black/')
@app.route('/<int:x>/<int:y>/<color0>/<color1>/')
def playground(x, y, color0, color1):
    return render_template('index.html', x = x, y = y,  color0 = color0, color1 = color1)

if __name__=="__main__":
    app.run(debug=True)

