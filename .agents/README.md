# `.agents` architecture

`skills/` contains narrow, composable Codex Agent Skills. `rules/` contains shared constraints loaded only when relevant.

The normal team workflow starts from `brand-design`, which inspects the request and loads specialist skills as needed. Specialists may also be invoked directly for narrow work.

Each skill should define:

1. required context or inputs
2. procedure
3. deliverables
4. review / verification
5. failure conditions

Keep the orchestration layer compact. Put reusable domain detail in shared rules instead of duplicating it across skills.
