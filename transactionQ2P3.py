import bitcoin.wallet
from bitcoin.core import COIN, b2lx, serialize, x, lx, b2x
from utils import *


# tx_out: 99268c1dd44b013c5b870a6d71c0e297f2280eae6d821a33d115007c08261e75

# mnKuYGmxjsnQCTbjNyEjdspHoEZUXVoVLb
bitcoin.SelectParams("testnet") ## Select the network (testnet or mainnet)
my_private_key = bitcoin.wallet.CBitcoinSecret("9231aPuNzk3wjsPyXYfScGM1h6B9U9WaM7QVH7T2E1uNNA8YCEa") # Private key in WIF format XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
my_public_key = my_private_key.pub
my_address = bitcoin.wallet.P2PKHBitcoinAddress.from_pubkey(my_public_key)


def P2PKH_txin_scriptPubKey():
    return [OP_DUP, OP_HASH160, Hash160(my_public_key),OP_EQUALVERIFY ,OP_CHECKSIG]

def P2PKH_scriptSig(txin, txout, txin_scriptPubKey):
    signature = create_OP_CHECKSIG_signature(txin, txout, txin_scriptPubKey, my_private_key)
    return [signature, my_public_key]

def prime_output_pubKey():
    return [OP_ADD,8 , OP_EQUALVERIFY,OP_SUB, 2,OP_EQUAL]
    # return [5,3,5,3]

def make_prime_transaction(amount_to_send, txid_to_spend, utxo_index,
                                txout_scriptPubKey):
    txout = create_txout(amount_to_send, txout_scriptPubKey)

    txin_scriptPubKey = P2PKH_txin_scriptPubKey()
    txin = create_txin(txid_to_spend, utxo_index)
    txin_scriptSig = P2PKH_scriptSig(txin, txout, txin_scriptPubKey)
    new_tx = create_signed_transaction(txin, txout, txin_scriptPubKey,
                                       txin_scriptSig)

    return broadcast_transaction(new_tx)

if __name__ == '__main__':
    amount_to_send = 0.000005
    txid_to_spend = ('09ab66715379227810f14b465747effca749f6b9628d7450d8b35fedbea00403')
    utxo_index = 0
    ### make_transaction
    txout_scriptPubKey = prime_output_pubKey()
    response = make_prime_transaction(amount_to_send, txid_to_spend, utxo_index, txout_scriptPubKey)
    print(response.status_code, response.reason)
    print(response.text)
