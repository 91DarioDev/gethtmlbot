# gethtmlbot - send formatted html text messages and get back plain text messages
# Copyright (C) 2017  Dario 91DarioDev <dariomsn@hotmail.it> <github.com/91dariodev>
#
# gethtmlbot is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# gethtmlbot is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with gethtmlbot.  If not, see <http://www.gnu.org/licenses/>.

import logging
import sys
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters)


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)


def error(bot, update, error):
    logger.warning('Update "%s" caused error "%s"' % (update, error))


def help_command(bot, update):
    text = (
        "send here formatted html text messages and get back plain text messages.\n\n"
        "This program is released under the terms of the AGPL-3.0 license. "
        "<a href=\"https://github.com/91DarioDev/gethtmlbot\">View the source code</a>"
    )
    update.message.reply_text(text=text, parse_mode='HTML', disable_web_page_preview=True)


def send_plain_text(bot, update):
    if update.message.text:
        update.message.reply_text(update.message.text_html)
    else:
        text = "This is not a text message. Send here formatted html text messages and get back plain text messages"
        update.message.reply_text(text, quote=True)


def main():
    if len(sys.argv) == 2:
        bot_token = sys.argv[1]
    else:
        print("\n!WARNING!:\nadd the bot token as paramter when running the bot.\nExiting...")
        sys.exit(0)

    print("\nrunning...")
    # define the updater
    updater = Updater(token=bot_token)
    
    # define the dispatcher
    dp = updater.dispatcher

    # commands
    dp.add_handler(CommandHandler(('start', 'help'), help_command))
    # messages
    dp.add_handler(MessageHandler(Filters.all, send_plain_text))

    # handle errors
    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
