data_str = "M/O: Y87007-1; Model: NLXXAU/AU1(-N02); MO Qty: 101;Line: Line2; P/N: 6-04- 25256 - 470; Type: BIOS; Checksum: 02AC; " \
           "Position: U37; Nameplate: 25L25673G; Version: 1.07.09; Date: 2024/7/23;Reel Qty:101;" \
           "Operator:T2405641"
data_list = data_str.split(";")
data_dict = {}
for item in data_list:
    print(item)
    key, value = item.split(":")
    data_dict[key.strip()] = value.strip()
print(data_dict)