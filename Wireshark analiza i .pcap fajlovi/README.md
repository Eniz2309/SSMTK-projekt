# Analiza .pcap zapisa *VoLTE* i *VoNR* poziva


## *VoLTE* poziv

U Wireshark fajlu *VoLTE_poziv* je snimljeni saobraćaj uspostave *VoLTE* poziva između dva uređaja povezanih na baznu stanicu. Jedna od mnogih prednosti *Wireshark*-a jeste i njegova mogućnost kreiranje MSC dijagrama od snimljenog saobraćaja. U opcijama *Telephony*, u sekciji *VoIP calls*


<p align="center">
  <img src="https://github.com/Eniz2309/SSMTK-projekt/blob/main/Ilustracije/VoLTE_invite.png" alt="*VoLTE* invite" width="700" />
</p>
<p align="center">
  <em>VoLTE invite</em>
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

Dijagram prikazuje uspostavu, tok i završetak VoLTE poziva, gdje se koristi SIP (Session Initiation Protocol) za signalizaciju, a RTP (Real-Time Transport Protocol) za prijenos glasovnih podataka. Na samom početku, klijent koji inicira poziv šalje SIP INVITE poruku sa SDP-om (Session Description Protocol) prema odredištu, pri čemu SDP sadrži informacije o podržanim kodecima (kao što su AMR-WB i AMR) i dodatnim opcijama, poput podrške za DTMF signale putem RTP-a. Ova INVITE poruka prolazi kroz IMS infrastrukturu, koja uključuje ključne čvorove poput P-CSCF-a i S-CSCF-a, te stiže do krajnjeg korisnika ili serverskog čvora.

Nakon što INVITE stigne, odgovara se sa 100 Trying porukom kako bi se signaliziralo da je zahtjev primljen. Slijedi 183 Session Progress, koja uključuje povratni SDP kako bi se definirao početni medijski kanal. U ovoj fazi koristi se i PRACK (Provisional Acknowledgment) kako bi se osigurala pouzdana dostava privremenih odgovora, što je potvrđeno sa 200 OK. Nadalje, dolazi do dodatnih UPDATE poruka za ažuriranje SDP parametara, posebno u slučaju pregovora o kodecima ili medijskom toku.

Nakon završetka pregovora i odgovora u obliku 200 OK, šalje se ACK, čime se medijski kanal uspostavlja, a glasovni paketni tok kreće putem RTP-a. RTP tokovi koriste AMR-WB kodek za visokokvalitetni zvuk. Dijagram pokazuje više RTP tokova između različitih SSRC identifikatora, koji predstavljaju audio strimove u realnom vremenu.

Kada pozivatelj ili primatelj odluči prekinuti poziv, šalje se BYE poruka kako bi se signalizirao završetak sesije. Odredište odgovara sa 200 OK, čime se osigurava uspješno zatvaranje sesije. Cijeli proces uključuje nekoliko iteracija signalizacije između različitih čvorova IMS infrastrukture i uređaja, uz korištenje standardnih SIP procedura za uspostavu, održavanje i završetak poziva.

Dijagram također pokazuje precizne vremenske oznake za svaku poruku i RTP tok, omogućujući detaljnu analizu kašnjenja i performansi mreže. Ovo je ključni korak za razumijevanje VoLTE poziva, jer omogućava otkrivanje potencijalnih problema u pregovorima o kodecima, kašnjenjima u uspostavi medijskog kanala, te efikasnosti završetka sesije



## *VoNR* poziv

U fajlu *VoNR_poziv_PJSUA* je sadržan snimljeni saobraćaj prilikom uspostave *VoNR* poziva, korištenjem *pjsua* klijenta. 

