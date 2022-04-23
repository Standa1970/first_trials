from urllib.request import urlopen

url = "https://www.toprecepty.cz/recept/8800-holandske-rizky/"

def iteruj(i, end_chr):
    ingr_lst = []
    while html[i] != chr(end_chr):
        if html[i] == chr(34):
            i += 1
            ingr = ""
            while html[i] != chr(34):
                if ord(html[i]) not in ignore:
                    ingr += html[i]
                i += 1
            ingr_lst.append(ingr)
        i += 1
    ingr_lst.append(i)
    return ingr_lst

def open_(url):
    page = urlopen(url)
    html_bytes = page.read()
    html = html_bytes.decode("unicode-escape")
    return html

units = ["g", "hrnek", "lžíce", "ks"]
html = open_(url)
start_txt="recipeIngredient"
start_index = html.find(start_txt)
i = start_index + 18
ignore = [34, 39, 91, 93, 10]

suroviny = iteruj(i,93)

i = suroviny[-1]
suroviny.pop()
i += 35

postup = iteruj(i,93)
postup.pop()

print(suroviny)
print(postup)