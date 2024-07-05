# Description
This Python script interacts with the VK API to either shorten URLs using VK's link shortening service or retrieve click statistics from a shortened VK link.

## Requirements
- Python 3.x
- `requests` library (`pip install requests`)
- `python-dotenv` library (`pip install python-dotenv`)

## Usage
1. Ensure you have Python installed along with the required libraries (`requests` and `python-dotenv`).
2. Obtain a VK API access token and store it in a `.env` file in the script's directory with the variable name `TOKEN`.

   Example `.env` file: TOKEN=your_vk_api_token_here

3. Run the script by executing `python script_name.py` in your terminal.
4. Follow the prompts to either shorten a URL or retrieve click statistics for a VK short link.

## Example
Assume you want to shorten a URL using VK's API:

```bash
$ python script_name.py
Введите ссылку: https://example.com/your-long-url
Сокращенная ссылка: https://vk.cc/abc123
```
##### Or, if you want to get click statistics for an existing VK short link:
```
$ python script_name.py
Введите ссылку: https://vk.cc/abc123
Количество просмотров: 1234
```
## Notes
* This script assumes you have a valid VK API access token.

* It distinguishes between input URLs to either shorten them or fetch statistics based on whether they are VK short links (vk.cc).

* Error handling is provided for failed API requests or invalid URLs.
  
