# In this experience, I aim to work practically with the Bitcoin network.
## The steps and sections of this project are:
1. Perform Transactions: Learning how to send and receive Bitcoin transactions, gaining hands-on experience with how transactions are constructed, signed, and broadcasted in the network.
2. Test Blockchain Mechanisms: Exploring and testing various fundamental mechanisms of the Bitcoin network, such as block mining. This will help you understand the process of adding new blocks to the blockchain and the role of miners.

## Why Use Testnet?
The main Bitcoin network (Mainnet) involves real costs and requires you to pay transaction fees in Bitcoin. To avoid these costs, we’ll be using the Testnet, a testing environment that mimics the Mainnet but with valueless Bitcoins. This means you can experiment freely without any financial risk.

## Key Features of Testnet:
- Technical Similarity: The Testnet is technically identical to the Mainnet, so anything you successfully implement on the Testnet should work on the Mainnet.
- No Real Value: Bitcoins on the Testnet have no real-world value, which makes it a safe environment for testing and development.
- Independent Blockchain: The Testnet operates on its independent blockchain, separate from the Mainnet, ensuring there is no overlap or interference between the two.


# Questions and Sections
## Question 1: Generating Address and Corresponding Key Using Elliptic Curve
To generate an address and its corresponding key, I used the Elliptic Curve Digital Signature Algorithm (ECDSA). Here's the process I followed:
  1. Private Key Generation: I generated a 256-bit random number as the private key using the 'secrets' library.
  2. WIF Format Conversion: I converted the private key to Wallet Import Format (WIF). This involved:
     -  Extending the key with “0xef”.
     -  Optionally, for compression, extending the key with “0x01”.
     -  Finding the checksum by performing SHA-256 twice and taking the first 4 bytes.
     -  Encoding the result in base58 to obtain the WIF.

### Using EllipticalCurve.py
  Instead of using the pre-built ecdsa library, I implemented the required steps manually in EllipticalCurve.py as per the project requirements. The process included taking the SHA-256 hash and then the RIPEMD-160 hash of the public key.

### Address Generation for Network
To generate an address:
  -  I performed SHA-256 and RIPEMD-160 hashing on the public key.
  -  For Testnet addresses, I prefixed the result with “0x6f”. For Mainnet addresses, I would have used “0x00”.
  -  I calculated the checksum and appended it to the result.
  -  The final address was encoded in base58.

## Question 2: Key Generation Loop
I created multiple keys using a 'while' loop until the desired conditions were met, demonstrating control over key generation processes.

### Performing Transactions
The code for this part is labeled as Q2P, with a separate file for spending transactions (_2), and additional utility functions added to utils.py. I used transaction.py with modifications for this purpose.

### Transaction Outputs
1. Spendable by All: I used 'OP_CHECKSIG' so that anyone could apply a signature and use the output.
2. Non-Spendable: I used OP_RETURN, which always returns to the top of the stack, making it unusable for signatures.

### Redeeming Outputs
To redeem outputs that anyone can spend, I applied my signature.

### Transaction Confirmation
After performing a transaction, there is a necessary waiting period for confirmation. Given the low fees allocated for miners, this process took a significant amount of time.

### Special Script
For a specific script, I used OP_ADD and OP_SUB to calculate the sum and difference of two numbers, validating the transaction if the correct values were entered. This allowed anyone with the correct numbers to complete the transaction and return the funds to their address.

### Script Output
The script output was a P2PKH (Pay-to-PubKey-Hash) script sending 6.25 BTC to our address. This included calculating the Merkle root using the serialize() method to obtain the stream format since the Merkle root equals the coinbase (with only one transaction here).

### Mining
To mine, I calculated the target from the nBits based on difficulty, set to have four leading zeros (“0x1f010000”).

### Block Header Creation
I partially created the block header and appended the nonce, hashing it twice with SHA-256.

### Mining Process
I iterated the nonce from zero to the maximum, checking each result against the target. If the condition was met, the block was mined and outputted; otherwise, the process continued.



## Summary of the goal:
This project demonstrates a comprehensive understanding of Bitcoin's technical operations, from key and address generation to transaction creation and mining, learning and practicing fundemental informaiton and details in blockchain.

  


  





