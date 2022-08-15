# """01.06.2022 YIL
# MAVZU:tasodifiy raqamlar random"""
# numbers={'\t\t\t\t\t\t\t\t\t\t\t+998.90.699.88.81.\t\t\t\t\tkodni kiriting 1881',
#          '\t\t\t\t\t\t\t\t\t\t\t+998.90.641.16.56.\t\t\t\t\tkodni kiriting 2891',
#          '\t\t\t\t\t\t\t\t\t\t\t+998.93.278.26.10.\t\t\t\t\tkodni kiriting 8841',
#          '\t\t\t\t\t\t\t\t\t\t\t+998.90.797.04.53.\t\t\t\t\tkodni kiriting 7841',
#          '\t\t\t\t\t\t\t\t\t\t\t+998.94.621.38.48.\t\t\t\t\tkodni kiriting 4851',
#          '\t\t\t\t\t\t\t\t\t\t\t+998.90.212.12.12.\t\t\t\t\tkodni kiriting 7891',
#          '\t\t\t\t\t\t\t\t\t\t\t+998.90.212.20.09.\t\t\t\t\tkodni kiriting 7821',
#          '\t\t\t\t\t\t\t\t\t\t\t+998.99.999.09.99.\t\t\t\t\tkodni kiriting 2821',
#          '\t\t\t\t\t\t\t\t\t\t\t+998.90.942.06.46.\t\t\t\t\tkodni kiriting 7891',
#          '\t\t\t\t\t\t\t\t\t\t\t+998.99.998.26.10.\t\t\t\t\tkodni kiriting 4861',
#          '\t\t\t\t\t\t\t\t\t\t\t+998.88.204.20.04.\t\t\t\t\tkodni kiriting 4891',
#          '\t\t\t\t\t\t\t\t\t\t\t+998.99.000.00.00.\t\t\t\t\tkodni kiriting 5851',
#          '\t\t\t\t\t\t\t\t\t\t\t+998.77.202.00.02.\t\t\t\t\tkodni kiriting 7801',
#          '\t\t\t\t\t\t\t\t\t\t\t+998.90.942.55.05.\t\t\t\t\tkodni kiriting 7891',
#          '\t\t\t\t\t\t\t\t\t\t\t+998.99.998.26.88.\t\t\t\t\tkodni kiriting 4861',
#          '\t\t\t\t\t\t\t\t\t\t\t+998.88.204.20.00.\t\t\t\t\tkodni kiriting 4841',
#          '\t\t\t\t\t\t\t\t\t\t\t+998.99.000.00.01.\t\t\t\t\tkodni kiriting 5811',
#          '\t\t\t\t\t\t\t\t\t\t\t+998.77.202.33.11.\t\t\t\t\tkodni kiriting 7801',
#          '\t\t\t\t\t\t\t\t\t\t\t+998.90.641.33.31.\t\t\t\t\tkodni kiriting 2891',
#          '\t\t\t\t\t\t\t\t\t\t\t+998.93.278.33.21.\t\t\t\t\tkodni kiriting 8841',
#          '\t\t\t\t\t\t\t\t\t\t\t+998.90.797.33.15.\t\t\t\t\tkodni kiriting 7814',
#          '\t\t\t\t\t\t\t\t\t\t\t+998.94.621.33.13.\t\t\t\t\tkodni kiriting 4118',
#          '\t\t\t\t\t\t\t\t\t\t\t+998.90.212.33.01.\t\t\t\t\tkodni kiriting 7218',
#          '\t\t\t\t\t\t\t\t\t\t\t+998.90.212.84.51.\t\t\t\t\tkodni kiriting 7128',
#          '\t\t\t\t\t\t\t\t\t\t\t+998.99.999.33.91.\t\t\t\t\tkodni kiriting 2823',
#          '\t\t\t\t\t\t\t\t\t\t\t+998.90.942.33.51.\t\t\t\t\tkodni kiriting 1123',
#          '\t\t\t\t\t\t\t\t\t\t\t+998.99.998.33.11.\t\t\t\t\tkodni kiriting 4823',
#          '\t\t\t\t\t\t\t\t\t\t\t+998.88.204.33.10.\t\t\t\t\tkodni kiriting 4823',
#          '\t\t\t\t\t\t\t\t\t\t\t+998.99.000.33.16.\t\t\t\t\tkodni kiriting 5023',
#          '\t\t\t\t\t\t\t\t\t\t\t+998.77.202.33.18.\t\t\t\t\tkodni kiriting 1113',
#          '\t\t\t\t\t\t\t\t\t\t\t+998.90.942.33.19.\t\t\t\t\tkodni kiriting 9023',
#          '\t\t\t\t\t\t\t\t\t\t\t+998.99.998.33.16.\t\t\t\t\tkodni kiriting 4023',
#          '\t\t\t\t\t\t\t\t\t\t\t+998.88.204.33.12.\t\t\t\t\tkodni kiriting 3323',
#          '\t\t\t\t\t\t\t\t\t\t\t+998.99.000.33.22.\t\t\t\t\tkodni kiriting 5023',
#          '\t\t\t\t\t\t\t\t\t\t\t+998.77.202.33.13.\t\t\t\t\tkodni kiriting 7023',}
#
# print(numbers.pop())
#
# n1 = numbers.pop()
# n2 = numbers.pop()
# numbers.add(n1)
# numbers.add(n2)
# print("Omadli ishtirokchI siz bizni uyinga taklif qilindingiz",
#       "tasodifiy Rendin pragrammasi orqali ishtirokchimizga aylandungiz::")
# uyin=(input("\t\t\t\t\tUyinga hush kelibsiz UYINNI BOSHLASH UCHUN.kodni kriting ???: "))
# ism=(input("Ismingizni kriting: "))
# FAMILIYA=(input("FAMILIYA KIRITING: "))
# YILINGIZ=(input("TUG`ILGAN YILINGIZ KIRITING : "))
# YOSH=(input("YOSHINGIZ KRITING: "))
# MANZIL=(input("YASHASH HUDUDINGIZ: "))
# print("\t\t\t\t\tSizga vaqt berilgan shu vaqt ichida ishlab bo`lishingiz kerak : 7 daqiqa ")
#
# numbers = {'1','2','3','4','5','6','7','8','9','10','11',
#            '12','13','14','15',
#            '16','17','18','19',
#            '20','21','22','23',
#            '24','25','26','27',
#            '28','29','30','31',
#            '32','33',
#            '34','35','36','37',
#            '38','39','40','41',
#            '42','43','44','45',
#            '46','47','48','49',
#            '50','51','52','53',
#            '54','55','56','57',
#            '58','59','60','61',
#            '62','63','64','65',
#            '66','67','68','69',
#            '70','71'
#             '72','73','74','75',
#            '76','77','78','79',
#            '80','81','82','83',
#            '84','85','86',
#            '87','88','89','90',
#            '91','92','93','94',
#            '95','96','97','98',
#            '99','100','10','20',
#            '30',
#            '40','50','60','70',
#            '80','90','100'}
#
# notogri_javob=0
# while True:
#     n1 = numbers.pop()
#     n2 = numbers.pop()
#     numbers.add(n1)
#     numbers.add(n2)
#     qiymat =int(n1) +int (n2)
#     javob = int(input(f"{n1}+{n2} = "))
#     if qiymat == javob:
#         print('Tug`ri javob ✅ ')
#     elif notogri_javob==5:
#         print('tugadi')
#         break
#     else:
#         print('Notug`ri javob ❌ ')
#         notogri_javob+=1
#
# print("BU uyinimizdan broz miyyangizni charhlab oldingiz .Uyinimiz tugadi...")
# print("SIZ yuttingiz 10 misol ishlab 50% yutiq 50.000 so`m yutib oldingiz")
#
#
#
#
#
#
#
#
