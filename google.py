import asyncio
import os

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from pydantic import SecretStr

from browser_use import Agent

load_dotenv()
api_key = os.getenv('GEMINI_API_KEY')
if not api_key:
	raise ValueError('GEMINI_API_KEY is not set')

llm = ChatGoogleGenerativeAI(model='gemini-2.0-flash-exp', api_key=SecretStr(api_key))


async def run_search(tasks: tuple[str]):
	agent = Agent(
		task=tasks,
		llm=llm,
		max_actions_per_step=4,
	)

	await agent.run(max_steps=25)


if __name__ == '__main__':
	task = (
		'Go to google.com and search for "Travel recommendations for 2 people in Europe in August 2025"',
		'Click on the first result',
		'Print the title and url of the page',
		'Finished'
	)
	asyncio.run(run_search(task))
