# SISTEMI I SERVISI MOBILNIH TELEKOMUNIKACIJA 
PROJEKTNI ZADATAK - IZVJEŠTAJ
Studenti:
Eniz Balihodžić
Lejla Ćosić
Adna Pugonja


Ovdje će biti uploadani materijali za SSMTK projekt tema 2
Posljednje izmjene 16.12.2024

# Uvod #

Razvoj mobilnih komunikacija kontinuirano unapređuje svakodnevni život ljudi, omogućavajući ne samo brži prijenos podataka već i implementaciju novih usluga. Uvođenjem 4G LTE i kasnije 5G NR (New Radio) mreža, otvorene su mogućnosti za glasovne usluge poput VoLTE (Voice over LTE) i VoNR (Voice over New Radio), koje osiguravaju stabilne i pouzdane komunikacije.

Jedan od ključnih izazova u modernom društvu jeste omogućiti pravovremeno informisanje korisnika o stanju na cestama kako bi se povećala sigurnost i optimiziralo vrijeme putovanja. Ova potreba može se efikasno adresirati korištenjem VoLTE i VoNR tehnologija. Iako postoje različite platforme za informisanje o stanju na cestama, njihova integracija u mobilne mreže putem glasovnih usluga još uvijek nije široko implementirana. VoLTE i VoNR tehnologije omogućavaju inovativan pristup pružanju audio obavještenja direktno putem glasovnih poziva, čime se poboljšava dostupnost informacija, posebno za korisnike u pokretu.

Cilj ovog rada je razviti aplikaciju koja koristi VoLTE i VoNR tehnologije za pružanje glasovnih obavještenja o stanju na cestama, uz analizu kompletne signalizacije i performansi mreže. Rad također istražuje mogućnosti implementacije ovakvog sistema u eksperimentalnoj 4G/5G mreži.

# Amarisoft CallBox Mini #
U ovom poglavlju će biti predstavljena i analizirana oprema koja će biti korištena za realizaciju projektnog zadatka. Glavna komponenta za izvedbu ovog sistema jeste Amarisoft Callbox mini bazna stanica. Njena osnovna funkcija jeste testiranje uređaja koji se koriste u 4G i 5G mrežnim tehnologijama. Na narednoj slici je prikzana arhitektura Amarisoft CallBox mini uređaja. 



<p align="center">
  <img src="https://www.amarisoft.com/media/ll-mini.png" alt="Arhitektura Amarisoft CallBox mini"/>
</p>

U osnovi, uređaj se ponaša kao 5G *stand-alone* mreža, međutim podržava i neterestrijalne 5G mreže kao i 5G *Reduced Capacity* mreže. Iako je inicijalno dizajnirana za rad na 5G, ova stanica omogućava testiranje i rad sa uređajima u LTE mreži. Zavisnosti od konfiguracije i krajnjih uređaja, ova bazna stanica može postići brizine do 200Mbps na *downlink*-u i do 75Mbps na *uplink*-u. Također podržava rad raznih servisa, kao što su VoLTE, VoNR, VioNR, VioLTE, SMS kao i *emergency call* servise. Kada je u pitanju frekvencijski opseg, *Amarisoft Callbox mini* podržava široki frekvencijski opseg, uključujući sub-6GHz opseg kao i milimetarsko talasno područje (*mmWave*). Za realizaciju ovog projektnog zadatka, pored bazne stanice, potrebni su također i mobilni uređaji (koji podržavaju 5G tehnologiju) kao i standardna PC periferija koja je potrebna za upravljanje baznom stanicom.


# Realizacija *VoLTE/VoNR* mreže

## *VoLTE* mreža
Voice over LTE (VoLTE) predstavlja tehnologiju koja omogućava realizaciju glasovnih poziva preko LTE (4G) mreže korištenjem IP protokola. Za razliku od tradicionalnih GSM/UMTS mreža koje koriste circuit-switched (CS) pristup za pozive, VoLTE koristi packet-switched (PS) pristup preko LTE infrastrukture. Ovaj koncept uvodi niz prednosti, uključujući poboljšan kvalitet glasa, efikasnije korištenje mrežnih resursa i integraciju glasovnih i podatkovnih usluga.

