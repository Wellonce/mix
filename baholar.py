# def malumot( ism, familiya, t_yil, t_joy, email, telefon):
#     lugat = {
#         'ismi': ism,
#         'familiyasi': familiya,
#         'tug\'ilgan yili': t_yil,
#         'tug\'ilgan joyi': t_joy,
#         'email addresi': email,
#         'telefon raqami': telefon
#         }
#     return lugat

# while True: 
#     list = [] 
#     print("Quyidagi ma\'lumotlarni kiriting: ")
#     ismi = input("ismingiz: ")
#     familiyasi = input("familiyangiz ")
#     tu_yil = input("tug\'ilgan yilingiz ")
#     tu_joy = input("tug\'ilgan joyingiz ")
#     emaili = input("emailingiz ")
#     telefoni = input("telefon raqamingiz ")
#     list.append(malumot(ismi, familiyasi, tu_yil, tu_joy, emaili, telefoni))
#     yana = input("yana mijoz qo\'shasizmi? ha/yo\'q ")
#     if yana.title() != 'Ha':
#         break
# print(list, len(list))

# import math

# def toliq(rad):
#     s = math.pi * pow(rad, 2)
#     u = 2 * math.pi * rad
#     info = {
#         'uzunligi' : u,
#         'yuzasi': s
#         }
#     return (info)


# print(toliq(8))
# ismlar = ['ali', 'vali', 'hasan', 'husan']

# def katta_qil(ismlar):
#     ismlar_katta = []
#     while ismlar:
#         ism = ismlar.pop()
#         ismlar_katta.append(ism.title())
#     return ismlar_katta

# print(katta_qil(ismlar[:]), ismlar)

ismlar = ['ali', 'vali', 'hasan', 'husan']

def bahola(ismlar):
    baholar ={}
    for ism in ismlar:
        baho = input(f"{ism.title()}ning bahosini kiriting: ")
        baholar[ism.title()]=int(baho)
    return baholar

print(bahola(ismlar))
