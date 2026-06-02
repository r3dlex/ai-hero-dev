# Spec: ai-hero-cli

**Origin:** https://github.com/mattpocock/ai-hero-cli
**Role:** CLI for navigating and running AI Hero exercises

## Commands

```bash
ai-hero exercise        # interactive picker
ai-hero exercise 1      # run exercise 1 directly
ai-hero internal upgrade  # upgrade AI SDK packages
```

## Shortcuts (during exercise)

| Key | Action |
|-----|--------|
| Enter | Choose exercise |
| n | Next |
| p | Previous |
| q | Quit |
| h | Help |

## Expected Structure

```
exercises/
└── 1-section/
    └── 1-exercise/
        ├── main.ts
        └── readme.md
```
