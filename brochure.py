from openai import OpenAI
from dotenv import load_dotenv
from scraper import scrape_website,get_links
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

def select_reslevant_links(url):
    links=get_links(url)
    links_system_promt=(
                        "Yor are given a list of links found on the webpage. "
                        "Decide which ones are relevant for building a company brochure. "
                        "(e.g About, Comapny,Team Page) "
                        "Ignore the things like Terms of Service ,Privacy Policy ,or social media links. "
                        "Respond ONLY in JSON,in this exact format: \n"
                        '{"links":[{"type":"about page,"url":"https://..."},]}'
                        )
    
    links_user_prompt=(
        f"Here are the list of the links from the {url}:\n{links}\n\nReturn the relvant ones as JSON"
    )
    response=client.chat.completions.messages(model="gpt-4o-mini",
                                              messages=[{"role":"system","content":links_system_promt},
                                                        {"role":"user","content":links_user_prompt}],
                                              #resonse formate
                                              response_format={"type":"json_object"}
                                              )
    result =json.loads(response.choice[0].message.content)  
    return result["links"]
 ##Json.loads
    #!response_format in openai client
brochure=generate_brochure("https://anthropic.com")
print(brochure)