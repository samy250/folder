from functions import extract_exchange_rate, transform_exchange_rate, loading_exchange_rate

url = "https://www.beac.int/"

try: 
    html = extract_exchange_rate(url)
    rates = transform_exchange_rate(html)
    loading_exchange_rate(rates)
except Exception as e:
    print(e)