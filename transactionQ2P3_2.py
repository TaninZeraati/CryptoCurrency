import bitcoin.wallet
from bitcoin.core import COIN, b2lx, serialize, x, lx, b2x
from utils import *


# tx: 9f50030b30775aef635fe7475b7e99fd24e2e82b0d8eaf602f71ccc72d82e450

# mnKuYGmxjsnQCTbjNyEjdspHoEZUXVoVLb
bitcoin.SelectParams("testnet") ## Select the network (testnet or mainnet)
my_private_key = bitcoin.wallet.CBitcoinSecret("9231aPuNzk3wjsPyXYfScGM1h6B9U9WaM7QVH7T2E1uNNA8YCEa") # Private key in WIF format XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
my_public_key = my_private_key.pub
my_address = bitcoin.wallet.P2PKHBitcoinAddress.from_pubkey(my_public_key)



def redeem_data():
    return [5,3,5,3]

def redeem_txin_scriptPubKey():
    return [OP_ADD,8 , OP_EQUALVERIFY,OP_SUB, 2,OP_EQUAL]

def script_output():
    return [OP_DUP, OP_HASH160, Hash160(my_public_key),OP_EQUALVERIFY ,OP_CHECKSIG]

def make_prime_transaction(amount_to_send, txid_to_spend, utxo_index,
                                txout_scriptPubKey):
    txout = create_txout(amount_to_send, txout_scriptPubKey)

    txin_scriptPubKey = redeem_txin_scriptPubKey()
    txin = create_txin(txid_to_spend, utxo_index)
    rd = redeem_data()
    new_tx = create_signed_transaction(txin, txout, txin_scriptPubKey,
                                       rd)

    return broadcast_transaction(new_tx)

if __name__ == '__main__':
    amount_to_send = 0.000001
    txid_to_spend = ('99268c1dd44b013c5b870a6d71c0e297f2280eae6d821a33d115007c08261e75')
    utxo_index = 0
    ### make_transaction
    txout_scriptPubKey = script_output()
    response = make_prime_transaction(amount_to_send, txid_to_spend, utxo_index, txout_scriptPubKey)
    print(response.status_code, response.reason)
    print(response.text)
