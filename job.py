import requests
from twilio.rest import Client
acc_STD="AC6846f8d49e1d90b506e919335f5da165"
auth_token="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
client=Client(acc_STD,auth_token)
students=["whatsapp:+91xxxxxxxxx","whatsapp:+91xxxxxxxxx"]
url="https://remoteok.com/api"
jobs=requests.get(url).json()
for job in jobs:
    if isinstance(job,dict):
        title=job.get("position","")
        if "java" in title.lower() or "python" in title.lower() or "engineer" in title.lower():
            message=f"""JOB ALERT !!!!
company: {job.get('company')}
role: {title}
link: {job.get('url')}"""
            for student in students:
                client.messages.create(
                    body=message,
                    from_="whatsapp:+14155238886",
                    to=student
                )
            print("message sent")
            break
