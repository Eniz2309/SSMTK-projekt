# Analiza .pcap zapisa *VoLTE* i *VoNR* poziva


## *VoLTE* poziv

U Wireshark fajlu *VoLTE_poziv* je snimljeni saobraćaj uspostave *VoLTE* poziva između dva uređaja povezanih na baznu stanicu.

Wireshark omogućava kreiranje MSC dijagrama na osnovu snimljenog saobraćaja. 
<p align="center">
  <img src="https://github.com/Eniz2309/SSMTK-projekt/blob/main/Ilustracije/VoLTE_invite.png" alt="*VoLTE* invite" width="700" />
</p>
<p align="center">
  <em>VoLTE invite</em>
</p>

Sa prethodne slike vidimo da su 3 instance u upostavi poziva. Ukoliko se analiziraju *users* u modulu *ims* 
