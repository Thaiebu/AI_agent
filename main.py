from phi.agent import Agent 
from phi.model.groq import Groq 
from phi.tools.yfinance import YFinanceTools


from dotenv import load_dotenv 
load_dotenv() 
agent = Agent( 
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, company_info=True, company_news=True)],
    instructions=["Use tables to display data"],
    show_tool_calls=True,
    markdown=True
    
    

    ) 

# agent.print_response("Summarize analyst recommendations for NVDA", stream=True)
agent.print_response("Summarize and compare analyst recommendations and fundamentals for TSLA and NVDA")