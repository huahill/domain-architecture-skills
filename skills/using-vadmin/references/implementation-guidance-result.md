# VAdmin Implementation Guidance Result

Return this result envelope after completing the decision flow. Use `completed` when
the adoption setup is actionable; use `needs-input` only when a missing choice blocks
responsible implementation.

## Result Format

```text
VAdmin Implementation Guidance Result
  status: completed | needs-input
  runtime: Spring Boot | undecided
  identity: local-iam | oidc | self-provided | undecided
  visual-language: vaadin | ant | undecided
  modules:
    - module-id
      pages: [page-id, ...]
      permissions: [permission-code, ...]
      translation-bundles: [base-name, locales]
      production-anchors: [view-class, ...]
  assumptions:
    - ...
  unresolved:
    - ...
  next-activity: ...
```

## Status Semantics

- `completed`: the consumer can proceed to add dependencies, declare modules, and
  run verification.
- `needs-input`: a blocking choice is unresolved (for example, the identity strategy
  is unknown and database setup depends on it). Preserve completed results, emit an
  interim result, and ask the smallest blocking question.

## What To Record

- The confirmed runtime and identity strategy.
- Each declared module with its pages, permissions, and translation bundles.
- Whether `@Uses` production anchors are in place for every dynamic view.
- Whether the default shell is retained or a full replacement is intended.
- Assumptions made when the user did not specify a choice.
- Unresolved choices that do not block the current step but should be tracked.
