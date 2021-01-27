from fastapi import FastAPI
from typing import Optional
from random import choice
from loader import iload, nload

app = FastAPI(docs_url=None)

compliments = iload("random")
names = nload()
nouns, adjectives = compliments['nouns'], compliments['adjectives']
many_cap = 32

def clamp(min: int, max: int, num: int):
    if num > max: return max
    if num < min: return min
    return num

def get_an(word):
    if word[0] in 'aeiou':
        return f"an {word}"
    return f"a {word}"

def get_one(name):
    adj, noun = choice(adjectives), choice(nouns)
    compliment = f"{name} is {get_an(adj)} {noun}"
    data = {
        "status": "ok",
        "compliment": compliment
    }
    return data

def get_two(name):
    adj, adj2, noun = choice(adjectives), choice(adjectives), choice(nouns)
    compliment = f"{name} is {get_an(adj)} {adj2} {noun}"
    data = {
        "status": "ok",
        "compliment": compliment
    }
    return data

def get_one_many(name, amount: int):
    amount = clamp(1, many_cap, amount)
    compliments = [data['compliment'] for data in [get_one(name) for _ in range(amount)]]
    data = {
        "status": "ok",
        "compliments": compliments
    }
    return data

def get_two_many(name, amount: int):
    amount = clamp(1, many_cap, amount)
    compliments = [data['compliment'] for data in [get_two(name) for _ in range(amount)]]
    data = {
        "status": "ok",
        "compliments": compliments
    }
    return data

@app.get("/")
async def get_main():
    endpoints = [
        "/compliment/random",
        "/compliment/random/<name>",
        "/compliment/random/<name>/<amount>",
        "/compliment/randomdouble",
        "/compliment/randomdouble/<name>",
        "/compliment/randomdouble/<name>/<amount>",
        "/compliment/list/adjectives",
        "/compliment/list/nouns"
    ]
    return endpoints

@app.get("/compliment/random")
async def get_one_compliment():
    return get_one(choice(names))

@app.get("/compliment/randomdouble")
async def get_two_compliments():
    return get_two(choice(names))

@app.get("/compliment/random/{name}/{amount}")
async def get_one_many_named(name: str, amount: int):
    return get_one_many(name, amount)

@app.get("/compliment/randomdouble/{name}/{amount}")
async def get_one_many_named(name: str, amount: int):
    return get_two_many(name, amount)

@app.get("/compliment/random/{name}")
async def get_one_compliment_named(name: str):
    return get_one(name)

@app.get("/compliment/randomdouble/{name}")
async def get_two_compliments_named(name: Optional[str]):
    return get_two(name)

@app.get("/compliment/list/adjectives")
async def get_adj():
    return adjectives

@app.get("/compliment/list/nouns")
async def get_nouns():
    return nouns
