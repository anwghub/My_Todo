import streamlit as st
from sidebar import create_sidebar
import important
from datetime import datetime

# Initialize session state variables
if 'tasks' not in st.session_state:
    st.session_state.tasks = []
if 'important_tasks' not in st.session_state:
    st.session_state.important_tasks = []
if 'view' not in st.session_state:
    st.session_state.view = "tasks"
if 'completed_tasks' not in st.session_state:
    st.session_state.completed_tasks = []

create_sidebar()

def get_due_tasks():
    today = datetime.today().date()
    return [task for task in st.session_state.tasks if task['date'] == today]

# Main application logic
if st.session_state.view == "important":
    important.show_important_tasks()
elif st.session_state.view == "today_tasks":
    st.header("Due Today...")
    due_tasks = get_due_tasks()
    if not due_tasks:
        st.write("No tasks for today ... Yeppiii")
    else:
        for task in due_tasks:
            st.write(f"* {task['task']} (Due Date: {task['date']})")

elif st.session_state.view == "completed":
    st.header("Completed Tasks")
    if not st.session_state.completed_tasks:
        st.write("No completed tasks.")
    else:
        for task in st.session_state.completed_tasks:
            st.write(f"- {task}")
elif st.session_state.view == "all_tasks":
    st.header("All Tasks")
    if not st.session_state.tasks:
        st.write("No tasks added.")
    else:
        for task in st.session_state.tasks:
            st.write(f"- {task['task']} (Due Date: {task['date']})")
else:
    st.header('My Todo')

    add_task = st.text_area("Enter your task")
    add_time = st.date_input("Choose date...")

    submit_button = st.button("Submit")

    if submit_button:
        if not add_task:
            st.warning("Add your task first....")
        else:
            # Store the task as a dictionary
            st.session_state.tasks.append({'task': add_task, 'date': add_time})
            st.balloons()
            st.success("Task added successfully!")

    st.divider()

    due_tasks = get_due_tasks()
    st.header("Due Today...")
    if not due_tasks:
        st.write("No tasks for today ... Yeppiii")
    else:
        for task in due_tasks:
            st.write(f"* {task['task']} (Due Date: {task['date']})")
    
    if not st.session_state.tasks:
        st.write("No tasks added...")
    else:
        st.header("Your added tasks")
        for task in st.session_state.tasks:
            task_container = st.container()
            with task_container:
                col1, col2, col3, col4 = st.columns([1, 2, 1, 1])
                with col1:
                    completed = st.checkbox("", key=f"checkbox_{task['task']}")  
                    if completed:
                        if task['task'] not in st.session_state.completed_tasks:
                            st.session_state.completed_tasks.append(task['task'])
                            st.session_state.tasks.remove(task)  # Remove from active tasks
                            st.success(f"Task marked as completed: {task['task']}")
                with col2:
                    st.write(f"{task['task']} (Due Date: {task['date']})") 
                with col3:
                    if st.button("⭐", key=f"star_{task['task']}"):  
                        if task['task'] not in st.session_state.important_tasks:             
                            st.session_state.important_tasks.append(task['task'])
                            st.success(f"Added to Important: {task['task']}")
                with col4:
                    if st.button("Remove", key=f"remove_{task['task']}"):  
                        st.session_state.tasks.remove(task)
                        st.success(f"Removed task: {task['task']}")
