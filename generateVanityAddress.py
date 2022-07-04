import generateAddress
import base58   

def find_vanity_address(first_bytes):
    if (len(first_bytes) > 3):
        return "error","Three first characters(except n/m),at most, must be entered!"
    try:
        base58.b58decode(first_bytes)
    except:
        return "error","Your characters are not in Base58 format!"
    produced_private_key, produced_address = generateAddress.produce_keys()
    while True:
        if produced_address[1:(len(first_bytes) + 1)].decode("utf-8")  == first_bytes:
            break
        
        produced_private_key, produced_address = generateAddress.produce_keys()
        # print(produced_address[1:(len(first_bytes) + 1)].decode("utf-8"))
    return produced_private_key, produced_address        


print('Enter the First Three Char:')
first_bytes = input()
private_key, address = find_vanity_address(first_bytes)
if private_key == "error":
    print(address)
else:
    print(private_key.decode("utf-8"))
    print(address.decode("utf-8"))