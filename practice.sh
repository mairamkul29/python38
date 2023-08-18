#!/bin/bash

read -p "name your repository: " repo_name

  response="$(curl -X POST \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer $GITHUB_TOKEN" \
  https://api.github.com/user/repos \
  -d '{"name" : "'"$repo_name"'", "description" : "My repo created with api"}')"