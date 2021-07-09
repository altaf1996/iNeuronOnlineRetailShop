from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///signup.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

class SignUp(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(200), nullable=False)
    password = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"{self.email} - {self.date_created} "

# Home Page
@app.route("/")
@app.route("/home")
def index():
    #signup = SignUp(email="Altaf", password="1234")
    #db.session.add(signup)
    #db.session.commit()
    return render_template("index.html") 

# About Page
@app.route("/about", methods=["POST", "GET"])
def about():
    return render_template("about.html")

# More Page
@app.route("/contact", methods=["POST", "GET"])
def contact():
    return render_template("contact.html")

# Cart Pagr
@app.route("/cart", methods=["POST", "GET"])
def cart():
    return render_template("cart.html")


@app.route("/show", methods=["POST", "GET"])
def show():
    allSignUp = SignUp.query.all()
    print(allSignUp)
    return "this is a show page"



if __name__ == "__main__":
    app.run(debug=True)