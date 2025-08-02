{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "d62530bc-1ee7-4bf9-b3d0-cbff6134f0ff",
   "metadata": {},
   "outputs": [
    {
     "ename": "StreamlitSecretNotFoundError",
     "evalue": "No secrets found. Valid paths for a secrets.toml file or secret directories are: C:\\Users\\fgmbr\\.streamlit\\secrets.toml, C:\\Users\\fgmbr\\.streamlit\\secrets.toml",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mStreamlitSecretNotFoundError\u001b[0m              Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[2], line 12\u001b[0m\n\u001b[0;32m      9\u001b[0m df \u001b[38;5;241m=\u001b[39m pd\u001b[38;5;241m.\u001b[39mread_csv(\u001b[38;5;124mr\u001b[39m\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mC:\u001b[39m\u001b[38;5;124m\\\u001b[39m\u001b[38;5;124mUsers\u001b[39m\u001b[38;5;124m\\\u001b[39m\u001b[38;5;124mfgmbr\u001b[39m\u001b[38;5;124m\\\u001b[39m\u001b[38;5;124mData\u001b[39m\u001b[38;5;124m\\\u001b[39m\u001b[38;5;124mGames.csv\u001b[39m\u001b[38;5;124m\"\u001b[39m)\n\u001b[0;32m     11\u001b[0m \u001b[38;5;66;03m# Initialize OpenAI client from a secret\u001b[39;00m\n\u001b[1;32m---> 12\u001b[0m api_key \u001b[38;5;241m=\u001b[39m st\u001b[38;5;241m.\u001b[39msecrets[\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mOPENAI_API_KEY\u001b[39m\u001b[38;5;124m\"\u001b[39m]\n\u001b[0;32m     13\u001b[0m llm \u001b[38;5;241m=\u001b[39m ChatOpenAI(model\u001b[38;5;241m=\u001b[39m\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mgpt-3.5-turbo\u001b[39m\u001b[38;5;124m\"\u001b[39m, temperature\u001b[38;5;241m=\u001b[39m\u001b[38;5;241m0\u001b[39m, openai_api_key\u001b[38;5;241m=\u001b[39mapi_key)\n\u001b[0;32m     14\u001b[0m agent \u001b[38;5;241m=\u001b[39m create_pandas_dataframe_agent(llm, df, verbose\u001b[38;5;241m=\u001b[39m\u001b[38;5;28;01mFalse\u001b[39;00m, allow_dangerous_code\u001b[38;5;241m=\u001b[39m\u001b[38;5;28;01mTrue\u001b[39;00m)\n",
      "File \u001b[1;32m~\\anaconda3\\Lib\\site-packages\\streamlit\\runtime\\secrets.py:470\u001b[0m, in \u001b[0;36mSecrets.__getitem__\u001b[1;34m(self, key)\u001b[0m\n\u001b[0;32m    464\u001b[0m \u001b[38;5;250m\u001b[39m\u001b[38;5;124;03m\"\"\"Return the value with the given key. If no such key\u001b[39;00m\n\u001b[0;32m    465\u001b[0m \u001b[38;5;124;03mexists, raise a KeyError.\u001b[39;00m\n\u001b[0;32m    466\u001b[0m \n\u001b[0;32m    467\u001b[0m \u001b[38;5;124;03mThread-safe.\u001b[39;00m\n\u001b[0;32m    468\u001b[0m \u001b[38;5;124;03m\"\"\"\u001b[39;00m\n\u001b[0;32m    469\u001b[0m \u001b[38;5;28;01mtry\u001b[39;00m:\n\u001b[1;32m--> 470\u001b[0m     value \u001b[38;5;241m=\u001b[39m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_parse()[key]\n\u001b[0;32m    471\u001b[0m     \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;129;01mnot\u001b[39;00m \u001b[38;5;28misinstance\u001b[39m(value, Mapping):\n\u001b[0;32m    472\u001b[0m         \u001b[38;5;28;01mreturn\u001b[39;00m value\n",
      "File \u001b[1;32m~\\anaconda3\\Lib\\site-packages\\streamlit\\runtime\\secrets.py:372\u001b[0m, in \u001b[0;36mSecrets._parse\u001b[1;34m(self)\u001b[0m\n\u001b[0;32m    366\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;129;01mnot\u001b[39;00m found_secrets_file:\n\u001b[0;32m    367\u001b[0m     error_msg \u001b[38;5;241m=\u001b[39m (\n\u001b[0;32m    368\u001b[0m         secret_error_messages_singleton\u001b[38;5;241m.\u001b[39mget_no_secrets_found_message(\n\u001b[0;32m    369\u001b[0m             file_paths\n\u001b[0;32m    370\u001b[0m         )\n\u001b[0;32m    371\u001b[0m     )\n\u001b[1;32m--> 372\u001b[0m     \u001b[38;5;28;01mraise\u001b[39;00m StreamlitSecretNotFoundError(error_msg)\n\u001b[0;32m    374\u001b[0m \u001b[38;5;28;01mfor\u001b[39;00m k, v \u001b[38;5;129;01min\u001b[39;00m secrets\u001b[38;5;241m.\u001b[39mitems():\n\u001b[0;32m    375\u001b[0m     \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_maybe_set_environment_variable(k, v)\n",
      "\u001b[1;31mStreamlitSecretNotFoundError\u001b[0m: No secrets found. Valid paths for a secrets.toml file or secret directories are: C:\\Users\\fgmbr\\.streamlit\\secrets.toml, C:\\Users\\fgmbr\\.streamlit\\secrets.toml"
     ]
    }
   ],
   "source": [
    "import os\n",
    "import pandas as pd\n",
    "import streamlit as st\n",
    "from openai import OpenAI\n",
    "from langchain_openai import ChatOpenAI\n",
    "from langchain_experimental.agents import create_pandas_dataframe_agent\n",
    "\n",
    "# Load your DataFrame once at startup\n",
    "df = pd.read_csv(r\"C:\\Users\\fgmbr\\Data\\Games.csv\")\n",
    "\n",
    "# Initialize OpenAI client from a secret\n",
    "api_key = st.secrets[\"OPENAI_API_KEY\"]\n",
    "llm = ChatOpenAI(model=\"gpt-3.5-turbo\", temperature=0, openai_api_key=api_key)\n",
    "agent = create_pandas_dataframe_agent(llm, df, verbose=False, allow_dangerous_code=True)\n",
    "\n",
    "# Streamlit UI\n",
    "st.title(\"Games Data Chatbot\")\n",
    "query = st.text_input(\"Ask a question about the dataset:\")\n",
    "if st.button(\"Submit\") and query:\n",
    "    result = agent.invoke(query, return_only_outputs=True)\n",
    "    answer = result.get(\"output\", result) if isinstance(result, dict) else result\n",
    "    st.write(answer)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "id": "7f7353d4-9502-49f5-ac14-efca9f055f64",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
