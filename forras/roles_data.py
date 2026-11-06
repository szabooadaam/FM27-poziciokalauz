# -*- coding: utf-8 -*-
# Szerepkör-adatok az FM26/FM27 pozíciókalauzhoz.
# Koordináták: pálya 68 x 105, y=0 az ellenfél kapuja (fent), y=105 a saját kapu (lent).
# arrows: (x1, y1, x2, y2, típus)  típus: 'ip' = labdával / támadásban, 'oop' = labda nélkül / védekezésben

GK = (34, 99)
CB = (34, 89)
RCB = (42, 89)
WCBR = (50, 87)
FBR = (60, 85)
WBR = (62, 74)
DM = (34, 75)
CMR = (44, 61)
WMR = (61, 57)
AM = (34, 40)
WR = (60, 37)
ST = (34, 22)

GROUPS = [
    ("gk", "Kapus", "GK", "A kapus az FM26-tól két szerepet kap: egyet arra az időre, amikor a csapatodnál van a labda (labdakihozatal, passzjáték), és egyet arra, amikor az ellenfélnél (meddig jön ki, hogyan védi a védelem mögötti teret). A régi „Sweeper Keeper Támadó” típusú duty-k helyett most a két szerep párosítása dönti el a viselkedést."),
    ("cb", "Középhátvéd", "D (K)", "A középhátvédeknél válik el a legtisztábban a két fázis. Labdával azt választod ki, mennyire vegyen részt az építkezésben (egyszerű passz, vonalbontó passz, előrelépés a középpályára, kiszélesedés, átfedés), labda nélkül pedig azt, hogy kilépjen-e a csatárra (Stopping), vagy maradjon a vonalban és biztosítson (Covering). Háromvédős rendszerben a szélső középhátvédek külön, „Wide” szerepeket kapnak."),
    ("fb", "Szélső hátvéd és szárnyvédő", "D/WB (J/B)", "A modern futball legsokoldalúbb posztja. Támadásban a szerep dönti el, hogy szélességet ad (Wing-Back, Advanced Wing-Back), befelé húzódik (Inside Full-Back, Inside Wing-Back), vagy a játékot szervezi (Playmaking Wing-Back). Védekezésben három fokozat van: alap, letámadó (Pressing) és visszatartott (Holding). A szélső hátvéd szerepét mindig az előtte játszó szélsőhöz igazítsd."),
    ("dm", "Védekező középpályás", "DM", "A védelem előtti zóna gazdája. Labdával lehet egyszerű összekötő (DM), irányító (Deep-Lying Playmaker) vagy harmadik középhátvéd (Half Back). Labda nélkül öt viselkedés közül választhatsz: tartja a zónát (Screening), visszalép a védővonalba (Dropping), kilép a letámadásba (Pressing), vagy kisegít a szélen (Wide Covering)."),
    ("cm", "Középső középpályás", "M (K)", "Itt történt a legnagyobb átalakítás. A Mezzala, a Carrilero és a régi duty-változatok helyére új, beszédes nevű szerepek léptek: Channel Midfielder (CHM), Midfield Playmaker (MPM), Wide Central Midfielder (WCM), Box-to-Box Playmaker (BBP). Labda nélkül három alapviselkedés van: letámadó (Pressing), szűrő (Screening) és szélre kisegítő (Wide Covering). Figyelem: a WCM rövidítés két szerepet is jelöl, a labdás Wide Central Midfieldert és a labda nélküli Wide Covering Central Midfieldert."),
    ("wm", "Szélső középpályás", "M (J/B)", "A középpálya-sor szélén (4-4-2, 4-1-4-1) játszó játékos. Labdával lehet mélyről beadó szélső középpályás, klasszikus szélső, befelé húzódó szélső vagy széles játékmester. Labda nélkül a kérdés az, hogy visszazár-e a hátvéd mellé (Tracking), átlagos munkát végez (Wide Midfielder), vagy fent marad kontrára (Wide Outlet)."),
    ("am", "Támadó középpályás", "AM (K)", "A tízes pozíció. Labdával szabad helyeket keres a vonalak között (AM), gólpasszokat ad (Advanced Playmaker), szabadon kóborol (Free Role) vagy csatárként érkezik a tizenhatosba (Second Striker). Labda nélkül vagy visszazár (Tracking), vagy a középpályás pivotokat fogja (AM), vagy fent marad kontrakiindulópontnak (Central/Splitting Outlet)."),
    ("w", "Szélső támadó", "AM (J/B)", "A támadósor szélén játszó játékos. A labdás szerep dönti el a futás irányát: a vonalon marad (Winger, Wide Forward), befelé, a félterekbe húzódik (Inside Winger, Inside Forward), vagy szervez (Playmaking Winger). Labda nélkül visszakövetheti az ellenfél szélső hátvédjét (Tracking Winger), vagy fent maradhat kontrára (Wide/Inside Outlet Winger)."),
    ("st", "Csatár", "ST (K)", "A támadósor csúcsa. Labdával hét nagyon különböző csatártípus közül választhatsz, a kirobbanó mélységi futótól (Poacher, Channel Forward) a visszalépő irányítóig (False Nine, Deep-Lying Forward). Labda nélkül a csatár vagy az első letámadó (Centre Forward), vagy visszazár a középpályához (Tracking), vagy fent marad kontrára (Central/Splitting Outlet)."),
]

R = []

def role(group, phase, abbr, name, hu, base, arrows, zone, desc, attrs, good, avoid, src=""):
    R.append(dict(group=group, phase=phase, abbr=abbr, name=name, hu=hu, base=base, arrows=arrows,
                  zone=zone, desc=desc, attrs=attrs, good=good, avoid=avoid, src=src))

# ---------------- KAPUS ----------------
role("gk", "IP", "GK", "Goalkeeper", "kapus",
     GK, [(34, 99, 34, 84, 'ip')], (34, 96, 10, 6),
     "Kiegyensúlyozott kapus: a csapat építkezési stratégiája szerint indít, hol röviden a védőknek, hol hosszan. Nem lép ki feltűnően a kapuból, de passzlehetőségként sem bújik el. A legbiztonságosabb kiindulópont, ha nem tudod, mire képes a kapusod a lábával.",
     ["Kézzel játék", "Reflexek", "Helyezkedés", "Egy az egy elleni", "Rúgás", "Higgadtság"],
     ["bármelyik OOP kapusszerep", "Centre-Back párok"], [], "nyelvi fájl")
role("gk", "IP", "BGK", "Ball-Playing Goalkeeper", "labdajátékos kapus",
     GK, [(34, 99, 34, 86, 'ip'), (34, 86, 24, 80, 'ip'), (34, 86, 46, 78, 'ip')], (34, 92, 12, 9),
     "Aktív része az építkezésnek: kilép a kapuból, hogy passzlehetőség legyen, és gyakorlatilag tizenegyedik mezőnyjátékosként segít kijátszani az ellenfél letámadását. A rövid indítás és a nyomás alatti higgadtság a lényeg. Csak akkor válaszd, ha a kapus passza, első érintése és higgadtsága legalább átlag feletti, különben a hibái közvetlenül gólhoz vezetnek.",
     ["Passz", "Első érintés", "Higgadtság", "Döntéshozatal", "Előrelátás", "Rúgás"],
     ["Sweeper Keeper (OOP)", "Ball-Playing CB", "Half Back", "magas védővonal"],
     ["No-Nonsense CB pár mellé", "direkt, hosszú labdás játék"], "nyelvi fájl")
role("gk", "IP", "NGK", "No-Nonsense Goalkeeper", "biztonsági kapus",
     GK, [(34, 99, 34, 60, 'ip')], (34, 98, 8, 5),
     "Óvatos kapus: a gólvonal közelében marad, és nyomás alatt a lehető legkevesebb kockázatot vállalja, inkább hosszan kirúgja a labdát. Alsóbb osztályban, gyenge lábú kapussal vagy direkt, célcsatáros játékhoz ideális. Rövid építkezéshez nem való.",
     ["Kézzel játék", "Reflexek", "Helyezkedés", "Rúgás", "Légi elérés", "Koncentráció"],
     ["Line-Holding Goalkeeper (OOP)", "Target Forward", "mély védekező blokk"],
     ["Ball-Playing CB-kre épülő rövid építkezés"], "nyelvi fájl")
role("gk", "OOP", "GK", "Goalkeeper", "kapus (labda nélkül)",
     GK, [(34, 99, 34, 92, 'oop')], (34, 96, 12, 6),
     "A kapus alapfeladata: a kapu védése lövések és beadások ellen. Mérlegel a kapuban maradás és a kifutás között, a védővonal magasságához igazodik. A legtöbb taktikához megfelelő.",
     ["Reflexek", "Kézzel játék", "Helyezkedés", "Egy az egy elleni", "Légi elérés", "Kommunikáció"],
     ["közepes védővonal"], [], "nyelvi fájl")
