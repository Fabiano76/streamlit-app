import os
import pandas as pd
from langchain_openai import ChatOpenAI
from langchain_experimental.agents import create_pandas_dataframe_agent

# Load your CSV into a DataFrame
df = pd.read_csv(r'C:\Users\fgmbr\Data\Games.csv')

# Read your OpenAI API key from the environment
api_key = os.environ.get("OPENAI_API_KEY")
if not api_key:
    raise EnvironmentError(
        "OPENAI_API_KEY environment variable is not set. "
        "Set it to your real API key before running this script."    
    )

# Initialise the LLM
llm = ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=0,
    openai_api_key=api_key,
)

# Create the DataFrame agent
agent = create_pandas_dataframe_agent(
    llm,
    df,
    verbose=False,
    agent_type="openai-tools",
    allow_dangerous_code=True,
)

# Interactive loop
print("Welcome to the Games chatbot! Ask questions about the dataset.")
print("Type 'quit' or 'exit' to end the session.\n")

while True:
    question = input("Ask a question (or 'quit'): ")
    if question.strip().lower() in {"quit", "exit"}:
        print("Exiting the chatbot. Goodbye!")
        break
    try:
        result = agent.invoke(question, return_only_outputs=True)
        if isinstance(result, dict):
            answer = result.get("output", result)
        else:
            answer = result
        print(answer, "\n")
    except Exception as e:
        print(f"An error occurred: {e}\n")
