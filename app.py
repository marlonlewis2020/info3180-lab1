from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

'''
# Routing for your application.
# Put your routes below this comment
'''

@app.route("/")
def home():
    info = {"content":"My Home Page",
            "title":"Home"}
    return render_template("home.html", page=info)

@app.route("/about")
def about():
    info = {"title":"About"}
    return render_template("about.html", page=info)

@app.route("/home")
@app.route("/index")
def home2():
    return redirect(url_for("home"))


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404
