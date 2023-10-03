import os

DEVELOPMENT = "development"
PRODUCTION = "production"
STAGING = "staging"
CODE_SPACE = "code_space"
LOCAL = "local"

# If ENV_NAME has no value, use the default of DEVELOPMENT
# export ENV_NAME='some unknown environment'
current_env = os.environ.get("ENV_NAME", DEVELOPMENT)

if current_env == DEVELOPMENT:
    print("Development environment")
elif current_env == PRODUCTION:
    print("Production environment")
elif current_env == STAGING:
    print("Staging environment")
elif current_env in [CODE_SPACE, LOCAL]:
    print("Codespace or local environment")
else:
    print("Unknown environment")
