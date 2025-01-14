import ollama

def query_local_llm(model_name, query):
    response = ollama.generate(model=model_name, prompt=query)
    return response['response']