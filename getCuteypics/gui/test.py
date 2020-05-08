def spit_link(entry_link, i):
    pre_link = entry_link.split('-1', 1)[0]
    link = pre_link + f'-{i}.html'
    return link

for i in range(10):
    link=spit_link('https://www.xinwenba.net/plus/view-573875-1.html',i+1)
    print(link)

