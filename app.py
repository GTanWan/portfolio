from flask import Flask, send_from_directory

app = Flask(__name__)

# Serve static files
@app.route('/static/<path:filename>')
def static_files(filename):
    return send_from_directory('static', filename)

# Downloads
@app.route('/uploads/<path:filename>')
def uploaded_files(filename):
    return send_from_directory('uploads', filename)

# Full Page (Base Page)
@app.route('/')
def index():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Portfolio</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
        <script src="https://unpkg.com/htmx.org"></script>
    </head>
    <body>
        <div class="container my-5">
            <h1 class="text-center mb-4">George Tatulea - Web and App Developer</h1>
            <div class="d-flex justify-content-center gap-2 mb-4">
                <button hx-get="/about-me" hx-target="#content" class="btn btn-outline-primary">About Me</button>
                <button hx-get="/todo-list" hx-target="#content" class="btn btn-outline-secondary">To-Do App</button>
                <button hx-get="/scoring-app" hx-target="#content" class="btn btn-outline-success">Baseball Scoring App</button>
                <button hx-get="/powerbi-dashboard" hx-target="#content" class="btn btn-outline-warning">Power BI Dashboard</button>
            </div>
            <div id="content" class="border rounded p-3">
                <h2>Welcome</h2>
                <p>Click a button above to learn more about my projects and skills!</p>
            </div>
        </div>
    </body>
    </html>
    """

# About Me Section
@app.route('/about-me')
def about_me():
    return """
    <div class="container">
        <h2 class="mt-4 text-primary">About Me</h2>
        <div class="row align-items-center">
            <div class="col-md-4">
                <img src="/static/images/about_me.jpg" alt="About Me" class="img-fluid rounded">
            </div>
            <div class="col-md-8">
                <h3 class="mt-4">Introduction</h3>
                <p>
                    I am George Tatulea, a web and app developer passionate about creating innovative solutions to address modern challenges.
                    With a diverse educational background in Computer Programming and Analysis, as well as Biology, I bring unique insights to my projects.
                </p>
                <p>
                    My professional journey includes developing data-driven applications, collaborating with teams, and ensuring user-centric designs.
                    These experiences have honed my ability to troubleshoot complex systems, integrate emerging technologies, and deliver scalable solutions.
                </p>
                <h3 class="mt-4">Technical Expertise</h3>
                <p>
                    My technical skill set includes expertise in .NET, C#, Django, FastAPI, and SQL, alongside front-end technologies
                    such as HTML, CSS, and JavaScript. I specialize in designing and developing responsive web applications, robust back-end systems,
                    and data-rich dashboards.
                </p>
                <p>
                    Additionally, I am skilled in leveraging tools such as Git and SQL Management Studio to streamline workflows, optimize database queries,
                    and enhance overall project efficiency.
                </p>
                <h3 class="mt-4">Professional Philosophy</h3>
                <p>
                    I thrive in collaborative environments, where teamwork and clear communication drive success. My professional philosophy centers around clean,
                    maintainable code and leveraging innovative technologies to meet client or project requirements.
                </p>
                <p>
                    My ultimate goal is to build impactful software solutions that simplify processes and improve user experience across industries.
                    I continuously strive to learn new technologies and embrace challenges that push the boundaries of my skills.
                </p>
            </div>
        </div>
    </div>
    """

# Baseball Scorekeeping App Section
@app.route('/scoring-app')
def scoring_app():
    return """
    <div class="container">
        <h2 class="mt-4 text-success">Baseball Scorekeeping App</h2>
        <a href="https://drive.google.com/file/d/12OtBTj-EsNrs8NwEqPusfFP7CTUWzKEu/view?usp=sharing" download class="btn btn-success mb-3">Download scorekeepingapp.zip</a>
        <div class="row">
            <div class="col-md-12">
                <p>
                    This Baseball Scorekeeping App was developed for youth baseball leagues to track game stats, player performance,
                    and manage game schedules effectively. Built using ASP.NET Core MVC with Razor Pages, the app provides a robust and intuitive user experience.
                </p>
                <p>
                    My contributions included developing a RESTful API, designing a database schema using T-SQL, and integrating front-end components
                    to create a seamless workflow for users. I collaborated with a team to ensure each feature met real-world needs.
                </p>
            </div>
        </div>
        <div class="row mt-4">
            <div class="col-md-12">
                <img src="/static/images/wmba_score_app.jpg" alt="Scorekeeping UI" class="img-fluid rounded mb-3" style="display: block; margin: 0 auto;">
                <h3>Scorekeeping UI</h3>
                <p>
                    The scorekeeping UI features a clear visual representation of the baseball field with player positions and bases.
                    This intuitive design ensures real-time tracking of game events and player movements.
                </p>
                <p>
                    The interface is designed to reduce user errors and provide instant feedback, ensuring coaches and managers can focus
                    on strategic decisions rather than technical hurdles.
                </p>
            </div>
        </div>
        <div class="row mt-4">
            <div class="col-md-12">
                <img src="/static/images/wmba_upcoming_games.jpg" alt="Upcoming Games" class="img-fluid rounded mb-3" style="display: block; margin: 0 auto;">
                <h3>Upcoming Games Schedule</h3>
                <p>
                    The upcoming games list provides a detailed schedule of future matches, including date, time, teams, and game locations.
                    Real-time updates ensure everyone involved stays informed.
                </p>
                <p>
                    Using database management tools, I created an efficient and scalable scheduling system to handle league-level data seamlessly.
                </p>
            </div>
        </div>
        <div class="row mt-4">
            <div class="col-md-12">
                <img src="/static/images/wmba_stats.jpg" alt="Player Search" class="img-fluid rounded mb-3" style="display: block; margin: 0 auto;">
                <h3>Player Search Functionality</h3>
                <p>
                    The app includes a powerful search feature that allows users to locate players using either full or partial names.
                    This functionality is invaluable for large teams, simplifying the management of player stats and profiles.
                </p>
                <p>
                    Through optimization techniques, such as caching and indexing, the search system delivers results instantly, enhancing user satisfaction.
                </p>
            </div>
        </div>
    </div>
    """

# To-Do App Section
@app.route('/todo-list')
def todo_list():
    return """
    <div class="container">
        <h2 class="mt-4 text-secondary">To-Do App</h2>
        <a href="https://drive.google.com/file/d/1s_D1Ao6wUSPQK57GjliWToLcz2Ibu8dI/view?usp=sharing" download class="btn btn-secondary mb-3">Download ToDoApp.7z</a>
        <div class="row align-items-center">
            <div class="col-md-4">
                <img src="/static/images/todo_app.jpg" alt="To-Do App" class="img-fluid rounded">
            </div>
            <div class="col-md-8">
                <h3 class="mt-4">About the App</h3>
                <p>
                    The To-Do App is a task management desktop application developed using UWP and .NET technologies.
                    It empowers users to organize and prioritize tasks effectively.
                </p>
                <p>
                    Features include real-time updates, categorization of tasks by deadlines, and a clean interface designed to minimize distractions.
                </p>
                <h3 class="mt-4">Features</h3>
                <p>
                    The app allows users to group tasks by deadlines, importance, and urgency while dynamically updating tasks in real-time.
                </p>
                <p>
                    Its modular architecture ensures flexibility, making it adaptable to both personal and professional use cases.
                </p>
            </div>
        </div>
    </div>
    """

# Power BI Dashboard Section
@app.route('/powerbi-dashboard')
def powerbi_dashboard():
    return """
    <div class="container">
        <h2 class="mt-4 text-warning">Power BI Dashboard</h2>
        <a href="https://drive.google.com/file/d/1ec84OGxTx0xG3lfA75ttBcl8lA5HENga/view?usp=sharing" download class="btn btn-warning mb-3">Download gtatuleaFinalProject.pbix</a>
        <div class="row align-items-center">
            <div class="col-md-6">
                <img src="/static/images/powerbi_dashboard.jpg" alt="Power BI Dashboard" class="img-fluid rounded">
            </div>
            <div class="col-md-6">
                <h3 class="mt-4">About the Project</h3>
                <p>
                    The Power BI Dashboard is an advanced data visualization project designed to provide actionable insights through dynamic, interactive elements.
                </p>
                <p>
                    By leveraging external datasets, I created calculated measures, designed scalable data models, and developed intuitive visualizations.
                </p>
                <h3 class="mt-4">Features</h3>
                <p>
                    Includes filters, drill-down capabilities, and real-time data updates for intuitive data analysis.
                </p>
                <p>
                    Its versatility ensures practical applications across industries such as retail, healthcare, and finance.
                </p>
            </div>
        </div>
    </div>
    """

if __name__ == '__main__':
    app.run(debug=True)
