# Proxy Scraper

A Python script that scrapes Socks5 proxies from https://proxygenerator.azura.best/ and saves them to a file.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine.

### Prerequisites

- Python 3
- grequests library

### Installing

1. Clone the repository to your local machine
```
git clone https://github.com/DAMcraft/proxymilker.git
```
2. Change into the project directory
```
cd proxymilker
```
3. Install the required libraries
```
pip install grequests
```
4. Run the script
```
python3 proxymilker.py
```


## Functionality

- The script will scrape Socks5 proxies from https://proxygenerator.azura.best/
- It will write the proxies to a file named `proxies.txt`
- The script will run indefinitely and keep updating the file with new proxies
- If the site is out of stock, the script will wait for a minute and check again

## Contributing

1. Fork the project
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.


