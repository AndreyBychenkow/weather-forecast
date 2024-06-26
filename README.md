# Description

The script prompts the user to input city names separated by spaces. For each city, it retrieves the weather information and prints it out in the console.

## Requirements

- Python 3.x
- `requests` library

You can install the `requests` library using pip:
```sh
pip install requests
```

## Usage

1. Clone the repository or download the script file.
2. Open a terminal and navigate to the directory containing the script.
3. Run the script using Python:
```sh
python script_name.py
```
Replace script_name.py with the actual name of your script file.

4. When prompted, enter the city names separated by spaces and press Enter. For example:
```sh
Enter the cities separated by a space: London Sheremetyevo Cherepovets
```
5. The script will fetch and display the weather information for each city.

## Example

```csharp
Enter the cities separated by a space: London Sheremetyevo Cherepovets
London:
[Weather data for London]

Sheremetyevo:
[Weather data for Sheremetyevo]

Cherepovets:
[Weather data for Cherepovets]
```

### Notes

* The script uses the wttr.in service to fetch weather information. 
Make sure you have an active internet connection while running the script.

* The script is designed to handle basic errors such as invalid city names by raising an HTTP error.

