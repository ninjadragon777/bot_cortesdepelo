import discord
from discord.ext import commands
from model import get_class


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def verificar_adjuntos(ctx):
    if ctx.message.attachments:
        for archivo in ctx.message.attachments:
            nombre = archivo.filename
            url = archivo.url
            await archivo.save(nombre)
            await ctx.send("archivo guardado")
            try:
                class_name = get_class("keras_model.h5", "labels.txt", nombre)
                await ctx.send(class_name)
                if class_name[0] == "taper bajo":
                    await ctx.send("este es un taper fade bajo")
                elif class_name[1] == "taper medio":
                    await ctx.send("este es un taper fade medio")
                elif class_name[2] == "low bajo":
                    await ctx.send("este es un low fade bajo")
                elif class_name[3] == "low medio":
                    await ctx.send("este es un low fade medio")
                elif class_name[4] == "mullet clasico":
                    await ctx.send("este es un mullet clasico")
                elif class_name[5] == "modern mullet":
                    await ctx.send("este es un modern mullet")
                elif class_name[6] == "mohicano bajo":
                    await ctx.send("este es un mohicano bajo")
                elif class_name[7] == "mohicano medio":
                    await ctx.send("este es un mohicano medio")
                elif class_name[6] == "mohicano alto":
                    await ctx.send("este es un mohicano alto")

            except:
                await ctx.send("no se pudo clasificar, recuerde mandar imagenes en formato png, jpg, o jpeg")



    else:
        await ctx.send("No hay archivos adjuntos en este mensaje.")



bot.run()