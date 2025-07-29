from api.ai.llms import get_openai_llm
from api.ai.tools import get_unread_emails, send_email

EMAIL_TOOLS = {
    "get_unread_emails": get_unread_emails,
    "send_email": send_email
}

def email_assistant(query: str):
    llm_base = get_openai_llm()
    llm = llm_base.bind_tools(list(EMAIL_TOOLS.values()))
    messages = [
        {
            "role": "system",
            "content": "You are an assistant for managing emails. You can get unread emails and send emails. When getting unread emails, specify how many hours back to search (e.g., 48 for the last 48 hours, 24 for the last day)."
        },
        {
            "role": "user",
            "content": f"{query}"
        }
    ]
    response = llm.invoke(messages)
    
    if hasattr(response, "tool_calls") and response.tool_calls:
        tool_results = []
        
        for tool_call in response.tool_calls:
            tool_name = tool_call["name"]
            tool_function = EMAIL_TOOLS.get(tool_name)
            tool_args = tool_call.get("args", {})
            
            if not tool_function:
                continue
                
            if tool_name == "get_unread_emails" and "hours_ago" not in tool_args:
                tool_args = tool_args.copy()
                tool_args["hours_ago"] = 48
                
            result = tool_function.invoke(tool_args)
            tool_results.append(f"Tool '{tool_name}' result: {result}")
        
        if tool_results:
            results_text = "\n\n".join(tool_results)
            new_messages = [
                {
                    "role": "system",
                    "content": "You are an assistant for managing emails. Provide a helpful response based on the tool results."
                },
                {
                    "role": "user",
                    "content": f"Original request: {query}\n\nTool results:\n{results_text}\n\nPlease provide a helpful summary or response based on these results."
                }
            ]
            final_response = llm_base.invoke(new_messages)
            return final_response
    
    return response