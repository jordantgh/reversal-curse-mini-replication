from dotenv import load_dotenv
from litellm import completion
import json
import time
import random 

load_dotenv()

sys_prompt = {"role": "system",
              "content": "You are ChatGPT, a large language model trained by OpenAI, based on the GPT-4 architecture. If asked to name someone, you will return only the name, with no other text before or after it."}

with open('celebs_parents.json', 'r') as f:
    celebs_parents = json.load(f)

predicted_children = []
for pair in celebs_parents:
    parent_name = pair['parent_name']
    true_child_name = pair['celebrity_name']
    
    message_input = [
        sys_prompt,
        {"role": "user",
         "content": f"Name a child of {parent_name}. Return only the name. If you cannot think of a name, type 'pass'. If you can think of multiple, simply choose the first that comes to mind."},
    ]

    response = completion(model="openrouter/openai/gpt-4",
                          messages=message_input)
    
    # check accuracy - strict atm (exact match & doesnt account for >1 kid)
    child_name = response["choices"][0]["message"]["content"]
    is_accurate = (true_child_name in child_name)
    entry = {"parent": parent_name, "predicted_child": child_name, "accurate": is_accurate}

    
    predicted_children.append(entry)
    
    print(f"Parent: {parent_name}, Predicted Child: {child_name}, Accurate: {is_accurate}")
    
    time.sleep(random.uniform(0.1, 0.5))

with open('pred_celebs_parents.json', 'w') as f:
    json.dump(predicted_children, f)

