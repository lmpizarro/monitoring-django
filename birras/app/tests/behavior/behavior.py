import requests
import json
from datetime import datetime, date, timedelta
import pytz
import utils

be_url = "http://localhost:8080/{}"
header = {'Content-type': 'application/json'}


def set_header(authorization):
    header['Authorization'] = f'Bearer {authorization}'


# curl http://127.0.0.1:8080/api/token/ -d "username=admin&password=admin"
def login(user='admin', password='admin'):
 
    url = be_url.format('api/token/')

    payload = {'username': user, 'password': password}
    headers = {}

    response = requests.post(url, headers=headers, data=payload)
    tokens = response.json()
    set_header(tokens['access'])
    
    return tokens


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


def create_meeter(email='algun_meeter@gmail.com', name='algun meeter'):
    url_create_meeter = be_url.format("api/create_meeter/")
    data = {'email': email, 'name': name}
    response_create = requests.request('POST', url_create_meeter, data=json.dumps(data), headers=header)

    return response_create.json()


def confirm_create_meeter(email):
    endpoint = f"api/confirm_create_meeter/{email}/"
    url_confirm_create = utils.be_url.format(endpoint)
    response = requests.request('GET', url_confirm_create, headers=header)

    return response.json()


def delete_meeter(email='pepe_alcorta@pepe.com'):
    url_delete_meeter = be_url.format("api/delete_meeter/")
    data = {'email': email}
    response_create = requests.request('POST', url_delete_meeter, data=json.dumps(data), headers=header)

    return response_create.json()


def confirm_delete_meeter(email):
    endpoint = f"api/confirm_delete_meeter/{email}/"
    url_confirm_delete = utils.be_url.format(endpoint)
    response = requests.request('GET', url_confirm_delete, headers=header)

    return response.json()


def create_delete_meeter_sequence():
    # create-delete meeter through email confirmation
    utils.print_out(create_meeter(email='pepe_alcorta@pepe.com', name='pepe alcorta'), 'create_meeter')

    utils.print_out(confirm_create_meeter(email='pepe_alcorta@pepe.com'), 'confirm_create_meeter')

    utils.print_out(delete_meeter(email='pepe_alcorta@pepe.com'), 'delete_meeter')
    utils.print_out(confirm_delete_meeter(email='pepe_alcorta@pepe.com'), 'confirm_delete_meeter')


def main():
    utils.print_out(login(), 'LOGIN')

    utils.print_out(getMeetUps(), 'GETMEETUPS')
    
    utils.print_out(getMeetUpDetails(6), 'getMeetUpDetails')
    
    utils.print_out(getMeetUpsToday(), 'getMeetUpsToday')

    # print_out(create_meetup(), 'create_meetup')    

    utils.print_out(subscribe_meetup(), 'subscribe_meetup')

    utils.print_out(unsubscribe_meetup(), 'unsubscribe_meetup')
    
    utils.print_out(delete_meetup(), 'delete_meetup')

    utils.print_out(checkin(), 'checkin')



if __name__ == '__main__':
    # main()
    # utils.print_out(checkin(), 'checkin')

    create_delete_meeter_sequence()


