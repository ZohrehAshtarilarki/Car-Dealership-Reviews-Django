from cloudant.client import Cloudant
from cloudant.error import CloudantException
import requests

def main(dict):
    """
    This is the main function that will be run when you invoke this action.

    Args:
        dict (dict): Cloud Functions actions accept a single parameter, which must be a JSON object.

    Returns:
        dict: The output of this action, which must be a JSON object.
    """
    database_name = "dealerships"  # Renamed the variable to follow snake_case convention

    try:
        client = Cloudant.iam(
            account_name=dict["COUCH_USERNAME"],
            api_key=dict["IAM_API_KEY"],
            connect=True,
        )
        print("Databases: {0}".format(client.all_dbs()))
    except CloudantException as ce:
        print("Unable to connect")  # Corrected the capitalization
        return {"error": str(ce)}  # Convert CloudantException to string
    except (requests.exceptions.RequestException, ConnectionResetError) as err:
        print("Connection error")
        return {"error": str(err)}  # Convert the exception to string

    return {"dbs": client.all_dbs()}  # Return a JSON response
