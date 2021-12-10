# Copyright (C) 2021 By VeezMusicProject

from driver.queues import QUEUE
from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from config import (
    ASSISTANT_NAME,
    BOT_NAME,
    BOT_USERNAME,
    GROUP_SUPPORT,
    OWNER_NAME,
    UPDATES_CHANNEL,
)


@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""**ʜᴇʀᴇ ɪꜱ ᴛʜᴇ ᴏꜰꜰɪᴄɪᴀʟ ꜱᴜᴘᴘᴏʀᴛ ᴄʜᴀᴛ ɢʀᴏᴜᴘ ꜰᴏʀ ꜱᴏʟᴠɪɴɢ ᴜʀ ᴘʀᴏʙʟᴇᴍꜱ ᴀɴᴅ ᴏꜰꜰɪᴄɪᴀʟ ᴜᴘᴅᴀᴛᴇ ᴄʜᴀɴɴᴇʟ ꜰᴏʀ ɴᴇᴡ ʀᴇɢᴜʟᴀʀ ᴜᴘᴅᴀᴛᴇꜱ.**
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ꜱᴜᴘᴘᴏʀᴛ", url=f"https://t.me/creatorpavansupport"
                    ),
                    InlineKeyboardButton(
                        "ᴜᴘᴅᴀᴛᴇꜱ", url=f"https://t.me/theCreatorPavan"
                    ),
                ],
            ]
        ),
        disable_web_page_preview=True,
    )


@Client.on_callback_query(filters.regex("cbhowtouse"))
async def cbguides(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""**ʜᴏᴡ ᴛᴏ ᴜꜱᴇ ᴘᴀᴠᴀɴ ᴛᴜɴᴇꜱ :**

» ꜰɪʀꜱᴛ, ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ. 
» ᴛʜᴇɴ, ᴘʀᴏᴍᴏᴛᴇ ᴍᴇ ᴀꜱ ᴀᴅᴍɪɴɪꜱᴛʀᴀᴛᴏʀ ᴀɴᴅ ɢɪᴠᴇ ᴀʟʟ ᴘᴇʀᴍɪꜱꜱɪᴏɴꜱ ᴇxᴄᴇᴘᴛ ᴀɴᴏɴʏᴍᴏᴜꜱ ᴀᴅᴍɪɴ.
» ᴀꜰᴛᴇʀ ᴘʀᴏᴍᴏᴛɪɴɢ ᴍᴇ, ᴛʏᴘᴇ /reload ɪɴ ɢʀᴏᴜᴘ ᴛᴏ ʀᴇꜰʀᴇꜱʜ ᴛʜᴇ ᴀᴅᴍɪɴ ᴅᴀᴛᴀ.
» ᴀᴅᴅ @PavanTunesAssistant ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴏʀ ᴛʏᴘᴇ /userbotjoin ᴛᴏ ɪɴᴠɪᴛᴇ ʜᴇʀ.
» ᴛᴜʀɴ ᴏɴ ᴛʜᴇ ᴠɪᴅᴇᴏ ᴄʜᴀᴛ ꜰɪʀꜱᴛ ʙᴇꜰᴏʀᴇ ꜱᴛᴀʀᴛ ᴛᴏ ᴘʟᴀʏ ᴍᴜꜱɪᴄ.
» ɪꜰ ᴛʜᴇ ᴜꜱᴇʀʙᴏᴛ ɴᴏᴛ ᴊᴏɪɴᴇᴅ ᴛᴏ ᴠɪᴅᴇᴏ ᴄʜᴀᴛ, ᴍᴀᴋᴇ ꜱᴜʀᴇ ɪꜰ ᴛʜᴇ ᴠɪᴅᴇᴏ ᴄʜᴀᴛ ᴀʟʀᴇᴀᴅʏ ᴛᴜʀɴᴇᴅ ᴏɴ, ᴏʀ ᴛʏᴘᴇ /userbotleave ᴛʜᴇɴ ᴛʏᴘᴇ /userbotjoin ᴀɢᴀɪɴ.

**ɪꜰ ʏᴏᴜ ʜᴀᴠᴇ ᴀ ꜰᴏʟʟᴏᴡ-ᴜᴘ Qᴜᴇꜱᴛɪᴏɴꜱ ᴀʙᴏᴜᴛ ᴛʜɪꜱ ʙᴏᴛ ᴏʀ ᴀ ᴀɴʏ ᴘʀᴏʙʟᴇᴍ ᴛʜᴇɴ ʏᴏᴜ ᴄᴀɴ ᴛᴇʟʟ ɪᴛ ᴏɴ ꜱᴜᴘᴘᴏʀᴛ ᴄʜᴀᴛ ʜᴇʀᴇ: @CreatorPavanSupport**""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 ʙᴀᴄᴋ ʜᴏᴍᴇ", callback_data="cbstart")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbcmds"))
async def cbcmds(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""💞 **ʜᴇʟʟᴏᴡ [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !**

» ꜰᴏʀ ᴋɴᴏᴡɪɴɢ ᴀ ᴄᴏᴍᴍᴀɴᴅ ʟɪꜱᴛ ᴏꜰ ʙʀᴏᴋᴇɴ ᴊᴜꜱᴛ ᴘʀᴇꜱꜱ ᴛʜᴇ ʙᴜᴛᴛᴏɴꜱ ɢɪᴠᴇɴ ʙᴇʟᴏᴡ ᴀɴᴅ ʀᴇᴀᴅ ᴄᴏᴍᴍᴀɴᴅꜱ ᴇxᴘʟᴀɴᴀᴛɪᴏɴ.

**ᴛʜɪꜱ ᴏᴘ ʙᴏᴛ ɪꜱ ꜱᴘᴇᴄɪᴀʟʟʏ ᴅᴇꜱɪɢɴᴇᴅ ʙʏ ᴄʀᴇᴀᴛᴏʀ ᴘᴀᴠᴀɴ.**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("ᴘʟᴀʏᴇʀ", callback_data="cbplay"), 
                    InlineKeyboardButton("ꜱᴜᴅᴏ", callback_data="cbsudo"),
                ],[
                    InlineKeyboardButton("ᴀᴅᴍɪɴ", callback_data="cbadmin"), 
                    InlineKeyboardButton("ᴠɪᴅᴇᴏ", callback_data="cbvideo"),
                ],[
                    InlineKeyboardButton("ᴘᴀᴠᴀɴ", callback_data="cbpavan"), 
                    InlineKeyboardButton("ᴀꜱꜱɪꜱᴛᴀɴᴛ", callback_data="cbassistant"),
                ],[
                    InlineKeyboardButton("ꜱᴛʀᴇᴀᴍ", callback_data="cbstream"), 
                    InlineKeyboardButton("ꜱᴛᴀᴛᴜꜱ", callback_data="cbstatus"),
                ],[
                    InlineKeyboardButton("ᴀʟɪᴠᴇ", callback_data="cbalive"), 
                    InlineKeyboardButton("ᴏᴡɴᴇʀ", callback_data="cbowner"),
                ],[
                    InlineKeyboardButton("ʙᴀꜱɪᴄ", callback_data="cbbasic"),
                    InlineKeyboardButton("ᴅᴏᴡɴʟᴏᴀᴅ", callback_data="cbdownload"),
                ],[
                    InlineKeyboardButton("🔙 ʜᴏᴍᴇ ʙᴀᴄᴋ", callback_data="cbstart")
                ],
            ]
        ),
    )

