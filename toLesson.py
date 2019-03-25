import sys, json

def run(args):
    print(json.dumps({
        "title": args[1],
        "text": open(args[2] + "/text.md").read(),
        "code": open(args[2] + "/code.py").read(),
        "test": args[3],
        "modules": json.load(open(args[2] + "/modules.json")),
        "vars":json.load(open(args[2] + "/vars.json"))
    }))
if __name__ == '__main__':
    run(sys.argv)
