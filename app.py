from flask import Flask, render_template, request 

app: Flask = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def create_portfolio():
    if request.method == "POST":

        name: str = request.form['name']
        college: str = request.form['college']
        year: str = request.form['year']
        major: str = request.form['major']
        about_me: str = request.form['about_me']
        project_1: str = request.form['project_1']
        project_1_github: str = request.form['project_1_github']
        email: str = request.form['email']
        resume: str = request.form['resume']
        linkedin: str = request.form['linkedin']
        git_hub: str = request.form['git_hub']

        if name == '':
            return render_template("index.html")

        return render_template("portfolio.html", name=name, college=college, year=year, major=major, about_me=about_me, project_1=project_1, project_1_github=project_1_github, email=email, resume=resume, linkedin=linkedin, git_hub=git_hub)

    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)