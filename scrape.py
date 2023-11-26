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
                
                
            ### Club ###
            if i.text.strip() == "Current club:":
              #  print(spans[index+1])
                club_picture = spans[index+1].find('img')
                club_picture_2 = club_picture.get('srcset')
                club_picture_3 = club_picture_2.split(" ")[0].replace("small", "normquad")
                
                club = spans[index+1].text.strip()
                
            ### Nationality_Pic ###
            if i.text.strip() == "Citizenship:":
                countryimg = spans[index+1].find('img')
                countryimg_2 = countryimg.get('src')
                countryimg_3 = countryimg_2.split(" ")[0].replace("tiny", "medium")
                
                
                
            ### Age ###
            if i.text.strip() == "Age:":
                age = spans[index+1].text.strip()
                
        ### League ###
        league = soup.find("a", class_="data-header__league-link")
        img_tag = league.find('img')
        src_value = img_tag.get('src')
        league_picture_1 = img_tag.get('src')
        league_picture_2 = league_picture_1.replace('verytiny', 'header')
        
        
        
        
        
        market_value = soup.find("div", class_="tm-player-market-value-development__max-value")
        print(market_value)
        
        
        
        print("POS:", position)
        print("SPECIFIC_POS:", specific_position)
        print("CLUB:", club)
        print("CLUB_PIC:", club_picture_3)
    
        print("COUNTRY_IMG:", countryimg_3)
        print("AGE:", age)
        print("LEAGUE:", league.text.strip())
        print("LEAGUE PICTURE:", league_picture_2)
   
    
    
else:
    print('Failed to retrieve the webpage')
    
                
  
    
    
    

    
