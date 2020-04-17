from flask import Blueprint, render_template, request, redirect
import random


bp = Blueprint(__name__, __name__,template_folder='templates')


def random_string(length=16):
	final_string = ''		#creates empty string
	chars = 'abcdefghjklmnopqrstuvwxyz1234567890'

	for i in range (0, length):  #iritiert durch Chars und gibt dann den final string aus
		final_string += chars[random.randint(0, len(chars)-1)]

	return final_string

@bp.route('/createnote', methods =['POST', 'GET']) #allows post form to get the data
def show():
	if request.method == 'POST':
		if request.form.get('createnote'):
			text = request.form.get('notetext')
			
			with open('noteapp/notes/{}.note'.format(random_string()), 'w+') as _file:
				_file.write(text)

				_file.close()

				return redirect('/')
	return render_template('createnote.html') #loads the index and the css via the index