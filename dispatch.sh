#!/usr/bin/bash
# TODO: replace :token, :user, and :repo
echo $ACTION_TOKEN
curl -H "Authorization: token $ACTION_TOKEN" \
    -H 'Accept: application/vnd.github.everest-preview+json' \
    "https://api.github.com/repos/hl7-be/fhir-roadmap/dispatches" \
    -d '{"event_type": "update", "client_payload": {"foo": "bar"}}'
