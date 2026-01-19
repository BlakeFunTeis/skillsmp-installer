# SkillsMP Installer

## 中文

此技能用來透過 SkillsMP 搜尋技能，並引導安裝至 Codex。

使用 Codex CLI 安裝此技能：

```sh
$skill-installer https://github.com/BlakeFunTeis/skillsmp-installer/tree/main
```

安裝完成後請重新啟動 Codex。

### 使用方式

1. 在環境變數中設定 `SKILL_MAP_API_KEY`（[SkillsMP 的 API key](https://skillsmp.com/docs/api)）。
2. 在 Codex CLI 輸入 `$skillsmp-installer` 並提供搜尋關鍵字。
3. 從結果中選擇要安裝的技能。
4. 安裝完成後重新啟動 Codex。

### 範例

```sh
$skillsmp-installer "web scraper"
```

```sh
$skillsmp-installer "golang backend"
```

### 環境變數

- `SKILL_MAP_API_KEY`: SkillsMP API key（必填）。

## English

This skill lets you search SkillsMP for skills and install them into Codex.

Install this skill using the Codex CLI:

```sh
$skill-installer https://github.com/BlakeFunTeis/skillsmp-installer/tree/main
```

Restart Codex to pick up the new skill.

### Usage

1. Set `SKILL_MAP_API_KEY` in your environment ([SkillsMP API key](https://skillsmp.com/docs/api)).
2. Run `$skillsmp-installer` in Codex CLI and provide a search query.
3. Choose a skill from the results to install.
4. Restart Codex after installation.

### Examples

```sh
$skillsmp-installer "web scraper"
```

```sh
$skillsmp-installer "golang backend"
```

### Environment Variables

- `SKILL_MAP_API_KEY`: SkillsMP API key (required).
