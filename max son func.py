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

def max_son(a, b, c):
    return(max(a, b, c))
           
while True:
    print("3 ta sonni kiriting: ")
    a = input("1-son: ")
    b = input("2-son ")
    c = input("3-son ")
    max_s = max_son(a, b, c)
    print(f"berilganlar ichida eng katta son {max_s}")
    yana = input("yana o\'ynaysizmi? ")
    if yana.title() != 'Ha':
        break
