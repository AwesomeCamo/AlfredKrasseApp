from pymongo import *

cluster = MongoClient("mongodb+srv://Dennis:MHhRui10mongodb@cluster0.aitqo.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = cluster["Alfred-Krasse-App"]
collection1 = db["Lehrerkürzel"]
collection2 = db["Unterricht"]
collection3 = db["Ausfall"]

collection1.delete_many({})
post1 = {"_id": 0,"Kürzel": "ALL","Name": "Allman, Peter","Email":"allmann@schulebza.de"}
post2 = {"_id": 1,"Kürzel": "AND","Name": "Andres, Kirsten","Email":"kirsten.andres@schulebza.de"}
post3 = {"_id": 2,"Kürzel": "BAM","Name": "Baumeister, Birgit","Email":"gitta.baumeister@schulebza.de"}
post4 = {"_id": 3,"Kürzel": "BEI","Name": "Beinghaus, Eleonore","Email":"eleonore.beinghaus@schulebza.de"}
post5= {"_id": 4,"Kürzel": "BIB","Name": "Bibus, Christine","Email":"christine.bibus@schulebza.de"}
post6= {"_id": 5,"Kürzel": "BIA","Name": "Bingler, Anette","Email":"annette.bingler@schulebza.de"}
post7= {"_id": 6,"Kürzel": "BI","Name": "Bingler, Stefan","Email":"stefan.bingler@schulebza.de"}
post8= {"_id": 7,"Kürzel": "BIJ","Name": "Bittighofer, Jeanette","Email":"jeanette.bittighofer@schulebza.de"}
post9= {"_id": 8,"Kürzel": "BLI","Name": "Blickensdörfer, Werner","Email":"werner.blickensdoerfer@schulebza.de"}
post10= {"_id":9,"Kürzel": "BHM","Name": "Böhm, Harald","Email":"harald.boehm@schulebza.de"}
post11= {"_id":10,"Kürzel": "BS","Name": "Bornschein, Christoph","Email":"christoph.bornschein@schulebza.de"}
post12= {"_id": 11,"Kürzel": "BOT","Name": "Bott, Sabine","Email":"sabine.bott@schulebza.de"}
post13= {"_id": 12,"Kürzel": "BU","Name": "Buck, Dr. Caroline","Email":"caroline.buck@schulebza.de"}
post14= {"_id": 13,"Kürzel": "CHE","Name": "Cherfouf, Marina","Email":"marina.cherfouf@schulebza.de"}
post15= {"_id": 14,"Kürzel": "ENM","Name": "Engel, Melanie","Email":"melanie.engel@schulebza.de"}
post16= {"_id": 15,"Kürzel": "FL","Name": "Flint, Elisabeth","Email":"elisabeth.flint@schulebza.de"}
post17= {"_id": 16,"Kürzel": "GAU","Name": "Gauer, Simone","Email":"simone.gauer@schulebza.de"}
post18= {"_id": 17,"Kürzel": "GRF","Name": "Gräf, Katharina","Email":"katharina.graef@schulebza.de"}
post19= {"_id": 18,"Kürzel": "GU","Name": "Guckert-Thiede, Christine","Email":"christine.guckert-thiede@schulebza.de"}
post20= {"_id": 19,"Kürzel": "GUT","Name": "Gutschmidt, Anja","Email":"anja.gutschmidt@schulebza.de"}
post21= {"_id": 20,"Kürzel": "HIM","Name": "Himpel, Hannah","Email":"hannah.himpel@schulebza.de"}
post22= {"_id": 21,"Kürzel": "HOR","Name": "Hohlreiter, Lisa","Email":"lisa.hohlreiter@schulebza.de"}
post23= {"_id": 22,"Kürzel": "HUP","Name": "Hust, Peter","Email":"peter.hust@schulebza.de"}
post24= {"_id": 23,"Kürzel": "HU","Name": "Hust-Korspeter, Kim","Email":"kim.hust-korspeter@schulebza.de"}
post25= {"_id": 24,"Kürzel": "IM","Name": "Imhoff, Daniela","Email":"daniela.imhoff@schulebza.de"}
post26= {"_id": 25,"Kürzel": "JEN","Name": "Jenrich, Stephan","Email":"stephan.jenrich@schulebza.de"}
post27= {"_id": 26,"Kürzel": "JNG","Name": "Jung, Pascal","Email":"pascal.jung@schulebza.de"}
post28= {"_id": 27,"Kürzel": "KER","Name": "Kerner, Simone","Email":"simone.kerner@schulebza.de"}
post29= {"_id": 28,"Kürzel": "KIN","Name": "Kinzinger, Désirée","Email":"desiree.kinzinger@schulebza.de"}
post30= {"_id": 29,"Kürzel": "KLI","Name": "Kliewer, Annette Dr.","Email":"annette.kliewer@schulebza.de"}
post31= {"_id": 30,"Kürzel": "LAN","Name": "Lang, Ramona","Email":"ramona.lang@schulebza.de"}
post32= {"_id": 31,"Kürzel": "LES","Name": "Leschinger, Franz","Email":"franz.leschinger@schulebza.de"}
post33= {"_id": 32,"Kürzel": "MED","Name": "Medart, Tanja","Email":"tanja.medart@schulebza.de"}
post34= {"_id": 33,"Kürzel": "MEI","Name": "Meißner, Stefan Dr.","Email":"stefan.meissner@schulebza.de"}
post35= {"_id": 34,"Kürzel": "MOH","Name": "Mohr, Christoph","Email":"christoph.mohr@schulebza.de"}
post36= {"_id": 35,"Kürzel": "MLR","Name": "Müller, Sascha, DDr.","Email":"sascha.mueller@schulebza.de"}
post37= {"_id": 36,"Kürzel": "OHL","Name": "Ohler, Hanna","Email":"hanna.ohler@schulebza.de"}
post38= {"_id": 37,"Kürzel": "PZ","Name": "Pätzold, Olaf","Email":"olaf.paetzold@schulebza.de"}
post39= {"_id": 38,"Kürzel": "PFA","Name": "Pfaffmann, Elke","Email":"elke.pfaffmann@schulebza.de"}
post40= {"_id": 39,"Kürzel": "PIN","Name": "Pinkle, Sarina","Email":"sarina.pinkle@schulebza.de"}
post41= {"_id": 40,"Kürzel": "RO","Name": "Rohe, Gunther","Email":"gunther.rohe@schulebza.de"}
post42= {"_id": 41,"Kürzel": "ROL","Name": "Roloff, Marion","Email":"marion.roloff@schulebza.de"}
post43= {"_id": 42,"Kürzel": "SCT","Name": "Schächter, Olivier","Email":"olivier.schaechter@schulebza.de"}
post44= {"_id": 43,"Kürzel": "SCA","Name": "Schäfer, Rebekka","Email":"rebekka.schaefer@schulebza.de"}
post45= {"_id": 44,"Kürzel": "SCE","Name": "Scheidner, Sven","Email":"sven.scheidner@schulebza.de"}
post46= {"_id": 45,"Kürzel": "SJK","Name": "Schejok-Gallier, Catherine","Email":"catherine.schejok-gallier@schulebza.de"}
post47= {"_id": 46,"Kürzel": "SCK","Name": "Schik, Susanne","Email":"susanne.schik@schulebza.de"}
post48= {"_id": 47,"Kürzel": "SCU","Name": "Schilling, Ulrike Dr.","Email":"ulrike.schilling@schulebza.de"}
post49= {"_id": 48,"Kürzel": "SH","Name": "Schmidt, Theodor","Email":"theodor.schmidt@schulebza.de"}
post50= {"_id": 49,"Kürzel": "SCP","Name": "Schuppe, Rosa","Email":"rosa.schuppe@schulebza.de"}
post51= {"_id": 50,"Kürzel": "SWM","Name": "Schwamm, Anne","Email":"anne.schwamm@schulebza.de"}
post52= {"_id": 51,"Kürzel": "SCW","Name": "Schwartz, Kirstin","Email":"kirstin.schwartz@schulebza.de"}
post53= {"_id": 52,"Kürzel": "SCZ","Name": "Schwarz, Gabriele","Email":"gabriele.schwarz@schulebza.de"}
post54= {"_id": 53,"Kürzel": "SE","Name": "Seringer, Petra","Email":"petra.seringer@schulebza.de"}
post55= {"_id": 54,"Kürzel": "SPI","Name": "Spicko, Bruno","Email":"bruno.spicko@schulebza.de"}
post56= {"_id": 55,"Kürzel": "STS","Name": "Stass, Lukas","Email":"lukas.stass@schulebza.de"}
post57= {"_id": 56,"Kürzel": "STF","Name": "Steinfurth, Thomas","Email":"thomas.steinfurth@schulebza.de"}
post58= {"_id": 57,"Kürzel": "STC","Name": "Streicher, Ulrike","Email":"ulrike.streicher@schulebza.de"}
post59= {"_id": 58,"Kürzel": "TR","Name": "Traudt, Werner","Email":"werner.traudt@schulebza.de"}
post60= {"_id": 59,"Kürzel": "TU","Name": "Tuschner, Stefanie","Email":"stefanie.tuschner@schulebza.de"}
post61= {"_id": 60,"Kürzel": "VOL","Name": "Vollstedt, Markus","Email":"markus.vollstedt@schulebza.de"}
post62= {"_id": 61,"Kürzel": "WAS","Name": "Waßmer, Annette","Email":"annet.wassmer@schulebza.de"}
post63= {"_id": 62,"Kürzel": "WEB","Name": "Weber, Andrea","Email":"andrea.weber@schulebza.de"}
post64= {"_id": 63,"Kürzel": "WE","Name": "Weiser, Ralf","Email":"ralf.weiser@schulebza.de"}
post65= {"_id": 64,"Kürzel": "WMR","Name": "Wiemer, Andreas","Email":"andreas.wiemer@schulebza.de"}
post66= {"_id": 65,"Kürzel": "WI","Name": "Winker, Susanne","Email":"susanne.winker@schulebza.de"}
post67= {"_id": 66,"Kürzel": "XBA","Name": "Bastian, Jessica","Email":"jessica.bastian@schulebza.de"}
post68= {"_id": 67,"Kürzel": "XGU","Name": "Güler, Sinem","Email":"sinem.gueler@schulebza.de"}
post69= {"_id": 68,"Kürzel": "XHE","Name": "Heilmann, Lena","Email":"lena.heilmann@schulebza.de"}
post70= {"_id": 69,"Kürzel": "XKU","Name": "Kurz, Benedict","Email":"benedict.kurz@schulebza.de"}
post71= {"_id": 70,"Kürzel": "XLE","Name": "Leim, Johannes","Email":"johannes.leim@schulebza.de"}
post72= {"_id": 71,"Kürzel": "XSC","Name": "Schummers, Timo","Email":"timo.schummers@schulebza.de"}


collection1.insert_many([post1,post2,post3,post4,post5,post6,post7,post8,post9,post10,post11,post12,post13,post14,post15,post16,post17,post18,post19,post20,post21,post22,post23,post24,post25,post26,post27,post28,
                         post29,post30,post31,post32,post33,post34,post35,post36,post37,post38,post39,post40,post41,post42,post43,post44,post45,post46,post47,post48,post49,post50,post51,post52,post53,
                         post54,post55,post56,post57,post58,post59,post60,post61,post62,post63,post64,post65,post66,post67,post68,post69,post70,post71,post72])

results = collection1.find({})

counter = 0
def count_elements():
    global counter
    for i in results:
        counter+=1
    print(counter)

count_elements()




