# Versão2 otimizada, menos código, menos uso de memória.
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.firefox.launch()
    page = browser.new_page()
    # Este range é setado manualmente, significa a quantidade de páginas/imagens que serão baixadas.
    # O processo é um pouco lento, então os downloads são feitos por partes.
    for c in range(133, 140+1):   # 1585pgs max(cada pg. dá acesso à 15 imagens)
        print(c)
        links = []
        try:
            page.goto('https://wallpaperscraft.com/catalog/nature/1920x1080' + f'/page{c}')
            mini15 = page.query_selector_all('.wallpapers__image')
            for cc in mini15:
                src = cc.get_attribute('src')
                src = src[:-11]+'1920x1080.jpg'
                links.append(src)

            for cc in links:
                try:
                    binarios = page.goto(cc).body()
                    nomeimage = cc[48:] # Cada imagem recebe um nome único, derivado de seu próprio link.
                    caminho = r'C:\Users\Daniel\Desktop\wallpaperscraft.com nature\\'
                    open(caminho + nomeimage, 'wb').write(binarios)
                except:
                    print(f'Erro ao abrir página!\n{cc[48:]}')

            print(f'Page {c} OK!')
        except:
            print(f'Erro ao abrir página {c}!')
    browser.close()
    print('FIM!')
