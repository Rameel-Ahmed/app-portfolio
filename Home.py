import streamlit as st
import pandas as pd

# Load your CSV
df = pd.read_csv('data/data.csv')

# --- Top section ---
st.title("My Portfolio")

col1, col2 = st.columns(2)

with col1:
    st.image("data/images/profile.png", width=250)

with col2:
    st.header("Hi, I'm Your Name 👋")
    st.write("""
    I’m a Mechatronics Engineer transitioning to Python development.
    I love building apps that merge engineering and data.
    """)

st.write("---")

# --- Projects section ---
st.header("My Projects")

# Loop through projects in pairs of 2
for i in range(0, len(df), 2):
    col1,middle_col, col2 = st.columns([1.5,0.5,1.5])
    
    # First project in this row
    with col1:
        row = df.iloc[i]
        st.image(row["Image"], width=200)
        st.subheader(row["Project"])
        st.write(row["Description"])
        st.markdown(f"[View Project]({row['Link']})")
    
    # Second project in this row (if it exists)
    if i + 1 < len(df):
        with col2:
            row = df.iloc[i + 1]
            st.image(row["Image"], width=200)
            st.subheader(row["Project"])
            st.write(row["Description"])
            st.markdown(f"[View Project]({row['Link']})")

    st.write("---")
