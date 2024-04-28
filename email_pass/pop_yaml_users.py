import crypt, re, subprocess
from jinja2 import Environment, FileSystemLoader

pass_m = 'password_map'

def user_proc():
	tf = 'yaml_user_template'

	file_loader = FileSystemLoader('templates')
	env = Environment(loader=file_loader)
	template = env.get_template(tf)

	text = template.render(user_name=user_name, password_hash=password_hash)
	print(text)


a = subprocess.check_output(['eyaml', 'decrypt', '-f', pass_m]).splitlines()

for i in a:
        i = i.strip()
        match = re.search('^(---|\\.)', i)
        if not match:
                receiver_email,user_name,password_clear = i.split(':')
		password_hash = crypt.crypt(password_clear, crypt.mksalt(crypt.METHOD_SHA512))
		user_proc()
