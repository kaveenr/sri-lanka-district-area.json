from bs4 import BeautifulSoup
import json

html = open("ikman.html","r").read()

data = dict();

soup = BeautifulSoup(html, 'html.parser')
scrape_div = soup.find(class_="scrape_div").find(class_="ui-sl-group is-level-1 has-sep has-sub").find("ul").children;

for i in scrape_div:
    print("---------")
    top_section = i.find("a").get_text()
    print(top_section)
    data[top_section] = dict()
    data[top_section]["popular"] = []
    data[top_section]["options"] = []
    for pop in i.find_all("li"):
        pop_section = pop.get_text()
        print("-POP-> "+ pop_section)
        data[top_section]["popular"].append(pop_section)

    for opt in i.find_all("option"):
        if opt['value']:
            opt_section = opt.get_text()
            print("-OPT-> "+ opt_section)
            data[top_section]["options"].append(opt_section)

out = open("locs.json","w");

out.write(json.dumps(data,indent=4))
