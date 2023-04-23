op = ""
arg1 = ""
arg2 = ""
result = ""
with open("input.txt", "r") as fp1, open("output.txt", "w") as fp2:
    for line in fp1:
        op, arg1, arg2, result = line.split()
        if op == "+":
            fp2.write(f"\nMOV R0,{arg1}")
            fp2.write(f"\nADD R0,{arg2}")
            fp2.write(f"\nMOV {result},R0")
        elif op == "*":
            fp2.write(f"\nMOV R0,{arg1}")
            fp2.write(f"\nMUL R0,{arg2}")
            fp2.write(f"\nMOV {result},R0")
        elif op == "-":
            fp2.write(f"\nMOV R0,{arg1}")
            fp2.write(f"\nSUB R0,{arg2}")
            fp2.write(f"\nMOV {result},R0")
        elif op == "/":
            fp2.write(f"\nMOV R0,{arg1}")
            fp2.write(f"\nDIV R0,{arg2}")
            fp2.write(f"\nMOV {result},R0")
        elif op == "=":
            fp2.write(f"\nMOV R0,{arg1}")
            fp2.write(f"\nMOV {result},R0")
