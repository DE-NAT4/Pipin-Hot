#!/bin/sh
set -eu     # -e = exit immediately if any command fails | -u = treat any undefined variable as an error and exit (typo protection)

### CONFIG SECTION ###
aws_profile="$1" # e.g. Marcell-DE, for the aws credentials
team_name="$2" # e.g. 'pipin-hot' USE YOUR TEAM NAME FOR THIS SESSION - WITH DASHES
deployment_bucket="${team_name}-shopper-deployment-bucket"
# use example: bash deploy.sh <AWSProfileName> <TeamName>
#### CONFIG SECTION ####

# Create deployment bucket stack
echo ""
echo "Doing deployment bucket..."
echo ""
aws cloudformation deploy --stack-name "${team_name}-deployment-bucket" \
    --template-file deployment-bucket-stack.yml --region eu-west-1 \
    --capabilities CAPABILITY_IAM --profile ${aws_profile} \
    --parameter-overrides \
      TeamName="${team_name}";
# --parameter-overrides TeamName="${team_name}" passes parameters into the cloudformation template, TeamName="${team_name}" maps to the parameters section in the YAML
# ; ends the command