@Client.on_callback_query(filters.regex("cbbasic"))
async def cbbasic(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""ʙʀᴏᴋᴇɴ ʙᴀꜱɪᴄ ᴄᴏᴍᴍᴀɴᴅꜱ :

» /play [ꜱᴏɴɢ ɴᴀᴍᴇ/ʟɪɴᴋ] - ᴘʟᴀʏ ᴍᴜꜱɪᴄ ᴏɴ ᴠɪᴅᴇᴏ ᴄʜᴀᴛ 
» /stream [Qᴜᴇʀʏ/ʟɪɴᴋ] - ꜱᴛʀᴇᴀᴍ ᴛʜᴇ ʏᴛ ʟɪᴠᴇ/ʀᴀᴅɪᴏ ʟɪᴠᴇ ᴍᴜꜱɪᴄ 
» /vplay [ᴠɪᴅᴇᴏ ɴᴀᴍᴇ/ʟɪɴᴋ] - ᴘʟᴀʏ ᴠɪᴅᴇᴏ ᴏɴ ᴠɪᴅᴇᴏ ᴄʜᴀᴛ 
» /vstream - ᴘʟᴀʏ ʟɪᴠᴇ ᴠɪᴅᴇᴏ ꜰʀᴏᴍ ʏᴛ ʟɪᴠᴇ/ᴍ3ᴜ8 
» /playlist - ꜱʜᴏᴡ ʏᴏᴜ ᴛʜᴇ ᴘʟᴀʏʟɪꜱᴛ 
» /video [Qᴜᴇʀʏ] - ᴅᴏᴡɴʟᴏᴀᴅ ᴠɪᴅᴇᴏ ꜰʀᴏᴍ ʏᴏᴜᴛᴜʙᴇ 
» /song [Qᴜᴇʀʏ] - ᴅᴏᴡɴʟᴏᴀᴅ ꜱᴏɴɢ ꜰʀᴏᴍ ʏᴏᴜᴛᴜʙᴇ 
» /lyrics [Qᴜᴇʀʏ] - ꜱᴄʀᴀᴘ ᴛʜᴇ ꜱᴏɴɢ ʟʏʀɪᴄ 
» /search [Qᴜᴇʀʏ] - ꜱᴇᴀʀᴄʜ ᴀ ʏᴏᴜᴛᴜʙᴇ ᴠɪᴅᴇᴏ ʟɪɴᴋ  
» /ping - ꜱʜᴏᴡ ᴛʜᴇ ʙᴏᴛ ᴘɪɴɢ ꜱᴛᴀᴛᴜꜱ 
» /uptime - ꜱʜᴏᴡ ᴛʜᴇ ʙᴏᴛ ᴜᴘᴛɪᴍᴇ ꜱᴛᴀᴛᴜꜱ 
» /alive - ꜱʜᴏᴡ ᴛʜᴇ ʙᴏᴛ ᴀʟɪᴠᴇ ɪɴꜰᴏ [ɪɴ ɢʀᴏᴜᴘ]

**ᴛʜɪꜱ ᴏᴘ ʙᴏᴛ ɪꜱ ꜱᴘᴇᴄɪᴀʟʟʏ ᴅᴇꜱɪɢɴᴇᴅ ʙʏ ᴄʀᴇᴀᴛᴏʀ ᴘᴀᴠᴀɴ.**""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 ʙʀᴏᴋᴇɴ ʙᴀᴄᴋ", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbadmin"))
async def cbadmin(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""ʙʀᴏᴋᴇɴ ᴀᴅᴍɪɴ ᴄᴏᴍᴍᴀɴᴅꜱ :

» /pause - ᴘᴀᴜꜱᴇ ᴛʜᴇ ꜱᴛʀᴇᴀᴍ 
» /resume - ʀᴇꜱᴜᴍᴇ ᴛʜᴇ ꜱᴛʀᴇᴀᴍ 
» /skip - ꜱᴡɪᴛᴄʜ ᴛᴏ ɴᴇxᴛ ꜱᴛʀᴇᴀᴍ 
» /stop - ꜱᴛᴏᴘ ᴛʜᴇ ꜱᴛʀᴇᴀᴍɪɴɢ 
» /vmute - ᴍᴜᴛᴇ ᴛʜᴇ ᴜꜱᴇʀʙᴏᴛ ᴏɴ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ 
» /vunmute - ᴜɴᴍᴜᴛᴇ ᴛʜᴇ ᴜꜱᴇʀʙᴏᴛ ᴏɴ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ 
» /volume 1-200 - ᴀᴅᴊᴜꜱᴛ ᴛʜᴇ ᴠᴏʟᴜᴍᴇ ᴏꜰ ᴍᴜꜱɪᴄ (ᴜꜱᴇʀʙᴏᴛ ᴍᴜꜱᴛ ʙᴇ ᴀᴅᴍɪɴ) 
» /reload - ʀᴇʟᴏᴀᴅ ʙᴏᴛ ᴀɴᴅ ʀᴇꜰʀᴇꜱʜ ᴛʜᴇ ᴀᴅᴍɪɴ ᴅᴀᴛᴀ 
» /userbotjoin - ɪɴᴠɪᴛᴇ ᴛʜᴇ ᴜꜱᴇʀʙᴏᴛ ᴛᴏ ᴊᴏɪɴ ɢʀᴏᴜᴘ 
» /userbotleave - ᴏʀᴅᴇʀ ᴜꜱᴇʀʙᴏᴛ ᴛᴏ ʟᴇᴀᴠᴇ ꜰʀᴏᴍ ɢʀᴏᴜᴘ

**ᴛʜɪꜱ ᴏᴘ ʙᴏᴛ ɪꜱ ꜱᴘᴇᴄɪᴀʟʟʏ ᴅᴇꜱɪɢɴᴇᴅ ʙʏ ᴄʀᴇᴀᴛᴏʀ ᴘᴀᴠᴀɴ.**""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 ʙʀᴏᴋᴇɴ ʙᴀᴄᴋ", callback_data="cbcmds")]]
        ),
    )

