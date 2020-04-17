from flask import Blueprint, render_template
import glob #lists files inside of directories


bp = Blueprint(__name__, __name__,template_folder='templates')


def fetch_notes():
	final_notes = []
	notes = glob.glob('noteapp/notes/*.note')
	
	for note in notes:
		with open(note) as _file:
			final_notes.append(_file.read())

		_file.close()

	return final_notes


@bp.route('/')
def show():
    return render_template('index.html', notes=fetch_notes()) #loads the index and the css via the index, Variable Notes will be accessable from the index file