from tracking_system.wsgi import application

# Gunicorn expects a variable named `app`
app = application