@Client.on_callback_query(filters.regex("cbsudo"))
async def cbsudo(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""ʙʀᴏᴋᴇɴ ꜱᴜᴅᴏ ᴄᴏᴍᴍᴀɴᴅꜱ :

» /rmw - ᴄʟᴇᴀɴ ᴀʟʟ ʀᴀᴡ ꜰɪʟᴇꜱ 
» /rmd - ᴄʟᴇᴀɴ ᴀʟʟ ᴅᴏᴡɴʟᴏᴀᴅᴇᴅ ꜰɪʟᴇꜱ 
» /sysinfo - ꜱʜᴏᴡ ᴛʜᴇ ꜱʏꜱᴛᴇᴍ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ 
» /update - ᴜᴘᴅᴀᴛᴇ ʏᴏᴜʀ ʙᴏᴛ ᴛᴏ ʟᴀᴛᴇꜱᴛ ᴠᴇʀꜱɪᴏɴ 
» /restart - ʀᴇꜱᴛᴀʀᴛ ʏᴏᴜʀ ʙᴏᴛ 
» /leaveall - ᴏʀᴅᴇʀ ᴜꜱᴇʀʙᴏᴛ ᴛᴏ ʟᴇᴀᴠᴇ ꜰʀᴏᴍ ᴀʟʟ ɢʀᴏᴜᴘ

**ᴛʜɪꜱ ᴏᴘ ʙᴏᴛ ɪꜱ ꜱᴘᴇᴄɪᴀʟʟʏ ᴅᴇꜱɪɢɴᴇᴅ ʙʏ ᴄʀᴇᴀᴛᴏʀ ᴘᴀᴠᴀɴ.**""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 ʙʀᴏᴋᴇɴ ʙᴀᴄᴋ", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbplay"))
async def cbplay(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""ʙʀᴏᴋᴇɴ ꜱᴜᴅᴏ ᴄᴏᴍᴍᴀɴᴅꜱ :

» /rmw - ᴄʟᴇᴀɴ ᴀʟʟ ʀᴀᴡ ꜰɪʟᴇꜱ 
» /rmd - ᴄʟᴇᴀɴ ᴀʟʟ ᴅᴏᴡɴʟᴏᴀᴅᴇᴅ ꜰɪʟᴇꜱ 
» /sysinfo - ꜱʜᴏᴡ ᴛʜᴇ ꜱʏꜱᴛᴇᴍ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ 
» /update - ᴜᴘᴅᴀᴛᴇ ʏᴏᴜʀ ʙᴏᴛ ᴛᴏ ʟᴀᴛᴇꜱᴛ ᴠᴇʀꜱɪᴏɴ 
» /restart - ʀᴇꜱᴛᴀʀᴛ ʏᴏᴜʀ ʙᴏᴛ 
» /leaveall - ᴏʀᴅᴇʀ ᴜꜱᴇʀʙᴏᴛ ᴛᴏ ʟᴇᴀᴠᴇ ꜰʀᴏᴍ ᴀʟʟ ɢʀᴏᴜᴘ

**ᴛʜɪꜱ ᴏᴘ ʙᴏᴛ ɪꜱ ꜱᴘᴇᴄɪᴀʟʟʏ ᴅᴇꜱɪɢɴᴇᴅ ʙʏ ᴄʀᴇᴀᴛᴏʀ ᴘᴀᴠᴀɴ.**""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 ʙʀᴏᴋᴇɴ ʙᴀᴄᴋ", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbmenu"))
async def cbmenu(_, query: CallbackQuery):
    if query.message.sender_chat:
        return await query.answer("you're an Anonymous Admin !\n\n» revert back to user account from admin rights.")
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("💡 only admin with manage voice chats permission that can tap this button !", show_alert=True)
    chat_id = query.message.chat.id
    if chat_id in QUEUE:
          await query.edit_message_text(
              f"⚙️ **ʙʀᴏᴋᴇɴ ꜱᴇᴛᴛɪɴɢꜱ ꜰᴏʀ** {query.message.chat.title}\n\n⏸ : ʙʀᴏᴋᴇɴ ᴘᴀᴜꜱᴇ\n▶️ : ʙʀᴏᴋᴇɴ ʀᴇꜱᴜᴍᴇ\n🔇 : ʙʀᴏᴋᴇɴ ᴍᴜᴛᴇ\n🔊 : ʙʀᴏᴋᴇɴ ᴜɴᴍᴜᴛᴇ\n⏹ : ʙʀᴏᴋᴇɴ ꜱᴛʀᴇᴀᴍ ꜱᴛᴏᴘ\n\n© @CreatorPavanNetwork",
              reply_markup=InlineKeyboardMarkup(
                  [[
                      InlineKeyboardButton("⏹", callback_data="cbstop"),
                      InlineKeyboardButton("⏸", callback_data="cbpause"),
                      InlineKeyboardButton("▶️", callback_data="cbresume"),
                  ],[
                      InlineKeyboardButton("🔇", callback_data="cbmute"),
                      InlineKeyboardButton("🔊", callback_data="cbunmute"),
                  ],[
                      InlineKeyboardButton("🗑 ʙʀᴏᴋᴇɴ ᴄʟᴏꜱᴇ", callback_data="cls")],
                  ]
             ),
         )
    else:
        await query.answer("❌ nothing is currently streaming", show_alert=True)


@Client.on_callback_query(filters.regex("cls"))
async def close(_, query: CallbackQuery):
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("💡 only admin with manage voice chats permission that can tap this button !", show_alert=True)
    await query.message.delete()
