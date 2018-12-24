from flask import Flask
import sqlite3
app=Flask(__name__)

@app.route('/')
def ret():
    receive=sqlite3.connect('../templates/country.db')
    receive=receive.execute("SELECT * FROM countryIndia")
    info=receive.fetchall()
    for det in info:
        print(det)
    return "Done"

app.run()
