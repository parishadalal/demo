import requests
import sys

url = "http://services.groupkt.com/state/get/USA/all"

get_response = requests.get(url).json()
print(get_response)
Response = get_response["RestResponse"]["result"]


def demo():
    state = input("Please provide input: ")

    for i in Response:
        try:
            if str(state).upper() == "N" or str(state).upper()== "Q":
                print("Quiting")
                sys.exit(0)
            elif i["name"] == str(state[0].upper() + state[1:].lower()) or i["abbr"] == str(state.upper()):
                print ("largest city is: " + i["largest_city"] + " " + "capital city: " + i["capital"])
                demo()
        except IndexError:
            print("Invalid input, provide legal input")
            demo()
    
    print("Invalid input, provide legal input")
    demo()

demo()