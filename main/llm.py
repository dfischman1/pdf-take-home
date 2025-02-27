import requests


url = "http://localhost:11434/api/chat"


def llama3(prompt):
    # data = {
    #     "model": "llama3",
    #     "prompt": prompt,
    #     "stream": False
    # }   
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
    # json = response.json()
    # return json['response']
