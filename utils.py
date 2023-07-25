import requests


def get_last_price(ticker: str) -> float:


    yahoo_finance_url = f"https://query1.finance.yahoo.com/v8/finance/chart/{ticker}"
    headers= {'User-agent' : 'Mozilla/5.0'}
    r = requests.get(url=yahoo_finance_url, headers=headers)
    if r.json().get('result') is None:
        raise ValueError(f"ticker: '{ticker}' not found")


    price = r.json().get('chart').get('result')[0].get('meta').get('regularMarketPrice')
    return price

#if __name__ == "__main__":
    #print(get_last_price('DIS'))

