import ollama

def query_local_llm(model_name, query):
    # client = OllamaClient()
    response = ollama.generate(model=model_name, prompt=query)
    return response['response']