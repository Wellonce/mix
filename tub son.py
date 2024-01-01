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

# def tub_sonlar_top(min, max):
#     tub_sonlar = []
#     for n in range(min, max + 1):
#         tub = True
#         if n == 1:
#             tub = False
#         elif n == 2:
#             tub = True
#         else:
#             for x in range(2, n):
#                 if n % x == 0:
#                     tub = False
#         if tub:
#             tub_sonlar.append(n)

#     return tub_sonlar

# print(tub_sonlar_top(2,10))

ismlar = ['ali', 'vali', 'hasan', 'husan']
ismlar_katta = []
def katta_qil(ismlar):
    ism = ismlar.pop.title()
    ismlar_katta.pop(ism)
    return ismlar_katta

katta_qil()