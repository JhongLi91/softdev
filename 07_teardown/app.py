#Jian Hong Li

from flask import Flask

app = Flask(__name__) # Q0: Where have you seen similar syntax in other langs?

@app.route("/") # Q1: What points of reference do you have for meaning of '/'?
def hello_world():
    print(__name__) # Q2: Where will this print to? Q3: What will it print?
    return "No hablo queso!"  # Q4: Will this appear anywhere? How u know?

app.run()  # Q5: Where have you seen similar constructs in other languages?


'''
DISCO:
QCC:
1. What is app

...
0. java
1. In python, '/' continues the next line to the current line
2. print to app
3. "No hablo queso!"
4. In a local server
5. java

...
INVESTIGATIVE APPROACH:
<Your concise summary of how
 you and your team set about
 "illuminating the cave of ignorance" here...>
'''
