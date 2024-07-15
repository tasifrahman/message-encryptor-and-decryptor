
def textToBinarySequence(text):
    return [format(ord(c), '08b') for c in text]

def keyToBinarySequence(key):
    if len(key) < 8:
        raise ValueError("Key must be at least 8 characters long")
    
    binaryKey = ord(key[0])
    for i in range(1, 8):
        binaryKey ^= ord(key[i])
    
    return f"{binaryKey:08b}"

def encryption(text, key):
    binaryList = textToBinarySequence(text)
    binaryKey = keyToBinarySequence(key)
    
    encryptedText = []
    for binaryChar in binaryList:
        encryptedChar = int(binaryChar, 2) ^ int(binaryKey, 2)
        encryptedText.append(chr(encryptedChar))
    
    return ''.join(encryptedText)

def main(text,key):
    if len(key) < 8:
        print("Key must be at least 8 characters long")
        return
    
    encryptedText = encryption(text, key)
    return(f"Encrypted text: {encryptedText}")

if __name__ == "__main__":
    main()
