import json
import requests
from requests.models import Response
#peticiones de los datos a la API 
class Lolconfig:
    def __init__(self,summoner,region):
        self.summoner = summoner
        self.region = region
        #guardar headers
        self.headers = {'X-Riot-Token': 'riot-token'}

    def start(self):
        #LAN server, buscar usuario
        url = f'https://la1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{self.summoner}'
        response = requests.get(url,headers=self.headers)
        return response.json()

class Lolmain(Lolconfig):
    def __init__(self, summoner,region):
        super().__init__(summoner,region)
        #enviar info
    def saludar(self):
        summoner = self.start()
        nombre = summoner['name']
        
        nivel = summoner['summonerLevel']
        icon_id = summoner['profileIconId']

        saludar = f'{nombre}, nivel {nivel}.'
        icon_url  = f'https://ddragon.leagueoflegends.com/cdn/11.6.1/img/profileicon/{icon_id}.png'
        return { 'saludar': saludar, 'icon_url': icon_url}

    def rank(self):
        summoner = self.start()
        summoner_id = summoner['id']
        url = f'https://la1.api.riotgames.com/lol/league/v4/entries/by-summoner/{summoner_id}'
        response = requests.get(url, headers=self.headers)
        return response.json()[1]

    def rank2(self):
        summoner = self.start()
        summoner_id = summoner['id']
        url = f'https://la1.api.riotgames.com/lol/league/v4/entries/by-summoner/{summoner_id}'
        response = requests.get(url, headers=self.headers)
        return response.json()[1]



    