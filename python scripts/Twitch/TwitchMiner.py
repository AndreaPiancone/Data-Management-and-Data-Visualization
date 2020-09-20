import requests
import json
import datetime

def get_top_games(url, headers):
    now = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
    game_list = [] #creo una lista vuota
    game_list.append({'timestamp':now})
    res = requests.get(url, headers = headers) #eseguo una richiesta all'API di Twitch
    game_list.extend(res.json()['top'])
    return(game_list)

def del_not_games(game_list): 
    d = {} #dizionario vuoto
    d['game'] = game_list[1:100]
    new_data = []
    new_data.append(game_list[0])
    for item in d['game']:
        if item['game']['giantbomb_id'] != 0:
            new_data.append(item)
    return(new_data)

def add_ranking(game_list):
    n = len(game_list)
    ranking = 1
    for item in game_list[1:n]:
        item['game']['ranking'] = ranking
        ranking = ranking + 1
    return(game_list)

def flatten_json(game_list):
    lista = [] #creo una lista 
    timestamp = list(game_list[0].values())[0] #estraggo il timestamp
    del game_list[0] #elimino il campo timestamp
    for i in range(0, len(game_list)):
        dati = {} #creo un dizionario vuoto dove poi inserire i vari campi del json
        dati['timestamp'] = timestamp
        dati['name'] = game_list[i]['game']['name']
        dati['giantbomb_id'] = game_list[i]['game']['giantbomb_id']
        dati['box_large'] = game_list[i]['game']['box']['large']
        dati['box_large'] = game_list[i]['game']['box']['large']
        dati['box_medium'] = game_list[i]['game']['box']['medium']
        dati['box_medium'] = game_list[i]['game']['box']['medium']
        dati['box_small'] = game_list[i]['game']['box']['small']
        dati['box_template'] = game_list[i]['game']['box']['template']
        dati['logo_large'] = game_list[i]['game']['logo']['large']
        dati['logo_medium'] = game_list[i]['game']['logo']['medium']
        dati['logo_small'] = game_list[i]['game']['logo']['small']
        dati['logo_template'] = game_list[i]['game']['logo']['template']
        dati['localized_name'] = game_list[i]['game']['localized_name']
        dati['locale'] = game_list[i]['game']['locale']
        dati['ranking'] = game_list[i]['game']['ranking']
        dati['viewers'] = game_list[i]['viewers']
        dati['channels'] = game_list[i]['channels']
        lista.append(dati) #aggiungo dentro la lista un gioco e tutti i suoi attributi.
    return(lista)
