# Package And Type Semantics Guidance

Use this reference when a non-trivial business application is adding or restructuring domain types, use cases, ports, adapters, or architecture tests. It complements the selected architecture style; it does not replace DDD modeling or a style-specific dependency rule.

## Package And Type Semantics Preflight

Before implementation, record a project-local inventory and package decision for the affected increment:

1. List business capabilities, aggregates, child entities, identifiers, value objects, domain events, domain policies/services, history records, enums, and exceptions.
2. List use cases and their application-owned commands, queries, results, expected failures, and any proposed neutral input model.
3. List secondary contracts by responsibility: aggregate repository, lookup, query, store, lease/CAS/history, external gateway, technical port, and adapter-local protocol/client model.
4. Choose the smallest navigable package tree. Prefer business capability, aggregate, or use case before technical role; introduce `shared` or `common` only as a narrowly documented exception.
5. Convert the decisions into architecture tests before moving or adding production types.

## Primary Port Contract Vocabulary Preflight

Before implementing or restructuring an application boundary, record one vocabulary for each primary contract:

1. `*UseCase` is the inbound port interface. A primary-port root should contain only use-case interfaces once model count makes navigation difficult.
2. A mutating operation receives an application-owned `*Command`. `*Input` must not coexist with `*Command` for the same use case; prefer `*Command` unless the project explicitly records a narrower reason for neutral input vocabulary.
3. A read operation receives an application-owned `*Query` or explicitly named read criteria.
4. An application output is a `*Result`. Keep transport rendering in the inbound adapter.
5. `*Request` and `*Response` name inbound-transport or protocol models only. Application code must not own `*Request` / `*Response` models, including outbound secondary-port models; use a command, query, result, snapshot, instruction, or port-specific contract name instead.
6. Split models only when navigation or ownership benefits: commonly `port.in.command`, `port.in.query`, and `port.in.result` for top-level models. Keep small, tightly coupled contract records nested in their owning port or service when that is easier to navigate.
7. Convert the selected vocabulary into architecture tests before implementation. A typical strict rule is: `*Command` must reside in a `port.in.command` or `port.out.command` package when top-level; `*Query` must reside in a `port.in.query` package when top-level; and `*Result` must reside in a `port.in.result` or `port.out.result` package when top-level.

Do not create the subpackages for symmetry on a two-type port. Do create them when the primary-port root otherwise mixes interfaces, inputs, and outputs.

## Package Granularity Signals

A global technical package is acceptable only while it remains easy to navigate. The package-granularity signals below are reasons to split it:

- unrelated use cases share one global `application.port.in` or `application.port.out` package;
- package content must be interpreted by suffix rather than by capability or aggregate;
- a domain root mixes aggregate roots, child entities, IDs, value objects, events, enums, and exceptions;
- an application root mixes use cases, orchestration services, commands, queries, results, exceptions, and outbound contracts;
- adapter code cannot distinguish a port implementation, protocol DTO, concrete client, mapper, or runtime helper;
- adding a type requires a debate about ownership because multiple global packages appear equally plausible.

Do not split merely because a package is large. Split when business meaning, ownership, or navigation has eroded. Do not create category packages for symmetry, and do not create a broad `shared` dumping ground.

A common non-trivial Hexagonal shape is:

```text
context.domain.<aggregate-or-concept>
context.application.<capability>...port.in
context.application.<capability>...port.out
context.adapter.in.<transport>.<feature>
context.adapter.out.<technical-shape>.<feature-or-system>
```

The exact names are project decisions. Business meaning wins over suffix-first folders such as a global `valueobject`, `dto`, or `manager` package.

## Type Semantics Inventory

| Semantic | Meaning | Typical Java signal |
|---|---|---|
| Aggregate Root | Owns a consistency boundary and lifecycle | Aggregate-root marker/base; aggregate repository |
| Child Entity | Has local identity inside an aggregate | Entity marker/base; no independent repository |
| Identifier | Identity of an aggregate or entity | Identifier marker; usually one-field record |
| Value Object | Immutable value equality | Value-object marker; record or final class |
| Domain Event | Business fact that already happened | Domain-event marker |
| Domain Service / Policy | Domain behavior without object state | Stateless domain class/function |
| History Record | Append-only history or audit fact | Explicit history contract; not automatically a domain event |
| Enum | Closed state or classification | Native enum |
| Exception | Named failure outcome | Exception type |

A Java `record` is syntax, not a domain classification. A record can be an identifier, value object, event, application model, or adapter protocol model. Every domain type must have an explicit semantic in the inventory or a recorded exception.

## Naming Contract Matrix

| Name | Owner / location | Meaning |
|---|---|---|
| `*UseCase` | Application capability primary port | Inbound use-case contract |
| `*Command` | Application command or secondary-port contract | Application-owned write intent |
| `*Query` | Application query capability | Application-owned read intent |
| `*Input` | Restricted application capability | Neutral input only when explicitly chosen; it must not duplicate a `*Command` for the same operation |
| `*Result` | Application capability | Application-owned output model |
| `*Request`, `*Response` | Inbound adapter only | Transport/protocol DTO |
| `*Repository` | Domain aggregate boundary | Aggregate lifecycle and command-side loading |
| `*Store` | Application secondary contract | Non-aggregate persistence or state access |
| `*QueryPort` | Application secondary contract | Read/read-model access |
| `*Gateway` | Application secondary contract | External business-system contract |
| `*Port` | Application secondary contract | Technical or abstract capability contract |
| `*Adapter` | Outer adapter | Concrete port implementation |
| `*Client` | Outer adapter | Concrete HTTP/SDK/protocol client |
| `*Controller` | Inbound adapter | Transport entry point |

These are defaults, not universal industry rules. A project may choose different names, but it must use one vocabulary consistently and guard it with architecture tests. In particular, `Gateway` should not name both an application contract and its concrete adapter implementation; `Client` must not leak into domain or application packages.

## Architecture Test Conversion

Convert the inventory into narrow project-local rules, typically:

- `*Id` domain types implement the selected identifier marker;
- non-ID, non-event domain records implement the selected value-object marker or a documented exception;
- aggregate roots and child entities use the selected aggregate/entity markers;
- domain events use the selected event marker;
- top-level `*Command`, `*Query`, and `*Result` models keep their selected contract packages;
- `Request` / `Response` models stay in inbound adapters; application code must not own `*Request` / `*Response` models;
- application primary-port roots contain only `*UseCase` interfaces when the project selected the strict contract layout;
- `Repository`, `Store`, `QueryPort`, `Gateway`, `Port`, `Adapter`, and `Client` keep their selected meanings;
- classes in a capability depend only on the models and ports owned by that capability;
- bounded contexts cross only through their selected application contracts.

Add a marker-coverage guard when using marker-based framework rules. An empty matched set can otherwise create a vacuous pass. Keep explicit migration exceptions in the project test with a reason and remove them after cleanup.
