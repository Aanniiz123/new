# streamlit_app.py

import streamlit as st
from joke import workflow  # Import your compiled workflow

st.title("Daily Joke Generator 😂")

# User input
topic = st.text_area("Enter your day's activities:", placeholder="e.g. I was lazy, ate snacks, and binge-watched TV.")

# When user clicks "Generate"
if st.button("Generate Joke"):
    if topic.strip() == "":
        st.warning("Please enter some activities first.")
    else:
        # Run LangGraph workflow
        initial_state = {'topic': topic}
        result = workflow.invoke(initial_state)

        # Display output
        st.subheader("Here's your joke:")
        st.success(result['joke'])

        st.subheader("Score:")
        st.info(f"{result['score']} / 10")

        st.subheader("Feedback:")
        st.write(result['feedback'])

        st.subheader("Should Post to Social Media?")
        st.write("✅ Yes!" if result['social_media'] == 'yes' else "❌ No")
