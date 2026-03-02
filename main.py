from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv("TOKEN")

server = smtplib.SMTP_SSL('smtp.gmail.com:465')

email = "karinakaa1966@gmail.com"
server.login(email, password=TOKEN)
feature_lessons =  ["Github", "API", "JS"]
finish_lessons = ["Введение Python", "Командная строка", "Веб-разработка"]
monthes = "6 месяцев"
email_to = 'karinakaa1966@gmail.com'
subject = 'Варр приде к вам'
text = f'Привет Мама(Папа), я занимаюсь в школе третье место уже {monthes}. В процессе я выполнил модули: {finish_lessons}! Сейчас я работаю над модулями {feature_lessons}. Обучение мне нравится, я получил море знаний!'
alternative_text = f"Привет Мама(Папа), я занимаюсь в школе третье место уже {monthes}. Сейчас я работаю над модулями {finish_lessons}. Пока что я улучшаю свои навыки и узнаю много нового!"

server.sendmail(email_from, email, f"Subject: {subject}\n\n{text}")
