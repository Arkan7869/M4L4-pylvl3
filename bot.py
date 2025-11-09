import discord
from discord.ext import commands
from logic import DB_Manager
from config import DATABASE
# Ganti "YOUR_BOT_TOKEN" dengan token botmu
TOKEN = 'YOUR_BOT_TOKEN'

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True

# Prefix perintah
bot = commands.Bot(command_prefix='!')
manager = DB_Manager()
# Event yang terpicu ketika bot siap
@bot.event
async def on_ready():
    print(f'Bot {bot.user.name} siap bekerja!')

# Event yang terpicu ketika anggota baru bergabung
@bot.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.text_channels, name='umum')
    if channel:
        await channel.send(f'Selamat datang di server, {member.mention}!')

# Respon sederhana untuk perintah !ping
@bot.command()
async def ping(ctx):
    await ctx.send('Pong!')

# Perintah !hello yang merespon dengan mention pengguna
@bot.command()
async def hello(ctx):
    await ctx.send(f'Halo, {ctx.author.mention}!')

# Perintah !echo yang mengulangi pesan pengguna
@bot.command()
async def echo(ctx, *, message: str):
    await ctx.send(message)

@bot.command()
async def get_data_market(ctx):
    data = manager.get_data()
    await ctx.send(data)



# Penanganan kesalahan perintah
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Harap tentukan semua argumen yang diperlukan.')
    elif isinstance(error, commands.CommandNotFound):
        await ctx.send('Perintah tidak ditemukan.')
    else:
        await ctx.send('Terjadi kesalahan saat menjalankan perintah.')

# Jalankan bot
bot.run(TOKEN)
