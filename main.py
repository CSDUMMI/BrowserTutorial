#! /usr/bin/python3
from flask import Flask, render_template, request
import json, importlib
import markdown

app = Flask(__name__)

# Set this once you edit the server or you don't want anybody to use editing capability
# Thus, no more than one can edit at a time, no race-condition
isEditing = False
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
                "test": Test file Module reference,
                "modules": Modules avaible to the learner and the test
                "vars": Variables that should be set before the learners code is executed
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

    lesson_index = int(lesson_index)
    # Get HREF to the next lesson
    if lesson_index == len(lesson)-1:
        # Is last lesson in tutorial
        next_lesson = "/" # Go back to Tutorial index
    else:
        next_lesson = "/" + tutorial + "/" + str(lesson_index+1) + "/"

    lesson = lesson[lesson_index]
    code_template = lesson["code"]
    return render_template  (
                            "exercise.html",
                            code=code_template,
                            tutorial = tutorial,
                            lesson_index = lesson_index,
                            next_lesson=next_lesson
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

@app.route("/<tutorial>/<lesson_index>/error")
def showError(tutorial,lesson_index):
    error_msg = request.args.get("e")
    return render_template("error.html",
                            error=error_msg
                        )

def getLocalOf(code,locs):

    try:
        exec(code,locs)
    except Exception as e:
        return { "error":e}

    return locs

@app.route("/<tutorial>/<lesson_index>/check")
def check_code(tutorial,lesson_index):
    lesson  = json.load(open("tutorials.json"))[tutorial]["lessons"][int(lesson_index)]
    modules = lesson["modules"]
    vars    = lesson["vars"] # dict

    namespace_exercise = {}
    # Import modules in modules
    for key in modules.keys():
        namespace_exercise[key] = importlib.import_module(modules[key])

    # Add the variables to the global namespace in the exercise code
    for key in vars.keys():
        namespace_exercise[key] = vars[key]

    code = request.args.get("code")
    test_module = importlib.import_module(lesson["test"])

    if test_module.test_mode == "code":
        # Give the local_test['test'] the locals of the code
        locs_exercises = getLocalOf(code,namespace_exercise)

        if locs_exercises.get("error") != None:
            return str(local_results["error"])
        return test_module.test(locs_exercises)

    elif test_module.test_mode == "text":
        return local_test['test'](request.args.get("code"))

    else:
        return "Bad test"

if __name__ == '__main__':
    app.run(host="0.0.0.0")