role("gk", "OOP", "LHK", "Line-Holding Goalkeeper", "vonalon maradó kapus",
     GK, [(34, 99, 34, 95, 'oop')], (34, 98, 9, 4),
     "A saját tizenhatosán belül marad, a feljebb történő védekezést teljesen a társaira bízza. Mély védekezéshez és lassú, de jó reflexű, jól helyezkedő kapushoz ideális. Magas védővonallal kerüld, mert a védelem mögötti terület gazdátlan marad.",
     ["Reflexek", "Helyezkedés", "Kézzel játék", "Légi elérés", "Koncentráció"],
     ["mély blokk", "No-Nonsense CB", "Covering CB"], ["magas védővonal", "magas letámadás"], "nyelvi fájl")
role("gk", "OOP", "SK", "Sweeper Keeper", "söprögető kapus",
     GK, [(34, 99, 34, 80, 'oop'), (34, 99, 22, 82, 'oop'), (34, 99, 46, 82, 'oop')], (34, 88, 18, 11),
     "Proaktív kapus: rendszeresen kifut a kapuból, hogy elcsípje a védelem mögé küldött labdákat, vagy már korán megállítsa a kiugró csatárt. Ez teszi lehetővé a magas védővonalat. Gyorsaság, kifutás és egy az egy elleni tudás nélkül öngól-gyár lehet.",
     ["Kifutás (Rushing Out)", "Egy az egy elleni", "Gyorsulás", "Előrelátás", "Döntéshozatal", "Higgadtság"],
     ["Ball-Playing GK (IP)", "magas védővonal", "Stopping CB", "letámadó csapat"], ["lassú kapus", "mély blokk"], "nyelvi fájl")

# ---------------- KÖZÉPHÁTVÉD ----------------
role("cb", "IP", "CB", "Centre-Back", "középhátvéd",
     RCB, [(42, 89, 42, 80, 'ip')], (42, 87, 8, 7),
     "A középhátvéd alapszerepe labdával: a csapatot védi, mindig olyan helyen áll, ahonnan labdavesztés után azonnal reagálhat. Egyszerű passzokkal adja tovább a labdát a kreatívabb társaknak, nem cselez, nem kockáztat feleslegesen. A Mastering Football Manager szerint ez az „üres vászon” típusú szerep: kevés beépített utasítással, szabadon testre szabhatod.",
     ["Szerelés", "Emberfogás", "Helyezkedés", "Fejjáték", "Higgadtság", "Passz"],
     ["Ball-Playing CB párja", "bármely OOP CB-szerep"], [], "nyelvi fájl, Mastering FM")
role("cb", "IP", "BCB", "Ball-Playing Centre-Back", "labdajátékos középhátvéd",
     RCB, [(42, 89, 42, 76, 'ip'), (42, 80, 58, 50, 'ip'), (42, 80, 36, 42, 'ip')], (42, 84, 9, 10),
     "Védő, aki a védelemből vonalbontó passzokkal és mélységi átadásokkal viszi előre a játékot, és ha van tere, maga is előrevezeti a labdát. Szinte védelmi játékmester: a nyomást is jobban bírja, ezért a labdabirtokláson alapuló játék kulcsa. A könyvek szerint az egyik leggyakrabban használt szerep, de csak higgadt, jó döntéshozó játékosnak add.",
     ["Passz", "Látás", "Higgadtság", "Döntéshozatal", "Technika", "Első érintés", "Helyezkedés"],
     ["No-Nonsense CB vagy Centre-Back pár", "Half Back", "Ball-Playing GK"], ["két BCB gyenge lábú játékosokkal erős letámadás ellen"], "nyelvi fájl, Mastering FM")
role("cb", "IP", "NCB", "No-Nonsense Centre-Back", "biztonsági középhátvéd",
     RCB, [(42, 89, 42, 60, 'ip')], (42, 89, 7, 6),
     "Az utolsó mezőnyvédő, aki mindig védekezésre kész. Labdával egyszerűen játszik: nyomás alatt inkább felszabadít vagy biztonsági passzt ad, minthogy veszélyes helyen elveszítse a labdát. Alsóbb osztályokban, gyenge labdakezelésű, de jó fejelő és szerelő védővel ideális; elrejti a gyengeségét.",
     ["Szerelés", "Fejjáték", "Emberfogás", "Erő", "Ugrás", "Bátorság", "Helyezkedés"],
     ["Ball-Playing CB párja", "No-Nonsense GK", "mély blokk"], ["rövid, türelmes építkezés két NCB-vel"], "nyelvi fájl, Mastering FM")
role("cb", "IP", "ACB", "Advanced Centre-Back", "előrelépő középhátvéd",
     CB, [(34, 89, 34, 72, 'ip'), (34, 72, 34, 66, 'ip')], (34, 79, 8, 12),
     "Mély építkezésnél középhátvéd, a játék előrehaladtával viszont kilép a középpályára, és védekező középpályásként dolgozik tovább (a régi Libero modern utódja). Középpályás szintű technika és játékintelligencia kell hozzá. Mivel a védelemből kivesz egy embert, mögötte biztosítás kell: Inside Full-Back vagy egy harmadik középhátvéd.",
     ["Passz", "Első érintés", "Higgadtság", "Előrelátás", "Döntéshozatal", "Helyezkedés", "Technika"],
     ["Inside Full-Back", "háromvédős rendszer", "Covering CB (OOP)"], ["két belső középpályás, akik szintén mélyre jönnek (zsúfolt zóna)"], "nyelvi fájl, FM Scout")
role("cb", "IP", "WCB", "Wide Centre-Back", "széles középhátvéd",
     WCBR, [(50, 87, 58, 76, 'ip'), (58, 76, 62, 60, 'ip')], (55, 80, 9, 12),
     "Háromvédős rendszer szélső középhátvédje. Labdával szélességet ad, kihúzódik a szélre, és támogatja az előtte játszó szélső embereket, gyakran hátsó, visszajátszható passzlehetőségként. Védekezésben a szélső hátvéd előretörésekor ő zárja a szélső zónát, ahogy a könyv is írja.",
     ["Helyezkedés", "Szerelés", "Passz", "Gyorsaság", "Munkabírás", "Beadás"],
     ["Wing-Back vagy Advanced Wing-Back előtte", "3-4-3, 3-5-2"], ["négyvédős rendszer (ott nem elérhető)"], "nyelvi fájl, Mastering FM")
role("cb", "IP", "OCB", "Overlapping Centre-Back", "átfedő középhátvéd",
     WCBR, [(50, 87, 56, 70, 'ip'), (56, 70, 62, 30, 'ip')], (57, 62, 9, 28),
     "Középhátvéd és szélső egyben: a támadás korai szakaszában védelmet ad, a támadó harmadban viszont átfedő futásokkal beadási pozícióba kerül. Háromvédős rendszerben a szárnyvédő befelé húzódásával kombinálva egészen különleges túlerőt ad a szélen. Fizikailag és taktikailag nagyon igényes szerep.",
     ["Munkabírás", "Állóképesség", "Gyorsaság", "Beadás", "Szerelés", "Helyezkedés"],
     ["Inside Wing-Back előtte", "Advanced Wing-Back", "Covering CB a másik oldalon"], ["Overlapping CB mindkét oldalon (nincs rest-defence)"], "nyelvi fájl, SI hivatalos")
role("cb", "OOP", "CB", "Centre-Back", "középhátvéd (labda nélkül)",
     RCB, [(42, 89, 42, 86, 'oop')], (42, 88, 9, 6),
     "Labda nélkül az alapfeladat: megállítani az ellenfél támadóit, és szükség esetén veszélyes zónából felszabadítani. A csapatutasításokban beállított védővonalhoz igazodik, nem lép ki sem előre, sem hátra.",
     ["Szerelés", "Emberfogás", "Helyezkedés", "Fejjáték", "Koncentráció"],
     ["bármely IP CB-szerep"], [], "nyelvi fájl")
role("cb", "OOP", "CCB", "Covering Centre-Back", "biztosító középhátvéd",
     RCB, [(42, 89, 42, 94, 'oop')], (42, 91, 9, 6),
     "Óvatosabb védő: tartja a vonalat, kicsit mélyebben helyezkedik, és megvárja, merre mozdul a támadó. Gyors csatárok ellen és magas védővonalnál ő a biztonsági háló. Gyorsaság kell hozzá, és mivel hátrébb áll, nehezebb a les­csapda.",
     ["Előrelátás", "Helyezkedés", "Gyorsaság", "Koncentráció", "Emberfogás"],
     ["Stopping CB párja", "magas védővonal", "Sweeper Keeper"], ["két Covering CB (a középpálya és a védelem közti rés nő)"], "nyelvi fájl, Mastering FM")
