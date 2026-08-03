from openai import OpenAI
from dotenv import load_dotenv
from scraper import scrape_website
import os

load_dotenv()
OPEN_API_KEY=os.getenv("OPENAI_API_KEY")
client=OpenAI(api_key=OPEN_API_KEY)

def generate_brochure(url):
    text,title=scrape_website(url)
    trimmed_text=text[:5000]
    system_prompt=(
        "You are an assitant that analyzes the content of a company website "
        "and creates a short ,engaging marketing brochure for the prospective customers. "
        "Respond in markdown"
                   )
    user_prompt=(
        f"Here is the content from the company's website (title:{title}).\n\n"
        f"{trimmed_text}\n\n"
        "Please write a short brochure about this company based on the content above."
    )
    response =client.chat.completions.create(model="gpt-4o-mini",
                                             messages=[{
                                                 "role":"system","content":system_prompt
                                             },
                                                       {
                                                           "role":"user",
                                                           "content":user_prompt
                                                       }]
                                             )
    return response.choices[0].message.content

brochure=generate_brochure("https://anthropic.com")
print(brochure)