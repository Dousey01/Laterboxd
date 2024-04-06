# Letterboxd Watchlist Comparator

## Overview
This script automates the process of comparing the watchlists of Letterboxd users to find common films. It utilizes Selenium for web automation to log in to Letterboxd, fetch watchlists, and identify overlaps. This tool is perfect for movie enthusiasts looking to quickly find common interests.

## Prerequisites
Before running this script, ensure you have the following installed:
- Python 3.6 or newer
- Selenium WebDriver
- ChromeDriver (or any driver compatible with your browser choice, configured in the script)
- A Letterboxd account

## Installation
1. Clone this repository or download the script to your local machine.
2. Install the required Python packages from the `requirements.txt` by running this command in the terminal:
```bash
pip3 install -r requirements.txt
```
3. Rename the `env.template` to `.env` and fill it with your Letterboxd credentials without quotaion marks.

## Usage

To run the script, navigate to the directory containing the script and execute the following command in the terminal:
```bash
python3 main.py
```
When prompted, enter the usernames of the Letterboxd users whose watchlist you want to compare with yours. **Don't forget to add your own username!** Otherwise your own watchlist will not be compared.

Example:

```bash
Enter a user name (or press Enter to proceed): YOUR_USERNAME
Enter a user name (or press Enter to proceed): USERNAME1
Enter a user name (or press Enter to proceed): USERNAME2
```

## Features
- Automatically logs into Letterboxd using your account credentials.
- Compares your watchlist with another user's watchlist to find common films.
- Prints the list of common films, or a message if no common films are found or if there's an issue with the user IDs.

## Notes
- This script is intended for educational purposes and personal projects.
- Ensure you have permission to access another user's watchlist if it is not publicly available.
- The execution time may vary depending on the size of the watchlists and your internet connection speed.

## License
MIT License

## Disclaimer
This project is not affiliated with, sponsored by, or endorsed by Letterboxd or any related entities.