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
  


  





