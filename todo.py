# Our list of tasks
todos = [
    {"id": 1, "task": "Learn Git"},
    {"id": 2, "task": "Make a PR"}
]

def show_todos():
    for item in todos:
        print(f"{item['id']}: {item['task']}")

show_todos()