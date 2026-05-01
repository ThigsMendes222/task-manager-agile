tasks = []

def create_task(title):
    tasks.append({"title": title, "done": False})

def list_tasks():
    return tasks

def update_task(index, new_title):
    if 0 <= index < len(tasks):
        tasks[index]["title"] = new_title

def complete_task(index):
    if 0 <= index < len(tasks):
        tasks[index]["done"] = True

def delete_task(index):
    if 0 <= index < len(tasks):
        tasks.pop(index)


        