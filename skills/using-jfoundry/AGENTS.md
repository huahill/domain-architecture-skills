# Maintaining `using-jfoundry`

These instructions apply only when changing this skill or its bundled references.

`using-jfoundry` is a **consumption contract** for downstream business projects. It is not a
jfoundry manual, not a second architecture skill, and not a place to freeze one project's incident
into a universal rule.

## Three Layers

Classify every finding before editing. Put it in one layer only.

| Layer | Owner | Ask | Typical content |
|---|---|---|---|
| Modeling and architecture | `domain-modeling`, `domain-architecture-guidance` | What is the model, and which architecture style applies? | Bounded contexts, package roles, Command/Query/Result semantics, Value Object vs Entity |
| Consumption contract | `using-jfoundry` | How should a business project use the selected jfoundry release? | Capability selection, landing after an architecture is chosen, anti-reinvention, routing, project-side ArchUnit obligations |
| Versioned framework fact | selected jfoundry release documentation or source | What is true of this jfoundry version? | Maven coordinates, properties, method signatures, exception mechanics, auto-configuration, runtime diagnostics, compatibility matrices, starter catalogues |

If a sentence would have to change when jfoundry ships a new minor or patch, it is a versioned
framework fact. Document it in jfoundry, then keep only a pointer here.

## Content Ownership

Keep here:

- Whether a capability is selected for this project, and why.
- Where the selected capability lands in the already chosen architecture.
- What the project must not reinvent, named as a stable contract rather than an API walkthrough.
  Examples: do not invent a `UnitOfWork` port; do not create a parallel business-exception hierarchy;
  do not name every persistence adapter a `Repository`.
- Version-aware routing to the selected JFoundry release documentation.
- Project-side verification that the consumption contract is kept, such as ArchUnit obligations.

Do not keep here:

- Maven coordinates, BOM versions, starter lists, or compatibility matrices.
- Configuration properties, auto-configuration class names, or Native Image hints.
- Method signatures, checked-versus-unchecked exception declarations, or call sequences.
- Runtime internals such as whether an HTTP exception handler logs a cause.
- A temporary incident, investigation, or workaround from one project, unless it has become a
  stable downstream contract that every affected project must follow.

Stable JFoundry type names may appear when they identify a landing or an anti-reinvention rule
(`TransactionRunner`, `DomainException`, `AggregateRepository`). Route their exact semantics and
version-specific mechanics to the selected release documentation. Prefer “use the selected
release's `TransactionRunner`; do not wrap it” over copying `run` / `call` signatures or exception
models into this skill.

## Change Check

Before adding or tightening guidance after a project incident:

1. Classify the finding against the three layers above. Do not patch this skill by default.
2. If the framework is incomplete or misleading, change jfoundry documentation or code first.
   This skill may then add a route or an anti-reinvention sentence, not a copy of the new API.
3. If the finding is framework-neutral architecture, edit `domain-architecture-guidance` or
   `domain-modeling` instead.
4. If the finding is project-local, leave it in that project. Do not promote it into the plugin.
5. Reject a draft sentence that contains a method name, property key, exception package, starter
   coordinate, or “this project just hit”, unless the method or type name is required to name a
   consumption contract and the mechanics are routed upstream.
6. After a jfoundry API or runtime change, update jfoundry first, then delete any copied fact from
   this skill rather than chasing the new signature here.
