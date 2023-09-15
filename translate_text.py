from flask import Flask
from flask import redirect
from flask import url_for
from flask import render_template
from flask import request
from flask import session
import googletrans
from googletrans import Translator
app=Flask(__name__)

@app.route("/home",methods=["POST","GET"])
def home():
    if request.method=="POST":
        text=request.form["i"]
        op=request.form["u"]
        trans=Translator()
        tr=trans.translate(text,dest=op)
        k=tr.text
        global pp
        pp=k
        return render_template("trans.html",a=k)
        #return redirect(url_for("log"))
    else:
        return render_template("trans.html")
@app.route("/log",methods=["POST","GET"])
def log():
    return render_template("capture.html")

if __name__=="__main__":
    app.run(debug=True, port=5000, host='0.0.0.0')
