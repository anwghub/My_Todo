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
    with st.sidebar.container(border=True):
        search_option = st.sidebar.text_input("Search here...", icon_search())    

    col1, col2, col3, col4 = st.sidebar.columns(4)
    
    with col1:
        st.sidebar.markdown(f'<div style="display: flex; align-items: center; margin-bottom: 20px;"><i class="fa-solid fa-calendar-week" style="color: #63E6BE;"></i><span style="margin-left: 8px;">Today</span></div>', unsafe_allow_html=True)
       
    with col2:
        if st.sidebar.markdown(f'<a href="#" onclick="window.location.reload();"><i class="fa-solid fa-person" style="color: #63E6BE;"></i><span style="margin-left: 8px;">Assigned to me</span></a>', unsafe_allow_html=True):
            st.session_state.view = "home"
    
    with col3:
        if st.sidebar.markdown(f'<a href="#" onclick="window.location.reload();"> <i class="fa-regular fa-star" style="color: #63E6BE;"></i><span style="margin-left: 8px;">Important</span></a>', unsafe_allow_html=True):
            st.session_state.view = "important"
    
    with col4:
        st.sidebar.markdown(f'<div style="display: flex; align-items: center; margin-bottom: 20px;"><i class="fa-solid fa-medal" style="color: #63E6BE;"></i><span style="margin-left: 8px;">Completed</span></div>', unsafe_allow_html=True)

    st.sidebar.button("Add list")
