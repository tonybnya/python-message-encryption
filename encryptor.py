import base64

print('')
print('======================================================')
print("This is a possible implementation of a quick script to")
print("   encrypt a message with 'base64' Python library")
print('======================================================')
print('')

key = 'some_secure_password'

print('')
print('Provide the message that you would like to encrypt below:')

message = input('-> ')
enc = []

for i in range(len(message)):
    key_c = key[i % len(key)]
    enc.append(chr((ord(message[i]) + ord(key_c)) % 256))

encryption = base64.urlsafe_b64encode("".join(enc).encode()).decode()

print('')
print('This is the encrypted message:\n' + encryption)
print('')

dec = []
message = base64.urlsafe_b64decode(encryption).decode()

for i in range(len(message)):
    key_c = key[i % len(key)]
    dec.append(chr((256 + ord(message[i]) - ord(key_c)) % 256))

print('This is the decryption of your message:\n' + "".join(dec))
print('')
