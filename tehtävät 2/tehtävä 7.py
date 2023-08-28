print("Anna leiviskät.")
leiv = input()
print()

print("Anna naulat.")
naul = input()
print()

print("Anna luodit.")
luo = input()
print()

kg = float(((leiv*20*32*13.3)+(naul*32*13.3)+(luo*13.3))//1000)
g = float(((leiv*20*32*13.3)+(naul*32*13.3)+(luo*13.3))%1000)

print("Massa nykymittojen mukaan:")
print(f"{float(kg):2d} + kilogrammaa ja + {float(g):5.2f} + grammaa.")



