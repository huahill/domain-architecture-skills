# First Use Guide

## Minimal Prompt

Use this prompt when adding VAdmin to a Java application:

```text
Use $using-vadmin to add VAdmin administration to a Java application.
Base package: PACKAGE_NAME
Runtime: Spring Boot, undecided
Identity: local IAM, OIDC, self-provided, or undecided
Visual language: vaadin, ant, or undecided
```

## Agent Sequence

The agent should:

1. Confirm or infer the base package and Java version (25 required).
2. Resolve the runtime. Spring Boot is currently the only supported runtime. For an undecided runtime, proceed with framework-neutral module declaration and record the pending adapter choice.
3. Read `spring-boot-runtime.md` for the confirmed runtime, then add the starter dependency and configure Vaadin package discovery.
4. Resolve the identity strategy. Local IAM needs PostgreSQL; self-provided identity can disable it. Read `identity.md`.
5. Declare each business `AdminModule` bean. Read `module-declaration.md` for the required metadata.
6. Add `@Uses` production anchors for each dynamic view. Read `production-anchor.md`.
7. Run Maven verification.

## Architecture-Neutral Defaults

Use these defaults when the user asks for scaffolding and the choice is independent of architecture:

- Java 25
- Spring Boot runtime (the only currently supported runtime)
- Local IAM enabled (default PostgreSQL + Flyway)
- `vaadin` visual language
- No OIDC unless explicitly requested

## When To Ask Before Proceeding

Ask before continuing when:

- The base package is unknown.
- The identity strategy is unknown and database setup depends on it.
- The user requests OIDC but does not identify the provider configuration.
- A full shell replacement is implied but the user has not confirmed it.
