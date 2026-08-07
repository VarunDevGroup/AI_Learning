#Steps to setup the enviornment

#Create new envionment variable

python -m venv .venv

#How to remove
Remove-Item .venv -Recurse -Force

#Activate the variable
.\.venv\Scripts\Activate.ps1

#If PowerShell blocks activation, run:
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

#Upgrade pip
python -m pip install --upgrade pip

#install AI Packages
pip install numpy pandas matplotlib seaborn scikit-learn scipy jupyter ipykernel

#for deep learning
pip install openai langchain langgraph chromadb sentence-transformers transformers torch

#save the enironment
pip freeze > requirements.txt

#install with saved file
pip install -r requirements.txt

#Select the Correct Python Interpreter
Press Ctrl + Shift + P
Choose Python: Select Interpreter
Select:

#how to check
import sys

print(sys.executable)

#configure Juypter Notebook
python -m ipykernel install --user --name classification-env --display-name "Python (Classification)"

#How to Work everyday
.\.venv\Scripts\Activate.ps1
code .

#How to deactivate
deactivate

Given your goal of becoming an AI Forward Deployment Engineer, I'd install these in phases:

Phase	            Packages
Core Python	        numpy, pandas, matplotlib, seaborn, scipy
Machine Learning	scikit-learn, xgboost, lightgbm
Deep Learning	    torch, torchvision, transformers
LLM & RAG	        openai, langchain, langgraph, chromadb, sentence-transformers, faiss-cpu, tiktoken
Data	            jupyter, ipykernel, plotly, polars
APIs	            fastapi, uvicorn, pydantic
MLOps	            mlflow, wandb, opentelemetry-sdk
Utilities	        python-dotenv, requests, rich, typer