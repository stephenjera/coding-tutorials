import uvicorn
import strawberry
from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter


# Define a Query class with a hello field that returns a string
@strawberry.type
class Query:
    @strawberry.field
    def hello(self) -> str:
        return "Hello World"


# Create a schema using the Query class
schema = strawberry.Schema(Query)

# Create a GraphQLRouter using the schema
graphql_app = GraphQLRouter(schema)

# Create a FastAPI app and include the GraphQLRouter with a prefix of "/graphql"
app = FastAPI()
app.include_router(graphql_app, prefix="/graphql")


if __name__ == "__main__":
    uvicorn.run("app:app", reload=True, port=3000)