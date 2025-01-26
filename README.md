# SISTEMI I SERVISI MOBILNIH TELEKOMUNIKACIJA 

PROJEKTNI ZADATAK - IZVJEŠTAJ

Ovdje će biti uploadani materijali za SSMTK projekt tema 2

**Posljednje izmjene 25.01.2025**

# Uvod #

Razvoj mobilnih komunikacija kontinuirano unapređuje svakodnevni život ljudi, omogućavajući ne samo brži prijenos podataka već i implementaciju novih usluga. Uvođenjem 4G LTE i kasnije 5G NR (New Radio) mreža, otvorene su mogućnosti za glasovne usluge poput VoLTE (Voice over LTE) i VoNR (Voice over New Radio), koje osiguravaju stabilne i pouzdane komunikacije.

Jedan od ključnih izazova u modernom društvu jeste omogućiti pravovremeno informisanje korisnika o stanju na cestama kako bi se povećala sigurnost i optimiziralo vrijeme putovanja. Ova potreba može se efikasno adresirati korištenjem VoLTE i VoNR tehnologija. Iako postoje različite platforme za informisanje o stanju na cestama, njihova integracija u mobilne mreže putem glasovnih usluga još uvijek nije široko implementirana. VoLTE i VoNR tehnologije omogućavaju inovativan pristup pružanju audio obavještenja direktno putem glasovnih poziva, čime se poboljšava dostupnost informacija, posebno za korisnike u pokretu.

Cilj ovog rada je razviti aplikaciju koja koristi VoLTE i VoNR tehnologije za pružanje glasovnih obavještenja o stanju na cestama, uz analizu kompletne signalizacije i performansi mreže. Rad također istražuje mogućnosti implementacije ovakvog sistema u eksperimentalnoj 4G/5G mreži.

# Postavka projektnog zadatka


Realizirati mrežu sa podrškom za VoLTE/VoNR uslugu sačinjenu od korisničkih uređaja
(mobitela) i eksperimentalne 4G/5G bazne stanice, u kojoj svaki korisnički uređaj ima
dodijeljen jedinstven javni identitet (broj telefona).

• Testirati VoLTE i VoNR usluge između svih korisničkih uređaja uz snimanje i analizu
kompletnog signalizacijskog saobraćaja (4G/5G protokoli, IMS/SIP).

• Implementirati aplikaciju za periodično preuzimanje i konverziju zvučnih obavještenja o
stanju na putevima sa web stranice BIHAMK-a.

• Konfigurisati VoIP klijenta (npr. pjsua) za reprodukciju zvučnog obavještenja i povezati ga
na eksperimentalnu 4G/5G mrežu.

• Testirati VoLTE/VoNR baziranu uslugu informisanja o stanju na putevima uz snimanje i
analizu IMS/SIP signalizacijskog saobraćaja.





# *Amarisoft CallBox Mini* #
U ovom poglavlju će biti predstavljena i analizirana oprema koja će biti korištena za realizaciju projektnog zadatka. Glavna komponenta za izvedbu ovog sistema jeste Amarisoft Callbox mini bazna stanica. Njena osnovna funkcija jeste testiranje uređaja koji se koriste u 4G i 5G mrežnim tehnologijama. Na narednoj slici je prikzana arhitektura Amarisoft CallBox mini uređaja. 



<p align="center">
  <img src="https://github.com/Eniz2309/SSMTK-projekt/blob/main/Ilustracije/amarisoft_callbox_mini_arhitektura.png" alt="PJSUA" width="600" />
</p>
<p align="center">
  <em>Arhitektura Amarisoft CallBox mini</em>
</p>

U osnovi, uređaj se ponaša kao 5G *stand-alone* mreža, međutim podržava i neterestrijalne 5G mreže kao i 5G *Reduced Capacity* mreže. Iako je inicijalno dizajnirana za rad na 5G, ova stanica omogućava testiranje i rad sa uređajima u LTE mreži. Zavisnosti od konfiguracije i krajnjih uređaja, ova bazna stanica može postići brizine do 200Mbps na *downlink*-u i do 75Mbps na *uplink*-u. Također podržava rad raznih servisa, kao što su VoLTE, VoNR, VioNR, VioLTE, SMS kao i *emergency call* servise. Kada je u pitanju frekvencijski opseg, *Amarisoft Callbox mini* podržava široki frekvencijski opseg, uključujući sub-6GHz opseg kao i milimetarsko talasno područje (*mmWave*). Za realizaciju ovog projektnog zadatka, pored bazne stanice, potrebni su također i mobilni uređaji (koji podržavaju 5G tehnologiju) kao i standardna PC periferija koja je potrebna za upravljanje baznom stanicom.


# Realizacija *VoLTE/VoNR* mreže

