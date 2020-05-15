import discord

client = discord.Client()


@client.event
async def on_message(message):
    message.content.lower()
    if message.author == client.user:
        return
    if message.content.startswith("hello"):
        await message.channel.send("Hello , Iam a test bot")
        if message.author == "Your discord username":
            await message.channel("Hello and " + message.author + "!!")


client.run('Your bot token')
