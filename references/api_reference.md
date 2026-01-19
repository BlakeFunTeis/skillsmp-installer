# SkillsMP API Reference

## Overview

Use the SkillsMP search API to find skills by keyword.

## Authentication

Send `Authorization: Bearer ${SKILL_MAP_API_KEY}` with every request.

## Endpoint

Send a GET request:

`https://skillsmp.com/api/v1/skills/ai-search?q=<query>`

## Headers

Use the headers below as a baseline:

- `Accept: application/json, text/plain, */*`
- `Origin: https://skillsmp.com`
- `Referer: https://skillsmp.com/`
- `User-Agent: skillsmp-installer/1.0`

## Response

Expect JSON with:

- `success` (bool)
- `data.object` (string)
- `data.search_query` (string)
- `data.data[]` (list)

Each item in `data.data[]` includes:

- `score` (float)
- `filename`, `file_id`
- `skill.id`, `skill.name`, `skill.author`
- `skill.description`, `skill.githubUrl`, `skill.skillUrl`
- `skill.stars`, `skill.updatedAt`

## Failure handling

If `success` is false or `data.data[]` is empty, ask the user to change the keyword
or replace the API key.
