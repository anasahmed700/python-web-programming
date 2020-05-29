from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/myform', methods=["GET", "POST"])
def myform_fn():
    if request.method == "GET":
        return "<h1>Please submit the form instead</h1>"
    else:
        getname = request.form.get("somename").capitalize()
        return render_template("myform.html", name=getname)