## *VoLTE* mreža
Voice over LTE (VoLTE) predstavlja tehnologiju koja omogućava realizaciju glasovnih poziva preko LTE (4G) mreže korištenjem IP protokola. Za razliku od tradicionalnih GSM/UMTS mreža koje koriste circuit-switched (CS) pristup za pozive, VoLTE koristi packet-switched (PS) pristup preko LTE infrastrukture. Ovaj koncept uvodi niz prednosti, uključujući poboljšan kvalitet glasa, efikasnije korištenje mrežnih resursa i integraciju glasovnih i podatkovnih usluga.

VoLTE je baziran na IMS (IP Multimedia Subsystem) platformi, koja omogućava prijenos glasovnih poziva kao podatkovnih paketa putem IP mreže. U standardnom VoLTE pozivu, korisnićki uređaj uspostavlja vezu s IMS jezgrom mreže, gdje se obavljaju funkcije kao što su signalizacija, autentifikacija i obrada poziva. Ključni protokoli korišteni u VoLTE pozivima uključuju SIP (Session Initiation Protocol), koji se koristi za signalizaciju i uspostavljanje, upravljanje i prekidanje poziva; RTP (Real-Time Protocol), koji omogućava prijenos glasovnih podataka u realnom vremenu; te QoS (Quality of Service), koji osigurava prioritet glasovnih paketa u mreži radi postizanja visokog kvaliteta usluge.

VoLTE donosi brojne prednosti. Kvalitet zvuka je bolji zahvaljujući upotrebi naprednih audio kodeka poput AMR-WB (Adaptive Multi-Rate Wideband), koji pružaju HD Voice kvalitet i osiguravaju širi frekvencijski opseg i prirodniji zvuk. VoLTE omogućava korisnicima da obavljaju glasovne pozive i istovremeno koriste mobilne podatke bez prekida. Efikasnije korištenje spektra omogućeno je optimiziranom LTE infrastrukturom, što znači da VoLTE pozivi koriste manje mrežnih resursa u poređenju s klasičnim CS pozivima. Vrijeme uspostave poziva je kraće u odnosu na 3G pozive zahvaljujući efikasnijoj signalizaciji. VoLTE također predstavlja prijelaznu tačku ka novim standardima poput VoNR (Voice over New Radio).

Međutim, postoje i izazovi u implementaciji VoLTE tehnologije. Efikasno funkcionisanje VoLTE usluge zavisi od potpunog usvajanja IMS platforme od strane mobilnih operatera. Kompatibilnost uređaja također može predstavljati problem jer korisnički uređaji moraju podržavati VoLTE kako bi mogli koristiti ovu uslugu. Stariji modeli telefona često nisu kompatibilni. Održavanje visokog kvaliteta usluge zahtijeva preciznu kontrolu mrežnih resursa, posebno u uvjetima velike zagušenosti mreže.

VoLTE je danas ključna tehnologija za mobilne operatere, posebno u zemljama gdje se LTE mreža koristi kao osnovna infrastruktura za mobilne usluge. U okviru ovog rada, VoLTE se koristi za implementaciju aplikacije za informisanje o stanju na putevima, gdje se putem glasovnih poziva prosljeđuju audio obavještenja korisnicima. VoLTE omogućava da se informacije prenesu s visokim kvalitetom zvuka i minimalnim kašnjenjem, što je od velike važnosti za sigurnost i zadovoljstvo korisnika u saobraćaju.




# Konfiguracija i povezivanje opreme

U prvom koraku realizacije, potrebno je povezati i konfigurisati uređaje koji će se koristiti u mreži. Za izradu ovog projektnog zadatka biće korištena sljedeća oprema:
- *Amarisoft CallBox Mini* bazna stanica
- PC računar ( za *remote* pristup baznoj stanici )
- 2 mobilna uređaja ( *User Equipment* - UE )


<p align="center">
  <img src="https://github.com/Eniz2309/SSMTK-projekt/blob/main/Ilustracije/amarisoft_konekcija.png" alt="PJSUA" width="500" />
</p>
<p align="center">
  <em>Shematski prikaz povezivanja uređaja u mrežu</em>
</p>

Operativni sistem koji se nalazi na baznoj stanici je *unix-like* pa se sva manipulacija baznom stanicom vrši preko terminala. Nakon pokretanja bazne stanice, potrebeno je unijeti kredencijale.
Za ispravan rad bazne stanice, pored fizičkog pokretanja, potrebno je i softverski pokrenuti njene servise. Pokretanje se vrši preko sljedeće komande:

<div align="center">
  <pre>
  <code>
service lte start
  </code>
  </pre>
</div>
Nakon pokretanja servisa, moguće je i provjeriti status isti preko sljedeće komande:
<div align="center">
  <pre>
  <code>
service lte status
  </code>
  </pre>
</div>

Ukoliko je sve ispravno konfigurisano, LTE servis bi trebao imati status *active(running)*.

