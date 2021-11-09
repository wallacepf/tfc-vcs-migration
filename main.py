import os
import logging
from terrasnek.api import TFC

logging.basicConfig(format='%(asctime)s - %(message)s',level=logging.INFO)

OLD_TFC_URL = os.environ["OLD_TFC_URL"]
OLD_TFC_TOKEN = os.environ["OLD_TFC_TOKEN"]
OLD_TFC_ORG = os.environ["OLD_TFC_ORG"]

NEW_TFC_URL = os.environ["NEW_TFC_URL"]
NEW_TFC_TOKEN = os.environ["NEW_TFC_TOKEN"]
NEW_TFC_ORG = os.environ["NEW_TFC_ORG"]

VCS_PROVIDER = os.environ["VCS_PROVIDER"]

if __name__ == "__main__":
    old_api = TFC(OLD_TFC_TOKEN, url=OLD_TFC_URL)
    old_api.set_org(OLD_TFC_ORG)

    new_api = TFC(NEW_TFC_TOKEN, url=NEW_TFC_URL)
    new_api.set_org(NEW_TFC_ORG)

    all_old_ws = old_api.workspaces.list_all()["data"]
    all_new_ws = new_api.workspaces.list_all()["data"]
    new_oauth_clients = new_api.oauth_clients.list()["data"]


    for oclients in new_oauth_clients:
        if VCS_PROVIDER == oclients["attributes"]["name"]:
            vcs_token_id = oclients["relationships"]["oauth-tokens"]["data"][0]["id"]
            logging.debug(vcs_token_id)

    for old_ws in all_old_ws:
        old_name = old_ws["attributes"]["name"]
        old_vcs = old_ws["attributes"]["vcs-repo"]


        for new_ws in all_new_ws:
            new_name = new_ws["attributes"]["name"]
            if old_name == new_name:
                payload = {
                    "data": {
                        "attributes": {
                        "name": new_name,
                        "vcs-repo": {
                            "identifier": old_vcs["identifier"],
                            "branch": old_vcs["branch"],
                            "oauth-token-id": vcs_token_id
                            },
                        },
                        "type": "workspaces"
                    }
                }
                logging.warning(payload)
                created_wrksps=new_api.workspaces.update(payload, workspace_name=new_name)
                logging.debug(created_wrksps)
