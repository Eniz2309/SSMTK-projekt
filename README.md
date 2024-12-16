# SSMTK-projekt
Ovdje će biti uploadani materijali za SSMTK projekt tema 2
Posljednje izmjene 27.11.2024


Update 21.11.2024 (termin 1):

- spajanje bazne stanice, upoznavanje sa uređajem, analiza tutorijala na amarisoft tech academy
- osposobljena 2 mobilna uređaja za VoLTE pozive
- konfiguracija ue-db.cfg fajlova, mijenjanje pozivnih brojeva mobitela


Update 12.12.2024 (termin 2):

Analiziran tutorijal: https://tech-academy.amarisoft.com/appnote_ims.doc#ccb4ba1f1744a74223b3d1fae8b6f410
Izvršeno povezivanje pozivnih brojeva sa IMEI-ima mobilnih uređaja ( *#06# )
Pročitali IMEI-e sa mobilnih uređaja i povezali ih sa pozivnim brojevima
Promjene izvršene u ue-db-ims.cfg


Update 16.12.2024 (termin 1.1):

Analizirani tutorijali na Amarisoft tech academy u vezi VoLTE/VoNR konfiguracije
Dodijeljeni trunk parametri u sip_add u konfiguracijskom fajlu
Pokušaj konfiguracije SIP ( dodavanje SIP u ims.cfg fajl, pokušaj dodavanja IP adrese )
Preko komande _tcpdump_ snimali saobraćaj na interfejsu lo, prebacivali .pcap fajlove na laptop preko scp komande, analizirani fajlovi u Wiresharku
