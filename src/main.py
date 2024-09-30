
from playwright.sync_api  import sync_playwright

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto('https://api-seguridad.sunat.gob.pe/v1/clientessol/4f3b88b3-d9d6-402a-b85d-6a0bc857746a/oauth2/loginMenuSol?originalUrl=https://e-menu.sunat.gob.pe/cl-ti-itmenu/AutenticaMenuInternet.htm&state=rO0ABXNyABFqYXZhLnV0aWwuSGFzaE1hcAUH2sHDFmDRAwACRgAKbG9hZEZhY3RvckkACXRocmVzaG9sZHhwP0AAAAAAAAx3CAAAABAAAAADdAAEZXhlY3B0AAZwYXJhbXN0AEsqJiomL2NsLXRpLWl0bWVudS9NZW51SW50ZXJuZXQuaHRtJmI2NGQyNmE4YjVhZjA5MTkyM2IyM2I2NDA3YTFjMWRiNDFlNzMzYTZ0AANleGVweA==')
        page.locator('input[id=txtRuc]').fill('20100145902')
        page.locator('input[id=txtUsuario]').fill('TIGREPER')
        page.locator('input[id=txtContrasena]').fill('T!PE2022')
        page.locator('button[id=btnAceptar]').click()
        page.wait_for_timeout(5000)
        element = page.locator('div[id=divOpcionServicio2]')
        element.hover()
        element.click()
        element2 = page.locator('li#nivel1_11.nivel1.liOpcion.backPlomo1.opcionPersonas.opcionEmpresas.opcionHuerfano')
        element2.hover()
        element2.click()
        page.evaluate("window.scrollTo(0,1000)")
        page.mouse.move(200,200,steps=5)
        page.mouse.down(button='middle')
        page.mouse.move(500,500, steps=5)
        element3 = page.locator('#nivel2_11_5.nivel2.liOpcion.opcionPersonas.opcionEmpresas.opcionHuerfano')
        element3.hover()
        element3.click()
        

        
        page.wait_for_timeout(50000)
        browser.close()

main()