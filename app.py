from flask import Flask, request,render_template
from Model import SpellCheckerModule

app = Flask(__name__,template_folder='templates')
spell_checker_module = SpellCheckerModule()

# routes
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/spell',methods=['POST','GET'])
def spell():
    if request.method=='POST':
        text = request.form['text']
        corrected_text = spell_checker_module.correct_spell(text)
        total_mistakes, suggestions = spell_checker_module.get_total_mistakes_and_suggestions(text)
        return render_template('index.html', corrected_text=corrected_text, total_mistakes=total_mistakes, suggestions=suggestions)
    
@app.route('/grammar',methods=['POST','GET'])
def grammar():
    pass
    if request.method == 'POST':
        file = request.files['file']
        readable_file = file.read().decode('utf-8',errors='ignore')
        corrected_file_text = spell_checker_module.correct_spell(readable_file)
        total_file_mistakes, file_suggestions = spell_checker_module.get_total_mistakes_and_suggestions(readable_file)
        return render_template('index.html',corrected_file_text=corrected_file_text, total_file_mistakes=total_file_mistakes, file_suggestions=file_suggestions)

# python main
if __name__ == "__main__":
    app.run(debug=True)