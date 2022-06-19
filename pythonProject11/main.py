import requests
import pandas as pd
from token import generate_token
from config import base_url


def create_dataframe_from_api():
    headers = {"Authorization":"Bearer" + token}
    r = requests.get(base_url + 'useres' , headers=headers)
    dataframe = pd.DataFrame(columns=r.json()['data'][0].keys())
    return dataframe

records_df = create_dataframe_from_api()
