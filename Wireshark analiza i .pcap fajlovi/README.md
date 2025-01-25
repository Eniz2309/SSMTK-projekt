# Analiza .pcap zapisa *VoLTE* i *VoNR* poziva


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
