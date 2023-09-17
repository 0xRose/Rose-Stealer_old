import subprocess
import logging
from colorama import Fore, Style, init

# Initialize colorama
init()

# Set up logging with different modules and colors
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

def log_module_status(module, count, total, status):
    module_text = f"{Fore.CYAN}{module}{Style.RESET_ALL}"
    count_text = f"{Fore.WHITE}({count}/{total}){Style.RESET_ALL}"
    status_text = f"{Fore.WHITE}{status}{Style.RESET_ALL}"
    logging.info(f"{module_text} {count_text} {status_text}")

# Log Python version
result = subprocess.run('python --version', shell=True, text=True, capture_output=True)
logging.info(f"{Fore.CYAN}{result.stdout.strip()}{Style.RESET_ALL}")

# Log installation start
logging.info(f"{Fore.CYAN}Install script ready{Style.RESET_ALL}")
logging.info(f"{Fore.CYAN}Starting installation...{Style.RESET_ALL}")

# Read modules from requirements.txt
with open('components\\scrapedata\\requirements.txt') as f:
    modules = [line.strip() for line in f]

total = len(modules)

# Initialize counters
count = 1

# Function to check and install module
def check_and_install(module):
    result = subprocess.run(f'python -c "import {module}"', shell=True, text=True, capture_output=True)
    if result.returncode != 0:
        log_module_status(module, count, total, "INSTALLING")
        subprocess.run(f'pip install {module}', shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        log_module_status(module, count, total, "INSTALLED")
    else:
        log_module_status(module, count, total, "CHECKING")

# Check and install modules
for module in modules:
    check_and_install(module)
    count += 1

logging.info(f"{Fore.CYAN}Installation completed.{Style.RESET_ALL}")

logging.info(f"{Fore.CYAN}Builder ready{Style.RESET_ALL}")
logging.info(f"{Fore.CYAN}Starting builder...{Style.RESET_ALL}")
subprocess.run('python components/roseui/builder.py', shell=True)
