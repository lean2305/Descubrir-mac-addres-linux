import os


cmd =" ip neigh|grep $(ip -4 route list 0/0|cut -d' ' -f3) |cut -d' ' -f5|tr '[a-f]' '[A-F]' "

print("\n")

returned_value = os.popen(cmd).read().splitlines().pop(1)  # returns the exit code in unix
print(f"2.4 ghz mac adress: |{returned_value}|")




print("\n")
print("-------------------------------\n")

print('5.0 ghz mac adress:')
mac_five = os.popen('sudo iwconfig wlan0').read().splitlines()
count = 0

for option in mac_five:

    if "Access Point" in option:
        new_array=option.split()

for option in new_array:

    count = count + 1
    if "Point:" in option:
        mac_addr_five = new_array[5]
        print(mac_addr_five)
#o endereço mac vai ser exibido como acess point



#ip neigh|grep "$(ip -4 route list 0/0|cut -d' ' -f3) "|cut -d' ' -f5|tr '[a-f]' '[A-F]' 
#para saber mac adress 2.4ghz



#para saber mac adress 5.0ghz
#sudo iwconfig