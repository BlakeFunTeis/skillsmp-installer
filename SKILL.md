---
name: skillsmp-installer
description: Search SkillsMP via its API and install selected skills via Codex skill-installer. Use when asked to find SkillsMP skills by keyword, handle SKILL_MAP_API_KEY setup, triage search failures, or install skills from SkillsMP results.
---

# SkillsMP Installer

## Overview

Search SkillsMP with a keyword and install a selected skill using `python3 scripts/install-skill-from-github.py --url {githubUrl}`.

## Workflow

1. Get the search query from the user.
2. Check the API key.
   - Run `printenv SKILL_MAP_API_KEY`.
   - If empty or missing, ask the user for the key and set it with `export SKILL_MAP_API_KEY="..."`.
   - If `export` does not persist across commands, prefix the next command with `SKILL_MAP_API_KEY="..."`.
3. Run the search.
   - Prefer the helper script: `python3 scripts/skillsmp_search.py --query "<query>"`
   - Or use the raw curl command (see below).
4. Review scripts and referenced code for safety concerns.
   - Inspect the scripts to be run (and any referenced code or URLs) before installation.
   - If any safety concerns or uncertainties are found, call them out and ask the user if they accept the risk before proceeding.
5. If `success` is false or no results are returned:
   - Ask the user to try a different keyword.
   - Ask whether the API key should be replaced.
6. Present the results and ask which skill to install.
   - Use the selected item's `skill.githubUrl`.
7. Install the chosen skill:
   - `python3 scripts/install-skill-from-github.py --url {githubUrl}`
8. Tell the user to restart Codex after installation.

## Script usage

```bash
python3 scripts/skillsmp_search.py --query "How to create a web scraper"
python3 scripts/skillsmp_search.py --query "How to create a web scraper" --format json
```

## Raw curl (fallback)

```bash
curl -sS --compressed --http1.1 --location \
  --request GET \
  --url "https://skillsmp.com/api/v1/skills/ai-search" \
  --get --data-urlencode "q=How to create a web scraper" \
  -H "Authorization: Bearer ${SKILL_MAP_API_KEY}" \
  -H "Accept: application/json, text/plain, */*" \
  -H "Accept-Language: zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7" \
  -H "Cache-Control: no-cache" \
  -H "Pragma: no-cache" \
  -H "Connection: keep-alive" \
  -H "Referer: https://skillsmp.com/" \
  -H "Origin: https://skillsmp.com" \
  -H "User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36" \
  -H "Sec-Fetch-Dest: empty" \
  -H "Sec-Fetch-Mode: cors" \
  -H "Sec-Fetch-Site: same-origin" \
  -H "DNT: 1"
```

## Response shape (for parsing)

- Expect a JSON response with `success`.
- Read results from `data.data[]`.
- Use `skill.githubUrl` for installation.

## Scripts

- `scripts/skillsmp_search.py`: Query SkillsMP and print a numbered result list (or JSON via `--format json`).
- `scripts/skillsmp_search_wrapper.py`: Thin wrapper that runs `skillsmp_search.py`.
- `scripts/install-skill-from-github.py`: Install a skill from Github.

## References

- `references/api_reference.md`: SkillsMP API request and response details.

## Assets

- `assets/skillsmp_curl_template.txt`: Copy-paste curl template for manual requests.
