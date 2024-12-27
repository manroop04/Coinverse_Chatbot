

# Currency Converter Chatbot

This project is a Flask-based chatbot integrated with Dialogflow and Telegram to perform currency conversion. It uses the Exchange Rate API for real-time currency exchange rates and is deployed on Render for hosting.

---

## Features
- Converts an amount from one currency to another using real-time exchange rates.
- Integrated with Dialogflow for NLP capabilities.
- Connected to Telegram to provide a conversational interface.
- Deployed on Render for easy access.

---

## Prerequisites

1. **Python 3.7+**
2. **Flask Framework**
3. **Dialogflow Agent**
4. **Exchange Rate API Key**
5. **Render Account**
6. **Telegram Bot Token**

---

## Setup Instructions

### 1. Clone the Repository
```
git clone <repository_url>
cd <repository_folder>
```

### 2. Install Required Dependencies
```
pip install -r requirements.txt
```

### 3. Configure API Keys
Replace the placeholder API key in `fetch_conversion_factor` with your Exchange Rate API key:
```python
api_key = "YOUR_EXCHANGE_RATE_API_KEY"
```

### 4. Dialogflow Setup
1. Create a new Dialogflow agent.
2. Define an intent to extract:
   - `unit-currency.currency`
   - `unit-currency.amount`
   - `currency-name`
3. Configure webhook to point to your Render app URL.

### 5. Telegram Setup
1. Create a Telegram bot using the BotFather.
2. Link your Telegram bot to Dialogflow via a webhook.

### 6. Run the Application Locally
```
python app.py
```

---

## Deployment

### Deploy on Render
1. Create a new web service in your Render account.
2. Connect your Git repository.
3. Add the following environment variables:
   - `EXCHANGE_RATE_API_KEY`
   - Other required keys (e.g., Telegram bot token).
4. Deploy and retrieve the Render app URL for Dialogflow webhook.

---

## API Details

- **Exchange Rate API**: Provides real-time currency conversion rates.
- Endpoint Example:
```
https://v6.exchangerate-api.com/v6/<API_KEY>/pair/USD/EUR
```

---

## Code Overview

### Main Endpoints
- `/`: Handles POST requests from Dialogflow, processes the input, and responds with the converted amount.

### Core Functionality
- **`fetch_conversion_factor(source, target)`**: Fetches the conversion rate between two currencies using the Exchange Rate API.

---

## Example Input and Output

### Input (from Dialogflow):
```json
{
  "queryResult": {
    "parameters": {
      "unit-currency": {
        "currency": "USD",
        "amount": 100
      },
      "currency-name": "EUR"
    }
  }
}
```

### Output (Response):
```json
{
  "fulfillmentText": "100 USD is 92 EUR"
}
```

---

## Possible Errors

1. **Invalid API Key**:
   - Ensure your API key is correct and valid.

2. **Missing Dialogflow Parameters**:
   - Ensure the intent captures all required parameters (`unit-currency` and `currency-name`).

3. **Conversion Factor Not Found**:
   - Check the API response structure and ensure the `conversion_rate` field exists.

4. **Deployment Issues**:
   - Verify the webhook URL and environment variable configurations.

---

## License
This project is licensed under the MIT License.

---

## Acknowledgments
- **Exchange Rate API**: For providing real-time currency data.
- **Dialogflow**: For NLP capabilities.
- **Telegram**: For creating an interactive chatbot interface.

