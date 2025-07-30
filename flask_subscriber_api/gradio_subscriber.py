import gradio as gr

# def save_email(email):
#     # Basic validation
#     if not email or '@' in email:
#         return "error: Please enter a Valid email address"
    
#     # Save to file
#     with open("subscribers.txt", "a") as f:
#         f.write(email + "\n")
    
#     return f"success: {email} saved successfully!"

import re

def save_email(email):
    # Validate using regex
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if not re.match(pattern, email):
        return "❌ Error: Please enter a valid email address."

    # Save to file
    with open("subscribers.txt", "a") as f:
        f.write(email + "\n")

    return f"✅ {email} saved successfully!"

# Gradio GUI

with gr.Blocks() as demo:
    gr.Markdown("###subscribe to Our Newsletter!###")

    email_input = gr.Textbox(label="Enter your email", placeholder="xyz@gmail.com")
    submit_btn = gr.Button("Subscribe")
    output = gr.Textbox(label="Status")

    submit_btn.click(fn=save_email, inputs=email_input, outputs=output)

# Launching the interface
demo.launch()