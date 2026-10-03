print("This is my first hackathon. I'm quiet excited")
import streamlit as st
from openai import OpenAI

client = OpenAI(api_key="YOUR_API_KEY") #add a free version 

st.title("QueueLess AI")

people = st.number_input("People ahead", min_value=0)
counters = st.number_input("Number of counters", min_value=1)
minutes = st.number_input("Average minutes per person", min_value=1)

if st.button("Estimate Waiting Time"):

    prompt = f"""
    There are {people} people ahead.
    There are {counters} counters working.
    Each person takes approximately {minutes} minutes.

    Estimate the waiting time and explain it simply.
    """

    response = client.responses.create(
        model="gpt-5",
        input=prompt
    )

    st.write(response.output_text)