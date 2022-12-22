from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__, static_url_path='/static')


@app.route('/', methods=['GET'])
def Load():
    return render_template("index.html")


@app.route('/Products', methods=['POST', 'GET'])
def Signin():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="users"
    )
    mycursor = mydb.cursor()
    if request.method == 'POST':
        signin = request.form
        username = signin['email']
        password = signin['pass']
        mycursor.execute("select * from user where email='" +
                         username+"' and password='"+password+"'")
        r = mycursor.fetchall()
        count = mycursor.rowcount
        if count == 1:
            return render_template("product-list.html")
    elif request.method == 'GET':
        return render_template("product-list.html")
    return render_template('index.html')


@app.route('/Signup', methods=['POST'])
def Signup():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="users"
    )
    mycursor = mydb.cursor()
    if request.method == "POST":
        result = request.form.to_dict()
        name = result['name']
        email = result['email']
        password = result['password']

        mycursor.execute(
            "insert into user (name,email,password) values(%s,%s,%s)", (name, email, password))
        mydb.commit()
        mycursor.close()
        return render_template('index.html')
    return render_template('index.html')


@app.route('/Products/product1', methods=['GET'])
def Products1():
    return render_template("product1.html")


@app.route('/Products/product2', methods=['GET'])
def Products2():
    return render_template("product2.html")


@app.route('/Products/product3', methods=['GET'])
def Products3():
    return render_template("product3.html")


@app.route('/Products/product4', methods=['GET'])
def Products4():
    return render_template("product4.html")


@app.route('/Products/product5', methods=['GET'])
def Products5():
    return render_template("product5.html")


@app.route('/Products/product6', methods=['GET'])
def Products6():
    return render_template("product6.html")


@app.route('/Cart', methods=['GET'])
def Cart():
    return render_template("cart.html")


@app.route('/payment', methods=['GET'])
def payment():
    return render_template("payment.html")


app.run()
