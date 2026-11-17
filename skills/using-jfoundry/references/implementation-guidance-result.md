# JFoundry Implementation Guidance Result Protocol

Use this protocol for jfoundry project setup, modification, and framework-landing work. Consume confirmed Domain Modeling and Architecture Guidance results when present. Translate those decisions into jfoundry choices; never override an earlier architecture decision.

## Required Shape

Return the shared envelope followed by the sibling `JFoundry Landing` payload. Complete every envelope field, but include only applicable landing fields.

```text
Phase: JFoundry Implementation Guidance
Status: completed | needs-input | not-applicable
Inputs:
Summary:
Assumptions:
Decisions:
Constraints:
Evidence:
Open Questions:
Artifacts:
Recommended Next Step:
Handoff Notes:

JFoundry Landing:
  Java version:
  Version source:
  Selected capabilities:
  Runtime choice:
  Application runtime integration policy:
  Project / Maven module shape:
  Primary architecture style:
  Other optional integrations (excluding Outbox, Inbox, locks, and brokers):
  Package roles / dependency direction:
  Architecture annotations:
  Port ownership:
  Aggregate repositories / read-side contracts or ports:
  Persistence mappers / data mapping:
  Exception handling / boundary mapping:
  Outbox / Inbox / lock / broker decisions:
  Templates / placeholders:
  Verification commands:
  Readiness for implementation planning:
```

The specialist owns the `JFoundry Landing` payload. Select its fields from the confirmed domain and architecture results, project evidence, and the relevant jfoundry references. Omit fields that do not apply rather than filling them speculatively. `Persistence mappers / data mapping` must name the chosen adapter shape for each aggregate being landed: `MybatisPlusAggregateRepository` with one `MybatisPlusAggregateData`/`MybatisPlusDataMapper`/`BaseMapper`, a business persistence adapter that keeps root-plus-dependent synchronization complete, `JpaAggregateRepository` with `JpaAggregateMapper`, or a direct repository implementation. Do not treat the MyBatis-Plus data types as a JPA or shared persistence contract. Do not write "mapper and data object in adapter.out.persistence" as a substitute for that shape. This result guides the next implementation activity; it does not claim that production code was written or verified, and it must not copy persistence or runtime tutorials into the business project handoff.

`Java version` is the language baseline for every later Java change in the project. Maven, persistence, messaging, and runtime assembly do not limit where it applies. Read `references/java-baseline.md` before writing or changing Java. Do not add another baseline field.

`Version source` names the project build file that selects the current jfoundry release. `Selected capabilities` names the capabilities this landing uses. Do not record a jfoundry release version, BOM version, or Maven coordinate in the result or in `docs/domain-architecture/`. Those products keep releasing. Implementation resolves coordinates and mechanics again from the project build and the selected release documentation.

It is an input to detailed planning, not the detailed plan itself. When a process companion is selected,
that companion owns its specification, plan, tasks, files, and execution state. Otherwise, detailed plans
belong under the workflow's default `docs/domain-architecture/plans/` directory. Do not duplicate a
companion's artifacts.

## Status And Applicability

- Use `not-applicable` when the target does not use jfoundry and the user did not request it. Record why no framework landing is needed.
- Resolve the primary architecture from confirmed Architecture Guidance, project evidence, established conventions sufficient for the requested change, or an explicit user choice. Do not manufacture an architecture decision inside the JFoundry landing.
- For an existing project or simple CRUD change, return `completed` when established conventions are sufficient and record that evidence; an upstream phase may be `not-applicable` when it adds no substantive decision.
- Use `needs-input` for architecture only when the unresolved choice materially changes dependency direction, package or module placement, architecture sketches, or architecture tests. Recommend `domain-architecture-guidance` and ask the smallest blocking question.
- Use `needs-input` for the Java baseline, runtime, module shape, persistence choice, or messaging requirement only when it prevents a responsible landing. Ask the smallest blocking question rather than choosing an unsafe exact value. Do not block on or record an exact jfoundry release version; the project build selects it.
- Keep nonblocking uncertainty in **Open Questions** or **Handoff Notes** and return `completed` when the landing is usable for its recommended next step.
- Return to architecture guidance when a jfoundry layout or convention conflicts with the confirmed architecture. Preserve the architecture result while the conflict is resolved.

Optional integrations are absent unless the use case justifies them. Do not add distributed locks, Outbox, Inbox, broker integration, or external messaging merely to complete the payload. Use the detailed dependency, architecture, persistence, repository/port, runtime, and integration references for selection rules instead of duplicating them here.

When a runtime is selected, record whether application code uses only framework-neutral jfoundry
contracts, may directly use selected-runtime orchestration support at declared application
boundaries, or follows a project-specific hybrid. Record that domain code remains free of runtime
and technology APIs, and name delivery, ORM, mapper, broker-record, cache-client, or SDK types
that remain outside application. Do not make this field block framework-neutral architecture work
when the runtime is undecided.

Consume the upstream Application Runtime Integration Policy when it exists. JFoundry runtime
guides, package templates, and annotations specify versioned landing mechanics; they do not
override the project's decision about a composition root, global cross-cutting components, or
adapter-local protocol mapping. Record a conflict and return to architecture guidance rather than
silently applying a template's `boot` package.
