import os
from config import Config
from .fonts import Fonts
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(filters.command('start'))
async def start(c, m):
    owner = await c.get_users(int(Config.OWNER_ID))
    owner_username = owner.username if owner.username else 'Ns_bot_updates'

    # start text
    text = f"""𝗛𝗲𝘆 {m.from_user.mention(style='md')},

     𝘀𝗲𝗻𝗱**/id**
**🧸𝗯𝘆:** {owner.mention(style='md')}
"""

