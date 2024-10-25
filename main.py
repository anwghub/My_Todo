import streamlit as st
from sidebar import create_sidebar
import important 

# Initialize session state variables
if 'tasks' not in st.session_state:
    st.session_state.tasks = []
if 'important_tasks' not in st.session_state:
    st.session_state.important_tasks = []
if 'view' not in st.session_state:
    st.session_state.view = "home"


create_sidebar()

if st.session_state.view == "important":
    important.show_important_tasks()
else:
    # Your existing todo list logic
    st.header('My Todo')

    add_task = st.text_area("Enter your task")
    add_time = st.date_input("Choose date...")

    submit_button = st.button("Submit")

    if submit_button:
        if not add_task:
            st.warning("Add your task first....")
        else:
            st.session_state.tasks.append(add_task)
            st.balloons()
            st.success("Task added successfully!")

    st.divider()

    if not st.session_state.tasks:
        st.write("No tasks added...")
    else:
        st.write("Your added tasks")
        for task in st.session_state.tasks:
            task_container = st.container()
            with task_container:
                col1, col2, col3 = st.columns([3, 1, 1])
                col1.write(f"- {task}")

                if col2.button("⭐", key=f"star_{task}"):  
                    if task not in st.session_state.important_tasks:             
                        st.session_state.important_tasks.append(task)
                        st.success(f"Added to Important: {task}")

                if col3.button("Remove", key=task):  
                    st.session_state.tasks.remove(task)
                    st.success(f"Removed task: {task}")
