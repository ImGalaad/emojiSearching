import requests


def search_emoji(search):
    # Connection with the API
    print(
        "\x1B[1m"
        + "[\x1B[34mⓘ \x1B[37m]\x1B[0m Try to connect with \x1B[4mapi.emojisworld\x1B[0m"
    )
    response = requests.request(
        "GET", ("https://api.emojisworld.fr/v1/search?q=" + search)
    )

    # 404
    if response.status_code == 404:
        print(
            "\x1B[1m"
            + "[\x1B[31m✗\x1B[37m]\x1B[0m Unable to reach \x1B[4mapi.emojisworld\x1B[0m"
        )

    # 202
    elif response.status_code == 200:
        print(
            "\x1B[1m"
            + "[\x1B[32m✓\x1B[37m]\x1B[0m Connection established with \x1B[4mapi.emojisworld\x1B[0m"
        )
        data = response.json()
        if data["totals"] != 0:
            for i in range(len(data["results"])):
                if len(data["results"][i]["emoji"]) == 1:
                    print(data["results"][i]["emoji"], end=" ")
    
    # Other error
    else:
        print(
            "\x1B[1m"
            + "[\x1B[31m✗\x1B[37m]\x1B[0m Unable to connect API or retrieve data"
        )
    print()


search_emoji(input("\x1B[1mSearch a emoji :\x1B[0m "))