<p align="center">
  <img src="https://github.com/Eniz2309/SSMTK-projekt/blob/main/Ilustracije/servis_lte_status.png" alt="PJSUA" width="600" />
</p>
<p align="center">
  <em>Provjera statusa LTE servisa</em>
</p>

Ukoliko se vrši određena modifikacija konfiguracijskih fajlova, da bi se njen rad ažurirao potrebno je restartovati servise narednim komandama:
<div align="center">
  <pre>
  <code>
systemctl restart lte ili service lte restart
  </code>
  </pre>
</div>

Baznoj stanici je moguće pristupiti preko *remote API*-ja, korištenjem *remote PC*-a. Bitno je napomenuti da bazna stanica i računar moraju biti povezani na istu mrežu. Da bi se pristupilo baznoj stanici *remote* potrebno je korsititi bilo koji *web browser* gdje se unosi sljedeći URL:

<div align="center">
  <pre>
  <code>
X.X.X.X/lte
  </code>
  </pre>
</div>

, gdje je *X.X.X.X* IP adresa bazne stanice.

Ukoliko je potrebno saznati IP adrese bazne stanice ili naziv nekog od *network interface*-a to je moguće pronaći preko *ifconfig* komande. IP adresa za *remote* pristup se uglavnom nalazi u *ens2p0* mrežnom *interface*-u.



# Konfiguracija i uspostava *VoLTE* poziva

*Amarisoft Callbox Mini* bazna stanica ima u sebi implementiranih više sotverskih *LTE* modula i to *IMS*, *MME*, *ENB* i *MBMS-GW*. Ovim modulima se može pristupiti preko sljedeće komande: 
<div align="center">
  <pre>
  <code>
screen -x lte
  </code>
  </pre>
</div>

Konfiguracijski fajlovi (*.cfg*) svakih od prethodno navedenih modula se nalaze u */root/* direktoriju.

## Postavke *UE* baze 

*UE* baza predstavlja bazu podataka gdje su smješteni podaci o mobilnim uređajima koji su povezani na baznu stanicu. Konfiguracijski fajle ove baze je *ue-db-ims.cfg*. Na narednoj slici je prikazan *ue-db-ims.cfg* fajl.

<p align="center">
  <img src="https://github.com/Eniz2309/SSMTK-projekt/blob/main/Ilustracije/ue_db_cfg.png" alt="PJSUA" width="600" />
</p>
<p align="center">
  <em>UE baza</em>
</p>


Svakom uređaju potrebno je dodijeliti jedinstveni telefonski broj koji se povezuje s njegovim IMEI brojem (*International Mobile Equipment Identity*), čime se osigurava ispravna VoLTE konfiguracija.
IMEI svakog korisničkog uređaja može se saznati unosom koda *#06#. Nakon što se dođe do IMEI-a mobitela, potrebno je isti u *UE* bazi povezati sa željenim pozivnim brojem. Kao što se vidi sa prethodne slike, prvi IMEI je povezan s brojem 0600000123, drugi IMEI je povezan s brojem 0600000124.



# *PJSUA* (*PJSIP USER AGENT*)

PJSUA je komandna linija SIP korisničkog agenta (*softphone*) temeljen na PJSIP open-source SIP biblioteci. Iako se koristi kao referentna implementacija za PJSIP, PJNATH i PJMEDIA, PJSUA nudi bogat skup funkcionalnosti za testiranje i rješavanje problema u SIP instalacijama. 
PJSIP

Ključne Karakteristike PJSUA:

- Podrška za Više Računa: Omogućava konfiguraciju više SIP računa s različitim postavkama registracije.

- Više SIP Poziva: Podržava simultano upravljanje više SIP poziva, uključujući konferencijske pozive.

- *Instant Messaging* i Prisutnost: Omogućava slanje instant poruka i praćenje prisutnosti korisnika.

- Napredne Medijske Funkcije: Podrška za različite audio kodeke, adaptivni jitter buffer, automatsko uklanjanje eha (AEC), PLC, VAD, STUN, ICE i druge funkcionalnosti.

- Podrška za Različite Kodeke: Podržava kodeke poput Speex, iLBC, GSM, G.711, L16 u različitim opsezima (narrow-band, wideband, ultra-wideband).

- Dodatne Funkcionalnosti: Omogućava petljanje medija (lokalno ili udaljeno), reprodukciju WAV datoteka i pruža statistiku kvaliteta putem RTCP-a.

## Instalacija i konfiguracija *PJSUA*

Prvi korak u instalaciji i konfiguraciji *PJSUA* je instlacija AMR WB (wideband) i NB (narrowband) kodeka, koji su potrebni za adekvatan rad sa baznom stanicom.
### Instalacija OpenCORE AMR NB i WB kodeka

Za instalaciju kodeka, potrebno je prvo preuzeti instalacijske fajlove. Sljedeći korak je ekstrakcija fajlova, komandom *tar*:
<div align="left">
  <pre>
  <code>
    
$ cd my_build_directory
$ tar xzf opencore-amr-0.1.3.tar.gz
$ 
</code>
  </pre>
</div>

Zatim je potrebno pokrenuti *configure* fajl za konfiguraciju i dodati *--prefix* i uraditi *build* i instalaciju:

<div align="left">
  <pre>
  <code>
    
$ ./configure --prefix=/home/foopencore-amr-0.1.3.tar.gz
$ make && make install

</code>
  </pre>
</div>




Provjera uspješne instalacije *ffmpeg* alata i potrebnih kodeka se može uraditi sljedećom komandom:
<div align="left">
  <pre>
  <code>
    
ffmpeg -codecs
</code>
  </pre>
</div>


Korištenjem *ffmpeg* alata, audio fajlovi koji će se reproducirati na baznoj stanici se konvertuju u *.wav* fajl preko komande:

<div align="left">
  <pre>
  <code>
    
ffmpeg -i myaudiofile -acodec pcm_s16le -ac 1 -ar 16000 test.wav

</code>
  </pre>
</div>

, gdje je *myaudiofile* ulazni fajl koji se konvertuje, *-acodec pcm16le* predstavlja PCM modulaciju sa 16 bita u Little endian formatu,dok *-ac 1* označava broj audio kanala, a *-ar 16000* predstavlja frekvenciju uzorkovanja koja je postavljena na 16kHz i konačno *test.wav* je konačni konvertovani fajl.

<p align="center">
  <img src="https://github.com/Eniz2309/SSMTK-projekt/blob/main/Ilustracije/ffmpeg_konverzija.png" alt="PJSUA" width="600" />
</p>
<p align="center">
  <em>Koverzija audio formata preko ffmpeg alata</em>
</p>


## Instalacija *pjproject*-a

U narednoj iteraciji je potrebno preuzeti i *build*-dati *pjproject* u kojem se zapravo nalazi PJSUA i koji koristi prethodno instalirane alate. Nakon preuzimanja *.zip* fajla, potrebno je izvršiti ekstraciju istog. U dobijeni *pjproject* je potrebno staviti *.wav* fajl koji će se reprodukovati kao i *pjsua.cfg* konfiguracijski fajl. 
Da bi PJSUA bio povezan sa VoLTE servisom preko kojeg će se vršiti komunikacija, potrebna je konfiguracija VoIP klijenta i konfiguracijskih fajlova na baznoj stanici. U fajlu *ue_db-ims.cfg* dodati linije za *dummy* SIP klijenta:


    /* Dummy SIM information for MME */
    sim_algo: "xor",
    imsi: "000000000000000",
    K: "00000000000000000000000000000000",
    amf: 0x0000,
    /* SIP client informations */
    impi: "sipclient",
    impu: ["tel:1234"],
    pwd: "sipclient",
    authent_type: "MD5",


