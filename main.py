import discord
from discord.ext import commands

intents = discord.Intents.default()

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f'✅ Bot đã đăng nhập: {bot.user}')
    try:
        synced = await bot.tree.sync()  # Đồng bộ slash command với Discord
        print(f'🔁 Đã sync {len(synced)} slash command.')
    except Exception as e:
        print(f'❌ Lỗi khi sync lệnh: {e}')

# Slash command thực sự
@bot.tree.command(name="script", description="Gửi đoạn script Roblox mới nhất")
async def script_command(interaction: discord.Interaction):
    code = 'loadstring(game:HttpGet("https://raw.githubusercontent.com/Dex-Bear/VxezeHubHopBoss/refs/heads/main/SkidConCacBaM"))()'
    await interaction.response.send_message(f"```lua\n{code}\n```")

bot.run("TOKEN_CỦA_BẠN")
