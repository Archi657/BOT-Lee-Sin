import discord
from discord import colour
from discord.ext import commands
from utils.api import Lolmain
from utils.number import roman_to_int

bot = commands.Bot(command_prefix='-', description='Lee Sin LOL STATS')

@bot.event
async def on_ready():
    print('Ready to start working')
    print(bot.user.name)

@bot.command()
async def ayuda(ctx):
    await ctx.send('pa casa platita')

@bot.command()
async def yo(ctx,summoner: str):
    lol = Lolmain(summoner,'LAN')
    datos = lol.saludar()
    elo = lol.rank()
    #elo2 = lol.rank2()
    #tier2 = elo2['tier']
    #lp2 = elo2['leaguePoints']
    #rank2 = elo2['rank']

    saludos = datos['saludar']
    icon_url = datos['icon_url']
    tier = elo['tier']
    rank = elo['rank']
    lp = elo['leaguePoints']
    wins = elo['wins']
    lossses= elo['losses']
    num = roman_to_int(rank)

    emb= discord.Embed(title=saludos,
    description = f'SOLO/DUO {tier} {rank} LP: {lp}',
    colour = discord.Colour.blue())

    
    
    emb.add_field(name='Victorias',value=wins , inline= True)
    emb.add_field(name='Derrotas',value=lossses , inline= True)

    #emb.add_field(name=f'Flex {tier2} {rank2} LP: {lp2}' , inline= False)

    emb.set_footer(text='por @JK11LL GitHub.')
    emb.set_image(url=icon_url)
    emb.set_thumbnail(url=f'https://opgg-static.akamaized.net/images/medals/{tier.lower()}_{num}.png?image=q_auto:best&v=1')
    await ctx.send(embed=emb)





bot.run('discord-token-here') 