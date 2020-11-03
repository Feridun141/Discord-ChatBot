import discord
from discord.ext import commands

client = commands.Bot(command_prefix="~")

@client.event
async def on_ready():
	print("Botunuz hazır üstadım")

@client.command()
async def kufur1(ctx):
	await ctx.send("Lütfen küfür etmeyiniz aksi taktirde BANLANABİLİRSİNİZ.")

@client.command()
async def kufur2(ctx):
	await ctx.send("Lütfen küfür etmeyiniz aksi taktirde BANLANABİLİRSİNİZ.")


@client.command()
async def kufur3(ctx):
	await ctx.send("Lütfen küfür etmeyiniz aksi taktirde BANLANABİLİRSİNİZ.")



client.run("NzczMDY3NTE4NzA0ODc3NTc4.X6D1Ow.PmYY45DZkE1W2_p8CRgQm9oJpfY")



