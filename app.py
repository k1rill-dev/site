from flask import Flask, render_template, redirect, url_for, request, flash
import psycopg2
from data import config

app = Flask(__name__)
app.secret_key = "super"


def sql_connection():
    try:
        con = psycopg2.connect(
            database="d3hb84250el4c1",
            user="glkqkbzeftqcvn",
            password="96e6b1c37d2bd73c9f2b1cef35a32bddf5730edbc240077e4a29963e91ac3637",
            host="ec2-52-54-38-229.compute-1.amazonaws.com",
            port="5432"
        )
        return con
    except Exception as ex:
        print(ex)


@app.route('/admin/<login>', methods=['POST', 'GET'])
def index(login):
    con = sql_connection()
    cur = con.cursor()
    cur.execute("SELECT * FROM Users ;")
    rows = cur.fetchall()
    if request.method == "POST":
        delete_id = request.form['lol']
        id_user_delete = request.form['id']
        if delete_id != ' ':
            cur.execute(f"UPDATE Users SET tovar=0, id_buy=0 WHERE id_buy='{delete_id[1::]}'")
            con.commit()
        elif id_user_delete != ' ':
            cur.execute('DELETE FROM Users WHERE id=%s', id_user_delete[1::])
            con.commit()
        return render_template("index.html", rows=rows)
    else:
        return render_template("index.html", rows=rows)


@app.route('/', methods=['POST', 'GET'])
def enter_panel():
    if request.method == "POST":
        login = request.form['loginnn']
        password = request.form['passwwword']
        if login == config.LOGIN and password == config.PASSWORD:
            return redirect('/admin/<login>')
        else:
            return render_template('kekich.html')

    else:
        return render_template("kekich.html")


if __name__ == "__main__":
    app.run(debug=True)
