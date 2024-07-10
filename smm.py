import requests

class Api:
    def __init__(self, api_key):
        self.api_url = 'https://smm_panel_domain/api/v2'
        self.api_key = api_key

    def order(self, data):
        data.update({'key': self.api_key, 'action': 'add'})
        response = requests.post(self.api_url, data=data)
        return response.json()

    def status(self, order_id):
        data = {
            'key': self.api_key,
            'action': 'status',
            'order': order_id
        }
        response = requests.post(self.api_url, data=data)
        return response.json()

    def multiStatus(self, order_ids):
        data = {
            'key': self.api_key,
            'action': 'status',
            'orders': ','.join(map(str, order_ids))
        }
        response = requests.post(self.api_url, data=data)
        return response.json()

    def services(self):
        data = {
            'key': self.api_key,
            'action': 'services'
        }
        response = requests.post(self.api_url, data=data)
        return response.json()

    def refill(self, order_id):
        data = {
            'key': self.api_key,
            'action': 'refill',
            'order': order_id
        }
        response = requests.post(self.api_url, data=data)
        return response.json()

    def multiRefill(self, order_ids):
        data = {
            'key': self.api_key,
            'action': 'refill',
            'orders': ','.join(map(str, order_ids))
        }
        response = requests.post(self.api_url, data=data)
        return response.json()

    def refillStatus(self, refill_id):
        data = {
            'key': self.api_key,
            'action': 'refill_status',
            'refill': refill_id
        }
        response = requests.post(self.api_url, data=data)
        return response.json()

    def multiRefillStatus(self, refill_ids):
        data = {
            'key': self.api_key,
            'action': 'refill_status',
            'refills': ','.join(map(str, refill_ids))
        }
        response = requests.post(self.api_url, data=data)
        return response.json()

    def cancel(self, order_ids):
        data = {
            'key': self.api_key,
            'action': 'cancel',
            'orders': ','.join(map(str, order_ids))
        }
        response = requests.post(self.api_url, data=data)
        return response.json()

    def balance(self):
        data = {
            'key': self.api_key,
            'action': 'balance'
        }
        response = requests.post(self.api_url, data=data)
        return response.json()