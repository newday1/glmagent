from langchain_core.messages import HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI

# 创建 LLM 实例
llm = ChatOpenAI(
    temperature=0.7,
    model="glm-4.6",
    api_key="6b01faf1b6ce4b6f87e9a0101d1c1b7c.9puVkn1V5vH4WOj2",
    base_url="https://open.bigmodel.cn/api/paas/v4/",
)

# 创建消息
messages = [
    SystemMessage(content="你是一个有用的 AI 助手"),
    HumanMessage(content="请介绍一下人工智能的发展历程"),
]

# 调用模型
response = llm.invoke(messages)
print(response.content)
