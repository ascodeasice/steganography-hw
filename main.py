from encoding import decode, encode

print("Enter the cleartext : ", end="")
cleartext = input()

ciphertext = encode(cleartext)

print(f"加密結果：\n{ciphertext}\n")

decode_result = decode(ciphertext)

print(f"解密結果：\n{decode_result}")
