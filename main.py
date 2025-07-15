import streamlit as st
import pandas as pd

# Load your CSV
df = pd.read_csv('data/portfolio.csv')

# --- Top section ---
st.title("My Portfolio")

col1, col2 = st.columns(2)

with col1:
    st.image("data/profile.png", width=250)

with col2:
    st.header("Hi, I'm Your Name 👋")
    st.write("""
    I’m a Mechatronics Engineer transitioning to Python development.
    I love building apps that merge engineering and data.
    """)

st.write("---")

# --- Projects section ---
st.header("My Projects")

for index, row in df.iterrows():
    proj_col1, proj_col2 = st.columns([1, 2])
    
    with proj_col1:
        st.image(row["Image"], width=200)
    
    with proj_col2:
        st.subheader(row["Project"])
        st.write(row["Description"])
        st.markdown(f"[View Project]({row['Link']})")

    st.write("---")
