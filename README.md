# GenPass

### Program for generating complex passwords

#### Description and recommendations
The script generates a unique password based on three keys: a private key (_PK_), a landmark phrase (_LP_), a local unique key (_LUK-file_).

_PK_ is a secret word or several words that should not be shared with anyone. Come up with a _PK_ that you will definitely never forget. Keep it in your head and don't tell anyone. Good practice, come up with your own _PK_ for each resource.
**If the _PK_ is lost/damaged, it will be impossible to recover the password. Even if other keys are known** 

_LP_ is a phrase/word/character_set that directly or indirectly refers to a resource for generating a password. For example: the name of the site, the comic name of the company, the name of the director of the company, the abstraction associated with the site, and more. 
**If the _LP_ is lost/damaged, it will be impossible to recover the password. Even if other keys are known** 

_LUK-file_ is a file with random characters inside. _LUK-file_ was created in case an ill-wisher wants to take possession of your passwords by using force on you. If there is enough time, delete or modify the _LUK-file_. And then your password can no longer be generated.
**If the _LUK-file_ is lost/damaged, it will be impossible to recover the password. Even if other keys are known** 

> When you first generate a password, the program will require you to specify how many characters will be in the _LUK-file_. The higher the number you specify, the higher the entropy of the key. 

**❗❗❗ I recommend, at the first generation, to save a copy of the _LUK-file_ in a safe place.**

#### Download
```sh
git clone https://github.com/AnDsergey13/GenPass.git
```

#### Running on Linux 
Go to the project folder and run the command in the terminal.
```sh
python Main.py
```
