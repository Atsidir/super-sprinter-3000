from flask import Flask, render_template, request, url_for, redirect, flash, abort
from models import *

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def base():
    stories=UserStory.select()
    return render_template('base.html',stories=stories)

@app.route('/story/', methods=['GET', 'POST'])
@app.route('/story/<int:param>', methods=['GET', 'POST'])
def story(param=0):
    if param != 0:
        story = UserStory.get(id=param)
        if request.method == 'POST':
            values = request.form.getlist("story")
            story.title = values[0]
            story.story = values[1]
            story.acceptance = values[2]
            story.bvalue = values[3]
            story.hours = values[4]
            story.status = values[5]
            story.save()
            return redirect("/list")
        else:
            return render_template('story.html', story=story, id=param)
    else:
        if request.method == 'POST':
            values = request.form.getlist("story")
            UserStory.create(title=values[0], story=values[1], acceptance=values[2], bvalue=values[3], hours=values[4],
                             status=values[5])
            return redirect(url_for("index"))

        else:
            return render_template('story.html', id=param)

@app.route('/bootstrap',methods=['GET','POST'])
def boot():
    return render_template('boot.html')

@app.route('/list', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        values = request.form.getlist("story")
        print(values)
        story = UserStory.get(UserStory.id == values[0])
        if values[7] == 'Update':
            return redirect("/story/{}".format(story.id))
        else:

            story.delete_instance()
            stories = UserStory.select()
            return render_template('index.html', stories=stories, length=len(stories))
    stories = UserStory.select()
    return render_template('index.html', stories=stories, length=len(stories))


if __name__ == "__main__":
    app.run(debug=True)
