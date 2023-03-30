"""
class Citron :
	couleur="jaune"


citron1=Citron()
print(Citron.couleur)
citron2=Citron()
print(citron2.couleur)
"""
class Citron :
	def __init__(self,couleur="jaune"):
		self.couleur=couleur
		self.affiche_message()
		affiche_message()

	def affiche_message(self):
		print("Le citron c'est trop bon !")

def affiche_message():
	print("Le citron est bon ")


citron1=Citron("jaune pâle")
citron1.affiche_message()
affiche_message()
#print(citron1.affiche_message())
