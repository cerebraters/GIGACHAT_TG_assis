from langchain.chat_models.gigachat import GigaChat
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory

import config

llm = GigaChat(credentials=config.AUTOR_TOKEN, model='GigaChat', verify_ssl_certs=False)
conversation = ConversationChain(
    llm=llm,
    verbose=True,
    memory=ConversationBufferMemory()
    )