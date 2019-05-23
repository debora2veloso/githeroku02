from flask import Flask, render_template 
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
   

if __name__=='__main__':
  app.run()

#TENHO DE FAZER O TRABALHO PRA APRESENTAR TERÇA MAS AINDA NAO SEI O TEMA , MAS TEM DE SER TEXTO / IMAGENS PROBABELMENTE
#instagram twitwr youtube facebook nome da empreza contactos horarios ....
