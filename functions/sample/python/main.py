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
    try:
        client = Cloudant.iam(
            account_name=dict["COUCH_USERNAME"],
            api_key=dict["IAM_API_KEY"],
            connect=True,
        )
        print("Databases:", client.all_dbs())  # Used an f-string for formatting
    except CloudantException as ce:
        print("Unable to connect")
        return {"error": str(ce)}
    except (requests.exceptions.RequestException, ConnectionResetError) as err:
        print("Connection error")
        return {"error": str(err)}

    return {"dbs": client.all_dbs()}  # Return a JSON response

if __name__ == "__main__":
    pass  # Placeholder to satisfy the missing module docstring warning
