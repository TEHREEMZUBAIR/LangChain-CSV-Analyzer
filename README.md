
---

# 📊 CSV Catalyst: CSV Analyzer and Visualizer using LangChain

CSV Catalyst is a powerful tool designed to analyze, clean, and visualize CSV data using LangChain and OpenAI. With an intuitive interface built on Streamlit, it allows you to interact with your data and get intelligent insights with just a few clicks.

## 🚀 Project Overview
This project leverages the power of large language models (LLMs) to analyze CSV datasets, generate summary reports, perform data analysis, and create visualizations (bar and line charts). It's powered by LangChain and OpenAI's GPT-4.

## 📦 Features
- **Upload CSV files** for automated analysis and visualization.
- **Summarize CSV data** with insights like data types, numeric ranges, and value counts.
- **Generate bar and line charts** for interactive visualizations.
- **Query-based data analysis** through LangChain's AI agent.

---

## 🛠 Setup Instructions

Follow these steps to get the project up and running on your machine.

### 1️⃣ Clone the Repository
```bash
git clone <repository-url>
cd <repository-directory>
```

### 2️⃣ Set Up a Virtual Environment
Create a virtual environment to manage dependencies.

```bash
python -m venv env
source env/bin/activate  # On Windows: .\env\Scripts\activate
```

### 3️⃣ Install Dependencies
Install the required dependencies from `requirements.txt`.

```bash
pip install -r requirements.txt
```

### 4️⃣ Obtain an OpenAI API Key
You need to create an OpenAI API key to enable the LangChain agent for querying the CSV data.

1. Sign up at [OpenAI](https://beta.openai.com/signup/).
2. Go to your [API Keys](https://beta.openai.com/account/api-keys) and create a new key.
3. Save the API key for the next step.

### 5️⃣ Set Up Environment Variables
Create a `.env` file in the root directory and add your OpenAI API key:

```bash
OPENAI_API_KEY="your-openai-api-key-here"
```

### 6️⃣ Run the Streamlit Interface
Run the Streamlit app to start the CSV analyzer interface.

```bash
streamlit run interface.py
```

After running the command, your app should open automatically in the browser.

---

## 📂 File Structure

```
📦 Project Directory
├── 📄 agent.py               # Contains the logic for LangChain-powered data analysis and visualization
├── 📄 interface.py           # Streamlit app for interacting with the CSV analyzer
├── 📄 requirements.txt       # Dependencies for the project
├── 📄 README.md              # This readme file
├── 📄 .env                   # OpenAI API key (not included in the repo)
```

---

## 🎨 Usage Instructions

1. **Upload CSV File**: Start by uploading your CSV file.
2. **Select Action**: Choose an action from the sidebar:
   - **Summarization Report**: Provides a summary of the dataset.
   - **Analysis**: Performs a detailed analysis of the dataset using AI.
   - **Visualization**: Query the system for visualizing data in bar or line charts.
3. **Submit Query**: For "Analysis" and "Visualization," enter a query to analyze or visualize the dataset.
4. **Download Reports**: For the summarization report, you can download a detailed text report of your dataset.

---

## 💻 Example Queries

- **Analysis Queries**: 
  - "Show me the summary of the dataset."
  - "Analyze the correlation between columns A and B."
  
- **Visualization Queries**: 
  - "Create a bar chart of column A."
  - "Plot a line chart for columns A and B."

---

🔎 Summarizer Example:
![Summarizer](https://github.com/user-attachments/assets/086b49b9-dbd2-4e2b-b388-37afb888a5f8)

🔎 Data Analysis Example:
You can ask the agent to analyze your dataset and provide detailed insights.

Example query:
"Which Products have the highest Sales"
Result:
![analysis](https://github.com/user-attachments/assets/49c16da0-c388-4f58-8674-44d8c5839804)

📈 Visualization Example:
By asking questions related to visualization, you can easily generate bar charts or line charts.

Example query:
"Create a bar chart of the sales of first five products."
Output:
![Visualization](https://github.com/user-attachments/assets/64954971-d0fa-4591-9d3d-b42a08ee2dc7)

---

## 🧑‍💻 Dependencies

- **LangChain**: Framework for building applications powered by language models.
- **OpenAI**: API for GPT-4 integration.
- **Streamlit**: Interactive web app framework for Python.
- **Pandas**: Data manipulation and analysis library.
  
---

## 🛠 Troubleshooting

1. **Environment Setup Issues**: Make sure your virtual environment is activated and all dependencies are installed correctly.
2. **OpenAI API Errors**: Double-check your `.env` file to ensure the API key is set correctly.
3. **Streamlit App Not Running**: Ensure Streamlit is installed and the port is not blocked.

---

## 🚀 Future Enhancements
- Add more advanced chart types like scatter plots.
- Integrate additional data analysis techniques such as clustering.
- Enhance the model's ability to interpret complex queries.

---

Made with ❤️ by Tehreem Zubair!

---
