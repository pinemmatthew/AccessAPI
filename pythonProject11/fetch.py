import requests
import pandas as pd
from token import generate_token
from config import base_url

def fetch_records():
    """""Fetch all pages of API results. """"
    headers = {"Authorization": f"Bearer {generate_token()}"}
    r = requests.get(base_url + 'users' , headers=headers)
    next_page = r.json()['pagination']['next_link']
    records_df = pd.DataFrame(columns=r.json()['data'][0].keys())
    if next_page:
        get_nextpage(next_page)