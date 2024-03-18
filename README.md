**Description:**

This tool generates an HTML email template based on a given subject using the GPT-3.5 Turbo Instruct model from OpenAI. It first generates the email content using the provided subject as a prompt, then constructs an HTML template with the generated content. The template includes the subject, email content, and an example button with a link. Finally, it saves the generated HTML template to a file named email_template_output.html.


**Usage:**

 - Ensure you have Python installed on your system.
 - Install the required Python packages using pip install openai.
 - Run the script with the subject of your email as a command-line argument using the ``` -s or --subject option ```.

```python email_generator.py -s "Security Portal Updates"```

**Expected Output:**
```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Security Portal Updates</title>
</head>
<body>
    <div style="text-align: center;">
        <h1>Security Portal Updates</h1>
        <p>Dear Subscriber,</p>
        <p>We are pleased to inform you about the latest updates on our security portal. These updates include...</p>
        <a href="https://example.com" style="display: inline-block; padding: 10px 20px; background-color: #007bff; color: #ffffff; text-decoration: none;">Click Here</a>
    </div>
</body>
</html>
```
