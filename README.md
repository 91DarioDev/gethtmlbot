# gethtmlbot

### This is a Telegram bot. send formatted html text messages and get back plain text messages

## How to install:

### On Linux:

- Move to the path where you want to create the virtualenv directory
```
cd path
```
- Create a folder containing the env named `ghbenv`
```
virtualenv -p python3 ghbenv 
```
- Install the bot from the zip
```
ghbenv/bin/pip install https://github.com/91dariodev/gethtmlbot/archive/master.zip
```
- Run the bot. The first parameter of the command is the token.
```
ghbenv/bin/gethtmlbot token
```
- To upgrade the bot:
```
ghbenv/bin/pip install --upgrade https://github.com/91dariodev/gethtmlbot/archive/master.zip
```
- To delete everything:
```
rm -rf ghbenv
```