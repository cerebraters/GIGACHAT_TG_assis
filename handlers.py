from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.handlers.callback_query import CallbackQueryHandler

import utils
import text
import kb

from langchain.memory import ConversationBufferMemory



router = Router()
user_conversations = {}

@router.message(Command("start"))
async def start_handler(msg: Message):
    await msg.answer(text.greet.format(name=msg.from_user.full_name),reply_markup=kb.help_keyboard)

@router.callback_query(F.data == "help")
async def input_report(clbck: CallbackQueryHandler, state: FSMContext):
    await clbck.message.answer(text.help, reply_markup=kb.help_keyboard)


@router.message()
async def message_handler(msg: Message):
# Функция, обрабатывающая текстовые сообщения

    user_id = msg.chat.id

    # Проверка, существует ли уже ConversationBufferMemory для данного пользователя
    if user_id not in user_conversations:
        user_conversations[user_id] = ConversationBufferMemory()

    # Обновление конфигурации ConversationChain для текущего пользователя
    utils.conversation.memory = user_conversations[user_id]

    # Получение и отправка ответа через GigaChat
    response = utils.conversation.predict(input=msg.text)
    await msg.answer(f"{utils.conversation.memory.chat_memory.messages[-1].content}",reply_markup=kb.help_keyboard)
    



