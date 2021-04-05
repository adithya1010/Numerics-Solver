import math

print("Chinese Remainder Theorem")
print("x ≅ a₁ mod n₁")
print("x ≅ a₂ mod n₂")
print("x ≅ a₃ mod n₃")

a1 = int(input("a₁ : "))
a2 = int(input("a₂ : "))
a3 = int(input("a₃ : "))

n1 = int(input("n₁ : "))
n2 = int(input("n₂ : "))
n3 = int(input("n₃ : "))

print("X = ( a₁N₁C₁ + a₂N₂C₂ + a₃N₃C₃ ) mod N\n\nN = n₁*n₂*n₃\n\nN₁ = N/n₁\nN₂ = N/n₂\nN₃ = N/n₃\n\nN₁*C₁ ≅ 1 mod n₁\nN₂*C₂ ≅ 1 mod n₂\nN₃*C₃ ≅ 1 mod n=₃")

N = n1*n2*n3
print("\n\n\nN = " + str(n1) + " * " + str(n2) + " * " + str(n3))
print("N = " + str(N))

N1 = N/n1
N2 = N/n2
N3 = N/n3
print("\nN₁ = " + str(N) + "/" + str(n1))
print("N₁ = " + str(N1))
print("N₂ = " + str(N) + "/" + str(n2))
print("N₂ = " + str(N2))
print("N₃ = " + str(N) + "/" + str(n3))
print("N₃ = " + str(N3))

print("\nN₁*C₁ ≅ 1 mod n₁")
print(str(n1) + "*C₁ ≅ 1 mod " + str(n1))
print("C₁ ≅ " + str(n1) + "⁻¹ mod " + str(n1))
C1 = pow(int(N1), -1, int(n1))
print("C₁ = " + str(C1))

print("N₂*C₂ ≅ 1 mod n₂")
print(str(n2) + "*C₂ ≅ 1 mod " + str(n2))
print("C₂ ≅ " + str(n2) + "⁻¹ mod " + str(n2))
C2 = pow(int(N2), -1, int(n2))
print("C₂ = " + str(C2))

print("N₃*C₃ ≅ 1 mod n₃")
print(str(n3) + "*C₃ ≅ 1 mod " + str(n3))
print("C₃ ≅ " + str(n3) + "⁻¹ mod " + str(n3))
C3 = pow(int(N3), int(-1), int(n3))
print("C₃ = " + str(C3))

print("\n\nX = (" + str(a1) + "*" + str(N1) + "*" + str(C1) + " + " + str(a2) + "*" + str(N2) + "*" + str(C3) + " + " + str(a3) + "*" + str(N3) + "*" + str(C3) + ") mod " + str(N))
t1 = a1*N1*C1
t2 = a2*N2*C2
t3 = a3*N3*C3
print("X = (" + str(t1) + " + " + str(t2) + " + " + str(t3) + ") mod " + str(N))
X = t1+t2+t3
print("X = " + str(X) + " mod " + str(N))
X = X % N
print("X = " + str(X))
