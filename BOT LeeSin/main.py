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
    elo2 = lol.rank2()

    tier2 = elo2['tier']
    lp2 = elo2['leaguePoints']
    rank2 = elo2['rank']
    wins2 = elo2['wins']
    lossses2= elo2['losses']
    #num2 = roman_to_int(rank2)


    saludos = datos['saludar']
    icon_url = datos['icon_url']
    tier = elo['tier']
    rank = elo['rank']
    lp = elo['leaguePoints']
    wins = elo['wins']
    lossses= elo['losses']
    num = roman_to_int(rank)

    emb= discord.Embed(title="Estadisticas",
    description = f'example',
    color = discord.Colour.dark_magenta()
    )
    emb.set_author(name=saludos,icon_url= icon_url)
    #Inicio ^
    #Solo duo stats v
    emb.add_field(name='Solo/Duo',value=f'{tier} {rank} {lp}PL', inline= True)
    emb.add_field(name='Victorias',value=wins , inline= True)
    emb.add_field(name='Derrotas',value=lossses , inline= True)

    #Flex stats
    emb.add_field(name='Flexible',value=f'{tier2} {rank2} {lp2}PL', inline= True)
    emb.add_field(name='Vistorias',value=wins2 , inline= True)
    emb.add_field(name='Derrotas',value=lossses2 , inline= True)

    #imagen esquina derecha "elo"
    emb.set_thumbnail(url=f'https://opgg-static.akamaized.net/images/medals/{tier.lower()}_{num}.png?image=q_auto:best&v=1')
    emb.set_footer(text='por @JK11LL GitHub.')
    await ctx.send(embed=emb)





bot.run('discord-token') 