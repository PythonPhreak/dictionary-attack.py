# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 12:51:08 2023

@author: user
"""
import time
import pyzipper
from tqdm import tqdm

def display_welcome_message():
    welcome_message = """
    ************************************************
    * Password Cracker created by PythonPhreak!   *
    ************************************************
    
    This program attempts to decrypt a ZIP file using a
    wordlist of potential passwords. Please provide the
    paths to the ZIP file and the wordlist.

    """
    print(welcome_message)

def main():
    display_welcome_message()
    # Get the path to the ZIP file and the wordlist file from the user
    zip_file_path = input("Enter the path to the ZIP file: ")
    wordlist_path = input("Enter the path to the wordlist file: ")

    # Count the number of words in the wordlist
    n_words = len(list(open(wordlist_path, "rb")))

    # Print the total number of passwords
    print("Total passwords to test:", n_words)
    time.sleep (1)
    with open(wordlist_path, "rb") as wordlist_file:
        for word in tqdm(wordlist_file, total=n_words, unit="word"):
            try:
                # Attempt to decrypt the ZIP file using pyzipper
                with pyzipper.AESZipFile(zip_file_path) as zf:
                    zf.pwd = word.strip()
                    zf.extractall()
                print("[+] Password found:", word.decode().strip())
                return
            except Exception as e:
                continue

    print("[!] Password not found, try other wordlist.")

if __name__ == "__main__":
    main()
