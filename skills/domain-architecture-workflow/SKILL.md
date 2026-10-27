---
name: domain-architecture-workflow
description: "Use when a business software project needs an end-to-end domain and architecture workflow: understanding requirements, modeling domains, deciding DDD/Hexagonal/Onion/CQRS boundaries, planning implementation, or handing off to framework-specific guidance such as jfoundry. Does not require any external workflow skill."
---

# Domain Architecture Workflow

## Purpose

Use this skill as the entry point for business-domain software architecture work. It coordinates domain modeling, architecture guidance, and optional framework-specific landing without depending on any external workflow skill.

If another planning, TDD, or review workflow is already active, use this skill only for the domain and architecture decisions inside that workflow.

## Workflow

1. Understand the business goal, acceptance expectations, actors, workflows, constraints, and uncertainty; select the decision scope and strategic, tactical, or combined modeling depth required by the requested outcome.
2. Use `domain-modeling` for non-trivial business behavior or strategic domain decisions and consume its `Domain Modeling Result`. The coordinator selects the required depth; it does not perform or rewrite the specialist's modeling method.
3. Use `domain-architecture-guidance` to choose appropriate boundaries and consume its `Architecture Guidance Result`.
4. Use `using-jfoundry` only when applicable and after domain and architecture assumptions are clear. If jfoundry use is undecided, continue framework-neutral phases without invoking it and defer the choice until a framework-specific next activity materially requires it.
5. Produce a composite `Domain Architecture Handoff` that makes planning readiness, dependent blockers, and the next owner explicit.
6. Persist workflow-owned artifacts under the default documentation directory, then route detailed planning to its `plans` subdirectory or to the user-selected process companion. The companion alone owns its plan files, tasks, and execution state.
7. During implementation or review, consume the persisted handoff as this project's decisions. Re-invoke the specialist whose concern is being implemented even when that phase is already `completed`. In a confirmed jfoundry project, every Java change is a `using-jfoundry` concern, including domain and application code; Maven, persistence, messaging, and runtime assembly are examples, not the whole trigger. Revisit modeling or architecture only when changed business meaning, drift, or conflicts invalidate assumptions. Write back only newly confirmed project decisions; do not copy specialist tutorials into the handoff.

## Skill Routing

- Use `domain-modeling` for requirements-to-model work: business landscapes and capabilities, system decomposition or modernization, multi-team ownership, Subdomains, Bounded Contexts, Context Maps and context relationships, current/target semantic conflicts, ubiquitous language, business commands, events, aggregates, invariants, value objects, domain services, aggregate lifecycle/access needs, and read needs/read models.
- Use `domain-architecture-guidance` for architecture decisions and reviews: dependency direction, Layered/Onion/Hexagonal/CQRS boundaries, jMolecules-style annotations, architecture tests, and source-aware rule interpretation.
- Use `using-jfoundry` when the target project uses jfoundry, or the user explicitly asks for a jfoundry landing. Once jfoundry is confirmed, every Java change in that project is in scope, including domain and application code. Dependencies, package layout, annotations, repositories, persistence, messaging, runtime assembly, and ArchUnit are examples of landing concerns, not a closed trigger list. `Undecided` alone does not make this specialist applicable.

## Result And Handoff Routing

Read [references/first-use.md](references/first-use.md) when the user asks how to start an end-to-end project, combine this workflow with an optional process companion, or implement from an existing handoff. Persisted artifacts are decision memory, not a substitute for specialist skills.

Read [references/implementation-planning.md](references/implementation-planning.md) when handing a completed analysis to detailed planning, selecting the smallest independently verifiable increment, or later introducing a process companion to an existing handoff.

Read [references/workflow-results.md](references/workflow-results.md) before coordinating phases. Require each specialist to return its own phase-specific payload in the shared result envelope. Check phase status and combine results without rewriting specialist guidance. When a phase reports `needs-input`, pause only dependent progression, preserve completed results, produce an interim handoff with blockers, and ask the smallest blocking question. Treat process companions as optional and user-selected; never make this workflow depend on one.

Do not read this skill directory recursively. Open one of the references above only when its condition matches.

## Handoff Rules

- Do not let framework choices drive the domain model.
- Do not force DDD ceremony into low-complexity CRUD.
- Preserve the specialist-owned modeling scope, depth, and applicable strategic or tactical payload directly or by artifact reference; do not reconstruct it in the coordinator.
- Keep open business questions visible before coding.
- Attribute guidance to the right source: DDD concepts, architecture style constraints, framework conventions, heuristics, or project policies.
- Keep this workflow independent. It can run alongside other process skills, but it must not require them.
- Treat a `Domain Architecture Handoff` as planning input, not as a detailed implementation plan. Use the plugin's default documentation directory for workflow-owned artifacts and never reproduce a selected companion's process artifacts.
- Persist project-specific decisions, constraints, and open questions. Do not copy specialist references, framework tutorials, or sample code into `docs/domain-architecture/`.
- A completed handoff does not replace specialist skills. Implementation still executes the relevant specialist for that increment's concern.
