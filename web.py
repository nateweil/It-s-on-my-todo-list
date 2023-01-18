import streamlit as stream
import functions as es

tasks = es.file_io(None, readwrite="r")

def add_task():
    task = stream.session_state["new task"] + "\n"
    tasks.append(task)
    es.file_io(tasks, readwrite="w")

def button_click():
    pass

stream.title("My Todo App")
stream.subheader("This is my todo app.")
stream.write("This app is to increase your productivity.")

for index, task in enumerate(tasks):

    key = f"{index}. {task}"

    # The app gets mad if two objects have the same key, which happens if two tasks are identical.
    # Therefore I changed the key to include the index number, since it's always unique. See above!
    checkbox = stream.checkbox(task, key=key)

    if checkbox == True: # Apparently the == True part isn't necessary, but I preferred it.
        tasks.pop(index)
        es.file_io(tasks, readwrite="w")
        del stream.session_state[key] # Something to do with not inserting whatever's in the input box into the list?
        stream._rerun() # This seems important to refresh the interface (specifically the checkboxes).

stream.text_input("", placeholder="add a task!", on_change=add_task, key="new task")
# stream.button("Click on me!", on_click=button_click, key="button")

stream.session_state