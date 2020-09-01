import requests
be_url = "http://localhost:8080/{}"
header = {'Content-type': 'application/json'}

def print_out(out_, mess):
    print(f'{mess}\n{out_}\n')

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