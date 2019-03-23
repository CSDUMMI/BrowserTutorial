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
                "test": Test for the code returned by the learner,
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
        eval(compile(code,"<string>","exec"),None,locs)
    except Exception as e:
        return { "error":e}

    locs = locals()
    locs["locs"]["code"] = locs["code"]
    locs = locs["locs"]

    return locs


@app.route("/<tutorial>/<lesson_index>/check")
def check_code(tutorial,lesson_index):
    lesson  = json.load(open("tutorials.json"))[tutorial]["lessons"][int(lesson_index)]
    modules = lesson["modules"]
    vars    = lesson["vars"] # dict

    for key in modules.keys():
        modules[key] = importlib.import_module(modules[key])

    modules.update(vars)

    local_test = getLocalOf(open(   "tests/"
                                    + tutorial
                                    + "/test_"
                                    + str(lesson_index)
                                    + ".py")
                                    .read(),modules)

    local_test["code"] = local_test["code"]

    code = request.args.get("code")
    if local_test['test_mode'] == "code":
        # Give the local_test['test'] the locals of the code
        local_results = getLocalOf(code,modules)

        if local_results.get("error") != None:
            return str(local_results["error"])

        return local_test['test'](local_results)

    elif local_test['test_mode'] == "text":
        return local_test['test'](request.args.get("code"))

    else:
        return "Bad test"


@app.route("/edit/addTutorial")
def addTutorial():
    global isEditing
    if isEditing == True:
        return "Error: Can't currently edit web server, try later!"
    else:
        isEditing = True

    name = request.args.get("name")
    title = request.args.get("title")
    info = json.load(open("tutorials.json"))

    if info.get(name) != None:
        isEditing = False
        return "Error: Tutorial with that name already exists!"
    else:
        info[name] = {
            "title":title,
            "lessons":[]
        }
        json.dump(info,open("tutorials.json","w+"))
        isEditing == False
        return ""

    return ""
@app.route("/edit/")
def addNewTutorial():
    return render_template("addNewTutorial.html")

@app.route("/edit/<tutorial>/")
def addNewLesson(tutorial):
    info = json.load(open("tutorials.json"))
    info = info.get(tutorial)

    if info == None:
        return "Error: Tutorial not created yet"

    lessons = info["lessons"]
    return render_template( "edit_list_lessons.html",
                            lessons = lessons,
                            tutorial = tutorial )

    # Attention:
    # Nobody but the admin
    # with access to tutorials.json
    # directly can remove anything!


if __name__ == '__main__':
    app.run(host="0.0.0.0")