role("cb", "OOP", "SCB", "Stopping Centre-Back", "kilépő középhátvéd",
     RCB, [(42, 89, 40, 76, 'oop')], (41, 83, 8, 9),
     "Agresszívebb védő: kilép a pozíciójából, hogy már a labda átvételekor zavarja a támadót, és a forrásnál vágja el a támadást. Visszalépő csatárok (False Nine, Deep-Lying Forward) ellen kiváló. Bátorság, agresszivitás és jó szerelés kell, mögötte pedig egy biztosító társ.",
     ["Szerelés", "Agresszivitás", "Bátorság", "Erő", "Előrelátás", "Döntéshozatal"],
     ["Covering CB párja", "Sweeper Keeper", "letámadó csapat"], ["két Stopping CB gyors csatárok ellen"], "nyelvi fájl, Mastering FM")
role("cb", "OOP", "WCB", "Wide Centre-Back", "széles középhátvéd (labda nélkül)",
     WCBR, [(50, 87, 52, 84, 'oop')], (51, 86, 8, 6),
     "A háromvédős sor szélső középhátvédjének alapviselkedése labda nélkül: az ellenfél támadóinak megállítása, a saját zóna és a szélső hátvéd mögötti terület őrzése.",
     ["Szerelés", "Helyezkedés", "Emberfogás", "Gyorsaság"],
     ["bármely IP széles CB-szerep"], [], "nyelvi fájl")
role("cb", "OOP", "CWD", "Covering Wide Centre-Back", "biztosító széles középhátvéd",
     WCBR, [(50, 87, 52, 93, 'oop')], (51, 90, 8, 6),
     "A háromvédős sor szélén óvatosan, a vonalat tartva védekezik, és a szárnyvédő mögötti teret biztosítja. Akkor jó, ha a szárnyvédőd sokat támad, és gyors ellenfél-szélső ellen kell fedezni.",
     ["Helyezkedés", "Gyorsaság", "Előrelátás", "Koncentráció"],
     ["Advanced Wing-Back előtte", "Pressing Wing-Back"], [], "nyelvi fájl")
role("cb", "OOP", "SWD", "Stopping Wide Centre-Back", "kilépő széles középhátvéd",
     WCBR, [(50, 87, 56, 74, 'oop')], (53, 81, 8, 9),
     "Kilép a pozíciójából, és agresszíven támadja a félterekben vagy a szélen labdát kapó ellenfelet. Háromvédős letámadásnál ő zárja az ellenfél belső szélsőjét.",
     ["Szerelés", "Agresszivitás", "Gyorsaság", "Bátorság", "Előrelátás"],
     ["Covering CB középen", "Holding Wing-Back"], [], "nyelvi fájl")

# ---------------- SZÉLSŐ HÁTVÉD / SZÁRNYVÉDŐ ----------------
role("fb", "IP", "FB", "Full-Back", "szélső hátvéd",
     FBR, [(60, 85, 62, 64, 'ip'), (62, 64, 64, 40, 'ip')], (61, 70, 6, 18),
     "A klasszikus szélső hátvéd: elsősorban védekező, de a hagyományos feladatai mellett átfedő futásokkal is támogatja a támadást, főleg amikor a csapatnak extra szélesség kell. Kiegyensúlyozott, biztonságos választás mindenhová.",
     ["Szerelés", "Emberfogás", "Helyezkedés", "Munkabírás", "Beadás", "Gyorsaság"],
     ["Inside Forward vagy Inside Winger előtte (ő ad szélességet)", "Winger mellé is"], [], "nyelvi fájl, Mastering FM")
role("fb", "IP", "IFB", "Inside Full-Back", "befelé húzódó szélső hátvéd",
     FBR, [(60, 85, 50, 86, 'ip')], (54, 86, 9, 6),
     "Speciális szerep: a korai építkezésnél még szélső hátvédként áll, majd ahogy a csapat feljebb jut, behúzódik, és harmadik középhátvéd lesz. Így háromfős hátsó sort ad a kontrák ellen, a szélesség viszont elveszik az adott oldalon. Igazából a 3-2-5-ös támadóalakzat egyik kulcsszerepe.",
     ["Helyezkedés", "Szerelés", "Emberfogás", "Higgadtság", "Passz", "Előrelátás"],
     ["Winger vagy Wide Forward előtte (ő adja a szélességet)", "Wing-Back a túloldalon", "Advanced CB"], ["Inside Winger előtte (az oldalon senki nem ad szélességet)"], "nyelvi fájl, Mastering FM")
role("fb", "IP", "WB", "Wing-Back", "szárnyvédő",
     WBR, [(62, 74, 64, 50, 'ip'), (64, 50, 64, 28, 'ip')], (63, 55, 5, 24),
     "A szélső hátvéd és a szélső keveréke: végig szélességet ad a támadáshoz. Mély építkezésnél a védelem mellé áll passzlehetőségnek, a támadás előrehaladtával viszont felzárkózik, és a támadó harmadban kiegészítő futásokat tesz. A Mastering Football Manager szerint széles középhátvéddel vagy erős középpályás fedezéssel működik a legjobban.",
     ["Munkabírás", "Állóképesség", "Gyorsaság", "Beadás", "Cselezés", "Szerelés", "Labda nélküli mozgás"],
     ["Inside Forward / Inside Winger előtte", "Wide Centre-Back mögötte", "Wide Covering CM"], ["Winger közvetlenül előtte (ugyanazt a sávot foglalják)"], "nyelvi fájl, Mastering FM")
role("fb", "IP", "IWB", "Inside Wing-Back", "befelé húzódó szárnyvédő",
     FBR, [(60, 85, 56, 74, 'ip'), (56, 74, 44, 70, 'ip')], (50, 74, 10, 8),
     "A támadás előrehaladtával középre húzódik, segíti a középső passzhálózatot, és fontos védelmet ad a középen indított kontrák ellen. Labdával gyakorlatilag középpályás (Nico O'Reilly a Manchester Citynél balhátvédből húzódik védekező középpályásba). A régi Inverted Wing-Back utódja.",
     ["Passz", "Első érintés", "Döntéshozatal", "Helyezkedés", "Technika", "Csapatjáték"],
     ["Winger vagy Wide Forward előtte", "Overlapping CB mögötte", "egyedüli DM mellé"], ["Inside Winger előtte", "zsúfolt középpálya két DM-mel"], "nyelvi fájl, SI hivatalos")
role("fb", "IP", "PWB", "Playmaking Wing-Back", "játékszervező szárnyvédő",
     FBR, [(60, 85, 54, 72, 'ip'), (54, 72, 44, 64, 'ip'), (44, 64, 36, 40, 'ip')], (50, 70, 11, 10),
     "Az Inside Wing-Backhez hasonlóan középre húzódik, de a fő feladata a kreatív játék: progresszív passzok, kiugratások, veszélyes beadások. A szárnyvédő-pozícióból irányít, ezért magas technikai szint kell hozzá. Figyelem: a PWB rövidítés a labda nélküli Pressing Wing-Backet is jelöli.",
     ["Passz", "Látás", "Technika", "Első érintés", "Döntéshozatal", "Beadás"],
     ["Winger vagy Wide Forward előtte", "Screening DM"], ["még egy játékmester ugyanazon az oldalon"], "nyelvi fájl, FM Scout")
role("fb", "IP", "AWB", "Advanced Wing-Back", "előretolt szárnyvédő",
     WBR, [(62, 74, 64, 56, 'ip'), (64, 56, 64, 24, 'ip')], (63, 44, 5, 22),
     "Agresszívebb szárnyvédő: a mély építkezésnél sem lép vissza a védők mellé, hanem eleve magasan, szélső középpályásként helyezkedik, majd a támadó harmadban is felzárkózik. Gyakorlatilag szélső. Mögötte kell egy széles középhátvéd vagy egy szélre kisegítő középpályás.",
     ["Gyorsaság", "Állóképesség", "Munkabírás", "Beadás", "Cselezés", "Labda nélküli mozgás"],
     ["Wide Centre-Back / Overlapping CB mögötte", "Inside Forward előtte", "Wide Covering CM"], ["négyvédős rendszer biztosítás nélkül"], "nyelvi fájl, SI hivatalos")
role("fb", "OOP", "FB", "Full-Back", "szélső hátvéd (labda nélkül)",
     FBR, [(60, 85, 58, 86, 'oop')], (59, 84, 6, 7),
     "Labda nélkül a szélső hátvéd fő dolga a szélső zóna védelme a védővonal részeként. A vonalhoz igazodik, és a saját szélsőjével közösen zárja az oldalt.",
     ["Szerelés", "Emberfogás", "Helyezkedés", "Gyorsaság", "Koncentráció"],
     ["bármely IP FB-szerep"], [], "nyelvi fájl")
