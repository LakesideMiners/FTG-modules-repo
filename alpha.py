#    Friendly Telegram (telegram userbot)
#    Copyright (C) 2018-2019 The Authors

#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.

#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

import asyncio
import logging
import wolframalpha
from .. import loader, utils

logger = logging.getLogger(__name__)


@loader.tds
class AlphaMod(loader.Module):
    """Description for module"""  # Translateable due to @loader.tds
    strings = {"name": "WA",
               "doc_app_id": "Your AppID"
              }

    def __init__(self):
        self.config = loader.ModuleConfig("APP_ID", None, lambda m: self.strings("doc_app_id", m))
        
    @loader.unrestricted  # Security setting to change who can use the command (defaults to owner | sudo)
    async def wacmd(self, message):
        """Do the search"""
        app_key = self.config["APP_ID"]
        client = wolframalpha.Client(app_key)
        input_string = utils.get_args_raw(message)
        res = client.query(input_string)
        output = next(res.results).text
        full_string = ("Input: " + input_string + "\n" + "Output: " + output)
        await utils.answer(message, full_string)
