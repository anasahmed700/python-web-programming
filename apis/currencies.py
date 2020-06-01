import requests
import json


def main():
    base = "USD"
    other = input("Enter the currency to find rates: ").upper()

    # res = requests.get('https://currencyapi.net/api/v1/rates?key=aMI7hhcCOIdKsY8Ml8M51etOrAh285WQkGaI')
    res = requests.get('https://currencyapi.net/api/v1/rates?key=aMI7hhcCOIdKsY8Ml8M51etOrAh285WQkGaI',
                       params={"base": base, "other": other})

    if res.status_code != 200:
        raise Exception("ERROR: API request unsuccessful!")
    data = res.json()
    rates_all = data["rates"]
    rate_one = data["rates"][other]

    for curr, rate in rates_all.items():
        print(f"1 USD is equal to {rate} {curr}")

    print(f"\n1 {base} is equal to {rate_one} {other}")



if __name__ == "__main__":
    main()
