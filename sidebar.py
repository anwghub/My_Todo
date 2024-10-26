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
    
    search_option = st.sidebar.text_input("Search here...", icon_search())    

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

# markdown(f'<div style="display: flex; align-items: center; margin-bottom: 20px;"><a href="#" onclick="window.location.reload();"><i class="fa-solid fa-calendar-week" style="color: #63E6BE;"></i><span style="margin-left: 8px;">Today</span></a></div>', unsafe_allow_html=True)

