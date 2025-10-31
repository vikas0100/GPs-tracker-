import phonenumbers
from phonenumbers import carrier, geocoder

number = input("Enter the number :")# Example number
print(number)
parsed_number = phonenumbers.parse(number)
country = geocoder.description_for_number(parsed_number, "en")
state = geocoder.description_for_number(parsed_number,"en",region = "IN")
def get_state_from_prefix(number):
    # Remove country code if present
    if number.startswith('+91'):
        number = number[3:]
    if number.startswith('0'):
        number = number[1:]
    prefix = number[:5]  # First 5-digits (for India)
    
    # Example mapping; real table is much larger
    prefix_state_map = {
        "98100": "Delhi",
        "98200": "Maharashtra",
        "98300": "West Bengal",
        "98910": "Haryana",
        "98450": "Karnataka",
        "9354": "Haryana",
    
        # ... (add more prefixes as needed)
    }
    return prefix_state_map.get(prefix, "Unknown or Portable Number")

# number = "+919810012345"
state = get_state_from_prefix(number)
print(f"State: {state}")
service_provider = carrier.name_for_number(parsed_number, "en")

print(f"Country/Region: {country}")
print(f"State/Region: {state}")
print(f"Carrier: {service_provider}")