role("fb", "OOP", "HFB", "Holding Full-Back", "visszatartott szélső hátvéd",
     FBR, [(60, 85, 60, 92, 'oop')], (60, 89, 6, 6),
     "Amikor a csapat magasan védekezik, ő mélyebben marad, hogy a direkt, hosszú labdák ellen plusz védelmet adjon. Egyfajta biztosítás a magas letámadás mögött.",
     ["Helyezkedés", "Előrelátás", "Gyorsaság", "Koncentráció"],
     ["magas letámadás", "Pressing Full-Back a túloldalon"], ["mély blokk (ott nincs értelme)"], "nyelvi fájl")
role("fb", "OOP", "PFB", "Pressing Full-Back", "letámadó szélső hátvéd",
     FBR, [(60, 85, 62, 66, 'oop')], (61, 75, 6, 11),
     "Aktívan, magasan támadja az ellenfél szélső játékosait, hogy segítse a csapat letámadását. Mögötte üres tér marad, ezért kell egy biztosító középhátvéd vagy kisegítő középpályás.",
     ["Munkabírás", "Gyorsaság", "Szerelés", "Agresszivitás", "Állóképesség"],
     ["Covering CB", "Wide Covering DM", "Inside Winger előtte"], ["lassú szélső hátvéd"], "nyelvi fájl")
role("fb", "OOP", "WB", "Wing-Back", "szárnyvédő (labda nélkül)",
     WBR, [(62, 74, 62, 84, 'oop')], (62, 79, 6, 8),
     "Labda nélkül a szárnyvédő a szélső zónákat védi; ötvédős blokkban visszaáll a védővonalba.",
     ["Munkabírás", "Gyorsaság", "Szerelés", "Helyezkedés"], ["bármely IP WB-szerep"], [], "nyelvi fájl")
role("fb", "OOP", "HWB", "Holding Wing-Back", "visszatartott szárnyvédő",
     WBR, [(62, 74, 60, 88, 'oop')], (61, 84, 6, 7),
     "Mélyebben marad, amikor a csapat magasan védekezik, és ötvédős sort alkot a hosszú labdák ellen. 5-3-2-ben és 5-4-1-ben a stabilitás alapja.",
     ["Helyezkedés", "Előrelátás", "Gyorsaság", "Koncentráció"],
     ["5-3-2 / 5-4-1", "Stopping Wide CB"], [], "nyelvi fájl")
role("fb", "OOP", "PWB", "Pressing Wing-Back", "letámadó szárnyvédő",
     WBR, [(62, 74, 62, 54, 'oop')], (62, 64, 6, 11),
     "Agresszíven, magasan támadja az ellenfél szélső embereit, a 3-4-3-as gegenpressing egyik motorja. Mögötte a széles középhátvédnek kell biztosítania.",
     ["Munkabírás", "Állóképesség", "Gyorsaság", "Agresszivitás", "Szerelés"],
     ["Covering Wide CB mögötte", "3-4-3 letámadás"], [], "nyelvi fájl, FM Scout")

# ---------------- VÉDEKEZŐ KÖZÉPPÁLYÁS ----------------
role("dm", "IP", "DM", "Defensive Midfielder", "védekező középpályás",
     DM, [(34, 75, 34, 66, 'ip')], (34, 74, 9, 7),
     "Fő feladata a védelem előtti helyezkedés és a kontrák elleni védelem; labdával egyszerű passzokkal a védelem és a támadás közötti összekötő. A Mastering Football Manager szerint ez is „üres vászon” szerep: kevés kötött utasítás, szabadon alakíthatod.",
     ["Helyezkedés", "Előrelátás", "Szerelés", "Passz", "Csapatjáték", "Koncentráció"],
     ["Box-to-Box Midfielder", "Midfield Playmaker", "Channel Midfielder"], [], "nyelvi fájl, Mastering FM")
role("dm", "IP", "DLP", "Deep-Lying Playmaker", "mélyen játszó irányító",
     DM, [(34, 75, 34, 72, 'ip'), (34, 72, 58, 40, 'ip'), (34, 72, 26, 34, 'ip')], (34, 73, 9, 7),
     "A védelem és a középpálya közötti térben dolgozik, és pontos passzokkal indítja a támadásokat a feljebb álló játékosok felé. Bár elsősorban kreatív, védekezni is tudnia kell, mert labdavesztéskor ő a legmélyebb középpályás. Középső középpályásként is választható. A Regista és az Anchor ma ennek és a DM-szerepnek a párosításából rakható össze.",
     ["Passz", "Látás", "Előrelátás", "Higgadtság", "Döntéshozatal", "Technika", "Első érintés"],
     ["Box-to-Box Midfielder", "Channel Midfielder", "Screening DM (OOP)", "Target Forward / Poacher a hosszú passzaihoz"], ["két DLP egymás mellett"], "nyelvi fájl, Mastering FM")
role("dm", "IP", "HB", "Half Back", "félhátvéd",
     DM, [(34, 75, 34, 88, 'ip')], (34, 82, 7, 9),
     "Védekező középpályás, aki az építkezésnél visszalép a két középhátvéd közé, így háromfős hátsó sort alkot. Ez ellenállóbbá teszi a csapatot a két csatárral letámadó ellenfelek ellen, és a Salida Lavolpiana (La Volpe, majd Guardiola) alapja. Oldalsó DM-pozícióban a középhátvédek mellé lép jobb/bal középhátvédnek.",
     ["Helyezkedés", "Passz", "Higgadtság", "Előrelátás", "Döntéshozatal", "Szerelés"],
     ["két középhátvéd", "Wing-Back mindkét oldalon", "Ball-Playing GK", "Midfield Playmaker előtte"], ["háromvédős rendszer (négy védő lesz hátul)", "Inside Full-Back (túl sok ember hátul)"], "nyelvi fájl, Mastering FM")
role("dm", "OOP", "DM", "Defensive Midfielder", "védekező középpályás (labda nélkül)",
     DM, [(34, 75, 34, 78, 'oop')], (34, 76, 9, 6),
     "Labda nélkül a védelem előtt helyezkedik, a kontrák első megállítója. Kiegyensúlyozott: nem lép ki feltűnően, és nem is süllyed a védelembe.",
     ["Helyezkedés", "Előrelátás", "Szerelés", "Munkabírás"], ["bármely IP DM-szerep"], [], "nyelvi fájl")
role("dm", "OOP", "DDM", "Dropping Defensive Midfielder", "visszalépő védekező középpályás",
     DM, [(34, 75, 34, 87, 'oop')], (34, 82, 7, 8),
     "Ha a csapat beszorul, visszalép a védővonalba, és plusz középhátvéd lesz. Mély blokknál ötvédős sort csinál a négyből, és a tizenhatos előtti beadásoknál is hasznos.",
     ["Helyezkedés", "Fejjáték", "Szerelés", "Emberfogás", "Koncentráció"],
     ["mély blokk", "Half Back (IP)"], ["magas letámadás"], "nyelvi fájl")
role("dm", "OOP", "PDM", "Pressing Defensive Midfielder", "letámadó védekező középpályás",
     DM, [(34, 75, 34, 60, 'oop')], (34, 68, 8, 9),
     "Gyakrabban lép előre a pozíciójából, hogy támogassa a csapat magasabb letámadását (a hivatalos bemutató példája a Brighton-os Carlos Baleba). Mögötte gyakran rés marad, ezért magas védővonal és jó középhátvédek kellenek mellé.",
     ["Munkabírás", "Agresszivitás", "Állóképesség", "Szerelés", "Gyorsulás"],
     ["Box-to-Box Playmaker (IP)", "magas letámadás", "Stopping CB"], ["mély blokk", "egyedüli DM gyenge középhátvédekkel"], "nyelvi fájl, SI hivatalos")
role("dm", "OOP", "SDM", "Screening Defensive Midfielder", "szűrő védekező középpályás",
     DM, [(34, 75, 28, 76, 'oop'), (34, 75, 40, 76, 'oop')], (34, 76, 10, 5),
     "Tartja a középhátvédek előtti zónát, és lezárja a passzsávokat; ritkán lép ki letámadni. Ez a régi Anchor viselkedése. Akkor a legjobb, ha előtte két mozgékony középpályás dolgozik.",
     ["Helyezkedés", "Előrelátás", "Koncentráció", "Csapatjáték", "Szerelés"],
     ["Deep-Lying Playmaker (IP)", "Channel Midfielder", "Midfield Playmaker"], ["magas letámadás, ahol mindenki kilép (üres tér keletkezik előtte)"], "nyelvi fájl, Mastering FM")
