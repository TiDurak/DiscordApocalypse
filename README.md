# DiscordApocalypse
Basic Discord crash bot

## Requirements
- Python 3.6.3 and higher
- Python modules:
  - Discord.py 1.7.3 or higher
  - Rich 10.16.1 or higher

## Setup

### 1st stage: Downloading all required modules

Open the console, go to directory with bot (`cd /path/to/bot/`), and type next command:
```pip install -r requirements.txt```
(In Linux you should to use `pip3`)
Open `config.py` file, and update all values in `settings` dictionary.
In `token` put your bot token (or make `APOCALYPSE_TOKEN` environment variable with your token value
in `bot_user` put your *bot (!)* username (Examples: *ExampleBot#1337*, *GoodBot#2468*, *NotBanMePls#2504*)
in `whitelist` put *your (!)* username:
```python
'whitelist': ["Owner#1337"]
```
And if you want your friend to use the bot, put her username too:
```python
'whitelist': ["Owner#1337", "OwnerFriend#1338"]
```
Finally, if you like to use another prefix (`a.` is default), change `prefix` value

*************************************

**Done!** Bot is ready to use. Run the `main.py` file, and crash the servers ^_^
