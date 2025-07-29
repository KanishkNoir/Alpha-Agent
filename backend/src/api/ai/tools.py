from langchain_core.tools import tool
from api.email_agent.sender import send_mail
from api.email_agent.inbox_reader import read_inbox
from api.ai.services import generate_email_message

@tool
def research_email(query: str) -> str:
    """Research the email based on the query and return the results"""
    response = generate_email_message(query)
    msg = f"Subject: {response.subject}\nBody: {response.content}"
    return msg


@tool
def send_email(subject: str, content: str) -> str:
    """Send an email to the user"""
    try:
        send_mail(subject=subject, content=content)
    except:
        return "Error sending email"
    
    return "Email sent successfully!"


@tool  
def get_unread_emails(hours_ago: int) -> str:
    """Get unread emails from the user's inbox. Specify how many hours back to search (e.g., 48 for last 48 hours)."""
    try:
        emails = read_inbox(hours_ago=hours_ago, verbose=False)
    except:
        return "Error getting unread emails"
    
    cleaned = []
    for email in emails:
        data = email.copy()
        if "html_body" in data:
            data.pop("html_body")
        msg = ""
        for key, value in data.items():
            msg += f"{key}: \t{value}\n"
        cleaned.append(msg)
    return "\n------\n".join(cleaned)
    
    
    