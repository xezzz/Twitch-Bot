from Bot.Bot import TwitchBot
from discord import Intents


if __name__ == "__main__":

    i = Intents.default()
    i.members = True
    i.guilds = True
    i.emojis = True

    args = {
        "command_prefix": "%", # doesn't really matter, since there aren't any commands
        "case_senitive": True,
        "max_messages": 1000,
        "intents": i,
        "chunk_guilds_at_startup": True
    }

    bot = TwitchBot(**args)
    bot.run()
