P = 10000
N = 12
R = .08

T = input ("How many years?")
T = int (T)
A = P*(1 + R/N)**(N*T)
print (A)