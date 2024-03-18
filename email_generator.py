import argparse
from openai import OpenAI

client = OpenAI(api_key='Your API Key')
#https://platform.openai.com/api-keys use this 
def generate_email_content(subject):
    try:
        response = client.completions.create(
            model="gpt-3.5-turbo-instruct",  # Specify the model
            prompt=f"Subject: {subject}\n\nBody:",
            max_tokens=100
        )
        email_content = response.choices[0].text.strip()
        return email_content
    except Exception as e:
        print(f"Error generating email content: {e}")
        return None

def generate_email_template(subject, content, button_text, button_link):
    # HTML template
    html_template = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{subject}</title>
    </head>
    <body>
        <div style="text-align: center;">
            <h1>{subject}</h1>
            <p>{content}</p>
            <a href="{button_link}" style="display: inline-block; padding: 10px 20px; background-color: #007bff; color: #ffffff; text-decoration: none;">{button_text}</a>
        </div>
    </body>
    </html>
    """

    return html_template

def save_template_to_file(html_content, filename):
    # Save HTML content to file
    with open(filename, "w") as file:
        file.write(html_content)

if __name__ == "__main__":
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Generate HTML email template")
    parser.add_argument("-s", "--subject", help="Subject of the email", required=True)
    args = parser.parse_args()

    # Generate email content using AI
    email_content = generate_email_content(args.subject)

    if email_content is None:
        print("Failed to generate email content. Exiting.")
        exit(1)

    # Example data for button and link
    button_text = "Click Here"
    button_link = "https://example.com"

    # Generate email template
    html_content = generate_email_template(args.subject, email_content, button_text, button_link)

    # Save template to HTML file
    save_template_to_file(html_content, "email_template_output.html")
