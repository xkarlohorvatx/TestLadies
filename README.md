# TestLadies
Web testing course for beginners.

Work in progress.

***

##Před instalací
Pokud nemáš tolik zkušeností a chceš se striktně držet tohoto návodu, bude dobré, když si nejprve založíš novou složku pojmenovanou `TestLadies` 
ve svém počítači na místě, kde běžně vznikají tvé nové programovací projekty.

Ve složce `~/TestLadies` poté vytvoř složku `WebDrivers` do které si později přidáš ovladače.

Pokud si nejsi jistá jak se vytváří a spouští Python soubory, [projeď si prosím tento manuál vytvořený pro PyLadies](http://pyladies.cz/v1/s002-hello-world/hello-world.html).

##Instalace Pythonu, virtuálního prostředí a prohlížečů
Nejprve musíme vše správně nainstalovat a nastavit. Pokud máš již v počítači nainstalovaný Python 3 a umíš vytvořit virtuální prostředí 
pro práci v Pythonu, máš na půl vyhráno. Pokud s tím potřebuješ pomoci, tak nejlépe postupuj 
podle materiálů [instalace Pythonu a venv vytvořených pro PyLadies.](http://pyladies.cz/v1/s001-install/instalace.html)

Než budeš instalovat dál, předpokladem je, že máš:

 - nainstalovanou poslední stabilní verzi Python 3
 - vytvořené virtuální prostředí
 - spuštěné virtuální prostředí
 - kromě primárního prohlížeče:

	>  - pro Windows - Internet Explorer 
	>  - pro macOS - Safari
	>  - pro Linux - již běžně Firefox či Chrome

si doinstaluj ještě Firefox a Chrome (automatické testy budeme psát na všechny, abychom si byli jistí, 
že naše webová aplikace funguje ve všech prohlížečích stejně)

***

## Instalace Selenia - Windows, macOS, Linux

Pro automatické testování budeme používat nástroj Selenium. Je to skvělý nástroj pro automatické testování webových aplikací. 
Má podporu pro Firefox, Chrome, Internet Explorer i Safari. Můžeš si tak vybrat podle platformy i prohlížeče, který používáš 
a také využít všech možností pro komplexní automatizaci a testování. Na tomto [odkazu](https://pypi.python.org/pypi/selenium) 
najdeš příkazy, kterými jej nainstaluješ v příkazové řádce. Postup se pro Windows, macOS a Linux nijak neliší.

**Nezapomeň, že bys měla mít před instalacemi spuštěné virtuální prostředí.**

![Použij jednotlivé příkazy.](https://github.com/PyLadiesCZ/TestLadies/blob/master/img/all_os_selenium_install.png)

## Instalace ovladačů - Windows, macOS, Linux
Teď si nainstalujeme ovladače (drivery) pro jednotlivé prohlížeče. 
Nezapomeň je nainstalovat pro všechny prohlížeče, na kterých budeš testovat. Pro **Windows** tedy Internet Explorer, Firefox, Chrome. 
Na **macOS** pro Safari, Firefox a Chrome. Na **Linux** Firefox a Chrome.

**Ovladače:**

 pro Firefox - Mozzila GeckoDriver

 pro Safari - SafariDriver - stahovat není potřeba, Safari 10 nativně podporuje WebDriver API.

 pro IE - Microsoft Edge Driver

 pro Chrome -  Google Chrome Driver

Instalace ovladačů najdeš na stránce až po scrollování kousek níž [zde](http://docs.seleniumhq.org/download/)

Stáhni si je a nainstaluj poklepáním.

![Ovladače najdeš na stránce až po scrollování kousek níž.](https://github.com/PyLadiesCZ/TestLadies/blob/master/img/all_os_drivers_install.png)

 
XXX Doplnit k cemu drivery slouzi.

## Nastavení cesty pro každý prohlížeč zvlášť

Nejprve si uděláme test, který nám pomůže ověřit, že máme vše připravené k testování na jednotlivých prohlížečích.
Hotové soubory si můžeš stáhnout z [repozitáře TestLadies na GitHubu](https://github.com/PyLadiesCZ/TestLadies), ale pročti si i následující instrukce, 
zejména kvůli nastavení cest k ovladačům, které musíš udělat sama. 
Stáhni si verze souborů začínající názvem `first_test_operacni-system_prohlizec.py` pro svůj operační systém a pro všechny prohlížeče.

XXX poladit cesty k browseru pro kazdy prohlizec na kazdem systemu zvlast TODO Veronika a Magda
http://stackoverflow.com/questions/40269229/python-selenium-3-0-firefox-47-0-1-installed-in-default-location-is-not-identi

### Windows

**Internet Explorer**

**Firefox**

**Chrome**

### macOS

**Safari**

Nastavení pro Safari je naštěstí velmi jednoduché. Řeší to řádek `browser = webdriver.Safari()` v souboru `first_test_macos_safari.py`.
Ovladač pro Safari nemusíme stahovat ani nastavovat jeho cestu, Safari podporuje WebDriver nativně. 

`browser.get('http://seleniumhq.org/')` - tento řádek nám umožňuje prohlížeč spustit a provést v něm test.

***Ověř si, zda je vše nastaveno správně:*** 
V Terminálu spusť soubor pomocí  `python first_test_macos_safari.py` (ano, v zapnutém virtuálním prostředí), se prohlížeč opravdu spustí, 
udělá test a opět prohlížeč vypne. V Terminálu poté vypíše výsledek testu.


![Náhled nastavení pro Safari.](https://github.com/PyLadiesCZ/TestLadies/blob/master/img/macos_safari_path.png)

**Chrome** a **Firefox**

Pro Chrome a Firefox je bohužel nastavení komplikovanější. Bude potřeba nastavit cestu na stažené ovladače,`chromedriver` a `geckodriver`, do $PATH.

***Postup je následující:***

1. Stažené `chromedriver` a `geckodriver` přesuň z `Downloads`složky do složky `WebDrivers`, kterou jsi si vytvořila v ~/TestLadies.

2. Otevři Terminál.

3. Zadej příkaz `sudo nano /etc/paths`.

4. Vyplň své heslo (ano, heslo je při psaní skryté úmyslně).

5. Otevřel se Ti editor `nano`, šipkami sjeď na poslední volný řádek a přidej cestu do složky `WebDrivers`

6. Pokud jsi se řídila instrukcemi, měla bys mít `WebDrivers` složku v projektu TestLadies, cesta by měla být `/Users/name/TestLadies/WebDrivers`,
 kde `name` je jméno tvého účtu na kterém jsi přihlášená. Za ním vyplň celou cestu do složky `WebDrivers`. 

7. Ulož cestu v `nano` editoru příkazy: control + x, Y, enter.

8. Vypni a zapni Terminál (změny se projeví až po jeho restartování). Zadej příkaz `echo $PATH`, měla by jsi již vidět přidanou cestu.

9. Hurááá, teď budou naše testy fungovat i v Chromu a Firefoxu.

V souborech `first_test_macos_chrome.py` a `first_test_macos_firefox.py` ovladače nastavuje řádek
`browser = webdriver.Chrome('chromedriver')` pro Chrome a `browser = webdriver.Firefox('geckodriver')` pro Firefox.

`browser.get('http://seleniumhq.org/')` - tento řádek nám umožňuje prohlížeč spustit a provést v něm test.

***Ověř si, zda je vše nastaveno správně:*** 

V Terminálu spusť postupně soubory pomocí `python first_test_macos_chrome.py` a `python first_test_macos_firefox.py`(ano, v zapnutém virtuálním prostředí), se prohlížeč opravdu spustí, 
udělá test a opět prohlížeč vypne. V Terminálu poté vypíše výsledek testu.


### Linux

**Firefox**

**Chrome**

***

**Oficiální dokumentace k Seleniu**

https://seleniumhq.github.io/selenium/docs/api/py/api.html

**Neoficiální dokumentace k Seleniu**

http://selenium-python.readthedocs.io