Zbog određenih neusaglašenosti u verzijama i njihovom načinu čitanja varijabli, u *impu* je potrebno dodati i "sip:1234".

## Pokretanje PJSUA


Nakon uspješne instalacije i konfiguracije, PJSUA se pokreće u pjproject direktoriju sljedećom komandom:

<div align="left">
  <pre>
  <code>
    
./pjsip-apps/bin/pjsua-x86_64-unknown-linux-gnu --config-file=pjsua.cfg

</code>
  </pre>
</div>

Ukoliko je sve ispravno urađeno, trebao bi se pokrenuti PJSUA u terminalu kao na slici ispod.
Korisno je napomenuti da AMR kodeci koristi određene biblioteke koje sistem ne može pronaći u standardnim /lib datotekama već se oni nalaze u instalacijskim datotekama kodeka te zbog toga može izbacivati grešku prilikom pokušaja pokretanja PJSUA. Da bi se taj problem riješio, potrebno je ručno izvršiti export potrebnih biblioteka sljedećom komandom:

<div align="left">
  <pre>
  <code>
 export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/lib_fajl_alata
</code>
  </pre>
</div>


<p align="center">
  <img src="https://github.com/Eniz2309/SSMTK-projekt/blob/main/Ilustracije/PJSUA_prozor.png" alt="PJSUA" width="500" />
</p>
<p align="center">
  <em>PJSUA</em>
</p>

Važno je napomenuti da je potrebno da *LTE* i *PJSUA* servisi trebaju biti pokrenuti istovremeno te je potrebno osigurati da rade na različitim portovima. Kako su ova dva servisa povezani, pokretanjem komande *users* u screenu *ims* bi se, pored mobilnih uređaja trebao prikazati i SIP klijent kao na narednoj slici.

<p align="center">
  <img src="https://github.com/Eniz2309/SSMTK-projekt/blob/main/Ilustracije/ims_users_nepodvuceno.png" alt="PJSUA" width="600" />
