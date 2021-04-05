import math

p = int(input("Enter 2 Prime No.\np : "))
q = int(input("q : "))

n = p * q
print("\nn = p * q")
print("n = " + str(p) + " * " + str(q))
print("n = " + str(n))

n_phi = (p-1) * (q-1)
print("\nϕ(n) = ϕ(p) * ϕ(q)")
print("ϕ(n) = (p-1) * (q-1)")
print("ϕ(n) = " + str(p-1) + " * " + str(q-1))
print("ϕ(n) = " + str(n_phi))

coprime = []
for i in range(2,n_phi):
    if(math.gcd(i,n_phi)):
        coprime.append(i)
print("\nThe possible co-primes of are : ")
for i in coprime:
    print(i, end=" ")
e = int(input("\nSelect any one coprime\ne : "))

d = pow(e, -1, n_phi)
print("\nd*e = 1 (mod ϕ(n))")
print("d = e⁻¹(mod ϕ(n))")
print("d = " + str(e) + "⁻¹(mod " + str(n_phi) + ")")
print("d = " + str(d))

print("\nPublic Keys : {e,n}")
print("Public Keys : {" + str(e) + ", " + str(n) + "}")
print("\nPirvate Keys : {d,n}")
print("Pirate Keys : {" + str(d) + ", " + str(n) + "}")

print("\nEncrpytion : (mess)ᵉ (mod n)")
print("Encrpytion : (mess)^" + str(e) + " (mod " + str(n) + ")")

mess = input("\nMessage : ")
cipher = []
print("\nChar\tASCII\t(mess)^" + str(e) + " (mod " + str(n) + ")\tCipher")
for i in range(0,len(mess)):
    temp = math.pow(ord(mess[i]), e) % n
    print(mess[i] + "\t" + str(ord(mess[i])) + "\t" + str(ord(mess[i])) + "^" + str(e) + " (mod " + str(n) + ")\t\t" + str(int(temp)))
    cipher.append(int(temp))
print("\n\nCipher : ")
for i in cipher:
    print(str(i), end=" ")


decrpyt = []
print("\n\nCipher\t(cipher)^" + str(d) + " (mod " + str(n) + ")\tASCII\tMessager")
for i in range(0,len(cipher)):
    temp = math.pow(cipher[i], d) % n
    print(str(cipher[i]) + "\t" + str(cipher[i]) + "^" + str(d) + " ( mod " + str(n) + ")\t" + str(ord(mess[i])) + "\t" + str(mess[i]))
    decrpyt.append(temp)
print("\n\nDecrypt Message : ")
for i in range(0, len(mess)):
    print(mess[i], end="")