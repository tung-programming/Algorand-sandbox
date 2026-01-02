# Algorand setup instructions

## Prerequisites

- Python
- Docker
- git bash

###

### Creating docker image

Go to the directory where u cloned my repo

```
./sandbox up dev
```

Check Stutus

```
./sandbox Status
```

Enter Algod mode

```
./sandbox enter Algod
```

Creating a new wallet

```
goal wallet new t --unencrypted
```

Creating address in that wallet

```
goal account new --wallet tab
```

Check ur account in the wallet

```
goal account list --wallet t
```

Since we opened dev mode there are already accounts pre-funded
Do

```
goal account list
```

Transfer microalgo from funded to your account

```
goal clerk send --amount 1000000 --from PASTE_FUNDED_ADDRESS --to YOUR-WALLET-address
```

Check the balance

```
goal account list --wallet t
```

exit the algod mode

```
exit
```

Create the main function file and compile it(Aldready present no need to do this)

```
touch counter.py
touch compile.py
```

Install pyteal and compile pyteal to teal(use venv if needed)

```
python -m pip install pyteal
```

run compile.py file to create the actual teal file

```
python compile.py
```

This creates approval.teal and clear.teal
Add these 2 files to sandbox

```
./sandbox copyTo approval.teal
./sandbox copyTo clear.teal
```

Reenter Algod mode

```
./sandbox enter algod
```

Check their existance by

```
ls /opt/data
```

Create the app(After successful creation you will get an APPID)

```
goal app create --creator Created_address --approval-prog /opt/data/approval.teal --clear-prog /opt/data/clear.teal --global-byteslices 1 --global-ints 1 --local-byteslices 0 --local-ints 0 --wallet t
```

Save the APPID

Check the current value of counter

```
goal app read --app-id APPID --global
```

Increment its value

```
goal app call --app-id APPID --from OUR_ADDRESS --wallet t
```

Create another wallet and an address and try changing the same value
