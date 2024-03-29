import bitcoin.wallet
from bitcoin.core import COIN, b2lx, serialize, x, lx, b2x
from utils import *

#txid: 7f8ab79cffd80b71bc11f65831ab55ec83f61d36b2dc15075e7d489a345cdc31
#my Address: mwxACSvznZKiCPymBuUCMyzhsMZ3ZMMetp
bitcoin.SelectParams("testnet") ## Select the network (testnet or mainnet)
my_private_key = bitcoin.wallet.CBitcoinSecret("92hM9Lk9Q1S8xVjvNiso94FmBijW2phRA8EB25ewzEiMhGjUm1x") # Private key in WIF format XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
my_public_key = my_private_key.pub
my_address = bitcoin.wallet.P2PKHBitcoinAddress.from_pubkey(my_public_key)

def no_return_script_PubKey():
    return [OP_RETURN]

def public_spendable_script_PubKey():
    return [OP_CHECKSIG]

def get_txin_scriptPubKey():
    return [OP_DUP, OP_HASH160, Hash160(my_public_key),OP_EQUALVERIFY ,OP_CHECKSIG]

def scriptSig(txin, first_txout, second_txout, txin_scriptPubKey):
    signature = create_OP_CHECKSIG_signature_two_outputs(txin, first_txout, second_txout, txin_scriptPubKey, my_private_key)
    return [signature, my_public_key]

def make_transaction(first_amount_to_spend, second_amount_to_spend, txid_to_spend, utxo_index,
                                first_txout_scriptPubKey, second_txout_scriptPubKey):
    first_txout = create_txout(first_amount_to_spend, first_txout_scriptPubKey)
    second_txout = create_txout(second_amount_to_spend, second_txout_scriptPubKey)
    txin_scriptPubKey = get_txin_scriptPubKey()
    txin = create_txin(txid_to_spend, utxo_index)
    txin_scriptSig = scriptSig(txin, first_txout, second_txout, txin_scriptPubKey)

    new_tx = create_signed_transaction_two_outputs(txin, first_txout, second_txout, txin_scriptPubKey,
                                       txin_scriptSig)

    return broadcast_transaction(new_tx)


if __name__ == '__main__':
    first_amount_to_spend = 0.00001
    second_amount_to_spend = 0.00008 
    txid_to_spend = ('7f8ab79cffd80b71bc11f65831ab55ec83f61d36b2dc15075e7d489a345cdc31') # TxHash of UTXO
    utxo_index = 0

    print(my_address) # Prints your address in base58
    print(my_public_key.hex()) # Print your public key in hex
    print(my_private_key.hex()) # Print your private key in hex
    first_txout_scriptPubKey = no_return_script_PubKey()
    second_txout_scriptPubKey = public_spendable_script_PubKey()
    response = make_transaction(first_amount_to_spend, second_amount_to_spend, txid_to_spend, utxo_index, first_txout_scriptPubKey, second_txout_scriptPubKey)
    print(response.status_code, response.reason)
    print(response.text) # Report the hash of transaction which is printed in this section result