</p>
<p align="center">
  <em>Users u ims screenu</em>
</p>

*PJSUA* će u terminalu ispisivati šta se trenutno dešava na tom servisu. Na narednoj slici je primjer poruke (*msg*) koju *PJSUA* ispisuje kada neki korisnik pozove ovaj servis.

<p align="center">
  <img src="https://github.com/Eniz2309/SSMTK-projekt/blob/main/Ilustracije/PJSUA_invite.png" alt="PJSUA" width="800" />
</p>
<p align="center">
  <em>PJSUA invite za poziv</em>
</p>

Sa slike se vidi da je *INVITE* tj. poziv upućen od strane mobilnog uređaja sa brojem 0600000123 prema sip serveru sip1234@amarisoft.com.
Nakon obavljenog poziva, u PJSUA se prikaže statistika i podaci o obavljenom pozivu.

<p align="center">
  <img src="https://github.com/Eniz2309/SSMTK-projekt/blob/main/Ilustracije/statistika_poziva.png" alt="PJSUA" width="600" />
</p>
<p align="center">
  <em>Statistika poziva u PJSUA</em>
</p>


# Preuzimanje audio sadržaja i priprema za reprodukciju

Da bi bazna stanica bila u mogućnosti reprodukovati ažuriran audio sadržaj o stanju na putevima, potrebno je napraviti skriptu koja će periodično preuzimati ažurirani audio snimak sa BIHAMK stranice. U okviru ovog projekta će biti realizovana *python* skripta koja će povremeno preuzimati novi audio sadržaj sa BIHAMK web stranice. Da bi se izbjegla kompleksna skripta, ovaj dio projekta je podijeljen u 3 segmenta, gdje su iskorištene pogodnosti Fedore kao linux-based sistema:
   - Python skripta koja preuzima potrebni audio snimak sa *BIHAMK* web stranice
   - *Bash* skripta koja pokreće python skriptu a zatim koristi *ffmpeg* alat za konverziju audio fajla u *.wav* format i smješta ga u pjproject direktorij
   - *Crontab* u kojem je podešeno periodično pokretanje *bash* skripte

Da bi se moglo vršiti preuzimanje, potrebno je doći do linka sa kojeg se preuzima audio fajl. To nije u ovom slučaju samo URL www.bihamk.ba već je potrebno pronaći sekciju *Stanje na putevima* na samoj stranici, te putem *Inspect element*-a pronaći link na kojem se pohranjuje audio sadržaj. Budući da se radi o audio fajlu, link se može naći relativno jednostavno, traženjem ključnih riječi poput *audio*.

<p align="center">
  <img src="https://github.com/Eniz2309/SSMTK-projekt/blob/main/Ilustracije/stanje_na_putevima.png" alt="PJSUA" width="800" />
</p>
<p align="center">
  <em>Pronalaženje linka za audio fajl na BIHAMK stranici</em>
</p>


## Python skripta

Za korištenje python programskog jezika, potrebno je imati python modul instaliran. Potrebno je napisati kod za skriptu koja će preuzimati fajl sa BIHAMK stranice, odnosno sa linka iz prethodne sekcije. Link na kojem se nalazi audio fajl nije uvijek isti te je potrebno napraviti kod koji će vršiti prezuimanje HTML fajla stranice, a zatim vršiti njegovo parsiranje i pronalazak potrebnog linka. Za tu svrhu je potrebno koristiti biblioteku *requests* koja se koristi za slanje *HTTP request*-a. Skripta za preuzimanje audio fajla je data u nastavku:
<div align="left">
  <pre>
  <code>
    
#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup

\# URL stranice koja sadrži audio fajl
page_url = 'https://bihamk.ba/spi/stanje-na-cesti-u-bih'

\# Slanje GET zahtjeva za preuzimanje HTML sadržaja stranice
response = requests.get(page_url)

\# Provjera uspješnog statusa (status kod 200)
if response.status_code == 200:
    # Parsiranje HTML sadržaja
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Tražimo <audio> tag sa klasom 'mt-3'
    audio_tag = soup.find('audio', class_='mt-3')
    
    if audio_tag:
        # Potražite <source> tag unutar <audio> taga
        source_tag = audio_tag.find('source')
        if source_tag and 'src' in source_tag.attrs:
            audio_url = source_tag['src']
            #print(f"Audio fajl se nalazi na: {audio_url}")
            
            # Sada skidamo audio fajl sa preuzetog URL-a
            filename = "bihamk_audio.mp3" 
            response = requests.get(audio_url, stream=True)
            response.raise_for_status()

            with open(filename, "wb") as audio_file:
                for chunk in response.iter_content(chunk_size=8192):
                    if chunk:
                        audio_file.write(chunk)


</code>
  </pre>
</div>

Bitno je imati na umu da se skripta pokreće u unix-based okruženju pa je potrebno dodati *#! (shebang)* da se osigura da bude izvršiva na samom Fedora operativnom sistemu.

