import requests
import time
import json

be_url = "http://localhost:8080/{}"
header = {'Content-type': 'application/json'}


def set_header(authorization):
    header['Authorization'] = f'Bearer {authorization}'


# curl http://127.0.0.1:8080/api/token/ -d "username=admin&password=admin"
def login(user='admin', password='admin'):
 
    url = be_url.format('api/token/')

    payload = {'username': user, 'password': password}
    headers= {}

    response = requests.post(url, headers=headers, data = payload)
    tokens = response.json()
    set_header(tokens['access'])
    
    return tokens

def hello():
    url_hello = be_url.format("api/hello/")

    response = requests.get(url_hello, headers=header)

    return response.json()

def temperature():
    url_temp = be_url.format("api/temperature/")

    response = requests.get(url_temp, headers=header)
    
    return response.json()


def bottlesByPerson():
    url_bott = be_url.format("api/bottlesByPerson/")

    response = requests.get(url_bott, headers=header)
    
    return(response.json())

def getMeetUps():
    url_meetup = be_url.format("api/getMeetUps/")

    response = requests.get(url_meetup, headers=header)
    
    return response.json()
    
    
def getMeetUpDetails(meetup_id):
    url_meetup_detail = be_url.format("api/get_meetup_details/{}/").format(meetup_id)
    
    response = requests.get(url_meetup_detail, headers=header)
    
    return response.json()

def getMeetUpsToday():
    url_meetup_today = be_url.format("api/get_meetups_today/")
  
    response = requests.get(url_meetup_today, headers=header)
    
    return response.json()


def print_out(out_, mess):
    print(f'{mess}\n{out_}\n')    
    
def main():
    print_out(login(), 'LOGIN')
    
    print_out(hello(), 'HELLO')
        
    print_out(temperature(), 'TEMPERATURA')
            
    print_out(bottlesByPerson(), 'bottles')
    
    print_out(getMeetUps(), 'GETMEETUPS')
    
    print_out(getMeetUpDetails(6), 'getMeetUpDetails')
    
    print_out(getMeetUpsToday(), 'getMeetUpsToday')
    
if __name__ == '__main__':
    main()
