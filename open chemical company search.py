import webbrowser, pyperclip, time

cas = str(input("Enter CAS number please:"))
pyperclip.copy(cas)

websites = {
	"sigma-aldrich": f"https://www.sigmaaldrich.com/DE/de/search/102-25-0?focus=products&page=1&perpage=30&sort=relevance&term={cas}&type=product",
	"abcr": f"https://abcr.com/de_en/catalogsearch/advanced/result/?cas={cas}",
	"tcigermany": f"https://www.tcichemicals.com/DE/en/search/?text={cas}",
	"chempur": f"https://chempur.de/en/product-search/",
	"carbolution": f"https://www.carbolution.de/search?search={cas}",
	"bldpharm": f"https://www.bldpharm.com/search/Search.html?keyword={cas}"
}
#print(type(websites))
#print(websites)

for x in websites.values():
	webbrowser.open_new_tab(x)
	time.sleep(0.1)

#input("exit...")