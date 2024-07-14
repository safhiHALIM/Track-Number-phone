# Ensure all necessary libraries are installed
# pip install phonenumbers folium opencage

import phonenumbers
from phonenumbers import geocoder, carrier
import folium
from opencage.geocoder import OpenCageGeocode
from pyfiglet import figlet_format 


def get_phone_details(phone_number, api_key):
    try:
        # Parse the phone number
        parsed_number = phonenumbers.parse(phone_number)

        # Get the location of the phone number
        #number_location = geocoder.description_for_number(parsed_number, 'en')
        number_location = "Africa Morocco"
        print("___________________________")
        print("Location:", number_location)

        # Get the carrier of the phone number
        #service_provider = carrier.name_for_number(parsed_number, 'en')
        #print("Carrier:", service_provider)

        service_provider = parsed_number
        print("___________________________")
        print("Carrier:", carrier.name_for_number(service_provider, 'en'))

        # Geocode the location using OpenCageGeocode
        geocoder_service = OpenCageGeocode(api_key)
        results = geocoder_service.geocode(number_location)

        if results:
            lat = results[0]['geometry']['lat']
            lng = results[0]['geometry']['lng']
            print("___________________________")
            print("Latitude:", lat, "Longitude:", lng)

            # Create a map using folium
            map_location = folium.Map(location=[lat, lng], zoom_start=9)
            folium.Marker([lat, lng], popup=number_location).add_to(map_location)
            map_location.save('location.html')
            print(" ____________________________")
            print("| Map saved as location.html |")
            print(" ____________________________")
        else:
            print("___________________________________")
            print("Geocoding failed. No results found.")
    except phonenumbers.NumberParseException as e:
        print("__________________________________________")
        print(f"Error parsing phone number: {e}")
    except Exception as e:
        print("___________________________")
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    print("===========================")
    print(figlet_format(" T.N.P", font = "standard" ))
    print("===========================")
    number = input('Enter number: ')
    api_key = 'b3fd8076d09e463e983bc84515ee1efe'  # OpenCageGeocode API key
    get_phone_details(number, api_key)
