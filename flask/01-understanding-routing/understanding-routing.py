from flask import Flask
app = Flask(__name__)    

@app.route('/')          
def hello_world():
    return '<h1 style="color:blue;">WELCOME</h1> <br> available routes are: <br> http://127.0.0.1:5000/dojo <br> http://127.0.0.1:5000/say/your_name <br> http://127.0.0.1:5000/repeat/(int number of times)/(str) <br> http://127.0.0.1:5000/converted/(integer) <br> <h4 style="color:red">all other routes you\'ll get 404 error</h4>'

@app.route('/dojo')
def dojo():
    return 'Hello from dojo bootcamp!'  

@app.route('/say/<username>') 
def say_name(username):
    print(f"Hi {username}!")
    return (f"Hi {username}!")

@app.route('/repeat/<num>/<str>')
def repeat(num, str):

    return int(num) * (str+' ')

""" 
http://exploreflask.com/en/latest/views.html#url-converters)
This table shows Flask’s built-in URL converters.
string	Accepts any text without a slash (the default).
int	Accepts integers.
float	Like int but for floating point values.
path	Like string but accepts slashes.
"""
@app.route('/converted/<int:num>')
def convert(num):
    greet = 'HAHA'
    for i in range(num):
        print(f"{greet}")
    return (f"i'm converted to int and will print <b> {greet}*{num} times </b> to the console")


    
if __name__=="__main__":
    app.run(debug=True)                   

@app.errorhandler(404)
def page_not_found(error):
    print('*** 404 you already know ***')
    link = "<img src='https://i1.wp.com/saedx.com/blog/wp-content/uploads/2019/01/saedx-blog-featured-70.jpg'>"
    return link

if __name__=="__main__":
    app.run(debug=True)