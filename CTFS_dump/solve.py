from tqdm import tqdm  # Progress bar :)
from pwn import *     # Import the pwntools module to interact with the server
from Crypto.Cipher import AES  # AES encryption module for solving AES challenges

# Set the host and port
HOST = 'ctfnhack.challs.ctflib.eu'  # Replace with the actual host
PORT = 49879         # Replace with the actual port
t = remote(HOST, PORT)  # Connect to the server

t.level = 'debug'  # This will print the data sent and received

# Receive until the challenges start
t.recvlines(2)

for _ in tqdm(range(25)):
    line = t.recvline().decode()   # Receive a line, decode from bytes to string
    action = line.split()[1]       # Extract the type of challenge ('math' or 'aes')

    match action:
        case 'math':
            equation = t.recvuntil(' = ').decode().split(' = ')[0]  # Receive the math equation
            result = eval(equation)  # Evaluate the equation safely
            t.sendline(str(result))  # Send the result as a string

        case 'aes':
            line = t.recvline().decode()  # Receive the line with the key
            key = line.split()[-1]       # Extract the key
            line = t.recvline().decode()  # Receive the line with the ciphertext
            enc = line.split()[-1]       # Extract the ciphertext (in hex format)

            # Decrypt the ciphertext
            cipher = AES.new(key.encode(), AES.MODE_ECB)
            plaintext = cipher.decrypt(bytes.fromhex(enc)).decode()

            t.sendline(plaintext)  # Send the decrypted plaintext

    res = t.recvline().decode()  # Receive the result of the challenge

flag = t.recvline().decode()  # If everything went well, the flag is printed
print(flag)

