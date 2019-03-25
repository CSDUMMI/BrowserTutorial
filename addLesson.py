# Add a Lesson from stdin to a tutorial and write that to tutorials.json
import sys,json

def run(args):
    print(args)
    tutorial_name = args[1]
    index = args[2]
    tutorials = json.load(open("tutorials.json"))
    lesson = json.load(open(args[3]))
    tutorials[tutorial_name]["lessons"].insert(int(index),lesson)
    json.dump(tutorials,open("tutorials.json","w"))
if __name__ == '__main__':
    run(sys.argv)
