import base64
import json
import os
from backend.state import CarState
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail, Attachment, FileContent, FileName, FileType, Disposition

def convert_to_json(state: CarState) -> CarState:
    recipient = str(os.getenv("GMAIL_TO"))
    finalize_output(state, recipient)
    return state


def finalize_output(state: CarState, recipient: str):

    json_output = state.get("output", {})
    json_output = json.dumps(state.get("output", {}), indent=4)

    image_bytes = state.get("image")
    image_name = "car_image.jpg"

    if image_bytes is not None:
        encoded_image = base64.b64encode(image_bytes).decode()
    
    message = Mail(
        from_email=os.getenv("GMAIL_USER"),
        to_emails=recipient,
        subject="Car Information Extraction Result",
        plain_text_content="Below you can find car's details " + json_output 
    )

    attachedFile = Attachment(
        FileContent(encoded_image),
        FileName(image_name),
        FileType('image/jpeg'),
        Disposition('attachment')
    )

    message.attachment = attachedFile

    try:
        sg = SendGridAPIClient(os.getenv("SendGridAPI"))
        response = sg.send(message)
        print(f"Email sent! Status code: {response.status_code}")
    except Exception as e:
        print(f"Error sending email: {e}")