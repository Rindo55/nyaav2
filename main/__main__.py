import asyncio
from main.modules.parser import auto_parser
from main import app
from pyrogram import filters, idle
from pyrogram.types import Message
from uvloop import install
from contextlib import closing, suppress
from main.modules.tg_handler import tg_handler



@app.on_message(filters.command(["help","ping"]))
async def start(bot, message: Message):
  return await message.reply_text("⚡ **Bot Is up...**")

async def start_bot():
  print("==================================")
  print("[INFO]: AutoAnimeBot Started Bot Successfully")
  print("==========JOIN @Latest_ongoing_airing_animes=========")

  print("[INFO]: Adding Parsing Task")
  asyncio.create_task(auto_parser())
  asyncio.create_task(tg_handler())
  
  await idle()
  print("[INFO]: BOT STOPPED")
  await app.stop()  
  for task in asyncio.all_tasks():
    task.cancel()
if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(start_bot())
  
