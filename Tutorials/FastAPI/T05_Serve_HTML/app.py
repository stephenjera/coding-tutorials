import uvicorn
from fastapi import FastAPI, Request
from starlette.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

# Create a FastAPI app instance
app = FastAPI()

# Create a Jinja2Templates instance to render templates from the "templates" directory
templates = Jinja2Templates(directory="templates")


# Define a route for the root path ("/") that returns an HTML response
@app.get("/", response_class=HTMLResponse)
def home(*, request: Request):
    # Render the "index.html" template and return it as a response
    return templates.TemplateResponse(
        "index.html",
        context={"request": request},
    )


if __name__ == "__main__":
    uvicorn.run("app:app", reload=True, port=3000)
