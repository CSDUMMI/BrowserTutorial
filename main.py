#! /usr/bin/python3
from flask import Flask, render_template
import json
import markdown

app = Flask(__name__)

"""
tutorials.json:
{
    <tutorial> { <tutorial> : Must be compatible with links, no withespaces
        "title": Title of the Tutorial,
        "description": Description of the Tutorial
        "lessons": [
            {
                "title":Lesson Title,
                "text": Markdown of the Text of Lesson,
                "code": Code to be shown before editing by learner,
                "test": Test for the code returned by the learner
            }
        ]
    }
}
"""

@app.route("/")
def index():
    tutorials = json.load(open("tutorials.json"))
    tutorials = zip(tutorials.keys(),tutorials.values())
    return render_template  (
                            "index.html",
                            tutorials = tutorials
                            )

@app.route("/<tutorial>")
def index_tutorial(tutorial):
    tutorial_info = json.load(open("tutorials.json"))[tutorial]
    tutorial_info["lessons"] = zip  (
                                    range   (
                                            0,
                                            len(tutorial_info["lessons"])
                                            ),
                                            tutorial_info['lessons']
                                    )
    return render_template  (
                            "index_tutorial.html",
                            tutorial=tutorial,
                            lessons=tutorial_info["lessons"]
                            )

@app.route("/<tutorial>/<lesson_index>/text")
def showText(tutorial,lesson_index):
    lesson = json.load (open("tutorials.json"))
    lesson = lesson[tutorial]
    lesson = lesson["lessons"]
    lesson = lesson[int(lesson_index)]

    text_html   = markdown.markdown(str(lesson["text"]))
    return render_template  (
                            "text.html",
                            text=text_html,
                            tutorial=tutorial,
                            lesson=lesson["title"]
                            )

@app.route("/<tutorial>/<lesson_index>/exercise")
def showExercise(tutorial,lesson_index):
    lesson = json.load (open("tutorials.json"))
    lesson = lesson[tutorial]
    lesson = lesson["lessons"]
    lesson = lesson[int(lesson_index)]

    code_template = lesson["code"]
    return render_template  (
                            "exercise.html",
                            code=code_template
                            )

@app.route("/<tutorial>/<lesson_index>/")
def showLesson(tutorial,lesson_index):
    lesson = json.load (open("tutorials.json"))
    lesson = lesson[tutorial]
    lesson = lesson["lessons"]
    lesson = lesson[int(lesson_index)]
    return render_template  (
                            "lesson.html",
                            lesson = lesson,
                            tutorial = tutorial,
                            lesson_index = lesson_index
                            )

if __name__ == '__main__':
    app.run()
