---
name: using-jfoundry
description: Guide AI agents and developers when starting or modifying Java business projects that use the jfoundry framework. Use for every Java change in such a project, including domain, application, adapter, and test code. Maven dependency selection, architecture landing, aggregate persistence, reliable messaging, Spring, Quarkus, or Helidon runtime assembly, and ArchUnit verification are examples of landing concerns, not a closed trigger list. Re-invoke for any Java edit even if a prior landing document exists. Do not use for maintaining jfoundry internals.
---

# Using JFoundry

Use this skill for downstream business projects, not for changing jfoundry itself. It turns an already selected architecture into JFoundry capability decisions, package roles, version-aware lookup, and verification.

## Decision Flow

1. Before writing or changing any Java, read `references/java-baseline.md`. This includes domain, application, adapter, and test code. Maven, persistence, messaging, and runtime assembly are examples of specialized concerns; they do not define when the baseline applies. A persisted landing does not exempt the edit. If a persisted landing already exists, consume it as the project decisions. Do not implement from `docs/domain-architecture/04-jfoundry-implementation-guidance.md` alone.
2. Read one specialized reference for the concern being changed. Do not read the other references in the routing table, and do not read the skill directory recursively.
   - Adding a dependency: `references/dependencies.md`, then the selected release's documentation, BOM, or source POM. Also read `references/version-selection.md` when the version itself is unresolved.
   - Landing packages or annotations after Hexagonal or Onion has already been selected: `references/architecture.md`. Consume the confirmed Application Runtime Integration Policy from domain-architecture guidance; JFoundry templates do not replace project package ownership decisions.
   - Aggregate persistence: both `references/persistence-data-mappers.md` and `references/repository-and-read-contracts.md`, and complete the Aggregate Persistence Preflight before writing adapters. This is the concern that has two references.
   - One runtime, reliable messaging, locks, exceptions, or tests: the one matching row in the routing table.
   - Exact framework APIs, properties, auto-configuration, or implementation algorithms: `references/upstream-documentation.md` as well as that one concern reference.
3. Preserve the project's selected jfoundry version, runtime, architecture style, and conventions. Ask only when an unknown choice changes a required dependency, package role, or test.
4. When the task must return the JFoundry Implementation Guidance Result, read `references/implementation-guidance-result.md`. A Java edit that follows an existing landing does not read it only to restate that landing.
5. Run the narrowest relevant Maven verification and return the result when one is required.

## Non-Negotiable Boundaries

- Keep domain code free of runtime, ORM, mapper, broker, HTTP, and client-SDK types.
- Keep business orchestration in application code; primary adapters enter through an application boundary rather than calling persistence or clients directly. A secondary adapter that implements an outbound port still must not load an aggregate and choose its state transition.
- Keep technology-specific persistence and messaging in outer adapters or infrastructure.
- Do not select Hexagonal, Onion, CQRS, Spring Boot, Outbox, Inbox, locks, or a persistence provider merely because an implementation is available.
- Keep aggregate repositories for aggregate lifecycle. Add read contracts or ports only when a read responsibility needs one.
- Treat persistence base classes as optional support. A project-local adapter may implement its aggregate repository contract directly.
- Write project Java on the selected release's language baseline. Do not copy the framework repository's comment, formatting, or context-carrier rules into the business project.

## Reference Routing

| Need | Read |
|---|---|
| Any Java change in the business project | `references/java-baseline.md` |
| Result format, assumptions, and unresolved choices | `references/implementation-guidance-result.md` |
| Version, BOM, and capability composition | `references/version-selection.md`, `references/dependencies.md` |
| Architecture landing and package roles | `references/architecture.md` |
| Aggregate repositories and read-side contracts | `references/repository-and-read-contracts.md` |
| JPA, MyBatis-Plus, mappers, and optimistic locking | `references/persistence-data-mappers.md` |
| Spring Framework or Spring Boot | `references/spring-runtime.md` |
| Quarkus CDI, JTA, REST, JPA, Outbox, Inbox, or broker assembly | `references/quarkus-runtime.md` |
| Helidon MP CDI, JTA, JAX-RS, JPA, Outbox, or Inbox assembly | `references/helidon-runtime.md` |
| Outbox, Inbox, broker selection, and JPA Inbox database support | `references/outbox-inbox.md` |
| Cross-instance locking | `references/distributed-locks.md` |
| Exception ownership and boundary translation | `references/exception-handling.md` |
| Architecture tests and Maven verification | `references/testing.md` |
| Exact framework behavior for the selected version | `references/upstream-documentation.md` |

Use the selected release as the source of truth for Maven coordinates, configuration, APIs, and framework behavior. This skill deliberately does not maintain a dependency catalog or code skeletons for those versioned facts.
