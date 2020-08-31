import requests
import json
from datetime import datetime, date, timedelta
import pytz

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


def create_meetup():
    today = datetime.combine(date.today(), datetime.min.time()).replace(tzinfo=pytz.UTC)
    delta = timedelta(days=60, hours=18)
    meetupday = today + delta
    
    url_create_meetup = be_url.format("api/Meetup/")
    data = {'name': 'python meetup about django3', 
            'meet_date': str(meetupday),
            'place': 'just the office behind us',
            'description': 'we will discuss the improvements to django admin'}
            
    response_create = requests.request('POST', url_create_meetup, data=json.dumps(data), headers=header)
    
    return response_create.json()


def create_meeter():    
    url_create_meeter = be_url.format("api/create_meeter/")
    data = {'email': 'algun_meeter@gmail.com', 'name': 'algun meeter'}
    response_create = requests.request('POST', url_create_meeter, data=json.dumps(data), headers=header)
    
    return response_create.json()

  
def subscribe_meetup():
    url_subscribe = be_url.format("api/subscribe_meetup/")
    data = {'email': 'algun_meeter@gmail.com', 'meetup_id': 8}
    response_create = requests.request('POST', url_subscribe, data=json.dumps(data), headers=header)
    
    return response_create.json()


def unsubscribe_meetup():
    url_unsubscribe = be_url.format("api/unsubscribe_meetup/")
    data = {'email': 'algun_meeter@gmail.com', 'meetup_id': 8}
    response_create = requests.request('POST', url_unsubscribe, data=json.dumps(data), headers=header)
    
    return response_create.json()


def delete_meetup():
    pk = 8
    endpoint = f'api/Meetup/{pk}/'
    
    url_delete_meetup = be_url.format(endpoint)
    print(url_delete_meetup)

    response_delete = requests.delete(url_delete_meetup,  headers=header)
    return response_delete.json()


def checkin():
    url_checkin = be_url.format("api/checkin/")
    data = {'email': 'rosa15@alba.com', 'meetup_id': 8}
    response_create = requests.request('POST', url_checkin, data=json.dumps(data), headers=header)

    return response_create.json()


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

    # print_out(create_meetup(), 'create_meetup')    
    
    # print_out(create_meeter(), 'create_meeter')
    
    print_out(subscribe_meetup(), 'subscribe_meetup')    

    print_out(unsubscribe_meetup(), 'unsubscribe_meetup')    
    
    print_out(delete_meetup(), 'delete_meetup')

    print_out(checkin(), 'checkin')
    
if __name__ == '__main__':
    # main()
    print_out(checkin(), 'checkin')

