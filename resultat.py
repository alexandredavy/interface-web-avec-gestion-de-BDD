#	coding: utf-8
import cgi , cgitb , sqlite3

def lecture(name):
	try:
		connection = sqlite3.connect("dataUser.db")

		cursor = connection.cursor()
		name = (name,)
		cursor.execute("SELECT * FROM user WHERE userName = ?",name)

		return cursor.fetchone()
	except:
		connection.rollback
		return False
	finally:
		connection.close()


print("Content-type: text/html ; charset = utf-8")

cgitb.enable()

form = cgi.FieldStorage()
recupUserName = form.getvalue("userName")
info = lecture(recupUserName)

try:
	if info[1] == recupUserName:
		html="""
		<!DOCTYPE html>
		<html>
			<head>
				<title>recherche de personne</title>
				<meta charset="UTF-8">
			</head>
			<body>
				<p> """
		print(html)
		print(recupUserName," vit a ",info[2])
		html = """ est bien dans la base de donnees
				</p>
			</body>
		</html>"""
		print(html)
except:
	html="""
	<!DOCTYPE html>
	<html>
		<head>
			<title>recherche de personne</title>
			<meta charset="UTF-8">
		</head>
		<body>
			<p>
				le nom """
	print(html)
	print(recupUserName)
	html = """ n'est pas dans la base de donnees, mais vous pouvez l'ajouter
			</p>
			<form method='post' action='ajout.py'>
			<p>nom:
				<input type='text' name='userName'>  ville:
				<input type='text' name='userCity'>
				<input type='submit' value='envoyer'>
			</p>
		</form>
		</body>
	</html>"""
	print(html)
