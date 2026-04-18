---
name: Project Workflow & Efficiency
description: Managed git pushes, concise communication, and token usage optimization.
---

# Project Workflow & Efficiency Skill

This skill defines the operational constraints for the Raag & Rhythm project to ensure development speed, cost efficiency, and control over remote deployments.

## 1. Git Push Policy
- **NO AUTOMATIC PUSHES**: Never execute `git push` or any command that syncs local changes to a remote repository (GitHub/GitLab) automatically.
- **Local Commits Only**: Standard workflow should involve `git add` and `git commit` to maintain local history.
- **Explicit Request Required**: Only push to the remote repository when the user explicitly says "push to git" or "push to remote".

## 2. Concise Communication
- **No Summaries**: Do not provide detailed summaries or explanations of what has been done after completing a task.
- **Direct Action**: Just perform the requested task. If successful, state "Task complete" or provide a very brief confirmation.
- **User Verification**: Rely on the user to verify the changes in the codebase.

## 3. Token & Scope Management
- **Ask Before Large Tasks**: For any task that involves modifying multiple files, creating complex logic, or tasks that are expected to use a high volume of tokens, stop and ask: "This task is large. Should I proceed?"
- **Confirmation**: Wait for the user's "Yes" or "Proceed" before starting such tasks.
