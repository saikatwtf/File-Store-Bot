# (c) @AbirHasan2005

import asyncio
from configs import Config
from pyrogram import Client
from pyrogram.errors import FloodWait, UserNotParticipant
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message


async def handle_force_sub(bot: Client, cmd: Message):
    try:
        user = await bot.get_chat_member(chat_id=(int(Config.UPDATES_CHANNEL) if Config.UPDATES_CHANNEL.startswith("-100") else Config.UPDATES_CHANNEL), user_id=cmd.from_user.id)
        if user.status == "kicked":
            await bot.send_message(
                chat_id=cmd.from_user.id,
                text="Sᴏʀʀʏ Sɪʀ Yᴏᴜ Aʀᴇ Bᴀɴɴᴇᴅ Fʀᴏᴍ Usᴇɪɴɢ Mᴇ Pʟᴇᴀsᴇ Cᴏɴᴛᴀᴄᴛ [Avishkar](https://t.me/AvishkarPatil).",
                parse_mode="markdown",
                disable_web_page_preview=True
            )
            return 400
    except UserNotParticipant:
        try:
            invite_link = await bot.create_chat_invite_link(chat_id=(int(Config.UPDATES_CHANNEL) if Config.UPDATES_CHANNEL.startswith("-100") else Config.UPDATES_CHANNEL))
        except FloodWait as e:
            await asyncio.sleep(e.x)
            invite_link = await bot.create_chat_invite_link(chat_id=(int(Config.UPDATES_CHANNEL) if Config.UPDATES_CHANNEL.startswith("-100") else Config.UPDATES_CHANNEL))
        except Exception as err:
            print(f"Unable to do Force Subscribe to {Config.UPDATES_CHANNEL}\n\nError: {err}")
            return 200
        await bot.send_message(
            chat_id=cmd.from_user.id,
            text="**Please Join My Updates Channel to use this Bot!**\n\n"
                 "Due to Overload, Only Channel Subscribers can use the Bot!",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🔅Jᴏɪɴ Cʜᴀɴɴᴇʟ Nᴏᴡ🔅", url=invite_link.invite_link)
                    ],
                    [
                        InlineKeyboardButton("Rᴇғʀᴇsʜ 😪", callback_data="refreshForceSub")
                    ]
                ]
            ),
            parse_mode="markdown"
        )
        return 400
    except Exception:
        await bot.send_message(
            chat_id=cmd.from_user.id,
            text="Sᴏᴍᴇᴛʜɪɴɢ Wᴇɴᴛ Wʀᴏɴɢ Cᴏɴᴛᴀᴄᴛ [Avi](https://t.me/AvishkarPatil).",
            parse_mode="markdown",
            disable_web_page_preview=True
        )
        return 400
    return 200
