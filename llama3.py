import streamlit as st
import boto3
import json

# Initialize Streamlit app
st.title("Llama3 AI Web App")
st.write("Enter your prompt below to get AI-generated responses.")

# User input
user_input = st.text_area("Your prompt:", "")

# AWS Bedrock client
bedrock = boto3.client(service_name="bedrock-runtime", region_name="ap-south-1")

# Function to get AI response
def get_llama3_response(prompt):
    payload = {
        "prompt": f"[INST] {prompt} [/INST]",
        "max_gen_len": 512,
        "temperature": 0.5,
        "top_p": 0.9
    }
    
    body = json.dumps(payload)
    model_id = "meta.llama3-8b-instruct-v1:0"

    response = bedrock.invoke_model(
        body=body,
        modelId=model_id,
        accept="application/json",
        contentType="application/json"
    )

    response_body = json.loads(response.get("body").read())
    return response_body.get("generation", "No response generated.")

# Button to submit the query
if st.button("Generate Response"):
    if user_input.strip():
        with st.spinner("Generating response..."):
            response_text = get_llama3_response(user_input)
            st.subheader("AI Response:")
            st.write(response_text)
    else:
        st.warning("Please enter a prompt before generating a response.")
