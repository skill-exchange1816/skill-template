# AI Skill Template

This is the standard template for creating AI skills for the Internal Skills Hub.

## Quickstart

1. Click **Use this template** to create a new repository in the `skill-exchange1816` organization.
2. Ensure the repository has the `ai-skill` topic.
3. Edit `skill.yaml` with your skill's metadata.
4. Implement your logic in `src/main.py`.
5. Add tests in `tests/`.
6. Tag a release (e.g., `v0.1.0`) to publish it to the hub.

## Manifest Format

See `schema/skill.schema.json` for the full specification.

```yaml
name: my-skill
version: 1.0.0
description: "Brief description"
entrypoint: "src.main:run"
runtime: python3.12
```
