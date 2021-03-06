# -*- coding: utf-8 -*-
# Author: Vladimir Pichugin <vladimir@pichug.in>

import sys, bot


if __name__ == "__main__":
    try:
        if "-d" in sys.argv:
            raise ModuleNotFoundError

        from settings_prod import BotSettings

    except ModuleNotFoundError:
        from settings import BotSettings

    bot = bot.Bot(BotSettings)
    
    bot.bots_longpoll_run()
