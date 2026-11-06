import time
import webbrowser

import pyperclip

cas = str(input("Enter CAS number please: "))
pyperclip.copy(cas)

websites = {
    "sigma-aldrich": f"https://www.sigmaaldrich.com/DE/de/search/{cas}?&term={cas}&type=cas_number",
    "abcr": f"https://abcr.com/de_en/catalogsearch/advanced/result/?cas={cas}",
    "tcigermany": f"https://www.tcichemicals.com/DE/en/search/?text={cas}",
    "chempur": "https://chempur.de/en/product-search/",
    "carbolution": f"https://www.carbolution.de/search?search={cas}",
    "bldpharm": f"https://www.bldpharm.com/search/Search.html?keyword={cas}",
}

for x in websites.values():
    webbrowser.open_new_tab(x)
    time.sleep(0.1)
