# Migrate VCS configs between workspaces in different deployments

Setup a virtual environment.

```bash
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

Set the variables you need to communicate with TFE or user the .env example

```bash
export OLD_TFC_URL=""
export OLD_TFC_TOKEN=""
export OLD_TFC_ORG=""
export NEW_TFC_URL=""
export NEW_TFC_TOKEN=""
export NEW_TFC_ORG=""
export VCS_PROVIDER=""
```

Run the script to migrate the VCS configs to your new TFE/TFC deployment

```bash
python main.py
```

## Additional Comments
Find the VCS_PROVIDER name in: Settings > VCS Providers
Make sure you're using the same workspace names in both deployments  once the script will look for this attribute.
