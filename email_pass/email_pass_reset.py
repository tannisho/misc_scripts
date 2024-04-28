import re
import subprocess
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from jinja2 import Environment, FileSystemLoader

pass_m = 'pw/password_map_last'

def email_proc():
	email_subject = 'xRDP Password Reset Credentials'
	sender_email = 'root@sicura1.test.local'
	tf = 'password_reset_template'

	file_loader = FileSystemLoader('templates')
	env = Environment(loader=file_loader)
	template = env.get_template(tf)

	text = template.render(first_name=first_name, username=username, password=password)
#	print(text)

	msg = MIMEMultipart('alternative')
	msg['Subject'] = email_subject
	msg['From'] = sender_email
	msg['To'] = receiver_email

	part = MIMEText(text, 'plain')
	msg.attach(part)

# uncomment to send emails #
#	s = smtplib.SMTP('localhost')
#	s.sendmail(sender_email, receiver_email, msg.as_string())
#	s.quit()



a = subprocess.check_output(['eyaml', 'decrypt', '-f', pass_m]).splitlines()

for i in a:
        i = i.strip()
        match = re.search('^(---|\\.)', i)
        if not match:
                receiver_email,username,password = i.split(':')
                email_split = receiver_email.split('.')
                first_name = email_split[0]
                first_name = first_name.capitalize()
		email_proc()
