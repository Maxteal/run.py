import requests
from bs4 import BeautifulSoup
 
# Create a request to get the HTML of the page with the ads
url = "https://ay.link/dn9JMD"  # insert URL here 
req = requests.get(url)  # make request to the URL and save HTML in `req` variable  
html_doc = req.text  # get text from response object and save in `html_doc` variable  

# Parse HTML using Beautiful Soup library 
soup = BeautifulSoup(html_doc, 'html.parser')  

# Find all links which have class="skip" attribute and extract their URLs  
skiplinks = soup.find_all('a', class_='skip')  

for link in skiplinks:    # iterate over each link found on the page   

    actual_link = link['href']    # extract actual link from href attribute of anchor tag    

    if actual_link != "#":      # if it's not empty, then make a new request with this URL      

        skipreq = requests.get(actual_link)      # make new request for this link    

        skiphtml = skipreq.text      # save response text to new variable      

        newsoup = BeautifulSoup(skiphtml, 'html5lib')      

        skiparticle = newsoup.find('div', id='article-body')  
        
        if skiparticle:
            print(skiparticle.text.strip())
