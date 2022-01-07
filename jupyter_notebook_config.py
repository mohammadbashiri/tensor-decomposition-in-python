import os

# Accept all incoming requests
c.NotebookApp.ip = "0.0.0.0"
c.NotebookApp.port = 8888
c.NotebookApp.open_browser = False
c.NotebookApp.token = ""  # os.environ.get("JUPYTER_PASSWORD", "my-secret-password")
