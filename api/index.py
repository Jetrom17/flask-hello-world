from flask import Flask, Response

app = Flask(__name__)

@app.route("/")
def hello_world():
    return Response("""
    <style>body {background-color: gold;}</style>
    <!Docctype html>
    <html>
    <center>
    <p>Hello, World!</p>
    </center>
    <div style="position: fixed; left: 0; right: 0; margin: auto; bottom: 0; text-align: center;">Feito em Flask</div>
    </html>
    """)