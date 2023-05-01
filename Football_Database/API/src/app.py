import uvicorn
from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
from schema import schema
from database import create_db_and_tables

app = FastAPI()
app.include_router(GraphQLRouter(schema=schema, path="/graphql"))


@app.on_event("startup")
def on_startup():
    create_db_and_tables()


if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", reload=False, port=3000)