VoLTE je baziran na IMS (IP Multimedia Subsystem) platformi, koja omogućava prijenos glasovnih poziva kao podatkovnih paketa putem IP mreže. U standardnom VoLTE pozivu, korisnićki uređaj uspostavlja vezu s IMS jezgrom mreže, gdje se obavljaju funkcije kao što su signalizacija, autentifikacija i obrada poziva. Ključni protokoli korišteni u VoLTE pozivima uključuju SIP (Session Initiation Protocol), koji se koristi za signalizaciju i uspostavljanje, upravljanje i prekidanje poziva; RTP (Real-Time Protocol), koji omogućava prijenos glasovnih podataka u realnom vremenu; te QoS (Quality of Service), koji osigurava prioritet glasovnih paketa u mreži radi postizanja visokog kvaliteta usluge.

VoLTE donosi brojne prednosti. Kvalitet zvuka je bolji zahvaljujući upotrebi naprednih audio kodeka poput AMR-WB (Adaptive Multi-Rate Wideband), koji pružaju HD Voice kvalitet i osiguravaju širi frekvencijski opseg i prirodniji zvuk. VoLTE omogućava korisnicima da obavljaju glasovne pozive i istovremeno koriste mobilne podatke bez prekida. Efikasnije korištenje spektra omogućeno je optimiziranom LTE infrastrukturom, što znači da VoLTE pozivi koriste manje mrežnih resursa u poređenju s klasičnim CS pozivima. Vrijeme uspostave poziva je kraće u odnosu na 3G pozive zahvaljujući efikasnijoj signalizaciji. VoLTE također predstavlja prijelaznu tačku ka novim standardima poput VoNR (Voice over New Radio).

Međutim, postoje i izazovi u implementaciji VoLTE tehnologije. Efikasno funkcionisanje VoLTE usluge zavisi od potpunog usvajanja IMS platforme od strane mobilnih operatera. Kompatibilnost uređaja također može predstavljati problem jer korisnićki uređaji moraju podržavati VoLTE kako bi mogli koristiti ovu uslugu. Stariji modeli telefona često nisu kompatibilni. Održavanje visokog kvaliteta usluge zahtijeva preciznu kontrolu mrežnih resursa, posebno u uvjetima velike zagušenosti mreže.

VoLTE je danas ključna tehnologija za mobilne operatere, posebno u zemljama gdje se LTE mreža koristi kao osnovna infrastruktura za mobilne usluge. U okviru ovog rada, VoLTE se koristi za implementaciju aplikacije za informisanje o stanju na putevima, gdje se putem glasovnih poziva prosljeđuju audio obavještenja korisnicima. VoLTE omogućava da se informacije prenesu s visokim kvalitetom zvuka i minimalnim kašnjenjem, što je od velike važnosti za sigurnost i zadovoljstvo korisnika u saobraćaju.



Update 21.11.2024 (termin 1):

- spajanje bazne stanice, upoznavanje sa uređajem, analiza tutorijala na amarisoft tech academy
- osposobljena 2 mobilna uređaja za VoLTE pozive
- konfiguracija ue-db.cfg fajlova, mijenjanje pozivnih brojeva mobitela


Update 12.12.2024 (termin 2):

- Analiziran tutorijal: https://tech-academy.amarisoft.com/appnote_ims.doc#ccb4ba1f1744a74223b3d1fae8b6f410
- Izvršeno povezivanje pozivnih brojeva sa IMEI-ima mobilnih uređaja ( *#06# )
- Pročitali IMEI-e sa mobilnih uređaja i povezali ih sa pozivnim brojevima
- Promjene izvršene u ue-db-ims.cfg


Update 16.12.2024 (termin 1.1):

- Analizirani tutorijali na Amarisoft tech academy u vezi VoLTE/VoNR konfiguracije
- Dodijeljeni trunk parametri u sip_add u konfiguracijskom fajlu
- Pokušaj konfiguracije SIP ( dodavanje SIP u ims.cfg fajl, pokušaj dodavanja IP adrese )
- Preko komande _tcpdump_ snimali saobraćaj na interfejsu lo, prebacivali .pcap fajlove na laptop preko scp komande, analizirani fajlovi u Wiresharku
