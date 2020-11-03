import discord
from discord.ext import commands

client = commands.Bot(command_prefix="~")

Kurallar = ["Sunucu İçinde Reklamın her türlüsü yasaktır, Reklam cezası bandır.",
"Atatürke, Allaha Ailevi Değerlere Küfür Yasaktır,Kalıcı Jaildir.",
"içinde Irk,Dil Ayrımı Yapmak  yasaktır.",
"ifşa Muhabbetleri Kesinlikle yasaktır ,Cezası kalıcı Jaildir.",
"Siyaset yapmak yasaktır."
]


@client.command()
async def kurallar(ctx):
	await ctx.send("Sunucu İçinde Reklamın her türlüsü yasaktır, Reklam cezası bandır.\nAtatürke, Allaha Ailevi Değerlere Küfür Yasaktır,Kalıcı Jaildir.\niçinde Irk,Dil Ayrımı Yapmak  yasaktır.\nifşa Muhabbetleri Kesinlikle yasaktır ,Cezası kalıcı Jaildir.\nSiyaset yapmak yasaktır.")



@client.event
async def on_ready():
	print("Botunuz hazır üstadım")

@client.command()
async def kural(ctx,*,number):
	await ctx.send(Kurallar[int(number)-1])

	

@client.command(aliases=['c'])
async def clear(ctx,amount=2):
	await ctx.channel.purge(limit=amount)


client.run("NzcwNTM4MzA4NDYzNzU1Mjk1.X5fBuA.qf7hlYpYyby31zjiJ5PozN-6Sj8")
