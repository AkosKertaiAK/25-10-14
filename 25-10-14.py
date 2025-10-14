# Be: víz hőmérséklet (pl:-12C)

#1. kimenet: szilárd (jég)
#2. kimenet: folyadék
#3. kimenet: légnemű

# Ha hőmérséklet <=0 AKKOR Ki: "szilárd halmaz."
# Különben ha a hőmérséklet >0 és hőmérséklet < 100 akkor KI: folyékony
# különben Ki: "légnemű"

homerseklet=float(input("Hőmérsékelt:"))

if(homerseklet<=0):
    print("Szilárd")
else: 
    if((homerseklet>0) and (homerseklet<100)):
        print("Folyékony")
    else:
        print("Légnemű")





