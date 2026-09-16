# Architecture And Integration Verification

Resolve the selected release's architecture-test artifact and rule entrypoints in the matching architecture documentation. Keep the selected annotations or rings in the analysis scope. Do not mix Hexagonal and Onion rules. Add optional CQRS or aggregate-repository rules only when the project uses those concepts; record temporary migration exceptions and remove them after cleanup.

Place the test in the module or test aggregate that can see the packages being analyzed. Verify the narrowest relevant scope first:

```bash
mvn -pl <module> -am test
```

Use `mvn test` for a single-module project or when the change crosses modules. Add focused runtime tests for selected persistence, transaction, broker, Outbox, Inbox, or WebMVC behavior.

## Repository naming and aggregate adapter rules

When aggregate persistence is selected, record a project-local aggregate inventory first. Translate that inventory into narrow architecture rules for the project's chosen package layout:

- Interfaces called `*Repository` must represent aggregate lifecycle and command-side loading and, for jfoundry projects, be assignable to `AggregateRepository`.
- Non-aggregate application contracts for lookup, query, snapshot, event history, lease, or CAS responsibility must not use the Repository suffix.
- A MyBatis-Plus adapter for a single-root aggregate must use `MybatisPlusAggregateRepository` or the release-documented equivalent. A composite root-plus-dependents adapter must preserve complete synchronization and runtime weaving. A direct implementation must be an explicit recorded exception, not an untracked shortcut.
- Add a focused runtime test when adapter behavior depends on transaction boundaries, persistence observers, or domain-event context wiring.

Architecture tests validate the project's selected meanings; they do not infer aggregate ownership from names alone. Read `references/upstream-documentation.md` for exact architecture-rule entrypoints and runtime test requirements.
