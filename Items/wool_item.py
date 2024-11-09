from Items.image_handler import get_base64_image
from Items.Item import Item


class WoolItem(Item):
    color: list[int]
    image: bytes

    def jsonify(self):
        # Include color and image in the output
        return {
            **super().jsonify(),
            "color": self.color,
            "image": self.image
        }





BROWN = WoolItem(
    id="0",
    name="חום",
    description="צמר חום ועבה",
    color=[101, 58, 43],
    image=get_base64_image(r"C:\Users\Paz Malul\PycharmProjects\croche\Items\wool_images\brown.jpg")
)

WHITE = WoolItem(
    id="1",
    name="לבן",
    description="צמר לבן נעים ורך",
    color=[255, 255, 250],
    image=get_base64_image(r"C:\Users\Paz Malul\PycharmProjects\croche\Items\wool_images\white.jpg")
)

YELLOW = WoolItem(
    id="2",
    name="צהוב",
    description="צמר צהוב ועבה",
    color=[101, 58, 43],
    image=get_base64_image(r"C:\Users\Paz Malul\PycharmProjects\croche\Items\wool_images\brown.jpg")
)

BLACK = WoolItem(
    id="3",
    name="שחור",
    description="צמר שחור נעים ורך",
    color=[255, 255, 250],
    image=get_base64_image(r"C:\Users\Paz Malul\PycharmProjects\croche\Items\wool_images\white.jpg")
)