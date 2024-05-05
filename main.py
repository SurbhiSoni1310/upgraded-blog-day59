from flask import Flask, url_for, redirect
from flask import render_template
import requests
from static.api_data.data import data

app = Flask(__name__)

# URL = "https://api.npoint.io/219f43871c1202a65cee"
# response = requests.get(URL).json()
blogs = data


@app.route("/")
def homepage():
    return render_template("index.html", heading="Surbhi's Space", sub="A place where my part lives",
                           img="static/assets/img/home-bg.jpg", sub_2=" ", class_heading="page-heading",
                           list=blogs)


@app.route("/about")
def about():
    return render_template("about.html", heading="About Me", sub="This is what I do."
                           , img="static/assets/img/about-bg.jpg", sub_2=" ", class_heading="page-heading")


@app.route("/contact")
def contact():
    return render_template("contact.html", heading="Contact Me"
                           , sub="Have questions? I have answers.",
                           img="static/assets/img/contact-bg.jpg",
                           sub_2=" ", class_heading="page-heading")


@app.route("/post/<element>")
def post(element):
    if element == "about":
        return redirect("/about")
    elif element == "contact":
        return redirect("/contact")
    elif element == "index":
        return redirect("/")
    else:
        ele = eval(element) - 1
        return render_template("post.html", heading=blogs[ele]["title"],
                               sub=blogs[ele]["subtitle"],
                               sub_2=f"Posted by Start Bootstrap on {blogs[ele]['date']}",
                               img=blogs[ele]["image_url"], class_heading="post-heading",
                               text=blogs[ele]["body"], ele=ele, list=blogs)


if __name__ == "__main__":
    app.run(debug=True)
