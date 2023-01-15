# Quantum Key Distribution (QKD)

This code demonstrates a basic implementation of Quantum Key Distribution (QKD) using the keypolarizer module. QKD is a method of securely distributing a secret key between two parties, typically called Alice and Bob, using the principles of quantum mechanics.

## Getting Started

The code prompts the user to enter a message to be sent. The message is then separated into individual characters and converted into their binary equivalent for transmission. The keypolarizer module is used to generate a 16-bit key shared by Alice and Bob, which is then used to produce a set of identical polarizers. The binary data is then sent through these polarizers, and the resulting stream of photons is used to reconstruct the original binary data on the receiving end. The binary data is then converted back to its original text form.

## Prerequisites

- Python 3

## Running the code

To run the code, simply run the script using python command in your terminal.

## Output

The code will output the original message entered by the user, the list of individual characters of the message, the binary equivalent of each character, the stream of photons being sent for each character, the binary data received after being sent through the polarizers, and the final text message received after QKD.


