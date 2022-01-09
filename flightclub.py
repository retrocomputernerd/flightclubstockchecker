import requests
import json
import discord
from discord.ext import commands
from discord import Permissions
import string
import os
import random
import time
import sys
import asyncio
from settings import *
bot = discord.Client()

@bot.event
async def on_message(message):
    if message.content.startswith("!fc"):
        sentinfo = format(message.content.split('!fc ')[1])
        searchurl = 'https://sell.flightclub.com/api/public/search?page=1&perPage=20&query=' + sentinfo
        searchrequest = requests.get(searchurl)
        json1 = searchrequest.json()
        resultjson = (json1['results'])
        filteredresult = resultjson[0]
        idnumber = (filteredresult['id'])
        url = 'https://sell.flightclub.com/api/public/products/' + str(idnumber)
        requests2 = requests.get(url)
        json2 = requests2.json()
        img = (json2['imageUrl'])
        title = (json2['name'])
        size4 = (json2['suggestedPrices']['4']['marketPriceCents'])
        size45 = (json2['suggestedPrices']['4.5']['marketPriceCents'])
        size5 = (json2['suggestedPrices']['5']['marketPriceCents'])
        size55 = (json2['suggestedPrices']['5.5']['marketPriceCents'])
        size6 = (json2['suggestedPrices']['6']['marketPriceCents'])
        size65 = (json2['suggestedPrices']['6.5']['marketPriceCents'])
        size7 = (json2['suggestedPrices']['7']['marketPriceCents'])
        size75 = (json2['suggestedPrices']['7.5']['marketPriceCents'])
        size8 = (json2['suggestedPrices']['8']['marketPriceCents'])
        size85 = (json2['suggestedPrices']['8.5']['marketPriceCents'])
        size9 = (json2['suggestedPrices']['9']['marketPriceCents'])
        size95 = (json2['suggestedPrices']['9.5']['marketPriceCents'])
        size10 = (json2['suggestedPrices']['10']['marketPriceCents'])
        size105 = (json2['suggestedPrices']['10.5']['marketPriceCents'])
        size11 = (json2['suggestedPrices']['11']['marketPriceCents'])
        size115 = (json2['suggestedPrices']['11.5']['marketPriceCents'])
        size12 = (json2['suggestedPrices']['12']['marketPriceCents'])
        size125 = (json2['suggestedPrices']['12.5']['marketPriceCents'])
        size13 = (json2['suggestedPrices']['13']['marketPriceCents'])
        size135 = (json2['suggestedPrices']['13.5']['marketPriceCents'])
        size14 = (json2['suggestedPrices']['14']['marketPriceCents'])
        size145 = (json2['suggestedPrices']['14.5']['marketPriceCents'])
        size15 = (json2['suggestedPrices']['15']['marketPriceCents'])
        if str(size4).endswith("0" * 2):
            size4 = str(size4)[:-2]
        if str(size45).endswith("0" * 2):
            size45 = str(size45)[:-2]
        if str(size5).endswith("0" * 2):
            size5 = str(size5)[:-2]
        if str(size55).endswith("0" * 2):
            size55 = str(size55)[:-2]
        if str(size6).endswith("0" * 2):
            size6 = str(size6)[:-2]
        if str(size65).endswith("0" * 2):
            size65 = str(size65)[:-2]
        if str(size7).endswith("0" * 2):
            size7 = str(size7)[:-2]
        if str(size75).endswith("0" * 2):
            size75 = str(size75)[:-2]
        if str(size8).endswith("0" * 2):
            size8 = str(size8)[:-2]
        if str(size85).endswith("0" * 2):
            size85 = str(size85)[:-2]
        if str(size9).endswith("0" * 2):
            size9 = str(size9)[:-2]
        if str(size95).endswith("0" * 2):
            size95 = str(size95)[:-2]
        if str(size10).endswith("0" * 2):
            size10 = str(size10)[:-2]
        if str(size105).endswith("0" * 2):
            size105 = str(size105)[:-2]
        if str(size11).endswith("0" * 2):
            size11 = str(size11)[:-2]
        if str(size115).endswith("0" * 2):
            size115 = str(size115)[:-2]
        if str(size12).endswith("0" * 2):
            size12 = str(size12)[:-2]
        if str(size125).endswith("0" * 2):
            size125 = str(size125)[:-2]
        if str(size13).endswith("0" * 2):
            size13 = str(size13)[:-2]
        if str(size135).endswith("0" * 2):
            size135 = str(size135)[:-2]
        if str(size14).endswith("0" * 2):
            size14 = str(size14)[:-2]
        if str(size145).endswith("0" * 2):
            size145 = str(size145)[:-2]
        size4 = "$" + size4
        size45 = "$" + size45
        size5 = "$" + size5
        size55 = "$" + size55
        size6 = "$" + size6
        size65 = "$" + size65
        size7 = "$" + size7
        size75 = "$" + size75
        size8 = "$" + size8
        size85 = "$" + size85
        size9 = "$" + size9
        size95 = "$" + size95
        size10 = "$" + size10
        size105 = "$" + size105
        size11 = "$" + size11
        size115 = "$" + size115
        size12 = "$" + size12
        size125 = "$" + size125
        size13 = "$" + size13
        size135 = "$" + size135
        size14 = "$" + size14
        size145 = "$" + size145
        from discord_webhook import DiscordWebhook, DiscordEmbed
        webhook = DiscordWebhook(url=webhookurl, username="Flight Club")
        embed = DiscordEmbed(
            title="Lowest Ask for " + title, color='03b2f8'
        )
        embed.set_author(
            name="Flight Club Price Checker",
            url="https://sell.flightclub.com/",
        )
        embed.set_footer(text="Flight Club Price Checker")
        embed.set_timestamp()
        embed.set_image(url=img)
        embed.add_embed_field(name="Size 4", value= size4 , inline=True)
        embed.add_embed_field(name="Size 4.5", value= size45 , inline=True)
        embed.add_embed_field(name="Size 5", value= size5 , inline=True)
        embed.add_embed_field(name="Size 5.5", value= size55 , inline=True)
        embed.add_embed_field(name="Size 6", value= size6 , inline=True)
        embed.add_embed_field(name="Size 6.5", value= size65 , inline=True)
        embed.add_embed_field(name="Size 7", value= size7 , inline=True)
        embed.add_embed_field(name="Size 7.5", value= size75 , inline=True)
        embed.add_embed_field(name="Size 8", value= size8 , inline=True)
        embed.add_embed_field(name="Size 8.5", value= size85 , inline=True)
        embed.add_embed_field(name="Size 9", value= size9 , inline=True)
        embed.add_embed_field(name="Size 9.5", value= size95 , inline=True)
        embed.add_embed_field(name="Size 10", value= size10 , inline=True)
        embed.add_embed_field(name="Size 10.5", value= size105 , inline=True)
        embed.add_embed_field(name="Size 11", value= size11 , inline=True)
        embed.add_embed_field(name="Size 11.5", value= size115 , inline=True)
        embed.add_embed_field(name="Size 12", value= size12 , inline=True)
        embed.add_embed_field(name="Size 12.5", value= size125 , inline=True)
        embed.add_embed_field(name="Size 13", value= size13 , inline=True)
        embed.add_embed_field(name="Size 13.5", value= size135 , inline=True)
        embed.add_embed_field(name="Size 14", value= size14 , inline=True)
        embed.add_embed_field(name="Size 14.5", value= size145 , inline=True)
        webhook.add_embed(embed)
        response = webhook.execute()

bot.run(token,bot=True)
