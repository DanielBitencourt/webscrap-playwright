from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.firefox.launch()
    page = browser.new_page()
    listalinks = []

    for c in range(101, 102+1):   # 1585pgs
        print(c)
        try:
            page.goto('https://wallpaperscraft.com/catalog/nature/1920x1080' + f'/page{c}')
            mini15 = page.query_selector_all('.wallpapers__image')

            for cc in mini15:
                try:
                    with page.expect_popup() as popup_info:
                        cc.click(button='middle')
                    aba = popup_info.value
                    aba.click('text=Download wallpaper 1920x1080')
                    listalinks.append(aba.url)
                    aba.close()
                except:
                    print('Erro ao abrir aba!')

        except:
            print('Erro ao abrir página!')

    print(len(listalinks))
    try:
        for c in listalinks:
            binarios = page.goto(c).body()
            nomeimage = page.url
            nomeimage = nomeimage[48:]
            caminho = r'C:\Users\Daniel\Desktop\wallpaperscraft.com nature\\'
            open(caminho + nomeimage, 'wb').write(binarios)
    except:
        print('Erro ao abrir link da imagem ou nos binários!')

    print('FIM')
    browser.close()