role("dm", "OOP", "WDM", "Wide Covering Defensive Midfielder", "szélre kisegítő védekező középpályás",
     DM, [(34, 75, 54, 80, 'oop')], (45, 77, 13, 6),
     "Oldalra húzódik, és duplázza a szélső hátvédet a széli veszélyek ellen. Akkor válaszd, ha az adott oldalon a szélső fent marad kontrára (Outlet), vagy a szárnyvédő sokat támad.",
     ["Munkabírás", "Gyorsaság", "Helyezkedés", "Szerelés", "Előrelátás"],
     ["Wide Outlet Winger / Wide Outlet WM az oldalon", "Advanced Wing-Back"], [], "nyelvi fájl, FM Scout")

# ---------------- KÖZÉPSŐ KÖZÉPPÁLYÁS ----------------
role("cm", "IP", "CM", "Central Midfielder", "középső középpályás",
     CMR, [(44, 61, 44, 50, 'ip'), (44, 61, 44, 70, 'ip')], (44, 60, 8, 12),
     "Szorgalmas, sokoldalú összekötő a védelem és a támadás között; a pálya közepén sokféle feladatot ellát, szükség szerint védekezik vagy támad. Taktikai intelligencia és technikai tudás kell hozzá. Az „üres vászon” középpályás szerep, amelyet egyéni utasításokkal formálhatsz.",
     ["Passz", "Döntéshozatal", "Munkabírás", "Csapatjáték", "Első érintés", "Előrelátás"],
     ["bármely más középpályás szerep mellé"], [], "nyelvi fájl, The Art of FM")
role("cm", "IP", "DLP", "Deep-Lying Playmaker", "mélyen játszó irányító (CM)",
     (40, 66), [(40, 66, 40, 70, 'ip'), (40, 70, 60, 36, 'ip')], (40, 67, 8, 7),
     "Középső középpályásként is választható. Ugyanaz a feladata, mint DM-ként: a középpálya alsó részében várja a labdát, és pontos, hosszú vagy vonalbontó passzokkal indít. Kétfős középpályában a párja legyen dinamikus (Box-to-Box vagy Channel Midfielder).",
     ["Passz", "Látás", "Higgadtság", "Döntéshozatal", "Technika"],
     ["Box-to-Box Midfielder", "Channel Midfielder"], ["Midfield Playmaker párban (két irányító, nincs futó)"], "nyelvi fájl")
role("cm", "IP", "BBM", "Box-To-Box Midfielder", "box-to-box középpályás",
     CMR, [(44, 61, 44, 70, 'ip'), (44, 61, 40, 24, 'ip')], (43, 48, 7, 24),
     "Kifogyhatatlan dinamizmus: az építkezésnél védekező középpályásként passzlehetőséget ad, a támadás késői szakaszában viszont előretör, és támadó középpályásként érkezik a tizenhatosba beadásokra, visszagurításokra, vagy a tizenhatos elől lő. Hatalmas munkabírás és állóképesség kell hozzá. A könyv szavaival a középpálya igáslova.",
     ["Munkabírás", "Állóképesség", "Labda nélküli mozgás", "Passz", "Távoli lövés", "Szerelés"],
     ["Deep-Lying Playmaker", "Screening DM", "Target Forward"], ["Channel Midfielder ugyanazon az oldalon"], "nyelvi fájl, Mastering FM")
role("cm", "IP", "BBP", "Box-To-Box Playmaker", "box-to-box irányító",
     CMR, [(44, 61, 40, 68, 'ip'), (40, 68, 40, 36, 'ip')], (42, 54, 8, 18),
     "A csapat szívverése: mély és előretolt területeken is kreatív kiindulópont. Az építkezésnél visszalép a labdáért, a támadó harmadban pedig ő adja az utolsó szikrát. A régi Segundo Volante labdás oldalának örököse; védekező középpályásként is beállítható. Sok futás és sok labdaérintés egyszerre: magas állóképesség kell.",
     ["Passz", "Látás", "Állóképesség", "Munkabírás", "Technika", "Döntéshozatal"],
     ["Pressing DM (OOP)", "Channel Midfielder a túloldalon", "Screening DM"], ["még egy irányító ugyanabban a sávban"], "nyelvi fájl, FM Scout")
role("cm", "IP", "CHM", "Channel Midfielder", "sávokba futó középpályás",
     CMR, [(44, 61, 52, 46, 'ip'), (52, 46, 56, 26, 'ip')], (51, 44, 8, 18),
     "Támogató futásokat tesz a széles zónák felé, és összekapcsolódik a csapat szélső támadóival. Mélységi futásokkal a védelem mögötti sávokba (csatornákba) indul, beadási pozícióba kerül, és belső átfedéssel (underlap) segíti a szélső társát. Gyakorlatilag a Mezzala utódja. A legjobb párja egy szélen maradó Winger, a túloldali vagy mögötte álló társ pedig egy tartó középpályás.",
     ["Labda nélküli mozgás", "Munkabírás", "Gyorsulás", "Cselezés", "Passz", "Befejezés"],
     ["Winger vagy Wide Forward előtte (ő tartja a szélességet)", "Screening DM / DLP mögötte", "Full-Back az oldalon"], ["Inside Forward vagy Inside Winger ugyanazon az oldalon (túlzsúfolt félterület)"], "nyelvi fájl, Mastering FM, Passion4FM")
role("cm", "IP", "MPM", "Midfield Playmaker", "középpályás irányító",
     CMR, [(44, 61, 40, 60, 'ip'), (40, 60, 38, 42, 'ip'), (38, 42, 58, 30, 'ip')], (40, 52, 8, 14),
     "Kreatív összekötő a védelem és a támadás között: progresszív passzokkal és gólpasszokkal indítja a támadásokat. Az építkezésnél középen, elérhető helyen mutatkozik a társainak, a támadó harmadban pedig feljebb lép, és szinte támadó középpályásként dolgozik. A régi Advanced Playmaker és Deep-Lying Playmaker keveréke, és azonnal tud védekezésből támadásba váltani.",
     ["Passz", "Látás", "Technika", "Döntéshozatal", "Első érintés", "Higgadtság", "Előrelátás"],
     ["Pressing CM vagy Screening DM mellé", "Channel Midfielder", "futó csatár (Poacher, Channel Forward)"], ["még egy előretörő középpályás (Box-to-Box, Channel) védekező fedezet nélkül"], "nyelvi fájl, Passion4FM")
role("cm", "IP", "WCM", "Wide Central Midfielder", "széles középső középpályás",
     CMR, [(44, 61, 54, 62, 'ip'), (54, 62, 56, 50, 'ip')], (52, 59, 8, 9),
     "Kétfős vagy háromfős középpálya oldalsó tagja: szorgalmas, sokoldalú összekötő, aki a hagyományos középpályásnál szélesebben helyezkedik. Így ő a jó célpont az átlós passzokra és a játékoldal-váltásokra, amelyekkel ki lehet kerülni az ellenfél letámadását. Ne keverd a Wide Covering CM-mel, amely labda nélküli szerep, de ugyanaz a rövidítése (WCM).",
     ["Passz", "Munkabírás", "Első érintés", "Helyezkedés", "Csapatjáték", "Állóképesség"],
     ["Inside Winger vagy Inside Forward előtte", "Inside Wing-Back mögötte"], ["Winger és Wing-Back ugyanazon az oldalon (három ember a vonalon)"], "nyelvi fájl, SI hivatalos")
role("cm", "OOP", "CM", "Central Midfielder", "középső középpályás (labda nélkül)",
     CMR, [(44, 61, 44, 66, 'oop')], (44, 63, 8, 7),
     "Labda nélkül a középpálya-blokk része: a csapatutasítások szerint zárja a középső területeket, nem lép ki feltűnően.",
     ["Helyezkedés", "Munkabírás", "Csapatjáték", "Szerelés"], ["bármely IP CM-szerep"], [], "nyelvi fájl")
role("cm", "OOP", "PCM", "Pressing Central Midfielder", "letámadó középső középpályás",
     CMR, [(44, 61, 42, 46, 'oop')], (43, 54, 7, 10),
     "Gyakrabban lép előre a pozíciójából, hogy támogassa a csapat feljebb induló letámadását. 4-3-3-ban egy CM kilépésével 4-4-2-es letámadó alakzat jön létre. Mögötte szűrő DM kell.",
     ["Munkabírás", "Állóképesség", "Agresszivitás", "Gyorsulás", "Szerelés"],
     ["Midfield Playmaker (IP)", "Screening DM mögötte"], ["két Pressing CM és Pressing DM egyszerre"], "nyelvi fájl, FM Scout")
