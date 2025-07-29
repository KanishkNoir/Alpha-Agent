from langgraph.prebuilt import create_react_agent
from langgraph_supervisor import create_supervisor
from api.ai.llms import get_openai_llm
from api.ai.tools import get_unread_emails, send_email, research_email

EMAIL_TOOLS = {
    "get_unread_emails": get_unread_emails,
    "send_email": send_email
}
EMAIL_TOOLS_LIST = list(EMAIL_TOOLS.values())
EMAIL_PROMPT = """
You are a helpful assistant for managing emails.
You can get unread emails and send emails.
"""
RESEARCH_PROMPT = """
You are a helpful assistant for researching and preparing email data.
"""

def get_email_agent():
    model = get_openai_llm()
    agent = create_react_agent(
        model=model,
        tools=EMAIL_TOOLS_LIST,
        prompt=EMAIL_PROMPT,
        name="Email Agent"
    )
    return agent

def get_research_agent():
    model = get_openai_llm()
    agent = create_react_agent(
        model=model,
        tools=[research_email],
        prompt=RESEARCH_PROMPT,
        name="Research Agent"
    )
    return agent

#supe = get_supervisor()
#supe.invoke({"messages": [{"role": "user", "content": "Find out how to make a latte and email me the recipe"}]})

def get_supervisor():
    llm = get_openai_llm()
    email_agent = get_email_agent()
    research_agent = get_research_agent()

    supervisor = create_supervisor(
        agents=[email_agent, research_agent],
        model=llm,
        prompt="You are a helpful assistant for managing a research agent and an email agent. You can get unread emails and send emails. Assign work to the research agent and the email agent. When getting unread emails, specify how many hours back to search (e.g., 48 for the last 48 hours, 24 for the last day).",
        name="Email Supervisor"
    ).compile()
    
    return supervisor