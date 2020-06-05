from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
import json

app = Flask("Notes App")

notes_json_name = "notes.json"
#öffnet einen neue datei - W = writing
def write_data_to_json(file_name, data):
	with open(file_name, 'w') as file:
		json.dump(data, file) #dump speichert die datei in einem json file ab

def load_data_from_json(file_name, default_value): #lädt die Dateien aus der Json datei & wiedergibt sie - R = read (nur leseerlaubnis)
	try:
		with open(file_name, 'r') as file:
			data = json.load(file)
			return data
	except Exception:
		return default_value

@app.route('/') #zählt die Anzahl der Notizen und rechnet sie dem entsprechenden Tag zu
def index():
	all_notes = load_data_from_json(notes_json_name, [])
	count_work = 0
	count_school = 0
	count_sparetime = 0
	for note in all_notes: 
		if note["tag"] == "Schule":
			count_school += 1
		elif note["tag"] == "Arbeit":
			count_work += 1
		elif note["tag"] == "Freizeit":
			count_sparetime += 1
	return render_template("index.html", notes=all_notes, count_school = count_school, count_work = count_work, count_sparetime = count_sparetime)
	

@app.route('/create_note', methods=["GET", "POST"])   #URL wird erstellt um Eingabeformular aufzurufen, die Methode wird angegeben in deisem Fall "Get" & "Post"
def create_note():
	all_notes = load_data_from_json(notes_json_name, [])
	if request.method == "POST":  #wenn die Post methode ausgewählt wird - werden die Daten (Titel, Tag, Text) abgefangen, welche dann im Notizzettel stehen, in den String eingebaut und zurückgeben
		note_titel = request.form["note-titel"]
		note_text = request.form["note-text"]

		note_tag = request.form["note-tag"]

		new_note = {
			"titel": note_titel,
			"text": note_text,
			"tag": note_tag
		}

		# Make sure note titel is unique
		note_already_exists = False
		for note in all_notes:
			if note["titel"] == note_titel:
				note_already_exists =  True

		if not note_already_exists:		
			all_notes.append(new_note)
			write_data_to_json(notes_json_name, all_notes)
			return redirect(url_for("index"))
		# Note already exists -> notify user
		return render_template("create_note.html", already_exists = note_already_exists) #gibt das Create_note.html template ausgeben, wenn die Post methode nicht ausgewählt wird

	return render_template("create_note.html", already_exists = False)

@app.route('/delete/<note_titel>', methods=["GET", "POST"]) #URL wird erstellt um Eingabeformular aufzurufen, um den Notizzettel zu löschen
def delete_note(note_titel):
	all_notes = load_data_from_json(notes_json_name, [])
	note = None
	for element in all_notes:
		if element["titel"] == note_titel:
			note = element
	if request.method == "POST": #wenn die Post methode ausgewählt wird - werden die Daten (Titel, Tag, Text) abgefangen, welche dann im Notizzettel gelöscht werden, aus dem String gelöscht und zurückgeben
		all_notes.remove(note)
		write_data_to_json(notes_json_name, all_notes)
		return redirect(url_for("index"))
	return render_template("delete_note.html", note=note) #gibt das delete_note.html template ausgeben

@app.route('/edit/<note_titel>', methods=["GET", "POST"]) #URL wird erstellt um Eingabeformular aufzurufen und die Notiz zu editieren
def edit_note(note_titel):
	all_notes = load_data_from_json(notes_json_name, [])
	note = None
	for element in all_notes:
		if element["titel"] == note_titel:
			note = element
	if request.method == "POST":
		new_note_titel = request.form["note-titel"]
		note_text = request.form["note-text"]
		note_tag = request.form["note-tag"]
		note_already_exists = False
		# Prüfe ob der editierte Titel bereits existiert, aber nur wenn sich der Nutzer den Titel editiert hat
		if note["titel"] != new_note_titel:
			for note in all_notes:
				if note["titel"] == new_note_titel:
					note_already_exists =  True

		if not note_already_exists:
			note["titel"] = new_note_titel
			note["text"] = note_text		
			note["tag"] = note_tag
			write_data_to_json(notes_json_name, all_notes)
			return redirect(url_for("index")) #gibt index.html template aus
		# Notiz mit dem Titel existiert bereits
		return render_template("edit_note.html", note=note, note_already_exists=note_already_exists)

	return render_template("edit_note.html", note=note, note_already_exists=False)

@app.route('/filter_notes', methods=["GET", "POST"]) #URL wird erstellt um Eingabeformular aufzurufen und Notizen nach Tag zu filtern
def filter_notes(): 
	if request.method == "POST":
		note_tag = request.form["note-tag"]
		all_notes = load_data_from_json(notes_json_name, [])
		result = []
		for note in all_notes:
			if note["tag"] == note_tag:
				result.append(note)
		return render_template("index.html", notes=result) #gibt das index_note.html template ausgeben
	return render_template('search.html') #gibt das search.html template ausgeben
if __name__ == "__main__":
    app.run(debug=True, port=5000)#


