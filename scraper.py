import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    #*Fetch the website using the request
    response=requests.get(url,{"User-Agent":"Mozilla/5.0"})
    
    soup=BeautifulSoup(response.content,"html.parser")
    
    title=soup.title.string if soup.title else "No title found"
    
    for tag in soup.find_all(["script","style","input","image"]):
        tag.decompose()
        
    text=soup.get_text(separator="\n",strip=True)
    
    return text,title



def scrape_relevant_links(url):
    #*Fetch the web from the server using request
    response=requests.get(url,{"User-Agent":"Mozilla/5.0"})
    
    soup=BeautifulSoup(response.content,"html-parser")
    links=[a.get("href") for a in soup.find_all("a") if a.get("href")]
    return links