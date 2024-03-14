

def save(functionName, story, result):
    with open(f"checkpoints/{functionName}_{story}.txt", 'w', encoding='utf-8') as f:
        f.write(result)

def get(functionName, story):
    with open(f"checkpoints/{functionName}_{story}.txt", 'r', encoding='utf-8') as f:
        return f.read()