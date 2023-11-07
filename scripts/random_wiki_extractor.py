import wikipedia

wikipedia.set_lang("ja")

rand = wikipedia.random()
try:
    random_page = wikipedia.page(title=rand)

    print(f"Title: {random_page.title}")
    print(f"URL: {random_page.url}")

except wikipedia.exceptions.DisambiguationError:
    print("DisambiguationError!!")
