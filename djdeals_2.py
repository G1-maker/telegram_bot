from telethon import TelegramClient, events
import os
import asyncio

# మీ Telegram API credentials
api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")
bot_token = os.getenv("BOT_TOKEN")

# Source and Destination Channel usernames or IDs
source_channels = ['@DealsLootersZone']  # ఉదా: '@deals_channel'
destination_channel = '@ExtraPeBot'  # ఉదా: '@my_deals_channel'

client = TelegramClient('bot', api_id, api_hash)

@client.on(events.NewMessage(chats=source_channels))
async def forward_deals(event):
    try:
        await client.send_message(destination_channel, event.message)
        print("Message forwarded.")
    except Exception as e:
        printf ("Error: {e}")

async def main():
    print("Bot is starting")
    await client.start(bot_token=bot_token)
    print("Bot is running...")
    await client.run_until_disconnected()

if __name__ == "__main__":
    asyncio.run(main())