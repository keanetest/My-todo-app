import streamlit as st
import functions

todos = functions.get_todos()


def add_todo():
    todo1 = st.session_state['new_todo'] + '\n'
    todos.append(todo1)
    functions.write_todos(todos)


st.title("My ToDo App")
st.subheader("This is my todo app")
st.write("This app is to increase your productivity")

for index, todo2 in enumerate(todos):
    checkbox = st.checkbox(todo2, key=todo2)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo2]
        st.experimental_rerun()


st.text_input(label="", placeholder="Enter a todo.....",
              on_change=add_todo, key='new_todo')










