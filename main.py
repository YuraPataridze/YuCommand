import webbrowser

search = input('Input what you want to search on YouTube.com: ')

webbrowser.open(f'https://www.youtube.com/results?search_query={search}')