'''
Author: Stefan Ignat
Date Modified: 4/23/2020
Purpose: 
  RSA Algorithm implementation
'''

from random import randint
import math

#Class declaration
class rsa: 
  
  #Declare constant global e
  def __init__(self):
    self.e = 65537

  #Calculates x^a (mod n).
  def modexp(self, x, a, n):
    return pow(x,a,n)

  #Writes the encrypted message given the public key
  def encrypt(self):
    #Open Files
    fileMessage = open("message.txt", "r")
    filePublicKey = open("public_key.txt","r")
    fileCipherText = open("ciphertext.txt", "w+")

    #Read message and public key
    message = int(fileMessage.read())
    public = int(filePublicKey.read())

    #Write encrypted text
    fileCipherText.write(str(self.modexp(message, self.e, public)))
    
  #Decrypts the message using the read keys
  def decrypt(self):
    #Open Files
    filePublicKey = open("public_key.txt","r")
    filePrivateKey = open("private_key.txt", "r")
    fileCipherText = open("ciphertext.txt", "r")
    fileDecryptedMessage = open("decrypted_message.txt", "w+")

    #Read encrypted message and keys
    cipher = int(fileCipherText.read())
    public = int(filePublicKey.read())
    private = int(filePrivateKey.read())

    #Write decrypted text
    fileDecryptedMessage.write(str(self.modexp(cipher, private, public)))

  #Generate a random public and private key at least 10^95 apart.
  def keySetup(self):
    filePublicKey = open("public_key.txt","w+")
    filePrivateKey = open("private_key.txt", "w+")
    
    #To ensure difference between primes
    diff = 10**95
    #First prime, p
    p = self.generatePrime()
    #Second prime, q
    q = self.generatePrime()

    while abs(p- q) < diff:
      #Keep generating until they are 10^95 apart
      q = self.generatePrime()

    n = p * q
    a, d, c = self.euclid(self.e, (p-1)*(q-1))

    filePublicKey.write(str(n))
    filePrivateKey.write(str(abs(d)))

  #Generate random prime numbers
  def generatePrime(self):
    print("Generating Prime...")
    randomInt = 0
    iterations = 0
    found = False
    while(found == False):
      iterations += 1
      randomInt = self.getRandom()
      a = self.getRandomRange(0, randomInt-1)
      randMinus = randomInt-1
      result = self.modexp(a, randMinus, randomInt)
      if(result == 1):
        found = True
        print("...Generated!")
    return randomInt

  #Generate random number between 10^100 and 10^150
  def getRandom(self):
    return randint(10**100, 10**150)

  #Generate random number in given range
  def getRandomRange(self, lowerRange, upperRange):
    return randint(lowerRange, upperRange)
    
  #Extended euclid algorithm
  def euclid(self, a, b):
    if a == 0:
      return (b, 0, 1)
    else:
      gcd, x, y = self.euclid(b % a, a)
      return (gcd, y - (b//a) * x, x)



def main():
  #Declare class
  rsaObj = rsa()
  rsaObj.keySetup()

  while True:
    print("Enter a command: e - encrypt, d - decrypt, q - quit")
    command = input(": ")
    
    if command == 'e':
      rsaObj.encrypt()
      print("..encrypted in ciphertext.txt \n")
    
    if command == "d":
      rsaObj.decrypt()
      print("..decrypted in decrypted_message.txt \n")

    if command == 'q':
      break #Quit

#Initialize
main()