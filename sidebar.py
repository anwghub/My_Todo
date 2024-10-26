import streamlit as st
from icon import icon_search

def create_sidebar():
    # Load Font Awesome
    st.markdown(
        '''
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
        ''',
        unsafe_allow_html=True
    )
    
    st.sidebar.title("Find here...")
    
    search_option = st.sidebar.markdown(
        '''
        <div style="display: flex; align-items: center; padding: 5px;">
            <i class="fas fa-search" style="margin-right: 10px; color: grey;"></i>
            <input type="text" id="search-input" placeholder="Search here..." style="width: 100%; padding: 5px; border: none; border-radius: 5px; outline: none; box-shadow: 0 0 2px rgba(0,0,0,0.2);">
        </div>
        ''',
        unsafe_allow_html=True
    )
    
    # if 'tasks' in st.session_state:
    #     if search_option:
    #         filtered_tasks = [task for task in st.session_state.tasks if search_option.lower() in task['task'].lower()]
    #     else:
    #         filtered_tasks = st.session_state.tasks

    #     st.sidebar.header("Filtered Tasks")
    #     if not filtered_tasks:
    #         st.sidebar.write("No matching tasks found.")
    #     else:
    #         for task in filtered_tasks:
    #             st.sidebar.write(f"- {task['task']} (Due Date: {task['date']})")
    
   

    col1, col2, col3 = st.sidebar.columns(3)
    
       
    with col1:
        if st.sidebar.button("👤 Assigned to me"):
            st.session_state.view = "all_tasks"
    
    with col2:
        if st.sidebar.button("⭐ Important"):
            st.session_state.view = "important"
    
    with col3:
        if st.sidebar.button("🏅 Completed"):
            st.session_state.view = "completed"

    if st.sidebar.button("🏠 Home"):
        st.session_state.view = "tasks"

    return search_option

# markdown(f'<div style="display: flex; align-items: center; margin-bottom: 20px;"><a href="#" onclick="window.location.reload();"><i class="fa-solid fa-calendar-week" style="color: #63E6BE;"></i><span style="margin-left: 8px;">Today</span></a></div>', unsafe_allow_html=True)