role("cm", "OOP", "SCM", "Screening Central Midfielder", "szűrő középső középpályás",
     CMR, [(44, 61, 40, 68, 'oop')], (42, 65, 8, 6),
     "A helyén marad, és a középső passzsávokat zárja. Kétfős középpálya esetén ő a „tartó” ember, amikor a párja kilép letámadni.",
     ["Helyezkedés", "Előrelátás", "Koncentráció", "Csapatjáték"],
     ["Pressing CM párja", "Box-to-Box Playmaker"], [], "nyelvi fájl")
role("cm", "OOP", "WCM", "Wide Covering Central Midfielder", "szélre kisegítő középső középpályás",
     CMR, [(44, 61, 58, 70, 'oop')], (51, 66, 10, 7),
     "Elmozdul a megszokott pozíciójából, és a szélen segíti a csapatot a széli veszélyek ellen, gyakorlatilag duplázza a szélső hátvédet. A régi Carrilero védekező oldala. Akkor nagyon fontos, ha az adott oldalon támadó szárnyvédő vagy fent maradó szélső játszik.",
     ["Munkabírás", "Állóképesség", "Helyezkedés", "Szerelés", "Gyorsaság"],
     ["Advanced Wing-Back az oldalon", "Wide Outlet Winger előtte"], [], "nyelvi fájl, Mastering FM")

# ---------------- SZÉLSŐ KÖZÉPPÁLYÁS ----------------
role("wm", "IP", "WM", "Wide Midfielder", "szélső középpályás",
     WMR, [(61, 57, 60, 44, 'ip'), (60, 44, 40, 20, 'ip')], (60, 52, 6, 11),
     "Mélyebbről támogatja a támadást, mint egy klasszikus szélső. Ahelyett, hogy le akarná győzni a hátvédet, és ki akarna jutni az alapvonalig, mélyről ad veszélyes passzokat és beadásokat; inkább a technikájában bízik, mint a cselezésben és a gyorsaságban. 4-4-2-ben sokoldalú, megbízható választás.",
     ["Beadás", "Passz", "Munkabírás", "Csapatjáték", "Technika", "Állóképesség"],
     ["Wing-Back vagy Full-Back mögötte", "Target Forward a beadásokhoz"], [], "nyelvi fájl, Mastering FM")
role("wm", "IP", "W", "Winger", "szélső (középpályán)",
     WMR, [(61, 57, 64, 30, 'ip'), (64, 30, 46, 14, 'ip')], (62, 40, 5, 20),
     "Klasszikus szélső a középpálya-sorban: a vonalon marad, sebességgel vagy cselekkel győzi le a hátvédet, és beadja a labdát. Széthúzza az ellenfél védelmét, így középen több hely lesz.",
     ["Gyorsaság", "Gyorsulás", "Cselezés", "Beadás", "Technika", "Mozgékonyság"],
     ["Full-Back vagy Inside Full-Back mögötte", "Target Forward, Poacher"], ["Wing-Back közvetlenül mögötte átfedés nélküli szerep nélkül"], "nyelvi fájl, Mastering FM")
role("wm", "IP", "IW", "Inside Winger", "befelé húzódó szélső (középpályán)",
     WMR, [(61, 57, 50, 40, 'ip')], (54, 46, 8, 12),
     "Támadáskor gyakran befelé, a félterekbe húzódik, középen kap labdát, és teret nyit a szélen az átfedő társnak. Közelebbről ad veszélyes passzokat és beadásokat, mint egy hagyományos szélső. Akkor működik a legjobban, ha mögötte a vonalat tartó szélső hátvéd vagy szárnyvédő játszik.",
     ["Cselezés", "Passz", "Technika", "Döntéshozatal", "Első érintés", "Látás"],
     ["Wing-Back / Advanced Wing-Back mögötte", "Full-Back átfedéssel"], ["Inside Full-Back mögötte", "Channel Midfielder ugyanazon az oldalon"], "nyelvi fájl")
role("wm", "IP", "PW", "Playmaking Winger", "játékszervező szélső",
     WMR, [(61, 57, 60, 46, 'ip'), (60, 46, 46, 42, 'ip')], (54, 48, 9, 10),
     "A csapat fő kreatív forrása: szélesről indul az építkezésnél, majd befelé húzódik, és a félterekből ad gólpasszokat. A szélről befelé lépve elkerüli a középpálya tömegét, és szabad tereket talál. A régi Wide Playmaker utódja; a könyv szerint pusztító lehet, de el is szigetelődhet.",
     ["Passz", "Látás", "Technika", "Döntéshozatal", "Első érintés", "Higgadtság"],
     ["Wing-Back átfedéssel", "futó csatár", "Channel Midfielder a túloldalon"], ["Midfield Playmaker ugyanazon az oldalon"], "nyelvi fájl, Mastering FM")
role("wm", "OOP", "WMF", "Wide Midfielder", "szélső középpályás (labda nélkül)",
     WMR, [(61, 57, 60, 66, 'oop')], (60, 62, 6, 7),
     "Egyensúlyt tart: védelmet ad a széli veszélyek ellen, de úgy helyezkedik, hogy labdaszerzés után indíthassa a kontrát.",
     ["Munkabírás", "Helyezkedés", "Szerelés"], ["bármely IP széles középpályás-szerep"], [], "nyelvi fájl")
role("wm", "OOP", "TWM", "Tracking Wide Midfielder", "visszazáró szélső középpályás",
     WMR, [(61, 57, 60, 82, 'oop')], (60, 70, 6, 13),
     "Az ellenfél előrenyomulásakor visszakövet a saját védekező harmadába, és segíti a mögötte álló védőket; időnként a védővonalba is beáll, mint egy extra védő. Mély, 4-4-2-es vagy 5-4-1-es blokkhoz ideális.",
     ["Munkabírás", "Állóképesség", "Szerelés", "Emberfogás", "Helyezkedés"],
     ["mély blokk", "Full-Back mögötte"], [], "nyelvi fájl")
role("wm", "OOP", "OWM", "Wide Outlet Wide Midfielder", "fent maradó szélső középpályás",
     WMR, [(61, 57, 62, 48, 'oop')], (61, 52, 6, 7),
     "Kevésbé segít vissza a szélső hátvédnek, inkább tartja a pozícióját, hogy labdaszerzés után veszélyes helyről indíthassa a kontrát. Mögötte kell egy szélre kisegítő középpályás.",
     ["Gyorsaság", "Gyorsulás", "Labda nélküli mozgás", "Cselezés"],
     ["Wide Covering DM / CM", "kontrajáték"], ["Pressing Full-Back mögötte"], "nyelvi fájl")

# ---------------- TÁMADÓ KÖZÉPPÁLYÁS ----------------
role("am", "IP", "AM", "Attacking Midfielder", "támadó középpályás",
     AM, [(34, 40, 28, 34, 'ip'), (34, 40, 40, 32, 'ip')], (34, 37, 9, 7),
     "Támadó szerep az ellenfél védelmi és középpályás vonala között: amennyire csak lehet, a szabad zsebekben kér labdát. Kiváló passz, cselezés és lövés kell hozzá, hogy folyamatosan helyzeteket teremtsen magának és a többieknek. Szintén „üres vászon” szerep: utasításokkal Advanced Playmaker-szerűre vagy árnyékcsatár-szerűre is formálhatod.",
     ["Passz", "Technika", "Cselezés", "Távoli lövés", "Labda nélküli mozgás", "Döntéshozatal"],
     ["Centre Forward", "Inside Forward a széleken"], [], "nyelvi fájl, Mastering FM")
role("am", "IP", "AP", "Advanced Playmaker", "előretolt irányító",
     AM, [(34, 40, 30, 38, 'ip'), (30, 38, 30, 16, 'ip'), (30, 38, 54, 20, 'ip')], (32, 38, 9, 7),
     "Kreatív szerep magasan, az ellenfél középpályája és védelme között. Elsősorban a társainak teremt helyzeteket, gólpasszokkal. Ma ide tartozik a régi Enganche és Trequartista öröksége is (ezeket az FM26 megszüntette). Futók kellenek körülötte, különben könnyen kivehető a játékból.",
     ["Passz", "Látás", "Technika", "Első érintés", "Döntéshozatal", "Higgadtság"],
     ["Poacher, Channel Forward", "Inside Forward", "Channel Midfielder"], ["Deep-Lying Forward / False Nine (ugyanazt a zsebet foglalják)"], "nyelvi fájl, A fordított piramis")
