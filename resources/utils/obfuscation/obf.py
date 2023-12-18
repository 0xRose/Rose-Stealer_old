import ast
import random
import string
import os
import re
import argparse
import logging
import colorlog
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
from base64 import urlsafe_b64encode, urlsafe_b64decode

log_format = "%(asctime)s [%(levelname)s] [%(module)s.%(funcName)s] %(message)s"
handler = colorlog.StreamHandler()
handler.setFormatter(colorlog.ColoredFormatter(log_format))
handler.setLevel(logging.INFO)
file_handler = logging.FileHandler('rose-obf.log', encoding='utf-8')
file_handler.setLevel(logging.DEBUG)
file_formatter = logging.Formatter(log_format)
file_handler.setFormatter(file_formatter)
root_logger = logging.getLogger()
root_logger.addHandler(handler)
root_logger.addHandler(file_handler)
root_logger.setLevel(logging.DEBUG)

def generate_key(length=16):
    characters = string.ascii_letters + string.punctuation
    key = ''.join(random.choice(characters) for _ in range(length))
    return key

def generate_random_string(length):
    characters = string.ascii_uppercase + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

def getCustom():
    choice = random.choice([1, 2, 3])

    if choice == 1:
        return generate_pattern1()
    elif choice == 2:
        return generate_pattern2()
    elif choice == 3:
        return generate_pattern3()

def generate_pattern1():
    return "__" + ''.join(random.choice("O0") for _ in range(10))

def generate_pattern2():
    return "__" + ''.join(random.choice("0123456789") for _ in range(10)) + "__"

def generate_pattern3():
    return ''.join(random.choice("Il") for _ in range(15)) + 'I'

def encryptData(text, key):
    cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=default_backend())
    encryptor = cipher.encryptor()

    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(text.encode()) + padder.finalize()

    ciphertext = encryptor.update(padded_data) + encryptor.finalize()
    return urlsafe_b64encode(ciphertext).decode()

def decryptData(ciphertext, key):
    cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=default_backend())
    decryptor = cipher.decryptor()
    
    decrypted_data = decryptor.update(urlsafe_b64decode(ciphertext)) + decryptor.finalize()

    unpadder = padding.PKCS7(128).unpadder()
    unpadded_data = unpadder.update(decrypted_data) + unpadder.finalize()

    return unpadded_data.decode()

def process_node(node, name_dict):
    if isinstance(node, ast.Name) and node.id in name_dict:
        node.id = name_dict[node.id]

def obfuscate_code(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    content = re.sub(r'\n\s*\n', '\n', content)

    tree = ast.parse(content)

    name_dict = {}

    root_logger.info('Renaming Classes, Functions, Arguments, Keyword Arguments and Variables...')
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            old_name = node.name
            new_name = getCustom()
            root_logger.debug(f'Function Name: {old_name} ---> New Function Name: {new_name}')
            name_dict[old_name] = new_name
            node.name = new_name

            for arg in node.args.args:
                old_arg_name = arg.arg
                new_arg_name = getCustom()
                root_logger.debug(f'Argument Name: {old_arg_name} ---> New Argument Name: {new_arg_name}')
                name_dict[old_arg_name] = new_arg_name
                arg.arg = new_arg_name

            for keyword in node.args.kwonlyargs:
                old_kwarg_name = keyword.arg
                new_kwarg_name = getCustom()
                root_logger.debug(f'Keyword Argument Name: {old_kwarg_name} ---> New Keyword Argument Name: {new_kwarg_name}')
                name_dict[old_kwarg_name] = new_kwarg_name
                keyword.arg = new_kwarg_name

        elif isinstance(node, ast.ClassDef):
            old_name = node.name
            new_name = getCustom()
            root_logger.debug(f'Class Name: {old_name} ---> New Class Name: {new_name}')
            name_dict[old_name] = new_name
            node.name = new_name

    for node in ast.walk(tree):
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name):
                    old_var_name = target.id
                    new_var_name = getCustom()
                    root_logger.debug(f'Variable Name: {old_var_name} ---> New Variable Name: {new_var_name}')
                    name_dict[old_var_name] = new_var_name
                    target.id = new_var_name

        process_node(node, name_dict)
    root_logger.info('Renaming of classes, functions, arguments, keyword arguments and variables done.')

    return ast.unparse(tree)

