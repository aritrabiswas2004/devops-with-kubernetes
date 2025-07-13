from flask import Flask, request, redirect
import os

app = Flask(__name__)

todos = [
    "Bake a cake",
    "Learn basic networking",
    "Learn containerization"
]

@app.route('/todos', methods=["GET", "POST"])
def get_todos():
    if request.method == "POST":
        print(request.values)
        todos.append(request.values.get("todo-input"))
        return "success"

    return todos

if __name__ == '__main__':
    app.run("0.0.0.0", port=int(os.environ.get('BACKEND-PORT', 4040))) # 4040 as backup for my sanity