## Bash skripta

Bash skripta je u suštini *.sh* u kojem su zapisane komande koje će pokretati u terminalu jedna za drugom. Za potrebe ovog zadatka, kreirana je *bash* skripta koja pokreće prethodno opisanu *python* skriptu za preuzimanje audio fajla, a zatim pokreće konverziju koristeći ranije objašnjenu *ffmpeg* funkciju i na kraju vrši kopiranje tog fajla u *pjproject* direktorij, koja ima sljedeći oblik:


<div align="left">
  <pre>
  <code>
    
#! /usr/bin/env bash

python3 skripta_za_preuzimanje.py

/var/lib/snapd/snap/bin/ffmpeg -i bihamk_audio.mp3 -acodec pcm_s16le -ac 1 -ar 16000 test.wav


</code>
  </pre>
</div>

Bitno je napomenuti da neki alati koji nisu *built-in* u operativnom sistemu, kao što je u ovom slučaju *ffmpeg*, se ne mogu pokrenuti u *bash* skriptama ukoliko se ne pozovu iz sistemskog direktorija gdje su i instalirane.

## Crontab

Crontab je alat u linux operativnim sistema koji služi za *schedule*-ing procesa na određeni period. Za ovaj projekat potrebno je postaviti task za povremeno pokretanje *bash* skripte, objašnjenje u prethodnoj skeciji, ovisno o rezoluciji vremena koja bude postavljena. Crontab editor se pokreće sljedećom komandom:

<div align="left">
  <pre>
  <code>
    crontab -e
</code>
  </pre>
</div>


U nastavku je data crontab komanda, koju je potrebno unijeti u crontab editor i spasiti, koja pokreće *bash* skriptu svaka 3 sata. Ovaj parametar može biti varijabilan, međutim zbog toga što se audio fajl na stranici ažurira 4 puta na dan, dovoljan period za osvježavanje je 2 do 3 sata. 

<div align="left">
  <pre>
  <code>
    0 */3 * * * /home/python_skripte/konverzija.sh 
</code>
  </pre>
</div>

Pregled pokrenutih taskova u crontabu se može izvršiti sljedećom komandom 
<div align="left">
  <pre>
  <code>
    crontab -l
</code>
  </pre>
</div>

# Analiza snimljenog saobraćaja

Snimanje saobraćaja na baznoj stanici se pohranjuje u *.pcap* fajlove, a komanda korištena za to jeste *tcpdump*. Budući da se *.pcap* fajlovi mogu analizirati preko *Wireshark*-a, čiji *GUI* nije moguće pokrenuti u terminalu bazne stanice, snimljene fajlove je potrebno prebaciti na *remote* računar. Kako su bazna stanica i računar u istoj mreži, na *remote* računar se mogu kopirati *.pcap* fajlovi sa bazne stanice preko *scp* komande:

<div align="center">
  <pre>
  <code>
scp ime_korisnika@IP_ADRESA_BAZNE_STANICE:/root/DIREKTORIJ_U_KOME_SU_POHRANJENI_PCAP_FAJLOVI C:\Users\DIREKTORIJ_GDJE_ĆE_BITI_POHRANJENI_FAJLOVI_NA_PC
  </code>
  </pre>
</div>

## Dekriptovanje ESP paketa u Wiresharku i izdvajanje SIP poruka

Prije započinjanja snimanja i analize mrežnog saobraćaja, potrebno je izvršiti izmjene u datoteci **ims.cfg** i pravilno konfigurisati Wireshark kako bi se omogućila dekripcija i prikaz SIP protokola. Bez ovih podešavanja, SIP poruke će ostati nečitljive, a u Wiresharku će se prikazivati samo šifrirani podaci.

### Podešavanje IMS Sistema za Prikaz SIP Poruka

Prvo je potrebno omogućiti zapisivanje ključnih parametara na IMS strani sistema. To se postiže izmjenom konfiguracijske datoteke `ims.cfg`. U sekciji `log_options` dodaje se sljedeći parametar:

<div align="center">
  <pre>
  <code>
ims.key=1
  </code>
  </pre>
</div>

Ova opcija omogućava sistemu da bilježi potrebne informacije, uključujući ključeve za autentifikaciju i enkripciju.

### Konfiguracija Wiresharka za Prikaz SIP Poruka

Nakon što su parametri za zapisivanje ključnih podataka omogućeni, potrebno je konfigurisati Wireshark kako bi se dekriptovale i prikazale SIP poruke. 
Za omogućavanje dekripcije i prikaza SIP poruka, potrebno je konfigurirati Wireshark na sljedeći način:

Potrebno je otvoriti **Wireshark**, pristupiti postavkama putem **Edit > Preferences**, te u sekciji **Protocols** odabrati **ESP**. Nakon toga, potrebno je označiti sve dostupne opcije (checkbox-ove) i kliknuti na dugme **Edit**. 
Nakon što se otvori prozor za unos, potrebno je popuniti parametre na sljedeći način:

