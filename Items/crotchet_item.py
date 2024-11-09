from Items.sellable_item import SellableItem
from Items.wool_item import WoolItem


class CrotchetItem(SellableItem):
    wools_used: list[str]
    images: list[str]
    main_image_index: int

    def jsonify(self):
        return {**super().jsonify(),
                "wools_used": self.wools_used,
                "images": self.images,
                "main_image_index": self.main_image_index}