key = [ord(char) for char in generate_key()]
#key = getKey()
decryptionFun = getCustom()
ciphertextParam = getCustom()
keyVar = getCustom()
cipherVar = getCustom()
decryptorVar = getCustom()
decrypted_textVar = getCustom()
unpadderVar = getCustom()
unpadded_dataVar = getCustom()

def replace_string(match):
    s = match.group(1)
    encrypted_string = encryptData(s, bytes(key))
    encrypted_string = encrypted_string.replace("'", r"\'")
    chr_format = "+".join([f"chr({ord(char)})" for char in repr(encrypted_string)])
    b_format = [ord(char) for char in chr_format]
    decrypted_string = decryptData(encrypted_string, bytes(key))
    root_logger.debug(f'String: {s} ---> Encrypted String: {encrypted_string} ---> Char Encrypted String: {chr_format} ---> Bytes Encrypted String: {b_format} ---> Aes Decrypted String: {decrypted_string}')
    #return f'{decryptionFun}({repr(encrypted_string)})[1:-1]'
    #randomizer = random.choice([f'{decryptionFun}(bytes({b_format}))[1:-1]', f'{decryptionFun}({chr_format})[1:-1]'])
    #return randomizer
    return f'{decryptionFun}({chr_format})[1:-1]'
    #return f'{decryptionFun}(bytes({b_format}))'

def obfuscate_strings(content):
    root_logger.info('Encrypting strings...')
    data = re.sub(r'(\'[^\']*\'|\"[^\"]*\")', replace_string, content)
    root_logger.info('Encryption of strings done.') 
    return data

def main(input_file, output_file):
    root_logger.debug('Entered main function.')
    content = obfuscate_code(input_file, output_file)

    with open(output_file, 'w') as f:
        f.write(''.join([
            'from cryptography.hazmat.primitives.ciphers import Cipher,algorithms,modes\n',
            'from cryptography.hazmat.primitives import padding\n',
            'from cryptography.hazmat.backends import default_backend\n',
            'from base64 import urlsafe_b64decode\n',
            f'def {decryptionFun}({ciphertextParam}):\n',
            f'   {keyVar}=bytes({key})\n'
            f'   {cipherVar}=Cipher(algorithms.AES({keyVar}),modes.ECB(),backend=default_backend())\n',
            f'   {decryptorVar}={cipherVar}.decryptor()\n',
            f'   {decrypted_textVar}={decryptorVar}.update(urlsafe_b64decode({ciphertextParam}))+{decryptorVar}.finalize()\n',
            #f'   return {decrypted_textVar}.rstrip().decode()\n\n',
            f'   {unpadderVar} = padding.PKCS7(128).unpadder()\n',
            f'   {unpadded_dataVar} = {unpadderVar}.update({decrypted_textVar}) + {unpadderVar}.finalize()\n',
            f'   return {unpadded_dataVar}.decode()\n\n',
            obfuscate_strings(content)
        ]))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Obfuscate Python code efficiently with Rose-obf.')
    parser.add_argument('-i', '--input', help='Input file name (required, .py)', dest='in_file', metavar='<input_file>', required=True)
    parser.add_argument('-o', '--output', help='Output file name', dest='out_file', metavar='<output_file>', required=False)
    args = parser.parse_args()

    input_file = args.in_file
    output_file = os.path.join(os.getcwd(), f"obf-{generate_random_string(10)}.py") if args.out_file is None else args.out_file

    if input_file.endswith('.py'):
        try:
            root_logger.info(f'{input_file} ---> {output_file}...')
            root_logger.debug('Entering main function.')
            main(input_file, output_file)
            root_logger.info(f'Done. {input_file} ---> {output_file}')
        except Exception as e:
            root_logger.error(f'Error: {e}')
    else:
        root_logger.error('Invalid Python file entered. Please make sure the file has a .py extension.')
        