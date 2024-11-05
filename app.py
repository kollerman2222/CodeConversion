from flask import Flask , render_template , request , redirect , jsonify
from flask_sqlalchemy import SQLAlchemy




app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///F:/Sqllite studio/codeconversion.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)





class Language(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50))
    syntax = db.relationship('Syntax', back_populates='language')
    image = db.Column(db.String(50))


class Controls(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50))
    syntax = db.relationship('Syntax', back_populates='control')


class Syntax(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    syntax = db.Column(db.String(50))
    languageid = db.Column(db.Integer, db.ForeignKey('language.id'))
    controlid = db.Column(db.Integer, db.ForeignKey('controls.id'))
    language = db.relationship('Language', back_populates='syntax')
    control = db.relationship('Controls', back_populates='syntax')





@app.route('/create/<classnameparameter>', methods=['POST'])
def create(classnameparameter):
    if request.method=='POST':
        if classnameparameter == 'language':
            languagename = request.form['languagename']
            data = Language(name=languagename)
        elif classnameparameter == 'controls':
            controlname = request.form['controlname']
            data = Controls(name=controlname)
        elif classnameparameter == 'syntax':
            controlname = request.form['controlname']
            languagename = request.form['languagename']
            syntaxname = request.form['syntaxname']
            getlanguage = Language.query.filter_by(name=languagename).first()
            getcontrol = Controls.query.filter_by(name=controlname).first()
            data = Syntax(syntax=syntaxname, languageid=getlanguage.id, controlid=getcontrol.id)

        db.session.add(data)
        db.session.commit()
        return redirect('/dashboard')



@app.route('/update/<classnameparameter>', methods=['POST'])
def update(classnameparameter):
    if request.method == 'POST':
        if classnameparameter=='language':
            languageid=request.form['languageid']
            findlanguage=db.session.get(Language, languageid)
            findlanguage.name=request.form['languagename']
        elif classnameparameter == 'controls':
            controlid = request.form['controlid']
            findcontrol=db.session.get(Controls, controlid)
            findcontrol.name=request.form['controlname']
        elif classnameparameter == 'syntax':
            syntaxid=request.form['syntaxid']
            findsyntax=db.session.get(Syntax, syntaxid)
            findsyntax.syntax = request.form['syntaxname']
            getlanguage = Language.query.filter_by(name=request.form['languagedropdown']).first()
            getcontrol = Controls.query.filter_by(name=request.form['controldropdown']).first()
            findsyntax.languageid = getlanguage.id
            findsyntax.controlid = getcontrol.id

        db.session.commit()
        return redirect('/dashboard')



@app.route('/delete/<classnameparameter>/<int:id>')
def delete(classnameparameter,id):
    classnamelist = {'language': Language, 'controls': Controls, 'syntax': Syntax}
    getclassname = classnamelist.get(classnameparameter)
    findclass = db.session.get(getclassname, id)
    db.session.delete(findclass)
    db.session.commit()
    return redirect('/dashboard')



@app.route('/',methods=['GET', 'POST'])
def singleconvert():
    languageslist = Language.query.all()
    controlslist = Controls.query.all()
    syntaxlist = Syntax.query.all()
    if request.method == 'GET':
        return render_template("singleconvert.html", languageslist=languageslist, controlslist=controlslist)
    if request.method == 'POST':
        languagename = request.form['languagename']
        controlname = request.form['controlname']
        getlanguage = Language.query.filter_by(name=languagename).first()
        getcontrol = Controls.query.filter_by(name=controlname).first()
        getsyntax = Syntax.query.filter_by(languageid=getlanguage.id, controlid=getcontrol.id).first()
        findsyntax = getsyntax.syntax
        return findsyntax


@app.route('/multiconvert',methods=['GET', 'POST'])
def multiconvert():
    languageslist = Language.query.all()
    controlslist = Controls.query.all()
    if request.method == 'GET':
        return render_template("multiconvert.html", languageslist=languageslist, controlslist=controlslist)
    if request.method == 'POST':
        firstlanguagename = request.form['firstlanguagename']
        secondlanguagename = request.form['secondlanguagename']
        controlname = request.form['controlname']
        getfirstlanguage = Language.query.filter_by(name=firstlanguagename).first()
        getsecondlanguage = Language.query.filter_by(name=secondlanguagename).first()
        getcontrol = Controls.query.filter_by(name=controlname).first()
        getfirstlanguagesyntax = Syntax.query.filter_by(languageid=getfirstlanguage.id, controlid=getcontrol.id).first()
        getsecondlanguagesyntax = Syntax.query.filter_by(languageid=getsecondlanguage.id, controlid=getcontrol.id).first()
        firstlanguagesyntax = getfirstlanguagesyntax.syntax
        secondlanguagesyntax = getsecondlanguagesyntax.syntax
        return jsonify(firstsyntaxresult=firstlanguagesyntax, secondsyntaxresult=secondlanguagesyntax)



@app.route('/dashboard')
def dashboard():
    languageslist = Language.query.all()
    controlslist = Controls.query.all()
    syntaxlist = Syntax.query.all()
    return render_template("dashboard.html", languageslist=languageslist, controlslist=controlslist, syntaxlist=syntaxlist)




if __name__ == "__main__":
    app.run(debug=True)