# Phone Number Location and Carrier Information Script

This Python script allows you to obtain the geographical location and carrier information of a phone number. Additionally, it generates a map displaying the location of the phone number using the OpenCageGeocode API and Folium library.

## Prerequisites

Ensure you have Python installed. You can download it from [python.org](https://www.python.org/downloads/).

## Installation

Before running the script, you need to install the required libraries. Open your terminal or command prompt and run the following commands:

```bash
pip install phonenumbers folium opencage
```

## Usage

1. Clone this repository or download the script file.

2. Open a terminal or command prompt and navigate to the directory containing the script.

3. Run the script using the following command:

```bash
python TNP.py
```

4. When prompted, enter the phone number you want to query.

## Script Details

### Function: get_phone_details(phone_number, api_key)

- **Parameters:**
  - `phone_number`: The phone number to query (string).
  - `api_key`: Your OpenCageGeocode API key (string).

- **Functionality:**
  - Parses the phone number.
  - Retrieves the location and carrier information of the phone number.
  - Uses the OpenCageGeocode API to get the geographical coordinates of the location.
  - Generates a map using Folium and saves it as `location.html`.

### Example

```python
number = input('Enter number: ')
api_key = 'YOUR_OPENCAGEGEOCODE_API_KEY'  # Replace with your actual OpenCageGeocode API key
get_phone_details(number, api_key)
```

### Error Handling

The script includes error handling for:
- Phone number parsing errors.
- General exceptions during execution.

### Output

- **Console Output:** Displays the location, carrier, latitude, and longitude of the phone number.
- **HTML File:** Generates an HTML file (`location.html`) containing a map of the location.

## Notes

- Ensure you replace `'YOUR_OPENCAGEGEOCODE_API_KEY'` with your actual OpenCageGeocode API key.
- The script handles valid phone numbers only. Enter the phone number in international format (e.g., `+1234567890`).

## License

This project is licensed under the MIT License.
