#	coding: utf-8
import cgi , cgitb , sqlite3

def ecriture(name,ville):
	connection = sqlite3.connect("dataUser.db")

	cursor = connection.cursor()
	value = (cursor.lastrowid,name,ville)

	cursor.execute("INSERT INTO user VALUES(?,?,?)",value)
	connection.commit()

	connection.close()




print("Content-type: text/html ; charset = utf-8")

cgitb.enable()

form = cgi.FieldStorage()
recupUserName = form.getvalue("userName")
recupUserCity = form.getvalue("userCity")

try:
	ecriture(recupUserName,recupUserCity)

	html="""
	<!DOCTYPE html>
	<html>
		<head>
			<title>recherche de personne</title>
			<meta charset="UTF-8">
		</head>
		<body>
			<p>le nom a bien ete enregistrer</p>
		</body>
	</html>
	"""
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
			<p>il y a un probleme d'enregistrement</p>
		</body>
	</html>
	"""
	print(html)	
