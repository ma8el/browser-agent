import os

# Optional: Disable telemetry
os.environ["ANONYMIZED_TELEMETRY"] = "false"

# Optional: Set the OLLAMA host to a remote server
os.environ["OLLAMA_HOST"] = "http://localhost:11434"
from langchain_ollama import ChatOllama
from browser_use import Agent
from dotenv import load_dotenv
load_dotenv()

import asyncio


# Initialize the model
llm=ChatOllama(
    model="qwen2.5:7b-instruct-q4_K_M", 
#    model="deepseek-r1:14b",
    num_ctx=6000, 
    temperature=0.5,
    top_p=0.9,
    top_k=0,
)

task="""
1. Go to google.com
2. Decline all cookies
3. Search for 'browser use'
4. Take a screenshot
5. Exit
"""

async def main():
    agent = Agent(
#        task="Go to duckduckgo.com and search for 'browser use'. Make a screenshot. Save the screenshot to the current directory. Finished.",
#        task="Use the first tab. Go to google and search for 'browser use'",
        task=task,
        llm=llm,
#        max_actions_per_step=10,
#        use_vision=True,
#        use_vision_for_actions=True,
    )
    result = await agent.run(max_steps=10)
    print(result)

if __name__ == "__main__":
    asyncio.run(main())