<h1>Steps to setup the enviornment</h1>

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

<Table>
<tr><td>Phase	</td><td>            Packages</td></tr>
<tr><td>Core Python	  	</td><td>        numpy, pandas, matplotlib, seaborn, scipy</td></tr>
<tr><td>Machine Learning	</td><td>  	scikit-learn, xgboost, lightgbm</td></tr>
<tr><td>Deep Learning	 	</td><td>     torch, torchvision, transformers</td></tr>
<tr><td>LLM & RAG	 	</td><td>         openai, langchain, langgraph, chromadb, sentence-transformers, faiss-cpu, tiktoken</td></tr>
<tr><td>Data		</td><td>              jupyter, ipykernel, plotly, polars</td></tr>
<tr><td>APIs		</td><td>              fastapi, uvicorn, pydantic</td></tr>
<tr><td>MLOps	   	</td><td>           mlflow, wandb, opentelemetry-sdk</td></tr>
<tr><td>Utilities	 	</td><td>         python-dotenv, requests, rich, typer</td></tr></table>
