from langchain.agents import create_agent
from langchain_openai import ChatOpenAI


def get_weather(city: str) -> str:
    """Get weather for a given city."""
    return f"It's always sunny in {city}!"


# 创建 GLM 模型实例
llm = ChatOpenAI(
    temperature=0.7,
    model="glm-4.6",
    api_key="6b01faf1b6ce4b6f87e9a0101d1c1b7c.9puVkn1V5vH4WOj2",
    base_url="https://open.bigmodel.cn/api/paas/v4/",
)

agent = create_agent(
    model=llm,
    tools=[get_weather],
    system_prompt="You are a helpful assistant",
)

# Run the agent
response = agent.invoke(
    {"messages": [{"role": "user", "content": "what is the weather in sf"}]}
)
print(response)