| Field              | Value                                        |
|--------------------|----------------------------------------------|
| Protocol           | IPv4                                        |
| Src IP             | *                                           |
| Dest IP            | *                                           |
| SPI                | 2564331439                                  |
| Encryption         | AES-CBC [RFC3602]                           |
| Encryption Key     | 0x62695abf7237e9bed1714abd757bf52b          |
| Authentication     | HMAC-SHA-1-96 [RFC2404]                     |
| Authentication Key | 0xba4fadc076b74fdd97b26e0aa42ce9a700000000  |



Nakon što su ovi parametri uneseni i postavke spremljene, SIP poruke će postati vidljive i spremne za analizu.

## *VoLTE* poziv

U Wireshark fajlu *VoLTE_poziv* je snimljeni saobraćaj uspostave *VoLTE* poziva između dva uređaja povezanih na baznu stanicu. Jedna od mnogih prednosti *Wireshark*-a jeste i njegova mogućnost kreiranje MSC dijagrama od snimljenog saobraćaja. U meniju *Telephony*, odabirom opcije *VoIP calls*

<p align="center">
  <img src="https://github.com/Eniz2309/SSMTK-projekt/blob/main/Ilustracije/VOIP_CALLS.png" alt="*VoLTE* invite" width="700" />
</p>
<p align="center">
  <em>VoLTE invite</em>
</p>

, otvara se prozor kao na prethodnoj slici. MSC dijagram se kreira odabirom svih stavki u prozoru i klikom na *Flow sequence*.

Dijagram prikazuje uspostavu, tok i završetak VoLTE poziva, gdje se koristi SIP (Session Initiation Protocol) za signalizaciju, a RTP (Real-Time Transport Protocol) za prijenos glasovnih podataka. Na samom početku, klijent koji inicira poziv šalje SIP INVITE poruku sa SDP-om (Session Description Protocol) prema odredištu, pri čemu SDP sadrži informacije o podržanim kodecima (kao što su AMR-WB i AMR) i dodatnim opcijama, poput podrške za DTMF signale putem RTP-a. Ova INVITE poruka prolazi kroz IMS infrastrukturu, koja uključuje ključne čvorove poput P-CSCF-a i S-CSCF-a, te stiže do krajnjeg korisnika ili serverskog čvora.


<p align="center">
  <img src="https://github.com/Eniz2309/SSMTK-projekt/blob/main/Ilustracije/VoLTE_invite.png" alt="*VoLTE* invite" width="700" />
</p>
<p align="center">
  <em>Kreiranje MSC dijagrama</em>
</p>

Sa prethodne slike vidimo da su 3 instance u upostavi poziva. Ukoliko se analiziraju *users* u modulu *ims*, može se jednostavno uočiti da su to IPv6 adrese mobilnih uređaja između kojih se uspotavlja poziv i SIP servera preko kojeg se poziv posreduje.
<p align="center">
  <img src="https://github.com/Eniz2309/SSMTK-projekt/blob/main/Ilustracije/ims_users.png" alt="*VoLTE* invite" width="700" />
</p>
<p align="center">
  <em>ims users</em>
</p>

U prvom koraku, mobilni uređaj koji želi uspostaviti poziv, šalje *INVITE SDP* prema SIP serveru. Zatim SIP server proslijeđuje *INVITE SDP* prema ciljnom mobilnom uređaju. Nadalje, SIP server proslijeđuje *INVITE* prema uređaju sa kojim pozivalac želi uspotaviti poziv.

<p align="center">
  <img src="https://github.com/Eniz2309/SSMTK-projekt/blob/main/Ilustracije/VoLTE_2dio.png" alt="VoLTE" width="700" />
</p>
<p align="center">
  <em>VoLTE Wireshark</em>
</p>



Nakon što INVITE stigne, odgovara se sa 100 Trying porukom kako bi se signaliziralo da je zahtjev primljen. Slijedi 183 Session Progress, koja uključuje povratni SDP kako bi se definirao početni medijski kanal. U ovoj fazi koristi se i PRACK (Provisional Acknowledgment) kako bi se osigurala pouzdana dostava privremenih odgovora, što je potvrđeno sa 200 OK. Nadalje, dolazi do dodatnih UPDATE poruka za ažuriranje SDP parametara, posebno u slučaju pregovora o kodecima ili medijskom toku.

Nakon završetka pregovora i odgovora u obliku 200 OK, šalje se ACK, čime se medijski kanal uspostavlja, a glasovni paketni tok kreće putem RTP-a. RTP tokovi koriste AMR-WB kodek za visokokvalitetni zvuk. Dijagram pokazuje više RTP tokova između različitih SSRC identifikatora, koji predstavljaju audio strimove u realnom vremenu.

