#!/usr/bin/python3

import requests
import json



def main() -> None:
    response = requests.get('https://api.osrsbox.com/items')
    json_payload = response.json()
    print(json_payload)
    
    


if __name__=="__main__":
    main()





