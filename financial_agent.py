from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
from dotenv import load_dotenv
import os
import getpass

load_dotenv('.env', override=True)
if 'GROQ_API_KEY' not in os.environ:
    os.environ['GROQ_API_KEY'] = getpass.getpass('GROQ_API_KEY')

# Assuming Groq() needs instantiation with an ID
groq_model = Groq(id='llama-3.3-70b-versatile')

web_search_agent = Agent(
    name='web_search_agent',
    role='search the web for reliable financial data for insightful use',
    model=groq_model,
    tools=[DuckDuckGo()],
    instructions=[
        "Utilize high-quality, trusted financial news sources",
        "Present summaries in a structured format",
        "Always include source links and publication dates",
    ],
    show_tool_calls=True,
    markdown=True,
)

finance_agent = Agent(
    name='finance_ai_agent',
    model=groq_model,
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True,
                         stock_fundamentals=True,
                         company_news=True)],
    instructions=[
        "Display financial data such as stock prices",
        "Summarize key financial trends and insights",
        "Provide actionable recommendations like 'Buy', 'Sell', or 'Hold'",
    ],
    show_tool_calls=True,
    markdown=True,
)

multi_ai_agent = Agent(
    team=[web_search_agent, finance_agent],
    model=groq_model,
    instructions=[
        "Streamline integration between web search and finance agents",
        "Condense financial summaries to highlight essential insights",
        "Cross-verify data for consistency",
        "Use markdown for clear, readable presentation",
    ],
    show_tool_calls=True,
    markdown=True,
)

stock_name = input("Enter the stock ticker symbol you want to analyze (e.g., TSLA for Tesla): ")

# Replace print_response with the correct method to handle response
# Assuming generate_response or a similar method needs to be called
response = multi_ai_agent.print_response(
    f"Summarize {stock_name}'s stock performance for the past week, including the latest analyst recommendations and relevant news. Provide a table with the stock price, analyst recommendations, and company news. Conclude with actionable financial advice based on the current trends, including whether to buy, sell, or hold {stock_name} stock."
)
print(response)
