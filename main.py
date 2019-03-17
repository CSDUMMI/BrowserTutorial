#! /usr/bin/python3
from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route('/')
def index():
    tutorials_list = json.load(open("tutorials_list.json"))
    return render_template("index.html",tutorials = tutorials_list)

@app.route('/<tutorial>')
def index_tutorial(tutorial_name):
    """
    <tutorial>.json:
    {
        "title": Title of the Tutorial must be compatible with Links,
        "lessons": [
            {
                "title":Lesson Title,
                "text": Markdown of the Text of Lesson,
                "code": Code to be shown before editing by learner,
                "test": Test for the code returned by the learner
            }
        ]
    }
    """
    tutorial = json.load(open(tutorial_name + ".json"))
    return render_template("index_tutorial.html",
                            title=tutorial_name,
                            lessons=tutorial["lessons"]
                            )

@app.route('/<tutorial>/<lesson>')
def showText(tutorial_name,lesson_name):
    text_md = json.load(open(tutorial_name + ".json"))

    return render_template("showText.html", text=text_html)

if __name__ == '__main__':
    app.run()
