# ss ke hisaab se total kharcha nikalein. Agar total kharcha 50000 (50 hazar) ya usse kam hai toh print karein "Hum budget ke andar hain" nahi toh print karo ki hum budget ke bahar hain. Note: Inn exercises mein aapko variables ke naam apne aap soch kar likhne haitotel=int(input ("enter the totel"))
student=int(input("enter the student"))
# totel=int(input ("enter the totel"))
kharcha=int(input("enter the kharcha"))
totel_kharcha=student*kharcha
if totel_kharcha<=50000:
    print("budget ke ander hai")
else:
    print("budget ke bhar hai")
 