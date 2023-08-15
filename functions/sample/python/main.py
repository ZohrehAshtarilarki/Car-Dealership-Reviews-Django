"""
This module contains the main function for the Cloud Functions 
action.
It connects to a Cloudant database and retrieves information.
Usage:
    - This module is invoked when the Cloud Function is 
    triggered.
"""

from cloudant.client import Cloudant
from cloudant.error import CloudantException
import requests

def main(input_dict):
    """
    This is the main function that will be run when you 
    invoke this action.

    Args:
        input_dict (dict): Cloud Functions actions accept a 
        single parameter, which must be a JSON object.

    Returns:
        dict: The output of this action, which must be a JSON 
        object.
    """
    try:
        client = Cloudant.iam(
            account_name=input_dict["COUCH_USERNAME"],
            api_key=input_dict["IAM_API_KEY"],
            connect=True,
        )
        print("Databases:", client.all_dbs())
    except CloudantException as cloudant_exception:
        print("Unable to connect")
        return {"error": str(cloudant_exception)}
    except (requests.exceptions.RequestException, ConnectionResetError) as err:
        print("Connection error")
        return {"error": str(err)}

    return {"dbs": client.all_dbs()}

if __name__ == "__main__":
    pass  # Placeholder to satisfy the missing module docstring warning
