#	coding: utf-8
import cgi
import datetime

print("Content-type: text/html ; charset = utf-8")

alex = str(datetime.datetime.now().hour)

html="""

<!DOCTYPE html>
<html>
	<head>
		<title>recherche de personne</title>
		<meta charset="UTF-8">
	</head>
	<body>
		<p>il est: """
print(html)

print(alex)

html = """h</br></br> entrer le nom que vous voulez chercher dans la base de donnees
		</p>
		<form method='post' action='resultat.py'>
			<p>
				<input type='text' name='userName'>
				<input type='submit' value='envoyer'>
			</p>
		</form>
		<p><a href="list.py">liste des personnes de la bdd</a></p>
	</body>
</html>

"""


print(html)