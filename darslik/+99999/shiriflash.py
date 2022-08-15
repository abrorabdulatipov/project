


"""shriflash uchun { qliflash yoz } shrifdan chiqarish uchun {ochish} """
# s=input("So`z kiriting: ")
# s2=""
# for i in range(len(s)-1,-1,-1):
#     s2=s2+s[i]
#     print(s2)
# alifbo = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
#           'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
#           's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ',
#           '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
#
# while True:
#     tur = input("Turi 'encode' - Shifrlash yoki 'decode' - Shifrdan chiqarish:").lower()
#     matn = input("Matninggizni kiriting:").lower()
#     raqam = int(input("Shifrlash raqami:"))
#
#
#     shifrlangan = ""
#     for harf in matn:
#         orni = alifbo.index(harf)
#         # print('asl orni',orni)
#         yangiorni = orni + raqam
#         # print('yangiorni',yangiorni)
#         yangiharf = alifbo[yangiorni]
#         shifrlangan += yangiharf
#     print('shiflangan matn', shifrlangan)
#
#     def shifrlash(matn, raqam):
#         shifrlangan = ""
#         for harf in matn:
#             orni = alifbo.index(harf)
#             yangiorni = orni + raqam
#             yangiharf = alifbo[yangiorni]
#             shifrlangan += yangiharf
#         print('shiflangan matn', shifrlangan)
#     def deshifrlash(matn, raqam):
#         shifrlangan = ""
#         for harf in matn:
#             orni = alifbo.index(harf)
#             yangiorni = orni - raqam
#             yangiharf = alifbo[yangiorni]
#             shifrlangan += yangiharf
#         print('shiflangan matn', shifrlangan)
#
#
#     if tur == 'qliflash':
#         shifrlash(matn, raqam)
#     elif tur == 'ochish':
#         deshifrlash(matn, raqam)
#
#     def toliq_ism(ism, familya):
#       print(f'Ism: {ism}\n'
#       f'Familya: {familya}')