bozor = {}
while True:
    mahsulot = input("mahsulot nomini kiriting \n")
    narx = input("narxi qanaqa? \n")
    bozor[mahsulot]=narx
    yangi = input("yana kiritasmi? ha/yoq \n")
    if yangi.capitalize() != 'Ha':
        break
for i,k in bozor.items():
    print(f"{i}ning qiymati {k}so'm \n")