Kada pozivatelj ili primatelj odluči prekinuti poziv, šalje se BYE poruka kako bi se signalizirao završetak sesije. Odredište odgovara sa 200 OK, čime se osigurava uspješno zatvaranje sesije. Cijeli proces uključuje nekoliko iteracija signalizacije između različitih čvorova IMS infrastrukture i uređaja, uz korištenje standardnih SIP procedura za uspostavu, održavanje i završetak poziva.

Dijagram također pokazuje precizne vremenske oznake za svaku poruku i RTP tok, omogućujući detaljnu analizu kašnjenja i performansi mreže. Ovo je ključni korak za razumijevanje VoLTE poziva, jer omogućava otkrivanje potencijalnih problema u pregovorima o kodecima, kašnjenjima u uspostavi medijskog kanala, te efikasnosti završetka sesije



## *VoNR* poziv

U fajlu *VoNR_poziv_PJSUA* je sadržan snimljeni saobraćaj prilikom uspostave *VoNR* poziva, korištenjem *pjsua* klijenta. 

Kada korisnik pozove broj koji je konfigurisan za automatski odgovor, proces započinje standardnom SIP signalizacijom, gdje uređaj inicijatora šalje SIP INVITE poruku sa SDP-om prema IMS modul. SDP u ovoj poruci pregovara audio parametre, kao što su podržani kodeci poput AMR-WB (kodek za zvuk) i AMR, kako bi se omogućilo dekodiranje unaprijed snimljenog odgovora.

Po prijemu INVITE poruke, IMS modul odgovara sa 100 Trying, čime se potvrđuje da je zahtjev primljen i prosljeđuje se serveru odgovornom za automatizirani odgovor. Server zatim šalje povratni 183 Session Progress sa SDP-om. Ovo je ključno jer omogućava uspostavu RTP toka još prije nego što pozivatelj dobije zvučni signal "zvoni".

Kao dio pouzdane signalizacije, šalje se PRACK, koja se potvrđuje sa 200 OK, osiguravajući da se privremeni odgovori ispravno prenose. UPDATE poruke omogućavaju dodatna ažuriranja SDP-a prije nego što se reprodukcija snimljenog odgovora započne. Kada je sve spremno, šalje se 200 OK, praćeno sa ACK, čime je RTP kanal potpuno uspostavljen.

Tokom ove faze, RTP prenosi unaprijed snimljeni audio sadržaj od servera prema korisniku. Ovo se može prepoznati kroz RTP tokove označene SSRC identifikatorima u dijagramu. Broj paketa i trajanje RTP tokova ukazuju na to koliko je audio sadržaj dugačak.

Nakon završetka reprodukcije audio snimka, automatizirani sistem završava poziv šaljući BYE poruku. Odgovor na ovu poruku je 200 OK, čime se potvrđuje uspješan završetak sesije. Ovaj tok omogućava da korisnici brzo dobiju potrebne informacije bez interakcije sa stvarnim agentom.



# Zaključak

U ovom projektu uspješno je realizirana eksperimentalna 4G/5G mreža sa podrškom za VoLTE i VoNR usluge, čime je omogućena komunikacija između korisničkih uređaja putem dodijeljenih javnih identiteta (brojeva telefona). Provedena su testiranja VoLTE i VoNR usluga, pri čemu je snimljen i analiziran kompletan signalizacijski saobraćaj, uključujući ključne 4G/5G mrežne protokole te IMS/SIP signalizaciju.

Dodatno, razvijena je aplikacija za automatsko preuzimanje i konverziju zvučnih obavještenja sa web stranice BIHAMK-a, čime je osigurano ažurno informisanje korisnika o stanju na putevima. Integracija ove aplikacije sa VoIP klijentom omogućila je reprodukciju zvučnih obavještenja na eksperimentalnoj 4G/5G mreži, pružajući primjer inovativne upotrebe mrežnih resursa u realnom okruženju.

Testiranjem VoLTE/VoNR bazirane usluge informisanja o stanju na putevima demonstrirana je funkcionalnost i pouzdanost sistema, uz detaljnu analizu IMS/SIP signalizacijskog saobraćaja. Ovi rezultati potvrđuju tehničku izvodivost i potencijal praktične primjene razvijenog sistema u kontekstu naprednih mrežnih usluga.


## Reference

- https://tech-academy.amarisoft.com/ims_play_file.wiki
- https://tech-academy.amarisoft.com/LTE_VoLTE_Loopback.html
- https://tech-academy.amarisoft.com/volte_support.wiki
- https://stackoverflow.com/questions/480764/linux-error-while-loading-shared-libraries-cannot-open-shared-object-file-no-s
- https://www.pjsip.org/download.htm
- https://trac.pjsip.org/repos/wiki/Using-OpenCORE-AMR-NB-WB-Codec
