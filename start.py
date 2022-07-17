import asyncio
import logging
import toml
import os

from vk import VK
from vk import types
from vk.types import message
from vk.utils import TaskManager
from vk.utils.auth_manager import AuthManager

with open("config.toml", "r", encoding="utf-8") as f:
    if "token" in os.environ:
        config = dict(os.environ)
        for key, value in toml.load(f).items():
            if key not in config:
                config[key] = value
    else:
        config = toml.load(f)

logging.basicConfig(level="INFO")
auth = AuthManager(config["user_id"], config["user_password"])
vk = VK(access_token=config["token"])
task_manager = TaskManager(vk.loop)
api = vk.get_api()

async def add_user():
    try:
        await api.messages.add_chat_user(chat_id = config["ID_chat"], user_id = config["ID_your"])
        await api.messages.add_chat_user(chat_id = config["ID_chat"], user_id = config["ID_user_to_add"])
        await api.messages.remove_chat_user(chat_id = config["ID_chat"], user_id = config["ID_your"])
        print("Done")
    except:
        try:
            await api.messages.add_chat_user(chat_id = config["ID_chat"], user_id = config["ID_user_to_add"])
            await api.messages.remove_chat_user(chat_id = config["ID_chat"], user_id = config["ID_your"])
            print("Done")
        except:
            await api.messages.remove_chat_user(chat_id = config["ID_chat"], user_id = config["ID_your"])
            print("User is already in chat or you can't do this without permission")

if __name__ == "__main__":
    task_manager.add_task(add_user)
    task_manager.run()
