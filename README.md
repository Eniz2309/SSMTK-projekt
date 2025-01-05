# SISTEMI I SERVISI MOBILNIH TELEKOMUNIKACIJA 

PROJEKTNI ZADATAK - IZVJEŠTAJ

Ovdje će biti uploadani materijali za SSMTK projekt tema 2

**Posljednje izmjene 29.12.2024**

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
  <img src="https://www.amarisoft.com/media/ll-mini.png" alt="Arhitektura Amarisoft CallBox mini"/>
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
  <img src="https://github.com/Eniz2309/SSMTK-projekt/blob/main/amarisoft_konekcija.png" alt="Shematski prikaz povezivanje uređaja u mrežu" width="400" />
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

OVDJE STAVITI SS STATUSA


Ukoliko se vrši određena modifikacija konfiguracijskih fajlova, da bi se njen rad ažurirao potrebno je restartovati servise narednim komandama:
<div align="center">
  <pre>
  <code>
systemctl restart lte ili service lte restart
  </code>
  </pre>
</div>

Baznoj stanici je moguće pristupiti preko *remote API*-ja, korištenjem *remote PC*-a. Bitno je napomenuti da bazna stanica i računar moraju biti povezani na istu mrežu. Da bi se pristupilo baznoj stanici *remote* potrebno je korsititi bilo koji *web browser* gdje se unosi sljedeća komanda:

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

## Postavke *VoLTE* mreže na mobilnom uređaju

Za pravilan rad *VoLTE* mreže potrebno je konfiguracija i podešavanje određenih opcija na samom mobilnom uređaju. 
Svakom uređaju potrebno je dodijeliti jedinstveni telefonski broj koji se povezuje s njegovim IMEI brojem (*International Mobile Equipment Identity*), čime se osigurava ispravna VoLTE konfiguracija.

IMEI svakog korisničkog uređaja može se saznati unosom koda *#06#. 
Prvi IMEI je povezan s brojem 0600000123.
Drugi IMEI je povezan s brojem 0600000124.

# Analiza snimljenog saobraćaja

O wiresharku i pcap
Snimanje saobraćaja na baznoj stanici se pohranjuje u *.pcap* fajlove, a komanda korištena za to jeste *tcpdump*. Budući da se *.pcap* fajlovi mogu analizirati preko *Wireshark*-a, čiji *GUI* nije moguće pokrenuti u terminalu bazne stanice, snimljene fajlove je potrebno prebaciti na *remote* računar. Kako su bazna stanica i računar u istoj mreži, na *remote* računar se mogu kopirati *.pcap* fajlovi sa bazne stanice preko *scp* komande:

<div align="center">
  <pre>
  <code>
scp ime_korisnika@IP_ADRESA_BAZNE_STANICE:/root/DIREKTORIJ_U_KOME_SU_POHRANJENI_PCAP_FAJLOVI C:\Users\DIREKTORIJ_GDJE_ĆE_BITI_POHRANJENI_FAJLOVI_NA_PC
  </code>
  </pre>
</div>


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

Prvi korak u instalaciji i konfiguraciji *PJSUA* je instlacija AMR WB (wideband) i NB (narrowband) kodeka, koji su potrebni za adekvatan rad sa baznom stanicom. Nadalje je potrebno konfigurisati konfiguracijske fajlove na baznoj stanici. U prvom koraku u fajlu *ue_db-ims.cfg* dodati linije za SIP klijenta (u slučaju ove bazne stanice su se već nalazile u fajlu zakomentarisane, potrebno ih je otkomentarisati):

    /* Dummy SIM information for MME */
    sim_algo: "xor",
    imsi: "000000000000000",
    K: "00000000000000000000000000000000",
    amf: 0x0000,
    
    /* SIP client informations */
    impi: "sipclient",
    impu: ["tel:1234"],
    **pwd: "sipclient",
    authent_type: "MD5",**

