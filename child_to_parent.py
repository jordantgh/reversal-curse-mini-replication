from dotenv import load_dotenv
from litellm import completion
import json
import time
import random 

load_dotenv()

functions = [
    {
      "name": "celebrity_parent",
      "description": "Provide names of a celebrity and one of their parents",
      "parameters": {
        "type": "object",
        "properties": {
          "celebrity_name": {
            "type": "string",
            "description": "A celebrity's full name."
          },
          "parent_name": {
            "type": "string",
            "description": "The full name of one of the celebrity's parents. It can be any of the two parents."
          }
        },
        "required": ["celebrity_name", "parent_name"]
      }
    }
  ]

sys_prompt = {"role": "system",
              "content": "You are ChatGPT, a large language model trained by OpenAI, based on the GPT-4 architecture."}

celebs_parents = []
for i in range(100):
    message_input = [
        sys_prompt,
        {"role": "user",
         "content": f"""
         
         Give me the names of a celebrity and one of their parents (pick any of the two parents at random). Don't use any existing examples in this prompt, if there are any.
         
         Examples here, if any:
         {celebs_parents}"""}
    ]
    
    response = completion(model = "openrouter/openai/gpt-4",
                          messages = message_input,
                          functions = functions)

    
    function_call_data = response["choices"][0]["message"]["function_call"]
    function_args = json.loads(function_call_data['arguments'])
    
    celebs_parents.append(function_args)
    
    print(f"Iteration {i+1}: {function_args}")
    
    time.sleep(random.uniform(0.1, 0.5))

with open('celebs_parents.json', 'w') as f:
    json.dump(celebs_parents, f)