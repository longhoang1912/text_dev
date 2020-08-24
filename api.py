import requests


def get_data():
    url = 'https://588814da8fb1b16ef5aa03b087de4858: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@longhoang1123.myshopify.com/admin/api/2020-07/customers.json'
    r = requests.get(url)
    return r.json()
