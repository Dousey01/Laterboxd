from functions import *
def main():
    chrome = setup_webdriver()
    login(chrome, LETTERBOXD_USERNAME, LETTERBOXD_PWD)

    user_id = input('Enter the user name: ')
    my_watchlist = get_user_watchlist(chrome, LETTERBOXD_USERNAME)  # Fetching the watchlist of the logged-in user
    user_watchlist = get_user_watchlist(chrome, user_id)  # Fetching the watchlist for the specified user

    common_elements = set(my_watchlist).intersection(set(user_watchlist))

    if common_elements:
        print(f"\nCommon films between '{LETTERBOXD_USERNAME}' and '{user_id}':\n")
        for film in common_elements:
            print(film)
    else:
        print("\nThere are no common films between the two users, or the user ID is wrong.\n")
        
    chrome.quit()


if __name__ == "__main__":
    main()