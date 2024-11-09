import base64


def get_base64_image(path: str) -> bytes:
    with open(path, "rb") as brown:
        converted_string = base64.b64encode(brown.read())
        return converted_string
