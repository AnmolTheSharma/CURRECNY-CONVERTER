import requests

# Function to fetch exchange rates from the API
def get_exchange_rates(base_currency):
    url = f"https://currencyapi.net/api/v1/rates?key=AHBxrqtofzq2N2AtIt2taCuEYdRIpI0gJqz8&base={base_currency}&output=JSON"
    response = requests.get(url)
    data = response.json()
    return data

# Function to perform currency conversion
def convert_currency(amount, from_currency, to_currency, exchange_rates):
    if from_currency == to_currency:
        return amount
    else:
        if from_currency in exchange_rates["rates"] and to_currency in exchange_rates["rates"]:
            conversion_rate = exchange_rates["rates"][to_currency] / exchange_rates["rates"][from_currency]
            converted_amount = amount * conversion_rate
            return converted_amount
        else:
            return None


# Main function
def main():
    base_currency = input("Enter the base currency (e.g., USD, EUR, GBP): ").strip().upper()
    exchange_rates = get_exchange_rates(base_currency)
    
    if "rates" not in exchange_rates:
        print("Invalid base currency or API error.")
    else:
        amount = float(input("Enter the amount:" ))
        from_currency =input("Enter the source currency: ").strip().upper()
        to_currency = input("Enter the target currency: ").strip().upper()


        if convert_currency(amount, from_currency, to_currency, exchange_rates) is not None:
            converted_amount = convert_currency(amount, from_currency, to_currency, exchange_rates)
            print(f"{amount} {from_currency} is equal to {converted_amount} {to_currency}")
        else:
            print("Invalid currency codes. Please check your input.")



        

if __name__ == "__main__":
    main()
