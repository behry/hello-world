with open('poem.txt','a') as f:
    f.write ('''Bunu sana yazdığımı bilmezsin
Bir yabancı şarkı gibi dinlersin
Benim için önce Tanrı sonra sensin
Bir tek dileğim var mutlu ol yeter''')

with open("poem.txt", "r") as f:
    lines=f.read()

print (lines)
