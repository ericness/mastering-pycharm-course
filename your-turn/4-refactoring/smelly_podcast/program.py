from service import episode_data, get_episode, get_latest_show_id, download_data


def main():
    print_header()

    download_data()

    # GET LATEST SHOW ID
    latest_show_id = get_latest_show_id()
    oldest_show_id = min(episode_data.keys())

    print("Working with total of {} episodes".format(latest_show_id))

    display_results(latest_show_id, oldest_show_id)


def display_results(latest_show_id, oldest_show_id):
    # DISPLAY RESULTS
    start = oldest_show_id
    end = latest_show_id + 1
    for show_id in range(start, end):
        # GET EPISODE
        info = get_episode(show_id)
        print("{}. {}".format(info.show_id, info.title))


def print_header():
    # SHOW THE HEADER
    print("Welcome to the talk python info downloader.")
    print()


if __name__ == '__main__':
    main()
