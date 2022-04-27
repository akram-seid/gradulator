from telegram import *
from telegram.ext import *
import datetime
import schedule
import time
from telethon import TelegramClient, events, sync
from telethon.tl.functions.channels import EditPhotoRequest
from telethon.tl.types import InputChatUploadedPhoto

bot = Bot("5326330995:AAFBG5l-w9Ks5ZCRwUEQwInCp7-RDzmxy58")
updater = Updater("5326330995:AAFBG5l-w9Ks5ZCRwUEQwInCp7-RDzmxy58", use_context=True)
api_id = 12293617
api_hash = 'ab44a1c03e0ba1bfddb152ba80bb403d'
phone = '+251908837083'
################################################
channel_username = "csinfo2"
################################################

client = TelegramClient('session_name',
                        api_id,
                        api_hash,
                        )
client.connect()
client.start()
channel_entity = client.get_entity(channel_username)


def send_messages():
    present = datetime.datetime.now().date()
    future = datetime.datetime(2022, 8, 6).date()
    difference = future - present

    bot.send_photo(-1001206131058, photo=open("assets/" + str(difference.days) + ".jpeg", 'rb'),
                   caption=str(difference.days) + "* Days until Graduation!*",
                   parse_mode="MARKDOWN")


def change_pic():
    present = datetime.datetime.now().date()
    future = datetime.datetime(2022, 8, 6).date()
    difference = future - present
    upload_file_result = client.upload_file(file="asset/" + str(difference.days) + ".png")
    input_chat_uploaded_photo = InputChatUploadedPhoto(upload_file_result)
    try:
        result = client(EditPhotoRequest(channel=channel_entity,
                                         photo=input_chat_uploaded_photo))
    except BaseException as e:
        print(e)


schedule.every().day.at("00.00").do(lambda: send_messages())
schedule.every(10).days.at(00.00).do(lambda: change_pic())

while 1:
    schedule.run_pending()
    time.sleep(1)
