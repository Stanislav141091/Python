import pyautogui


class UploadImage:

    @staticmethod
    def upload_image(file_name):
        pyautogui.write(file_name, interval=0.25)
        pyautogui.press('return')