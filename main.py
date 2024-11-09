import json

from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


app = FastAPI()

# Define the origins that are allowed to access the API
origins = [
    "*",
]

# Add CORS middleware to the app
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,          # Allows requests from `localhost:3000`
    allow_credentials=True,
    allow_methods=["*"],            # Allows all methods (GET, POST, etc.)
    allow_headers=["*"],            # Allows all headers
)


@app.get('/')
async def root():
    return {}


@app.get('/items/')
async def get_items():
    with open("items/items.json", "r") as file:
        items = json.load(file)

    return items


@app.get('/items/:{item_id}')
async def get_item_by_id(item_id: str):
    with open("items/items.json", "r") as file:
        items = json.load(file)

    # Check if the item with the given ID exists
    if item_id in items:
        return items[item_id]
    else:
        raise HTTPException(status_code=404, detail="Item not found")


@app.post('/items/{item_id}')
async def create_item(item_id: str, request: Request):
    for item in ITEMS:
        if item.id == item_id:
            raise HTTPException(status_code=404, detail="Item already exists")

    # add the item to the list
    # return success code
    

@app.put('/items/{item_id}')
async def update_item(item_id: str, request: Request):
    for item in ITEMS:
        if item.id == item_id:
            # update the item
            # return success code
            pass

    raise HTTPException(status_code=404, detail="Existing item not found")
