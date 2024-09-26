import streamlit as st
import pandas as pd
import json
import io
from langchain.agents import create_pandas_dataframe_agent
from langchain.chat_models import ChatOpenAI

# Importing the functions from agent.py
from agent import query_agent

# Set up the page without the theme argument
st.set_page_config(
    page_title="CSV Analyzer",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Use CSS to style the app to have a dark theme
st.markdown(
    """
    <style>
    .reportview-container {
        background-color: #0E1117;
        color: #FAFAFA;
    }
    .sidebar .sidebar-content {
        background-color: #262730;
        color: #FAFAFA;
    }
    .stButton>button {
        background-color: #FF4B4B;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

def decode_response(response: str) -> dict:
    """This function converts the string response from the model to a dictionary object."""
    return json.loads(response)

def write_response(response_dict: dict):
    """Write a response from an agent to a Streamlit app."""
    if "answer" in response_dict:
        st.write(response_dict["answer"])

    if "bar" in response_dict:
        data = response_dict["bar"]
        df = pd.DataFrame(data)
        df.set_index("columns", inplace=True)
        st.bar_chart(df)

    if "line" in response_dict:
        data = response_dict["line"]
        df.set_index("columns", inplace=True)
        st.line_chart(df)

    if "table" in response_dict:
        data = response_dict["table"]
        df = pd.DataFrame(data["data"], columns=data["columns"])
        st.table(df)

st.title("👨‍💻 Chat with your CSV")
st.write("Please upload your CSV file below.")

# Add dropdown menu in the sidebar
option = st.sidebar.selectbox(
    "Choose an action:",
    ("Summarization Report", "Analysis", "Visualization")
)

# Input for CSV file
data = st.file_uploader("Upload a CSV")

# Input for user query (only for analysis or visualization)
query = None
if option == "Analysis" or option == "Visualization":
    query = st.text_area("Insert your query")

# Submit button
if st.button("Submit Query", type="primary"):
    if data is not None:
        # Read the CSV file into a DataFrame
        df = pd.read_csv(data)

        if option == "Summarization Report":
            # Generate summary statistics for the dataset
            st.markdown("### **Dataset Summary**")

            # Prepare a StringIO buffer to hold the summary text
            summary_buffer = io.StringIO()

            # Number of rows and columns
            num_rows = df.shape[0]
            num_cols = df.shape[1]
            st.markdown(f"**Number of rows:** {num_rows}")
            st.markdown(f"**Number of columns:** {num_cols}")
            summary_buffer.write(f"Number of rows: {num_rows}\n")
            summary_buffer.write(f"Number of columns: {num_cols}\n")

            # Data types of each column
            st.markdown("### **Data Types**")
            st.markdown(df.dtypes.to_markdown())
            summary_buffer.write("Data types:\n")
            summary_buffer.write(f"{df.dtypes}\n\n")

            # Range of values for numeric columns
            numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
            if len(numeric_cols) > 0:
                st.markdown("### **Range of Values for Numeric Columns**")
                summary_buffer.write("Range of values for numeric columns:\n")
                for col in numeric_cols:
                    min_val = df[col].min()
                    max_val = df[col].max()
                    st.markdown(f"- **{col}:** min={min_val}, max={max_val}")
                    summary_buffer.write(f"{col}: min={min_val}, max={max_val}\n")
            else:
                st.markdown("No numeric columns found.")
                summary_buffer.write("No numeric columns found.\n")

            # Value counts for categorical columns
            categorical_cols = df.select_dtypes(include=['object', 'category']).columns
            if len(categorical_cols) > 0:
                st.markdown("### **Value Counts for Categorical Columns**")
                summary_buffer.write("Value counts for categorical columns:\n")
                for col in categorical_cols:
                    st.markdown(f"**{col}:**")
                    st.markdown(df[col].value_counts().to_markdown())
                    summary_buffer.write(f"{col}:\n{df[col].value_counts()}\n\n")
            else:
                st.markdown("No categorical columns found.")
                summary_buffer.write("No categorical columns found.\n")

            # Brief description about what the dataset represents
            st.markdown("### **Dataset Description**")
            st.write("""
                This dataset contains various columns representing different features. 
                Numeric columns show the range of values, and categorical columns list the value counts for each category. 
                The dataset provides insights based on these features.
            """)
            summary_buffer.write("""
                Dataset Description:\nThis dataset contains various columns representing different features. 
                Numeric columns show the range of values, and categorical columns list the value counts for each category. 
                The dataset provides insights based on these features.\n
            """)

            # Provide download link for the summary as a text file
            summary_text = summary_buffer.getvalue()
            st.download_button(
                label="Download Summary Report",
                data=summary_text,
                file_name="dataset_summary.txt",
                mime="text/plain"
            )
        
        else:
            # Create a ChatOpenAI instance using GPT-4 model
            openai_api_key = ''
            openai_instance = ChatOpenAI(api_key=openai_api_key, model="gpt-4", temperature=0)
        
            # Create the pandas DataFrame agent using the GPT-4 model
            agent = create_pandas_dataframe_agent(openai_instance, df, verbose=True)

            # Query the agent based on the option selected from the dropdown
            if option == "Analysis":
                response = query_agent(agent=agent, query="Perform an analysis of the dataset")
            elif option == "Visualization":
                response = query_agent(agent=agent, query=query)  # Use the user's input query for visualization

            # Decode the response
            decoded_response = decode_response(response)

            # Write the response to the Streamlit app
            write_response(decoded_response)
