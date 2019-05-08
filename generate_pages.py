from horoscope import generate_prophecies
from datetime import datetime as dt

def generate_page(head, body):
	page = f"<html>{head}{body}</html>"
	return page

def generate_head(title):
	head = f"""<head>
	<meta charset='utf-8'>
	<title>{title}</title>
	</head>
	"""
	return head

def generate_body(header, paragraphs):
	body = f"<h1>{header}</h1>"
	for p in paragraphs:
		body = body + f"<p>{p}</p>"
	
	body = body + f"""
	<hr/><p><a href="about.html">О реализации</a></p>
	"""

	return f"<body>{body}</body>"

def save_page(title, header, paragraphs, output="index.html"):
	fp = open(output, "w")
	today = dt.now().date()
	page = generate_page(
		head=generate_head(title),
		body=generate_body(header=header, paragraphs=paragraphs)
	)
	print(page, file=fp)
	fp.close()


today = dt.now().date()

save_page(
	title="Гороскоп на сегодня",
	header="Что день " + str(today) + " готовит",
	paragraphs=generate_prophecies(),
)

##########  ABOUT.HTML ниже


def generate_about_page(head_about, body_about):
	page_about = f"<html>{head_about}{body_about}</html>"
	return page_about

def generate_about_head(title_about):
	head_about = f"""<head>
	<meta charset='utf-8'>
	<title>{title_about}</title>
	</head>
	"""
	return head_about

def generate_about_body(header_about, times_list, advices_list, promises_list):
	times_about = ""
	for t in times_list:
		times_about = times_about + f"<li>{t}</li>"
	times_about = f"<ul>{times_about}</ul>"

	advices_about = ""
	for a in advices_list:
		advices_about = advices_about + f"<li>{a}</li>"
	advices_about = f"<ul>{advices_about}</ul>"
	
	promises_about = ""
	for p in promises_list:
		promises_about = promises_about + f"<li>{p}</li>"
	promises_about = f"<ul>{promises_about}</ul>"

	body_about = f"""
	<body>
		<h1>О чем все это</h1>
		<img src="horoscope.jpg"width="100", height="100">
		<br/>
		<h2>Параметры генерации:</h2>
		<ol>
			<li>times
			    {times_about}
			<li>advices
				{advices_about}
			<li>promises
				{promises_about}
			</li>
		</ol>
		<a href="index.html">Вернуться на главную страницу
		</a>
	</body>
	</html>"""
	return body_about

def save_about_page(title_about, header_about, output="about.html"):
	fp = open(output, "w")
	times_list = ["Утром", "Днем", "После обеда", "Вечером", "Перед сном", "Ночью"]
	advices_list = ["ожидайте", "предостарегайтесь", "будьте открыты для"]
	promises_list = ["гостей из забытого прошлого", "встреч со старыми знакомыми", "неожиданного праздника","приятных перемен"]
		
	page = generate_about_page(
		head_about=generate_about_head(title_about),
		body_about=generate_about_body(
			header_about=header_about,
			times_list=times_list,
			advices_list=advices_list,
			promises_list=promises_list
		)
	)
	print(page, file=fp)
	fp.close()


save_about_page(
	title_about="О чём все это",
	header_about="О чём все это"
)