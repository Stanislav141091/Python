import base64


class Encode:

    @staticmethod
    def encode_file(file_name):
        with open(file_name, "rb") as image_file:
            data = base64.b64encode(image_file.read())
        return data.decode('utf-8')