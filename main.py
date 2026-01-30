import sys
import string

class ShadowKey:
    def __init__(self):
        self.alphabet = string.ascii_letters + string.digits + string.punctuation
        self.banner = """
   _____ __               __                 __ __ZX 
  / ___// /_  ____ _____/ /___ _      __   / //_/__  __  __
  \__ \/ __ \/ __ `/ __  / __ \ | /| / /  / ,< / _ \/ / / /
 ___/ / / / / /_/ / /_/ / /_/ / |/ |/ /  / /| /  __/ /_/ / 
/____/_/ /_/\__,_/\__,_/\____/|__/|__/  /_/ |_\___/\__, /  
                                                  /____/   
        v1.0.0 - Simple Shift Cipher Tool
        """

    def encrypt(self, plain_text, shift_key):
        """
        Encrypts the plaintext using a shift cipher algorithm.
        """
        cipher_text = ""
        for char in plain_text:
            if char in self.alphabet:
                position = self.alphabet.find(char)
                new_position = (position + shift_key) % len(self.alphabet)
                cipher_text += self.alphabet[new_position]
            else:
                cipher_text += char
        return cipher_text

    def decrypt(self, cipher_text, shift_key):
        """
        Decrypts the ciphertext using the provided key.
        """
        plain_text = ""
        for char in cipher_text:
            if char in self.alphabet:
                position = self.alphabet.find(char)
                new_position = (position - shift_key) % len(self.alphabet)
                plain_text += self.alphabet[new_position]
            else:
                plain_text += char
        return plain_text

    def run(self):
        print(self.banner)
        while True:
            print("\n[1] Encrypt Data")
            print("[2] Decrypt Data")
            print("[3] Exit")
            
            choice = input("\nshadow-key > ")

            if choice == '1':
                text = input("Enter text to encrypt: ")
                try:
                    key = int(input("Enter shift key (int): "))
                    print(f"\n[+] Encrypted Output: {self.encrypt(text, key)}")
                except ValueError:
                    print("\n[!] Error: Key must be an integer.")

            elif choice == '2':
                text = input("Enter text to decrypt: ")
                try:
                    key = int(input("Enter shift key (int): "))
                    print(f"\n[+] Decrypted Output: {self.decrypt(text, key)}")
                except ValueError:
                    print("\n[!] Error: Key must be an integer.")

            elif choice == '3':
                print("\n[*] Terminating session...")
                sys.exit()
            else:
                print("\n[!] Invalid command.")

if __name__ == "__main__":
    tool = ShadowKey()
    tool.run()
