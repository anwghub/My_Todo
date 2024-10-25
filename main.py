import streamlit as st
from icon import icon_star,icon_person,icon_medal,icon_today,icon_search

#sidebar
#load font awesome
st.markdown(
    '''
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
    ''',
    unsafe_allow_html=True
)

with st.container():
    
    st.sidebar.title("Find here...")
    with st.sidebar.container(border=True):
        search_option = st.sidebar.text_input("Search here...",icon_search())    

    col1, col2, col3, col4 = st.sidebar.columns(4)
    with col1:
        st.markdown(f'<div style="display: flex; align-items: center; margin-bottom: 20px;"><i class="fa-solid fa-calendar-week" style="color: #63E6BE;"></i><span style="margin-left: 8px;">Today</span></div>', unsafe_allow_html=True)
         
    with col2:
        st.markdown(f'<div style="display: flex; align-items: center; margin-bottom: 20px;"><i class="fa-solid fa-person" style="color: #63E6BE;"></i><span style="margin-left: 8px;">Assigned to me</span></div>', unsafe_allow_html=True)
    
    with col3:
        st.markdown(f'<div style="display: flex; align-items: center; margin-bottom: 20px;"><i class="fa-regular fa-star" style="color: #63E6BE;"></i><span style="margin-left: 8px;">Important</span></div>', unsafe_allow_html=True)
    
    with col4:
        st.markdown(f'<div style="display: flex; align-items: center; margin-bottom: 20px;"><i class="fa-solid fa-medal" style="color: #63E6BE;"></i><span style="margin-left: 8px;">Completed</span></div>', unsafe_allow_html=True)


    st.sidebar.button("Add list")
    


#main home

if 'tasks' not in st.session_state:
    st.session_state.tasks = []

def remove_task(task):
    st.session_state.tasks.remove(task)

st.header('My Todo')

add_task = st.text_area("Enter your task")

submit_button = st.button("Submit")

if(submit_button):
    if not (add_task):
        st.warning(f"Add your task first....")
    else:
        st.session_state.tasks.append(add_task)
        st.balloons()
        st.success(f"We added your task...")


st.divider()

st.write(f"Your added tasks")
for task in st.session_state.tasks:
    task_container = st.container()
    with task_container:
        col1, col2 = st.columns([4, 1])  # Two columns for task and button
        col1.write(f"- {task}")
        if col2.button("Remove", key=task):  
            remove_task(task)
            st.success(f"Removed task: {task}")
            

# sentiment_mapping = ["one", "two", "three", "four", "five"]
# selected = st.feedback("stars")
# if selected is not None:
#     st.markdown(f"You selected {sentiment_mapping[selected]} star(s).")