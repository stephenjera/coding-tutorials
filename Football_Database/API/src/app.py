import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from strawberry.fastapi import GraphQLRouter
from schema import schema
from database import create_db_and_tables

app = FastAPI()
app.include_router(GraphQLRouter(schema=schema, path="/graphql"))

origins = [
    "http://localhost:3000",
    "https://fivetran-football.azurewebsites.net/"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def on_startup():
    create_db_and_tables()


if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", reload=False, port=3000)

