from __future__ import annotations

from dataclasses import dataclass
from environs import Env

#DataBaseConfig also should be here -_-
@dataclass
class TgBot:
    token: str # our Telegram token
    admin_ids: list[int] # admins id list

@dataclass
class Congif:
    tg_bot: TgBot


def load_config(path: str | None) -> Congif:
    env = Env()
    env.read_env()
    return Congif(tg_bot=TgBot(token=env('BOT_TOKEN'), admin_ids=list(map(int, env.list('ADMIN_IDS')))))