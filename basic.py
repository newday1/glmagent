from langchain_core.messages import HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv

load_dotenv()


# 创建 LLM 实例
llm = ChatOpenAI(
    temperature=0.7,
    model=os.getenv("GLM_MODEL"),
    api_key=os.getenv("GLM_API_KEY"),
    base_url=os.getenv("GLM_BASE_URL"),
)

# 创建消息
messages = [
    SystemMessage(content="你是一个有用的 AI 助手"),
    HumanMessage(content="请介绍一下人工智能的发展历程"),
]

# 调用模型
response = llm.invoke(messages)
print(response.content)

