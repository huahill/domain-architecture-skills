# Aggregate Persistence Decisions

Use this reference when a business project selects JPA or MyBatis-Plus aggregate persistence. Persistence is an outer adapter concern; domain aggregates remain free of ORM annotations, mapper types, table fields, and persistence versions.

## Aggregate Persistence Preflight

Before writing or changing an aggregate adapter, complete this project-local preflight:

1. List aggregate roots in the increment and the invariant each aggregate protects.
2. Name the owning contract for each root as a domain aggregate repository contract; keep it near the aggregate and free of ORM types.
3. Confirm the contract follows the selected jfoundry lifecycle abstraction and that application orchestration calls `add / modify / remove` rather than a generic `save`.
4. Name every non-aggregate read, store, CAS, lease, or history contract separately, with its consumer and result shape; do not give it the Repository suffix.
5. Select an adapter shape below for each aggregate, including any direct implementation exception and the reason runtime weaving or child synchronization makes it necessary.
6. Record existing tables, root-version policy, and database-specific statements, then turn the naming and adapter decisions into architecture tests before implementation proceeds.

If aggregate ownership or lifecycle is unclear, return to domain modeling rather than converting a DAO into a repository.

## Choose The Adapter Shape

| Situation | Recommended shape |
|---|---|
| One MyBatis-Plus root record fully stores one aggregate | `MybatisPlusAggregateRepository` with one `AggregateData`, `DataMapper`, and `BaseMapper` |
| MyBatis-Plus root plus dependent records | Keep complete load/write synchronization in one business persistence adapter; use the base helpers only when they fit |
| One JPA-managed entity graph per aggregate | `JpaAggregateRepository` and `JpaAggregateMapper` |
| Multiple independent entity graphs, stores, or persistence technologies | A business-owned composite adapter or direct repository implementation |
| Framework base obscures project behavior | Implement the aggregate repository contract directly |

Do not override public lifecycle methods on jfoundry repository bases. Use their supported extension points, or choose a direct implementation when the operation does not fit the base.

## Mapping And Transactions

- Keep domain IDs as strong jMolecules identifiers and convert them at the adapter boundary.
- Keep persistence mapping infrastructure-local. A MapStruct mapper may be used, but aggregate restoration must remain explicit.
- Keep aggregate load, domain behavior, and modify/remove in one transaction. Do not assume detached aggregate merge support.
- jFoundry `findById` / `findByIdForUpdate` on a versioned aggregate requires an active runtime transaction. Inject the selected runtime's `TransactionRunner` for that short boundary; HTTP use cases may use a `Transactional*` decorator. Do not invent `UnitOfWork` ports, and do not keep the transaction open across outbound HTTP.
- If the use case only needs codes or identity for an external call, prefer a lookup or snapshot contract over `AggregateRepository.findById`.
- A JPA aggregate is one managed entity graph. For JPA optimistic locking, put `@Version` on the graph root and ensure child-only changes participate according to the selected provider's rules.
- For MyBatis-Plus optimistic locking, put `@Version` on the root data object, configure the interceptor, and select tracked persistence only when the repository shape supports it.
- Do not expose persistence versions or `AggregatePersistenceContext` through domain or business constructors.

## Business-Owned Decisions

The project, not the persistence library, chooses full replacement, differential updates, append-only writes, child-delete ordering, audit mapping, and duplicate-key interpretation. Translate a database constraint to the selected release's documented application conflict outcome only when it represents the intended business conflict.

The business project's handoff records only the chosen adapter shape per aggregate, the existing tables the adapter must reuse, whether `@Version` is present and allowed on the root data, and which statements remain XML because compare-and-set, locking, or database-specific SQL requires them. Do not copy this reference into `docs/domain-architecture/`. Re-read it when implementing or changing persistence adapters.

Resolve the selected release's supported persistence artifacts after choosing the outer adapter and runtime assembly. Read `references/upstream-documentation.md` for coordinates, mapper signatures, helper methods, transaction integration, and provider-specific details.
