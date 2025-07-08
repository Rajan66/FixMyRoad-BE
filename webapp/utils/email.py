import os

from django.core.mail import EmailMultiAlternatives
from dotenv import load_dotenv

from .email_token import generate_verification_token

load_dotenv()


def send_verification_email(user):
    token = generate_verification_token(user)
    verification_url = f"http://localhost:8000/api/v1/auth/verify-email/?token={token}"

    subject = "Verify Your Email Address"
    from_email = os.getenv("EMAIL_HOST_USER")
    to_email = [user.email]
    print(from_email)
    print(to_email)

    text_content = f"Click the link to verify your email: {verification_url}"
    html_content = f"""
        <html>
            <body>
                <p>Hi {user.email},</p>
                <p>Please verify your email by clicking the button below:</p>
                <a href="{verification_url}" 
                   style="display: inline-block; padding: 10px 20px; background-color: #28a745; 
                          color: white; text-decoration: none; border-radius: 5px;">
                    Verify Email
                </a>
                <p>If the button doesn't work, copy and paste this link in your browser:</p>
                <p>{verification_url}</p>
            </body>
        </html>
    """

    try:
        email = EmailMultiAlternatives(subject, text_content, from_email, to_email)
        email.attach_alternative(html_content, "text/html")
        email.send()
        print("Email sent successfully")
    except Exception as e:
        print("Failed to send email:", e)
