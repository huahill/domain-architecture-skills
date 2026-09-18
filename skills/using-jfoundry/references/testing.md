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
- Application and worker/boot composition classes that call `AggregateRepository.findById` or `findByIdForUpdate` must own a transaction boundary: inject jFoundry `TransactionRunner`, or use a `Transactional*` use-case decorator. Do not invent a project-local transaction port. Record a red architecture test that rejects an aggregate load without that boundary.
- Do not wrap outbound HTTP, SDK, or broker calls in the same transaction that loaded the aggregate. Load a snapshot or lookup result, then call the external system outside the transaction.

## Domain type semantics and naming rules

Record a project-local semantic inventory before writing marker or naming rules. At minimum, guard the selected meaning of `Identifier`, `ValueObject`, `BaseAggregateRoot`, `BaseEntity`, `DomainEvent`, `Request`, `Response`, `Repository`, `Store`, `QueryPort`, `Gateway`, `Port`, `Adapter`, and `Client` for the packages being changed.

Marker-based rules can pass vacuously when no type carries the marker. Add a marker coverage assertion for the semantics the project actually uses, and record narrowly scoped migration exceptions with reasons. For example, non-ID, non-event domain records should implement `ValueObject` unless the inventory explicitly classifies them otherwise; `Gateway` should be an application outbound contract, while `Adapter` and `Client` remain outer-adapter implementation names.

Architecture tests validate the project's selected meanings; they do not infer aggregate ownership from names alone. Read `references/upstream-documentation.md` for exact architecture-rule entrypoints and runtime test requirements.

## Exception and problem mapping rules

When failure behavior is selected, convert the Exception And Problem Contract Preflight into tests:

- domain and application exception types extend `DomainException` or `ApplicationException`;
- expected domain, application, and external-access failures map through the selected runtime, such as `ProblemDetailsExceptionHandler`;
- application `ProblemMapper` beans are tested for custom problem types and extensions;
- project `@RestControllerAdvice` / `@ControllerAdvice` declarations are forbidden unless a narrow legacy protocol compatibility exception is recorded;
- scheduler, job, and outbound-result retry classification is tested without turning a generic exception into the durable retry contract.
- polling, reconciliation, and recovery loops retain their selected log-and-continue semantics for both framework-classified failures and unrelated runtime failures.
