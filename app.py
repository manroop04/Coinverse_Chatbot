from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/', methods=['POST'])
def index():
    data = request.get_json()
    source_currency = data['queryResult']['parameters']['unit-currency']['currency']
    amount = float(data['queryResult']['parameters']['unit-currency']['amount'])
    target_currency = data['queryResult']['parameters']['currency-name']

    cf = fetch_conversion_factor(source_currency, target_currency)
    if cf is None:
        response = {
            'fulfillmentText': "Unable to fetch conversion rate. Please try again later."
        }
        return jsonify(response)

    print("Conversion Factor:", cf)

    final_amount = amount * cf
    final_amount = round(final_amount, 2)  

    response = {
        'fulfillmentText': "{} {} is {} {}".format(amount, source_currency, final_amount, target_currency)
    }
    return jsonify(response)

def fetch_conversion_factor(source, target):
    api_key = "03f3dd7b7583ffc718a8d11e"
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/pair/{source}/{target}"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        if "conversion_rate" in data:
            return data["conversion_rate"]
        else:
            print("Error: conversion_rate not found in API response.")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error fetching conversion factor: {e}")
        return None

if __name__ == "__main__":
    app.run(debug=True)
