import sys
import requests




def download_url_and_get_all_hrefs(url):
    """
    Funkce stahne url predanou v parametru url pomoci volani response = requests.get(),
    zkontroluje navratovy kod response.status_code, ktery musi byt 200,
    pokud ano, najdete ve stazenem obsahu stranky response.content vsechny vyskyty
    <a href="url">odkaz</a> a z nich nactete url, ktere vratite jako seznam pomoci return
    """
    hrefs = []
    response = requests.get(url)
    if response.status_code == 200:
        pos = 0
        while True:
            tag_start = response.text.find('<a', pos)
            if tag_start == -1:
                break

            tag_end = response.text.find('>', tag_start)
            href_start = response.text.find('href="', tag_start)
            if href_start == -1:
                break

            if tag_end != -1 and href_start > tag_end:
                pos = tag_end
                continue

            url_start = href_start + len('href="')
            url_end = response.text.find('"', url_start)
            if url_end == -1:
                break

            urls = response.text[url_start:url_end]
            hrefs.append(urls)
            pos = url_end

    return hrefs


if __name__ == "__main__":
    try:
        url = sys.argv[1]
        print (download_url_and_get_all_hrefs(url))
    # osetrete potencialni chyby pomoci vetve except
    except Exception as e:
        print(f"Program skoncil chybou: {e}")
