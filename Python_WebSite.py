# Online_Gaming_Store created by devan dachenhausen
# October 31, 2022

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def page_1():
    return render_template('page_1.html')

@app.route('/p2')
def page_2():
    return render_template('page_2.html')

@app.route('/p3')
def page_3():
    return render_template('page_3.html')

@app.route('/p4')
def page_4():
    return render_template('page_4.html')

if __name__ == '__main__':
    app.run()
