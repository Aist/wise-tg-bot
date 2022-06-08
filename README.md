Simple Telegram bot for getting Wise account balance.

All what you need is:
- clone repository
- create ```.env``` file (see example at ```env.example``` file)
- add token for you bot
- add Wise API token
- add your Wise profile_id
- add your telegram user id
- start bot ```docker build -t wise-tg-bot ./ && docker run -d wise-tg-bot```

# How to get access token for Wise API
You need to login to your Wise account and go to the https://wise.com/settings/
Find section with API keys and create one. **Important!** Create a token with read-only permission!

# How to get Telegram bot token
Go to the [@BotFather](https://t.me/BotFather) and create a new bot. BotFather knows /help commande. Maybe, it will save you time.

# How to get my Wise profile_id
You can send API request https://api.transferwise.com/v2/profiles (don't forget to add Bearer authorization header). Or, for example, you can get it by the Wise support team?

# How to get your own Telegram user id
For example you can try the [@userbotinfo](https://t.me/userinfobot). Just start this bot and get your user id.
