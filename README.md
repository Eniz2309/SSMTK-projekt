# SISTEMI I SERVISI MOBILNIH TELEKOMUNIKACIJA 
PROJEKTNI ZADATAK - IZVJEŠTAJ

Ovdje će biti uploadani materijali za SSMTK projekt tema 2
Posljednje izmjene 16.12.2024

# Uvod #

Razvoj mobilnih komunikacija kontinuirano unapređuje svakodnevni život ljudi, omogućavajući ne samo brži prijenos podataka već i implementaciju novih usluga. Uvođenjem 4G LTE i kasnije 5G NR (New Radio) mreža, otvorene su mogućnosti za glasovne usluge poput VoLTE (Voice over LTE) i VoNR (Voice over New Radio), koje osiguravaju stabilne i pouzdane komunikacije.

Jedan od ključnih izazova u modernom društvu jeste omogućiti pravovremeno informisanje korisnika o stanju na cestama kako bi se povećala sigurnost i optimiziralo vrijeme putovanja. Ova potreba može se efikasno adresirati korištenjem VoLTE i VoNR tehnologija. Iako postoje različite platforme za informisanje o stanju na cestama, njihova integracija u mobilne mreže putem glasovnih usluga još uvijek nije široko implementirana. VoLTE i VoNR tehnologije omogućavaju inovativan pristup pružanju audio obavještenja direktno putem glasovnih poziva, čime se poboljšava dostupnost informacija, posebno za korisnike u pokretu.

Cilj ovog rada je razviti aplikaciju koja koristi VoLTE i VoNR tehnologije za pružanje glasovnih obavještenja o stanju na cestama, uz analizu kompletne signalizacije i performansi mreže. Rad također istražuje mogućnosti implementacije ovakvog sistema u eksperimentalnoj 4G/5G mreži.

# Amarisoft CallBox Mini #
U ovom poglavlju će biti predstavljena i analizirana oprema koja će biti korištena za realizaciju projektnog zadatka. Glavna komponenta za izvedbu ovog sistema jeste Amarisoft Callbox mini bazna stanica. Njena osnovna funkcija jeste testiranje uređaja koji se koriste u 4G i 5G mrežnim tehnologijama. Na narednoj slici je prikzana arhitektura Amarisoft CallBox mini uređaja. 



<p align="center">
  <img src="[https://github.com/waldyr/Sublime-Installer/blob/master/sublime_text.png?raw=true](https://github.com/user-attachments/assets/921cd9b3-bcf9-43e3-91f7-03fc8d93dab7)" alt="Sublime's custom image"/>
</p>

U osnovi, uređaj se ponaša kao 5G *stand-alone* mreža, međutim podržava i neterestrijalne 5G mreže kao i 5G *Reduced Capacity* mreže. Iako je inicijalno dizajnirana za rad na 5G, ova stanica omogućava testiranje i rad sa uređajima u LTE mreži. Zavisnosti od konfiguracije i krajnjih uređaja, ova bazna stanica može postići brizine do 200Mbps na *downlink*-u i do 75Mbps na *uplink*-u. Također podržava rad raznih servisa, kao što su VoLTE, VoNR, VioNR, VioLTE, SMS kao i *emergency call* servise. Kada je u pitanju frekvencijski opseg, *Amarisoft Callbox mini* podržava široki frekvencijski opseg, uključujući sub-6GHz opseg kao i milimetarsko talasno područje (*mmWave*). Za realizaciju ovog projektnog zadatka, pored bazne stanice, potrebni su također i mobilni uređaji (koji podržavaju 5G tehnologiju) kao i standardna PC periferija koja je potrebna za upravljanje baznom stanicom.


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
