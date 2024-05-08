print("hello")
f = open("version.txt", "r")
ver_number = 0
for line in f.readlines():
   print(line)
  
   if "VERSION" in line:
       ver_number = line.split("=")[1]
       break
print(ver_number)
ver_number = int(ver_number) + 1
f.close()
f = open("version.txt", "w")
f.write(f"VERSION=str(ver_number)")
print(ver_number)
