import random
from pyrogram import Client
from pyrogram.types import Message
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto, InputMediaVideo, Message
from config import LOGGER_ID as LOG_GROUP_ID
from VIPMUSIC import app  
from VIPMUSIC.utils.database import get_assistant
from VIPMUSIC.utils.database import delete_served_chat

photo = [
    "https://mallucampaign.in/images/img_1714463551.jpg",
    "https://mallucampaign.in/images/img_1713935923.jpg",
]

@app.on_message(filters.left_chat_member)
async def on_left_chat_member(_, message: Message):
    try:
        userbot = await get_assistant(message.chat.id)
        
        left_chat_member = message.left_chat_member
        if left_chat_member and left_chat_member.id == (await app.get_me()).id:
            remove_by = message.from_user.mention if message.from_user else "User Tidak Di Ketahui"
            title = message.chat.title
            username = f"@{message.chat.username}" if message.chat.username else "Private Chat"
            chat_id = message.chat.id
            left = f"<b><u>#Keluar Dari Group</u></b> \n\nChat Name : {title}\n\nChat ID : {chat_id}\n\nDiKeluarKan Oleh : {remove_by}\n\nBot : @{app.username}"
            await app.send_photo(LOG_GROUP_ID, photo=random.choice(photo), caption=left)
            await delete_served_chat(chat_id)
            await userbot.leave_chat(chat_id)
    except Exception as e:
        print(f"Error: {e}")
    