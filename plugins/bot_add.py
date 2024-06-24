import random
from pyrogram import Client
from pyrogram.types import Message
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto, InputMediaVideo, Message
from config import LOGGER_ID as LOG_GROUP_ID
from VIPMUSIC import app  
from VIPMUSIC.core.userbot import Userbot
from VIPMUSIC.utils.database import delete_served_chat
from VIPMUSIC.utils.database import get_assistant


photo = [
    "https://mallucampaign.in/images/img_1714463551.jpg",
    "https://mallucampaign.in/images/img_1713935923.jpg",
]

@app.on_message(filters.new_chat_members, group=2)
async def join_watcher(_, message):    
    try:
        userbot = await get_assistant(message.chat.id)
        chat = message.chat
        for members in message.new_chat_members:
            if members.id == app.id:
                count = await app.get_chat_members_count(chat.id)
                username = message.chat.username if message.chat.username else "Private Group"
                msg = (
                    f"**📝ᴍᴜsɪᴄ ʙᴏᴛ ᴀᴅᴅ ᴏɴ #ɴᴇᴡ_ɢʀᴏᴜᴘ**\n\n"
                    f"**📌Chat Name:** {message.chat.title}\n"
                    f"**🍂Chat ID:** {message.chat.id}\n"
                    f"**🔐Chat Username:** @{username}\n"
                    f"**📈Group Members:** {count}\n"
                    f"**🤔DiTambahkan Oleh:** {message.from_user.mention}"
                )
                await app.send_photo(LOG_GROUP_ID, photo=random.choice(photo), caption=msg, reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton(f"Add Me!", url=f"tg://openmessage?user_id={message.from_user.id}")]
             ]))
                await userbot.join_chat(f"{username}")
    except Exception as e:
        print(f"Error: {e}")