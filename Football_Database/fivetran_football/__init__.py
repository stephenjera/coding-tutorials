import logging
import azure.functions as func
import requests
import json


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("**Python HTTP trigger function processed a request.**")

    # Define the GraphQL query and variables
    query = """
    query {
        cards {
            cardId
            colourId
            matchId
            playerId
            timeGiven
        }
        clubs {
            club
            clubId
        }
        goals {
            goalId
            matchId
            playerId
            timeScored
        }
        groupNames {
            groupId
            groupName
        }
        matches {
            awayId
            awayScore
            dateTime
            friendly
            homeId
            homeScore
            matchId
            venueId
            week
        }
        players {
            clubId
            firstName
            groupId
            lastName
            playerId
        }
    }
    """
    variables = {}

    try:
        # Send the GraphQL query to the API
        response = requests.post(
            "http://localhost:3001/graphql",
            json={"query": query, "variables": variables},
        )
        data = response.json()
    except Exception as e:
        logging.error(f"An error occurred while fetching data from the API: {e}")
        return func.HttpResponse(
            "An error occurred while fetching data from the API.", status_code=500
        )

    # Return the data in the response
    return func.HttpResponse(json.dumps(data))
