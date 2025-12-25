width = 40
print("Kişisel Kartvizit Uygulamasına Hoş Geldiniz")
a = "Adı: " + input("Adı: ")
b = "Soyadı: " + input("Soyadı: ")
c = "Mesleği: " + input("Meslek: ")
d = "İletişim: " + input("İletişim: ")


print("*" * width)
print("*" + "KİŞİSEL KARTVİZİT".center(width-2) + "*")
print("*"* width)
text = [a,b,c,d]
for i in text:
    space_num = width -len(i)-2
    print("*" + i.ljust(width - 2) + "*")


print("*"* width)