import requests
import sys

def main():
    if len(sys.argv) != 2:
        sys.exit("Too little arguments! Please input a Singapore postal code in the command-line.")
    else:
        postal_code = sys.argv[1]   
    try:
        if postal_check(postal_code):
            results = get_onemap_data(postal_code) 
        if type(results) == list:
            output_str = ""
            for name in results:
                output_str += name + " "          
            sys.exit(f'There seems to be more than 1 building! Please double check the postal code. The buildings here are: {output_str}')
        elif results == 'NIL':
            sys.exit("Client seems to be staying in a HDB!")
        else:
            sys.exit(f"Client seems to be staying at a condominium of name {results}")
                   
    # results is either STRING (nil, building name) or array:
    except ValueError as e:
        sys.exit(f"{e}") 
       

def get_onemap_data(postal_code):
    api_url = f"https://www.onemap.gov.sg/api/common/elastic/search?searchVal={postal_code}&returnGeom=N&getAddrDetails=Y"
    try:
        res = requests.get(api_url)
        res.raise_for_status()
        data = res.json()
        if data['found'] == 1:
            print((data["results"][0]['BUILDING']))
            return data["results"][0]['BUILDING'] # returning building name to main() - as a string directly
        else:
            multiple = multi(data)
            print(multiple) # list of strings
            return multiple
    except requests.exceptions.RequestException as err:
        print(f"An error occurred: {err}")

# Function to check for valid postal code
def postal_check(postal):
    if len(postal) != 6:
        raise ValueError("Length of postal code is incorrect! It should be exactly 6 digits.")
    if not postal.isdigit():
        raise ValueError("Postal code should contain only digits, with no letters, spaces, or special characters.")
    return True

#Function to do results processing - based on either 1 result or > 1 result

def multi(data):
    building_list = [] #initiate empty array
    for result in data['results']:
        if result['BUILDING'] not in building_list: # adding the building into the array but also with a duplicate check
            building_list.append(result['BUILDING'])
    return building_list

if __name__ == "__main__":
    main()

