# """
# This script creates a database of information gathered from local text files.
# """

# from langchain.document_loaders import DirectoryLoader, TextLoader
# from langchain.text_splitter import RecursiveCharacterTextSplitter
# from langchain.embeddings import HuggingFaceEmbeddings
# from langchain.vectorstores import FAISS

# # define what documents to load
# loader = DirectoryLoader("./", glob="*.txt", loader_cls=TextLoader)

# # interpret information in the documents
# documents = loader.load()
# splitter = RecursiveCharacterTextSplitter(chunk_size=500,
#                                           chunk_overlap=50)
# # texts = splitter.split_documents(documents)
# # texts = splitter.create_documents(documents)


# texts = splitter.split_text(documents)
# embeddings = HuggingFaceEmbeddings(
#     model_name="sentence-transformers/all-MiniLM-L6-v2",
#     model_kwargs={'device': 'cpu'})

# # create and save the local database
# db = FAISS.from_documents(texts, embeddings)
# db.save_local("faiss")


# from transformers import pipeline

# model_id="/Users/daelin/Documents/Projects/Jobs/llama/llama-models/models/llama3_1/Meta-Llama-3.1-70B-Instruct"

# pipe = pipeline("text-generation", model=model_id, device="cuda")
# message = [{"role": "user", "content": "How to solve a quadtratic equation"}]

# outputs = pipe(message, max_new_tokens=256, do_sample=False)
# print(outputs[0]["generated_text"][-1]["content"])




import requests


url = "http://localhost:11434/api/chat"


def llama3(prompt):
    data = {
        "model": "llama3",
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ],
        "stream": False
    }

    headers = {
        "Content-Type": "application/json"
    }

    response = requests.post(url, headers=headers, json=data)
    return response.json()['message']['content']
