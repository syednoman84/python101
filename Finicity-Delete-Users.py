import requests

if __name__ == '__main__':
    search_url = 'https://api.finicity.com/aggregation/v1/customers'
    headers = {
        'Finicity-App-Key': 'XXX',
        'Finicity-App-Token': 'XXX',
        'Accept': 'application/json'
    }
    payload = {'start': 1, 'limit': 25}
    while True:
        r = requests.get(search_url, headers=headers)
        customers = r.json().get('customers')
        print(len(customers))
        if len(customers) > 0:
            for c in customers:
                r1 = requests.delete(f'https://api.finicity.com/aggregation/v1/customers/{c.get("id")}',
                                     headers=headers)
                if r1.status_code != 204:
                    print(r1.status_code)
                    break
        else:
            break