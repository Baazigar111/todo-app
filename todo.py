todos = [
    {"id": 1, "task": "Learn Git", "done": True},
    {"id": 2, "task": "Make a PR", "done": False}
]

def show_todos():
    for item in todos:
        # If done is True, show [x], otherwise show [ ]
        status = "[x]" if item["done"] else "[ ]"
        print(f"{item['id']} {status} {item['task']}")

show_todos()