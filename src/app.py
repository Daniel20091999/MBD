from flask import Flask, render_template, redirect, request, Response, session
from flask_mysqldb import MySQL, MySQLdb

app = Flask(__name__, template_folder="templates")

app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "root"
app.config["MYSQL_DB"] = "mbd"
app.config["MYSQL_CURSORCLASS"] = "DictCursor"
mysql = MySQL(app)

@app.route("/")
def login():
    return render_template("login.html")

@app.route("/admin")
def home():
    return render_template("home.html")

#Funcion de login

@app.route('/acceso_login',  methods = ["GET", "POST"])
def inicio_sesion():
    
    if request.method == "POST" and "txt_username" in request.form and "txt_password":
        _username = request.form['txt_username']
        _password = request.form['txt_password']
        
        cur = mysql.connection.cursor()
        cur.execute("select * from t_usuario where nombre_usuario = %s and password_usuario = %s",(_username, _password,))
        account = cur.fetchone()
        
        if account:
            cur.execute("update t_usuario set logueado_usuario = 1 where nombre_usuario = %s",(_username,))            
            return render_template("home_999.html")
    
        else:
    
            return render_template("login.html" , mensaje  = 'Usuario incorrecto')

    
if __name__ == "__main__":
    app.secret_key="mbd_secret_key"
    app.run(debug=True, host= "0.0.0.0", port=5000, threaded= True)