# CLAUDE.md

## Project Overview
This project will be a tool that I can use when going to Mizzou in the fall to get used to campus life and be able to ask questions and research things about daily campus life and how things work. I want multiple categorizes pages I can look through, also including a chatbot using the Claude API I can ask questions if there's something I'm missing or can't find on the guide.

## Architecture
- .py files will be for the app's functionality
- .html files will be for the site's frontend organization (the display and UI)

## Key Decisions
- Use JSON because it's the simplest I know and I already have experience with it.
- Use Flask because I have 2 projects worth of experience with it already.

## Constraints
- Never commit .env or any file containing API keys
- Error handling must be explicit — no bare except clauses
- Every function must have a docstring

## Open Questions
[Things not decided yet — Claude Code can raise these]