role("am", "IP", "FR", "Free Role", "szabad szerep",
     AM, [(34, 40, 18, 36, 'ip'), (34, 40, 50, 30, 'ip'), (34, 40, 34, 56, 'ip')], (34, 40, 18, 12),
     "Teljes alkotói szabadság: elhagyhatja a pozícióját, hogy támadási lehetőségeket teremtsen, és több kockázatot vállalhat a labdával, hogy gólt szerezzen vagy készítsen elő. Kevésbé követi a csapatutasításokat, és néha megbontja a szerkezetet, de kiszámíthatatlansága feltöri a zárt védelmet. Csak igazi sztárnak add.",
     ["Látás", "Technika", "Cselezés", "Excentricitás", "Passz", "Labda nélküli mozgás"],
     ["Channel Forward", "Screening DM", "fegyelmezett szélsők"], ["több Free Role vagy Outlet szerep egyszerre"], "nyelvi fájl")
role("am", "IP", "SS", "Second Striker", "második csatár",
     AM, [(34, 40, 34, 34, 'ip'), (34, 34, 36, 14, 'ip')], (34, 28, 7, 14),
     "A csapat egyik fő gólveszélye. A támadás elején a vonalak között helyezkedik, ahogy azonban a labda a támadó harmadba ér, agresszíven felzárkózik a csatársorba, és gólszerző helyzetbe kerül. Leginkább egyedüli csatárral használják (a régi Shadow Striker utódja).",
     ["Labda nélküli mozgás", "Befejezés", "Gyorsulás", "Előrelátás", "Higgadtság"],
     ["False Nine vagy Deep-Lying Forward", "Target Forward"], ["Poacher (két ember ugyanazon a ponton)"], "nyelvi fájl, Mastering FM")
role("am", "OOP", "AM", "Attacking Midfielder", "támadó középpályás (labda nélkül)",
     AM, [(34, 40, 34, 48, 'oop')], (34, 44, 8, 6),
     "Labda nélkül a pálya középső területeit védi, gyakran az a feladata, hogy elzárja az ellenfél középpályás pivotjait a labdától.",
     ["Munkabírás", "Előrelátás", "Helyezkedés"], ["4-2-3-1, 4-4-1-1"], [], "nyelvi fájl")
role("am", "OOP", "TAM", "Tracking Attacking Midfielder", "visszazáró támadó középpályás",
     AM, [(34, 40, 34, 64, 'oop')], (34, 52, 7, 13),
     "Az ellenfél előretörésekor visszakövet, és mélyebb védekező pozícióba áll; 4-2-3-1-ből így 4-5-1 lesz. Kontrára építő, mély blokkos taktika alapja.",
     ["Munkabírás", "Állóképesség", "Helyezkedés", "Szerelés"],
     ["mély blokk", "Central Outlet CF"], [], "nyelvi fájl")
role("am", "OOP", "OAM", "Central Outlet Attacking Midfielder", "fent maradó támadó középpályás",
     AM, [(34, 40, 34, 34, 'oop')], (34, 37, 7, 5),
     "Kevésbé segít vissza, inkább tartja a középső, magas pozícióját, hogy labdaszerzés után azonnal indíthassa a kontrát. Középen mögötte biztosítás kell (két DM).",
     ["Labda nélküli mozgás", "Gyorsulás", "Higgadtság", "Passz"],
     ["két védekező középpályás", "Channel Forward"], [], "nyelvi fájl")
role("am", "OOP", "SAM", "Splitting Outlet Attacking Midfielder", "kiszélesedő fent maradó támadó középpályás",
     AM, [(34, 40, 48, 32, 'oop')], (41, 36, 9, 6),
     "Még magasabb pozíciót tart, és a csatornák felé húzódik, hogy széles kontrák kiindulópontja legyen. Kontrás csapat fegyvere.",
     ["Gyorsaság", "Labda nélküli mozgás", "Cselezés"],
     ["Wide Covering DM", "Centre Forward középen"], [], "nyelvi fájl")

# ---------------- SZÉLSŐ TÁMADÓ ----------------
role("w", "IP", "W", "Winger", "szélső",
     WR, [(60, 37, 64, 18, 'ip'), (64, 18, 44, 12, 'ip')], (62, 28, 5, 14),
     "Végig szélességet ad a támadásban: az oldalvonal közeléből támad, széthúzza az ellenfél védelmét, és veszélyes passzokkal, beadásokkal szolgálja ki a csatárokat. A széles helyezkedés miatt gyakran kerül egy az egy elleni helyzetbe a hátvéddel, ahol a cselezőtudása érvényesül.",
     ["Gyorsaság", "Gyorsulás", "Cselezés", "Beadás", "Technika", "Mozgékonyság"],
     ["Inside Full-Back / Full-Back mögötte", "Channel Midfielder", "Target Forward"], ["Wing-Back mögötte (két ember a vonalon)"], "nyelvi fájl, Mastering FM")
role("w", "IP", "IW", "Inside Winger", "befelé húzódó szélső",
     WR, [(60, 37, 48, 30, 'ip'), (48, 30, 40, 16, 'ip')], (52, 30, 8, 10),
     "Gyakran befelé, a félterekbe sodródik, hogy középen kapjon labdát, és teret nyisson a szélen az átfedő társának. Közelebbről ad veszélyes passzokat és beadásokat, mint egy hagyományos szélső. A régi Inverted Winger utódja; jellemzően fordított lábas játékos.",
     ["Cselezés", "Passz", "Technika", "Látás", "Döntéshozatal", "Távoli lövés"],
     ["Wing-Back / Advanced Wing-Back mögötte", "Pressing Full-Back (OOP)", "Deep-Lying Forward"], ["Channel Midfielder ugyanazon az oldalon", "Inside Full-Back mögötte"], "nyelvi fájl, The Art of FM")
role("w", "IP", "IF", "Inside Forward", "belső csatár",
     WR, [(60, 37, 50, 28, 'ip'), (50, 28, 42, 12, 'ip')], (50, 25, 9, 12),
     "Szélső szerep, amely a támadás során befelé, a félterekbe húzódik, hogy teret nyisson az átfedő szélső hátvédnek. Elsősorban mégis támadó: az ellenfél védelme mögötti teret támadja, és gólhelyzetbe kerül (Szalah, Son). A könyv szerint visszalépő csatárral párosítva a legjobb: ő fut be a csatár által hagyott helyre.",
     ["Befejezés", "Labda nélküli mozgás", "Gyorsulás", "Cselezés", "Higgadtság", "Gyorsaság"],
     ["Wing-Back / Full-Back átfedéssel", "Deep-Lying Forward / False Nine", "Target Forward"], ["Channel Midfielder vagy Inside Wing-Back ugyanazon az oldalon"], "nyelvi fájl, Mastering FM, The Art of FM")
role("w", "IP", "PW", "Playmaking Winger", "játékszervező szélső",
     WR, [(60, 37, 58, 32, 'ip'), (58, 32, 46, 30, 'ip'), (46, 30, 30, 14, 'ip')], (53, 32, 9, 7),
     "Szélesről indul, majd befelé lépve keres teret, ahonnan gólpasszt adhat. A támadó harmadban a csapat elsődleges kreatív forrása lehet.",
     ["Passz", "Látás", "Technika", "Cselezés", "Döntéshozatal"],
     ["Wing-Back átfedéssel", "Poacher", "Channel Forward"], ["Advanced Playmaker középen (két irányító egy zsebben)"], "nyelvi fájl")
role("w", "IP", "WFD", "Wide Forward", "széles csatár",
     WR, [(60, 37, 63, 22, 'ip'), (63, 22, 52, 10, 'ip')], (60, 22, 7, 12),
     "A szélsőhöz hasonlóan szélességet ad, de a fő célja a mélységi futás a védelem mögé, és a kapu, illetve a tizenhatos támadása. Gyors, gólerős szélső játékosnak való. False Nine mellett kiváló, mert ő fut be a középhátvéd mögötti térbe.",
     ["Gyorsaság", "Labda nélküli mozgás", "Befejezés", "Gyorsulás", "Cselezés"],
     ["False Nine", "Inside Full-Back / Inside Wing-Back mögötte"], ["Advanced Wing-Back mögötte"], "nyelvi fájl, FM Scout")
role("w", "OOP", "W", "Winger", "szélső (labda nélkül)",
     WR, [(60, 37, 60, 46, 'oop')], (60, 42, 6, 7),
     "Labda nélkül az alapviselkedés: visszahúzódik a középpálya-sor szélére, és az ellenfél szélső hátvédjét zavarja.",
     ["Munkabírás", "Helyezkedés"], ["bármely IP szélső-szerep"], [], "nyelvi fájl")
