import discord
from discord.ext import commands
import pymongo
from pymongo import MongoClient
import urllib.parse
import string
import random


url = open("url.txt", "r").read()
mango_url = url
cluster = MongoClient(mango_url)
db = cluster["UniversityRecords"]
collection = db["GPA"]

class Database(commands.Cog):
  def __init__(self, client):
    self.client = client
  
  @commands.Cog.listener()
  async def on_ready(self):
    print(f'Database cog loaded.')
  
  @commands.command()
  async def add(self, ctx, *, arg):
    var = arg.split(" ")
    rec = {"_id": {"s_id":ctx.author.id, "s_code": var[0]}, "gpa": var[1]}
    collection.insert_one(rec)
    await ctx.send(f'record added.')

  @commands.command()
  async def findall(self, ctx):
    for x in collection.find():
      await ctx.send(f'{x["_id"]["s_code"]} {x["gpa"]}')
  
  @commands.command()
  async def find(self, ctx, *, arg):
    var = arg.split(" ")
    flag = 0
    for i in collection.find():
      if(i["_id"]["s_id"] == ctx.author.id and i["_id"]["s_code"] == var[0]):
        if len(var) > 1:
          if i["gpa"] == var[1]:
            flag = 1
            await ctx.send(f'{i["_id"]["s_code"]} {i["gpa"]}')
        else:
          flag = 1
          await ctx.send(f'{i["_id"]["s_code"]} {i["gpa"]}')
    if(flag == 0):
      await ctx.send(f'record not found.')
  
  @commands.command()
  async def delone(self, ctx, *, arg):
    var = arg.split(" ")
    flag = 0
    rec = {}
    for i in collection.find():
      if (i["_id"]["s_code"] == var[0] and i["gpa"] == var[1]):
        flag = 1
        rec = i
        break
    if flag == 0:
      await ctx.send(f'record does not exist.')
    else:
      print(rec)
      await ctx.send(f'record found and deleted.')
  
  @commands.command()
  async def delall(self, ctx):
    for i in collection.find():
      collection.delete_one(i)
    await ctx.send(f'all records deleted.')

  @commands.command()
  async def insrand(self,ctx):
    for _ in range(10):
      nm = ''.join(random.choices(string.ascii_uppercase, k = 2)) + ''.join(random.choices(string.digits,k=4))
      gpa = random.randint(5,11)
      rec = {"_id": {"s_id":ctx.author.id, "s_code": nm}, "gpa": gpa}
      collection.insert_one(rec)
    await ctx.send(f'added random ten records.')


def setup(client):
    client.add_cog(Database(client))