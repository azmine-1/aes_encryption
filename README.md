# AES Key Finder Script

## Description
This Python script attempts to find an AES key that was used to encrypt a given plaintext using AES in CBC (Cipher Block Chaining) mode. It tries different keys from a wordlist and checks if any can reproduce the provided ciphertext.

## Usage

```bash
./aes_key_finder.py <plaintext> <ciphertext_hex> <iv_hex>
