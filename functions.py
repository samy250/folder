import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import date
import csv
import os


def extract_exchange_rate(url):
    try:
        response = requests.get(url)
        return response.text
    except Exception as e:
        raise RuntimeError(f"extract_axchange_rate: An error occured {e}")

def transform_exchange_rate(html):
    try:
        soup = BeautifulSoup(html, "html.parser")
        container = soup.find("div", id="container")
        documents = container.findAll("div", class_="document")
        current_date = date.today().strftime("%d-%m-%Y")
        rates = [{"code": "Date", "valeur": current_date}]
        for document in documents[1:]:
            code_valeur = document.find("span", class_="code_valeur").get_text()[:3]
            valeur = document.find("div", id="middle").get_text()
            valeur = float(valeur)
            rates.append({"code": code_valeur, "valeur": valeur})
        return rates
    except Exception as e:
        raise RuntimeError(f"transform_exchange_rate: An error occured {e}")
    

def loading_exchange_rate(rates):
    try:
        rates_folder = "rates"
        if not os.path.exists(rates_folder):
            os.makedirs(rates_folder)
        
        current_date = date.today().strftime("%d_%m_%Y")
        filename= f"{rates_folder}/rate_{current_date}.csv"
        df = pd.DataFrame(rates)
        df.to_csv(filename, index=False, header=False)
        
        
        print("Exchange rates saved successfuly!!")
    except Exception as e:
        raise RuntimeError(f"loading_exchange_rate: An error occured {e}")