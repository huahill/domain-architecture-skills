# Spring Boot Runtime Adapter

Spring Boot is currently the only supported runtime for VAdmin. This reference covers
the adapter-specific setup. For exact Maven coordinates, property keys, and
auto-configuration behavior, use the selected VAdmin release documentation as the
source of truth.

## Dependency

Add the VAdmin Spring Boot starter to the application. The starter aggregates the
default shell, system administration, module assembly, and all Spring adapters in
one dependency.

For `spring-boot:run` development, also add Vaadin's optional development server
directly. It is intentionally not transitive and is excluded from the production
artifact.

## Vaadin Package Discovery

VAdmin registers its default shell and system view packages for Vaadin discovery.
If the application declares `@EnableVaadin` explicitly, that declaration replaces
the default scan roots. Include the VAdmin root package so Vaadin discovers the
default shell, system views, and Flow error handling.

This is Vaadin's route-discovery requirement, not custom shell composition.

## Database And Flyway

When local IAM is enabled (default), VAdmin manages its own tables through Flyway
and validates them with `ddl-auto: validate`. Point VAdmin at a PostgreSQL datasource.
Consumer Flyway migrations should live in a separate location from VAdmin's own
migrations.

When local IAM is disabled, no database is required for VAdmin.

## Configuration

VAdmin uses a unified `vadmin.*` property namespace for all its settings: brand name,
visual language, shell options, local IAM, OIDC, and bootstrap password. All
properties have working defaults. Environment variable names (such as
`APP_BOOTSTRAP_PASSWORD`) are deployment contracts and do not change when YAML
property keys change.

Route exact property keys, default values, and environment-variable mappings to the
selected VAdmin release documentation.
