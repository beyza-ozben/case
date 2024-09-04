with open('phishing.txt', 'r') as file:
    urls = file.readlines()

etiketli_veriler = [f"{url.strip()} ,phishing\n" for url in urls]

with open('etiketli_dataset.txt', 'w') as file:
    file.writelines(etiketli_veriler)
