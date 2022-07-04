import bitcoin.wallet
from bitcoin.core import COIN, b2lx, serialize, x, lx, b2x
from utils import *

# 77d13fccd61a5eb9c8cc089f25cd139c7217bd6bd93fe4c8894b9817f98832dd

bitcoin.SelectParams("testnet")
my_private_key = bitcoin.wallet.CBitcoinSecret("91c2c2h9a2FyVSHCJh5MNf6dVH1ZzscePUzX556hSKhjLrQUUz4")
first_person_private_key = bitcoin.wallet.CBitcoinSecret("91xjMw6VyHaD93QC751Kb8XZeor9Xi7rKLBdVaCtuhb9Wz56eg7")
second_person_private_key = bitcoin.wallet.CBitcoinSecret("92Pk448RcQDfhZEzP8xagBwcfMLtH5HZkmnVXgXWBfEyYmhiiHR")
third_person_private_key = bitcoin.wallet.CBitcoinSecret("92FVhnu9hWDANY4LG4eL9nnNytcfuhDb7fAPKBwYtwwZFK3nTYX")
my_public_key = my_private_key.pub
first_person_public_key = first_person_private_key.pub
second_person_public_key = second_person_private_key.pub
third_person_public_key = third_person_private_key.pub

def P2PKH_txin_scriptPubKey():
    return [OP_DUP, OP_HASH160, Hash160(my_public_key),OP_EQUALVERIFY ,OP_CHECKSIG]

def P2PKH_scriptSig(txin, txout, txin_scriptPubKey):
    signature = create_OP_CHECKSIG_signature(txin, txout, txin_scriptPubKey, my_private_key)
    return [signature, my_public_key]

def MultiSig_output_script():
    return [OP_2, first_person_public_key, second_person_public_key, third_person_public_key, OP_3, OP_CHECKMULTISIG]

def make_multisig_transaction(amount_to_send, txid_to_spend, utxo_index,
                                txout_scriptPubKey):
    txout = create_txout(amount_to_send, txout_scriptPubKey)

    txin_scriptPubKey = P2PKH_txin_scriptPubKey()
    txin = create_txin(txid_to_spend, utxo_index)
    txin_scriptSig = P2PKH_scriptSig(txin, txout, txin_scriptPubKey)
    new_tx = create_signed_transaction(txin, txout, txin_scriptPubKey,
                                       txin_scriptSig)

    return broadcast_transaction(new_tx)

if __name__ == '__main__':
    amount_to_send = 0.00005
    txid_to_spend = ('2a09612304fdba73f43df045c7fd008aec693dd32879f4a62a20c19090b25475')
    utxo_index = 1
    ### make_transaction
    txout_scriptPubKey = MultiSig_output_script()
    response = make_multisig_transaction(amount_to_send, txid_to_spend, utxo_index, txout_scriptPubKey)
    print(response.status_code, response.reason)
    print(response.text)