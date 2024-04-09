from functions import *
from functools import reduce

def main():
    chrome = setup_webdriver()
    login(chrome, LETTERBOXD_USERNAME, LETTERBOXD_PWD)

    # Collect multiple usernames
    usernames = []
    while True:
        user_id = input('Enter a user name (or press Enter to proceed): ')
        if not user_id:
            break
        usernames.append(user_id)

    # Fetch watchlists for each user
    watchlists = []
    for user_id in usernames:
        watchlist = get_user_watchlist(chrome, user_id)
        watchlists.append(set(watchlist))

    # Find common movies across all watchlists
    common_movies = reduce(lambda x, y: x.intersection(y), watchlists) if watchlists else set()

    # Display results
    if common_movies:
        print("\nCommon films among the users:\n")
        for film in common_movies:
            print(film)
    else:
        print("\nNo common films found among the users.\n")
        
    chrome.quit()


if __name__ == "__main__":
    main()
