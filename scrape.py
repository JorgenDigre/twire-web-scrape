import requests, re
from bs4 import BeautifulSoup

url = 'https://www.transfermarkt.com/mario-gotze/profil/spieler/74842'

# Headers mimic a legitimate browser request
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    
    player_data_div = soup.find("div", class_="large-6 large-pull-6 small-12 columns spielerdatenundfakten")
    
    if player_data_div:
        # Find all span elements within the player data div
        spans = player_data_div.find_all("span")
        for index, i in enumerate(spans):
         
            
            ### Position ###
            if i.text.strip() == "Position:":
                specific_position = spans[index+1].text.strip()
                if "Midfield -" in specific_position or "midfield -" in specific_position:
                    position = "MID"
                if "Defender -" in specific_position or "defender -" in specific_position:
                    position = "DEF"
                if "Attack -" in specific_position or "attack -" in specific_position:
                    position = "FOR"
                if "Goalkeeper" in specific_position or "goalkeeper" in specific_position:
                    position = "G"
                new_position = specific_position.split(" - ")
                specific_position = new_position[-1]
                
            ### Club ###
            if i.text.strip() == "Current club:":
                club = spans[index+1].text.strip()
                
            ### Nationality ###
            if i.text.strip() == "Citizenship:":
                nationality = spans[index+1].text.strip()
        
        print(nationality)
    
    
    ### Position ###
   # position_label = soup.find(lambda tag: tag.name == 'li' and 'Position:' in tag.text if tag.name == 'li' else False)
   # position_content = position_label.find_next('span', class_='data-header__content')
   # specific_position = position_content.text.strip()
   # positions = []
    
    
else:
    print('Failed to retrieve the webpage')
    
                
  
    
    
    

    
