from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", title="Techbros.io")

@app.route("/about_me")
def about():
    return render_template("about.html")

@app.route("/Beranda")
def beranda():
    return render_template("beranda.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

if __name__ == "__main__":
    app.run(port=6007, debug=True)