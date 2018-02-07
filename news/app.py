from flask import Flask, render_template
import os
import json
app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD']=True

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'),404


@app.route('/')
def index():
    file_dir='/home/python/shiyanlou_week2/files'
    l=[]
    title_list=[]
    for root ,dirs,files in os.walk(file_dir):
        for file in files:
            if os.path.splitext(file)[1]=='.json':
                l.append(os.path.join(root,file))
    for page in l:        
        with open(page) as file:
            article = json.load(file)
            title_list.append(article['title'])
    return render_template('index.html',titles = title_list)

@app.route('/files/<filename>')
def file(filename):
    path = '/home/python/shiyanlou_week2/files/'+filename+'.json'
    if os.path.exists(path):
        with open(path) as file:
            article = json.load(file)
        return render_template('file.html',article = article)
    else:
        return render_template('404.html'),404
    
    
    
if __name__=='__main__':
    app.run()