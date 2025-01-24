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

U prvom koraku, mobilni uređaj koji želi uspostaviti poziv, šalje *INVITE SDP* prema SIP serveru. Zatim SIP server proslijeđuje *INVITE SDP* prema ciljnom mobilnom uređaju.




## *VoNR* poziv

U fajlu *VoNR_poziv_PJSUA* je sadržan snimljeni saobraćaj prilikom uspostave *VoNR* poziva, korištenjem *pjsua* klijenta. 

