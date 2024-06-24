import random

from pyrogram import *
from pyrogram.types import *

from VIPMUSIC import app
from VIPMUSIC.misc import SUDOERS
from VIPMUSIC.utils.vip_ban import admin_filter

vip_text = [
  "hei tolong jangan ganggu aku.",
  "siapa kamu",
  "Hai",
  "Hanya owner yg bisa memarahiku",
  "Apa?",
  "Apakah kamu suka aku?",
  "Gimana hari hari nya?",
  "Saya butuh teman",
  "Jika kamu memarahi ku nanti aku sedih.",
  "Aku tidak suka sendiri",
  "Apakah kamu mau menemaniku",
  ]
  
strict_txt = [
  "aku tidak bisa membatasi terhadap sahabatku",
  "Apa ini?",
  "Hanya admin",
  "Apakah kamu temanku?",
  "aku tidak bisa hai adalah teman terdekatku",
  "aku mencintainya tolong jangan batasi pengguna ini, cobalah untuk mengerti"
]


ban = ["ban", "boom"]
unban = [
    "unban",
]
mute = ["mute", "silent", "shut"]
unmute = ["unmute", "speak", "free"]
kick = ["kick", "out", "nikaal", "nikal"]
promote = ["promote", "adminship"]
demote = ["demote", "lelo"]
group = ["group"]
channel = ["channel"]


# ========================================= #


@app.on_message(filters.command(["D"], prefixes=["/"]) & admin_filter)
async def restriction_app(app: app, message):
    reply = message.reply_to_message
    chat_id = message.chat.id
    if len(message.text) < 2:
        return await message.reply(random.choice(vip_text))
    bruh = message.text.split(maxsplit=1)[1]
    data = bruh.split(" ")

    if reply:
        user_id = reply.from_user.id
        for banned in data:
            print(f"present {banned}")
            if banned in ban:
                if user_id in SUDOERS:
                    await message.reply(random.choice(strict_txt))
                else:
                    await app.ban_chat_member(chat_id, user_id)
                    await message.reply(
                        "OK, Ban kar diya madrchod ko sala Chutiya tha !"
                    )

        for unbanned in data:
            print(f"present {unbanned}")
            if unbanned in unban:
                await app.unban_chat_member(chat_id, user_id)
                await message.reply(f"Ok, aap bolte hai to unban kar diya")

        for kicked in data:
            print(f"present {kicked}")
            if kicked in kick:
                if user_id in SUDOERS:
                    await message.reply(random.choice(strict_txt))

                else:
                    await app.ban_chat_member(chat_id, user_id)
                    await app.unban_chat_member(chat_id, user_id)
                    await message.reply("get lost! bhga diya bhosdi wale ko")

        for muted in data:
            print(f"present {muted}")
            if muted in mute:
                if user_id in SUDOERS:
                    await message.reply(random.choice(strict_txt))

                else:
                    permissions = ChatPermissions(can_send_messages=False)
                    await message.chat.restrict_member(user_id, permissions)
                    await message.reply(f"muted successfully! Disgusting people.")

        for unmuted in data:
            print(f"present {unmuted}")
            if unmuted in unmute:
                permissions = ChatPermissions(can_send_messages=True)
                await message.chat.restrict_member(user_id, permissions)
                await message.reply(f"Huh, OK, sir!")

        for promoted in data:
            print(f"present {promoted}")
            if promoted in promote:
                await app.promote_chat_member(
                    chat_id,
                    user_id,
                    privileges=ChatPrivileges(
                        can_change_info=False,
                        can_invite_users=True,
                        can_delete_messages=True,
                        can_restrict_members=False,
                        can_pin_messages=True,
                        can_promote_members=False,
                        can_manage_chat=True,
                        can_manage_video_chats=True,
                    ),
                )
                await message.reply("promoted !")

        for demoted in data:
            print(f"present {demoted}")
            if demoted in demote:
                await app.promote_chat_member(
                    chat_id,
                    user_id,
                    privileges=ChatPrivileges(
                        can_change_info=False,
                        can_invite_users=False,
                        can_delete_messages=False,
                        can_restrict_members=False,
                        can_pin_messages=False,
                        can_promote_members=False,
                        can_manage_chat=False,
                        can_manage_video_chats=False,
                    ),
                )
                await message.reply("demoted !")


__MODULE__ = "Ban"
__HELP__ = """
- `Dante`: [Ban or unban] users.
- `Dante`: [Mute, kick, promote, or demote] users.

Example:- ban this user (replied his message).

Note:- use without command.
"""
