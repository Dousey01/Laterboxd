from letterboxd import get_lettrboxd_lists

if __name__ == '__main__':

    user_id = input('Enter the user name: ')

    my_watchlist, user_watchlist = get_lettrboxd_lists(user_id)

    common_elements = set(my_watchlist).intersection(user_watchlist)

    for film in common_elements:
        print(film)