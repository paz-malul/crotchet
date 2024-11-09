import json

from Items.crotchet_item import CrotchetItem
from Items.image_handler import get_base64_image
from Items.wool_item import BROWN, WHITE

IMAGES_PATH = r"C:\Users\Paz Malul\Desktop\chrochet\post"

# ITEMS: list[CrotchetItem] = [CrotchetItem(
#     id="0",
#     name="צב ים",
#     description="צב ים חמוד וקטן",
#     price=100,
#     stock_amount=10,
#     available=True,
#     wools_used=["0", "1"],
#     images=[get_base64_image(rf"{IMAGES_PATH}\turtle2.png")],
#     main_image_index=0
# ), CrotchetItem(
#     id="1",
#     name="ממש ממש",
#     description="צב ים חמוד וקטן",
#     price=100,
#     stock_amount=10,
#     available=True,
#     wools_used=["0", "1"],
#     images=[get_base64_image(rf"{IMAGES_PATH}\chick_white3.png")],
#     main_image_index=0
# ), CrotchetItem(
#     id="2",
#     name="צדדים",
#     description="צב ים חמוד וקטן",
#     price=100,
#     stock_amount=10,
#     available=True,
#     wools_used=["0", "1"],
#     images=[get_base64_image(rf"{IMAGES_PATH}\bee.png")],
#     main_image_index=0
# ), CrotchetItem(
#     id="3",
#     name="ים ים ים",
#     description="צב ים חמוד וקטן",
#     price=100,
#     stock_amount=10,
#     available=True,
#     wools_used=["0", "1"],
#     images=[get_base64_image(r"C:\Users\Paz Malul\PycharmProjects\croche\Items\crotchet_images\turtle1.jpeg")],
#     main_image_index=0
# ), CrotchetItem(
#     id="4",
#     name="שששש",
#     description="שששש",
#     price=100,
#     stock_amount=10,
#     available=True,
#     wools_used=["0", "1"],
#     images=[get_base64_image(r"C:\Users\Paz Malul\PycharmProjects\croche\Items\crotchet_images\turtle1.jpeg")],
#     main_image_index=0
# ), CrotchetItem(
#     id="5",
#     name="שששדדדד",
#     description="צב ים חמוד וקטן",
#     price=100,
#     stock_amount=10,
#     available=True,
#     wools_used=["0", "1"],
#     images=[get_base64_image(r"C:\Users\Paz Malul\PycharmProjects\croche\Items\crotchet_images\turtle1.jpeg")],
#     main_image_index=0
# )]

# json_items = {}
# for item in ITEMS:
#     json_items[item.id] = item.jsonify()
#
# with open("items.json", "w") as file:
#     json.dump(json_items, file, indent=4)


def add_crotchet_item(key, value):

    with open("items.json", "r") as json_file:
        data = json.load(json_file)

    data[key] = value

    with open("items.json", "w") as json_file:
        json.dump(data, json_file, indent=4)

def drop_database():

    answer = input("enter password: ")
    if answer == "vasilenko":
        with open("items.json", "w") as json_file:
            json.dump({}, json_file, indent=4)
        print("dropped")
    else:
        print("wrong")


item = CrotchetItem(
    id="0",
    name="דבורה",
    description="דבורה מצמר צהוב שחור, כנפיים לבנות, ועם עיניים חומות",
    price=100,
    stock_amount=10,
    available=True,
    wools_used=["1", "2", "3"],
    images=[get_base64_image(rf"{IMAGES_PATH}\bee.png")],
    main_image_index=0
)

add_crotchet_item(item.id, item.jsonify())

# drop_database()
