from langchain.llms import GooglePalm
from langchain.utilities import SQLDatabase
from langchain_experimental.sql import SQLDatabaseChain
from langchain.prompts import SemanticSimilarityExampleSelector
import getpass
import os

if 'google_api_key' not in os.environ:
    os.environ['google_api_key'] = getpass.getpass('AIzaSyCGfCRen7rmwdsfWAnfc7QdO4ocb86_gpg')
### Enter your google password if two factor authentication is turned on 

import os
from langchain_google_genai import GoogleGenerativeAIEmbeddings

# Set the API key
os.environ["google_api_key"] = "AIzaSyCGfCRen7rmwdsfWAnfc7QdO4ocb86_gpg"

# Initialize the embeddings with the correct API key
embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
from langchain.vectorstores import Chroma
from langchain.prompts import FewShotPromptTemplate
from langchain.chains.sql_database.prompt import PROMPT_SUFFIX, _mysql_prompt
from langchain.prompts.prompt import PromptTemplate

from few_shots import few_shots

import os
from dotenv import load_dotenv
load_dotenv()  # take environment variables from .env (especially openai api key)


db_user = "root"
db_password = "subhajit257"
db_host = "127.0.0.1"
db_name = "atliq_tshirts"

db = SQLDatabase.from_uri(f"mysql+pymysql://{db_user}:{db_password}@{db_host}/{db_name}",sample_rows_in_table_info=3)
print(db.table_info)

    llm = GooglePalm(google_api_key=os.environ["GOOGLE_API_KEY"], temperature=0.1)