role("w", "OOP", "TW", "Tracking Winger", "visszazáró szélső",
     WR, [(60, 37, 60, 78, 'oop')], (60, 58, 6, 21),
     "Az ellenfél előrenyomulásakor visszakövet, és segíti a mögötte álló védőket, akár a védővonalba is beállva extra védőként. Követi az ellenfél szélső hátvédjét. Ha erős szélső hátvédű ellenfél ellen vagy vezetést tartanál, ez kell.",
     ["Munkabírás", "Állóképesség", "Szerelés", "Emberfogás", "Helyezkedés"],
     ["mély blokk", "Full-Back mögötte"], [], "nyelvi fájl")
role("w", "OOP", "WOW", "Wide Outlet Winger", "fent maradó szélső",
     WR, [(60, 37, 62, 32, 'oop')], (61, 34, 6, 5),
     "Szélesen és magasan marad, kevés védekező munkával, hogy labdaszerzés után azonnal indulhasson. Kontrás csapat széli fegyvere, mögötte azonban kisegítő középpályás kell.",
     ["Gyorsaság", "Gyorsulás", "Labda nélküli mozgás", "Cselezés"],
     ["Wide Covering DM / CM", "kontrajáték", "Channel Forward"], ["Pressing Full-Back mögötte"], "nyelvi fájl, FM Scout")
role("w", "OOP", "IOW", "Inside Outlet Winger", "befelé fent maradó szélső",
     WR, [(60, 37, 50, 32, 'oop')], (55, 34, 7, 5),
     "Fent marad kontrára, és befelé, a félterekbe húzódik, hogy a vonalak között direkt passzt kaphasson. Belső csatárhoz illő kontraszerep.",
     ["Gyorsulás", "Labda nélküli mozgás", "Előrelátás"],
     ["Inside Forward (IP)", "Wide Covering DM"], [], "nyelvi fájl")

# ---------------- CSATÁR ----------------
role("st", "IP", "CFD", "Centre Forward", "középcsatár",
     ST, [(34, 22, 34, 12, 'ip'), (34, 22, 30, 30, 'ip')], (34, 20, 8, 9),
     "A klasszikus „kilences”: vezeti a támadósort, és a támadások csúcspontja. Gólt is kell szereznie, és helyzetet is kell teremtenie. Sokoldalú, minden rendszerben működik. (A rövidítése a játékban CFD, mert a CF a régi Complete Forwardé.)",
     ["Befejezés", "Labda nélküli mozgás", "Higgadtság", "Első érintés", "Fejjáték", "Technika"],
     ["Inside Forward / Winger", "Attacking Midfielder", "Second Striker"], [], "nyelvi fájl, Mastering FM")
role("st", "IP", "DLF", "Deep-Lying Forward", "visszalépő csatár",
     ST, [(34, 22, 34, 36, 'ip'), (34, 36, 54, 24, 'ip')], (34, 29, 7, 10),
     "Fő dolga összekötni a támadást a középpályával: visszalép a vonalak közé, átveszi a mélyből érkező passzokat, majd vagy visszaadja, vagy szélre teríti, vagy ha meg tud fordulni, kiugratja a csatártársát. A Mastering Football Manager szerint a lényeg, hogy a visszalépéssel nyitott teret valaki más ki is használja.",
     ["Első érintés", "Passz", "Technika", "Erő", "Döntéshozatal", "Csapatjáték"],
     ["Poacher vagy Channel Forward párja", "Inside Forward", "Second Striker"], ["Advanced Playmaker ugyanabban a zsebben"], "nyelvi fájl, Mastering FM")
role("st", "IP", "F9", "False Nine", "hamis kilences",
     ST, [(34, 22, 34, 40, 'ip'), (34, 40, 24, 30, 'ip')], (34, 32, 9, 10),
     "Rendhagyó középcsatár: rendszeresen visszalép a vonalak közé, és Advanced Playmakerként viselkedik. A középhátvédek dilemmába kerülnek: ha követik, mögöttük tér nyílik a befutóknak, ha nem, akkor szabadon kap labdát. Hidegkuti Nándor 1953-as wembleyi játéka ennek az ősmintája. Mindenképp futókkal párosítsd.",
     ["Látás", "Passz", "Technika", "Cselezés", "Első érintés", "Labda nélküli mozgás"],
     ["Wide Forward / Inside Forward", "Second Striker", "Channel Midfielder"], ["szélesen maradó szélsők és kreatív AM (nincs, aki befusson)"], "nyelvi fájl, A fordított piramis")
role("st", "IP", "CHF", "Channel Forward", "sávokba futó csatár",
     ST, [(34, 22, 46, 14, 'ip'), (34, 22, 22, 14, 'ip')], (34, 17, 14, 7),
     "Nagy energiájú szerep: folyamatosan zavarja a védőket, és rendszeresen fut a középhátvéd és a szélső hátvéd közötti sávokba (csatornákba). Támadásban állandó futó, akinek direkt labdákat lehet küldeni a sávokba vagy a védelem mögé. Gyorsaságával és szívósságával teszteli a védelmet.",
     ["Gyorsaság", "Munkabírás", "Labda nélküli mozgás", "Gyorsulás", "Befejezés", "Elszántság"],
     ["Midfield Playmaker / Advanced Playmaker", "Free Role", "Second Striker"], [], "nyelvi fájl, FM Scout")
role("st", "IP", "P", "Poacher", "gólvadász",
     ST, [(34, 22, 36, 9, 'ip')], (35, 15, 6, 7),
     "Az utolsó védő vállán él: a védővonalat áttörve fut rá a középpályáról érkező mélységi passzokra. Kiváló labda nélküli mozgás kell, és ő a csapat fő gólforrása. A támadások építésében alig vesz részt, inkább középen marad, és a tizenhatos környékén szimatolja a lehetőséget.",
     ["Befejezés", "Labda nélküli mozgás", "Higgadtság", "Előrelátás", "Gyorsulás"],
     ["Advanced Playmaker / Midfield Playmaker", "Deep-Lying Forward", "Winger beadásokkal"], ["Second Striker (ugyanazon a ponton állnak)"], "nyelvi fájl, Mastering FM")
role("st", "IP", "TF", "Target Forward", "célcsatár",
     ST, [(34, 22, 34, 26, 'ip'), (34, 22, 36, 10, 'ip')], (34, 20, 7, 8),
     "Fizikumával és magasságával bontja meg a védelmet. Az építkezésnél ő a menekülőút: a hosszú passzok és felszabadítások célpontja, amelyeket lecsap, megcsúsztat vagy lekészít a társaknak. A támadó harmadban a beadások végére érkezik, és fejjel veszélyes.",
     ["Fejjáték", "Erő", "Ugrás", "Első érintés", "Bátorság", "Befejezés"],
     ["Inside Forward / Second Striker (a lecsorgókra)", "Winger, Wide Midfielder beadásokkal"], ["rövid, földön épülő játék, ahol nem kap labdát"], "nyelvi fájl, Mastering FM, The Art of FM")
role("st", "OOP", "CFD", "Centre Forward", "középcsatár (labda nélkül)",
     ST, [(34, 22, 34, 18, 'oop')], (34, 21, 9, 5),
     "Labda nélkül ő az első védekező vonal: a csapatutasítások szerint zavarja az ellenfél középhátvédjeit és a kapust.",
     ["Munkabírás", "Agresszivitás"], ["letámadás"], [], "nyelvi fájl")
role("st", "OOP", "TCF", "Tracking Centre Forward", "visszazáró középcsatár",
     ST, [(34, 22, 34, 46, 'oop')], (34, 34, 7, 13),
     "Visszakövet, és segíti a középpályásokat a védekezésben (a régi Pressing Forward védekező oldalának kiegészítője). Letámadó csapatnál vagy fáradt középpályánál hasznos.",
     ["Munkabírás", "Állóképesség", "Agresszivitás"], ["4-4-2 letámadás", "Second Striker (IP)"], [], "nyelvi fájl, FM Scout")
role("st", "OOP", "OCF", "Central Outlet Centre Forward", "fent maradó középcsatár",
     ST, [(34, 22, 34, 20, 'oop')], (34, 21, 6, 4),
     "Középen, magasan marad, és kevés védekező munkát végez, hogy labdaszerzés után azonnal kiindulópont legyen. A kontrázó csapat csatára.",
     ["Labda nélküli mozgás", "Erő", "Gyorsulás"], ["kontrajáték", "Tracking AM mögötte"], [], "nyelvi fájl")
role("st", "OOP", "SCF", "Splitting Outlet Centre Forward", "kiszélesedő fent maradó csatár",
     ST, [(34, 22, 48, 24, 'oop')], (41, 23, 9, 4),
     "Magasan marad, majd szélre húzódik, hogy a széles kontrák kiindulópontja legyen. Az ellenfél előretolt szélső hátvédje mögötti teret célozza.",
     ["Gyorsaság", "Labda nélküli mozgás", "Gyorsulás"], ["kontrajáték", "Channel Forward (IP)"], [], "nyelvi fájl")
