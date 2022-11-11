# Secret Santa Assignment Generator

![alt Rudolf assigned to Mrs. Claus](https://github.com/petebuffon/secretsanta/blob/main/example/rudolf.png)

A simple command line program for generating secret santa assignments. Provide a yaml list of names and housholds and a url to generate assignments.

People within the same household will not receive each other as assignments. Outputs a url with parameters including each person's secret assignment! The static website at https://petebuffon.github.io/secretsanta doesn't contain any personal information. Each person's assignment is obscured with a one-time-pad. The key is included with the url so it is not actually secret. The point is someone can generate assignments without knowing the actual assignments themselves.

The message payload is url-safe base64 encoded and has the format:  ciphertext (16 bytes) + random one-time-pad key (16 bytes)

ciphertext = name_length (1 byte) + name + padding (random bytes to message length of 16 bytes) xord with random one-time-pad key

The person visiting the specific url loads main.js which decrypts and displays the person's assignment client side.

## Installation

Clone the repo and install pyyaml
```
$ git clone https://github.com/petebuffon/secretsanta.git
$ cd secretsanta
$ python3 -m pip install -r requirements.txt
```

Create your yaml list of household names (households.yaml)
```
-
  - Rudolf
  - Prancer
  - Blitzen
-
  - Santa Claus
  - Mrs. Claus
-
  - Frosty
```

Generate the assignments
```
$ python secretsanta.py households.yaml https://petebuffon.github.io/secretsanta
https://petebuffon.github.io/secretsanta?name=Rudolf&msg=-jI8kAOS86l1goBmy4cjZPB_TuMtsrDFFPfzWWV0ksg=
https://petebuffon.github.io/secretsanta?name=Prancer&msg=Krq2NM-MoBCC3hnzx2nZPyz8xFu8-Nl3aGl1bzgck8w=
https://petebuffon.github.io/secretsanta?name=Blitzen&msg=x4OytQKP4JKej17LF1o0W8zQ09t27sDR8u4ruLTX9Uk=
https://petebuffon.github.io/secretsanta?name=Santa Claus&msg=BiQiYaOE67crKVDGRq6Q7wB2VwXM6I06Wsu4jR9KIeM=
https://petebuffon.github.io/secretsanta?name=Mrs. Claus&msg=AA_rMyYc6MDyw1GCU1uUAAdfmVJIf42yDU5l6nrikyA=
https://petebuffon.github.io/secretsanta?name=Frosty&msg=vho_VypYBXqZijPw8xAFDLlYUz5eImAU1lbHbz7RM7A=
```
