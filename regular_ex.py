import re
test_string = "Feb  5 23:59:46 Black-Eye forward: in:<pppoe-pavel> out:vlan2020, src-mac e8:65:d4:94:d1:f8, proto TCP (ACK), 10.30.5.117:60893->206.54.174.41:443,  (10.30.5.117:60893->115.127.116.170:60893)->206.54.174.41:443, len 64"
clean_test_string = re.sub(' +', ' ', test_string)
# monthday_pattern = r"^[JFMASOND][aepuco][nbrylgptvc].\d+[ ]"
# time_pattern = r"\d+[:]\d+[:]\d+"
# pop_name_pattern = r"(?<=[\d\d[:]\d\d[:]\d\d\b).+(?=(forward))"
# # source_user_pattren = r"(?<=(out:<)).+(?=(, src-mac))"
# source_user_pattren = r"(?<=(in:)).+(?=(, proto))"
# mac_pattern = r"(?<=(src-mac))\s\w\w:\w\w:\w\w:\w\w:\w\w:\w\w"
# protocal_pattern = r"(?<=(proto\s))[0-9a-zA-Z_]+\s.+?(?<=([)]))"
# ip_pattern = r"\d+\.\d+\.\d+\.\d+[:]\d+"
# ips = re.findall(ip_pattern,clean_test_string,flags=0)
# month = re.search(monthday_pattern, clean_test_string, flags=0)
# time = re.search(time_pattern, clean_test_string, flags=0)
# pop_name = re.search(pop_name_pattern, clean_test_string, flags=0)
# source_user = re.search(source_user_pattren, clean_test_string, flags=0)
# mac = re.search(mac_pattern, clean_test_string, flags=0)
# protocal = re.search(protocal_pattern, clean_test_string, flags=0)
# mongo_string = "mongodb://archLogUser:bracnet123@127.0.0.1:27017/bracnetWirelessLog"
# mongo_string_admin = "mongodb://mongoAdmin:faz1313@127.0.0.1:27017/admin"
# print(month.group().strip())
# print(time.group().strip())
# print(pop_name.group().strip())
# print(source_user.group().strip())
# print(mac.group().strip())
# print(protocal.group().strip())
# if clean_test_string.lower().find('nat'):
#     print('Source IP: '+ ips[2])
#     print('NAT Ip: '+ ips[3])
#     print('destination_ip: '+ ips[4])
# else:
#     print('Source IP: '+ ips[0])
#     print('destination_ip: '+ ips[1])
if re.search(r'\b' + 'NAT' + r'\b',clean_test_string,flags=0):
    print("yes")
    # source_user_pattren = r"(?<=(forward: )).+(?=(, src-mac))"
    # mac_pattern = r"(?<=(src-mac))\s\w\w:\w\w:\w\w:\w\w:\w\w:\w\w"
    # mac = re.search(mac_pattern, plain_line, flags=0)
    # print(mac.group().strip())
else:
    # source_user_pattren = r"(?<=(forward: )).+(?=(, proto))"
    print("No")

