import streamlit as st

def show_important_tasks():
    if 'important_tasks' not in st.session_state:
        st.session_state.important_tasks = []

    st.header("Important Tasks")

    if not st.session_state.important_tasks:
        st.write("No important tasks added...")
    else:
        for task in st.session_state.important_tasks:
            st.markdown(f"- {task}")

if __name__ == "__main__":
    show_important_tasks()
