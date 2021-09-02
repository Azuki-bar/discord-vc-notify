import os
import discord
import discordVc

if __name__ == '__main__':
    proxy = None
    if "HTTP_PROXY" in os.environ:
        proxy = os.environ["HTTP_PROXY"]
    client = discord.Client(proxy=proxy)

    discord_auth = discordVc.GetIdEnvVals()
    if not discord_auth.check_env_vals():
        discord_auth = discordVc.GetIdJson('./.auth_file.json')

    discord_vc = discordVc.DiscordVc(client, discord_auth.channel_id)


    @client.event
    async def on_ready():
        print("login success")


    @client.event
    async def on_voice_state_update(member, before, after):
        if member.bot:
            return
        discord_vc.member = member
        discord_vc.before = before
        discord_vc.after = after
        await discord_vc.send_message()


    client.run(discord_auth.access_token)
