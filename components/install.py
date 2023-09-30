import subprocess
import logging
from colorama import Fore, Style, init

init()

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

def log_module(module, count, total, status):
    module_text = f"{Fore.CYAN}{module}{Style.RESET_ALL}"
    count_text = f"{Fore.WHITE}({count}/{total}){Style.RESET_ALL}"
    status_text = f"{Fore.WHITE}{status}{Style.RESET_ALL}"
    logging.info(f"{module_text} {count_text} {status_text}")

result = subprocess.run('python --version', shell=True, text=True, capture_output=True)
logging.info(f"{Fore.CYAN}{result.stdout.strip()}{Style.RESET_ALL}")

logging.info(f"{Fore.CYAN}Install script ready{Style.RESET_ALL}")
logging.info(f"{Fore.CYAN}Starting installation...{Style.RESET_ALL}")

with open('components\\scrapedata\\requirements.txt') as f:
    modules = [line.strip() for line in f]

total = len(modules)
count = 0

for module in modules:
    log_module(module, count, total, 'INSTALLING')
    command = f'pip install {module} >nul 2>nul'
    subprocess.run(command, shell=True)
    count += 1
    log_module(module, count, total, 'INSTALLED')

logging.info(f"{Fore.CYAN}Installation completed.{Style.RESET_ALL}")

logging.info(f"{Fore.CYAN}Builder ready{Style.RESET_ALL}")
logging.info(f"{Fore.CYAN}Starting builder...{Style.RESET_ALL}")
subprocess.run('python components/roseui/builder.py', shell=True)
