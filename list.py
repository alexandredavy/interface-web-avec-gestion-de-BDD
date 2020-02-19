#	coding: utf-8
import cgi , cgitb , sqlite3

print("Content-type: text/html ; charset = utf-8")

cgitb.enable()

def info():
	connection = sqlite3.connect("dataUser.db")
	cursor = connection.cursor()
	cursor.execute("SELECT * FROM user")
	info = cursor.fetchall()
	connection.close()
	return info

info = info()

html="""
<!DOCTYPE html>
<html>
	<head>
		<title>recherche de personne</title>
		<meta charset="UTF-8">
		<style>
			table{
			  border-collapse: collapse
			}

			td{
			  border: 1px solid black;
			  padding: 10px;
			}
		</style>
	</head>
	<body>
		<table>
			<tr>
				<td><strong>noms :</strong></td>"""
print(html)

for Id, name, city in info:
	print("						<td>",name,"</td>")

html = """
			</tr>
			<tr>
				<td><strong>villes :</strong></td>"""
print(html)

for Id,name,city in info:
	print("					<td>",city,"</td>")

html = """
			</tr>
		</table>
	</body>
</html>
"""
print(html)