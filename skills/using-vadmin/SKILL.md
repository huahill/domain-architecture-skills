---
name: using-vadmin
description: Guide AI agents and developers when adding or modifying VAdmin administration capabilities in a Java application. Use for runtime adapter selection, dependency setup, AdminModule declaration, permission and translation resources, production frontend anchors, identity and access configuration, and shell boundary decisions. Re-invoke when adding modules, changing identity strategy, or modifying the default shell. Do not use for maintaining VAdmin internals.
---

# Using VAdmin

Use this skill for downstream applications that adopt VAdmin, not for changing VAdmin itself. It turns an already selected architecture into VAdmin capability decisions, runtime adapter setup, module declarations, and verification.

## Decision Flow

1. Confirm the application runs on Java 25 with Vaadin Flow 25.x on the classpath. If Vaadin Flow is not yet present, the starter brings it in transitively.
2. Confirm the runtime. VAdmin currently supports Spring Boot as the only runtime; other runtimes (Helidon, Quarkus) are future adapters. Record an undecided runtime as a pending choice and do not block framework-neutral module declaration.
3. Read the runtime adapter reference for the confirmed runtime. Currently `references/spring-boot-runtime.md` is the only runtime reference. Add the starter dependency and configure Vaadin package discovery.
4. Confirm the database and identity strategy. The default local IAM needs a PostgreSQL database; a self-provided identity strategy can disable it. Read `references/identity.md` for the three strategies. Self-provided identity contract implementations belong in outbound adapters; the composition root only wires them.
5. Read `references/module-declaration.md` and declare each business `AdminModule` bean with module ID, pages, permissions, icon keys, and bilingual translation bundles. Read `references/production-anchor.md` and add `@Uses` anchors for each dynamic view.
6. Run the narrowest relevant Maven verification and return the VAdmin Implementation Guidance Result.

## Non-Negotiable Boundaries

- Do not copy or recreate the default shell, theme, system administration pages, or `AppShellConfigurator`. VAdmin owns them.
- Do not put `@Route` on a consumer view. VAdmin registers routes from `AdminModule` page metadata.
- Do not bypass the service-level permission check. Navigation visibility and route guards improve the experience; the authoritative boundary is in the application or platform use case.
- Do not register a global stylesheet, mutate global theme properties, or target Vaadin component internals from a business module. Keep domain-specific CSS scoped to a module-owned component class.
- Do not add `@Uses` for VAdmin's built-in system views. VAdmin owns those production anchors.
- Do not partially replace the shell. A custom shell is an explicit complete replacement.
- Do not implement VAdmin identity or audit contracts in the composition root. Those are secondary adapters.
- Do not model host IAM tables as the host's aggregate repositories.

## Reference Routing

| Need | Read |
|---|---|
| First-use prompt, agent sequence, and when to ask | `references/first-use.md` |
| AdminModule declaration: ID, pages, permissions, translations | `references/module-declaration.md` |
| `@Uses` production frontend anchors | `references/production-anchor.md` |
| Local IAM, OIDC, or self-provided identity | `references/identity.md` |
| Shell ownership and full-replacement boundary | `references/shell-boundaries.md` |
| Spring Boot runtime adapter setup | `references/spring-boot-runtime.md` |
| Result format, assumptions, and unresolved choices | `references/implementation-guidance-result.md` |

Use the selected VAdmin release documentation as the source of truth for Maven coordinates, configuration properties, API signatures, and framework behavior. This skill deliberately does not maintain a dependency catalog or property reference for those versioned facts.
