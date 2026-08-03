from openai import OpenAI
from dotenv import load_dotenv
import os
##! Load .env file so our api key is available
load_dotenv()

#Create a client using the key from  .env openai key
client =OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

#send simple simple message to gpt
response=client.chat.completions.create(model="gpt-4o-mini",
                                        messages=[{"role":"user","content":"In one sentence, explain what an LLM is to a complete beginner."}])

print(response.choices[0].message.content)