# Identity And Access

## Three Strategies

### 1. Local IAM (Default)

Out of the box, VAdmin provides username/password sign-in with a local user store.
On first startup with an empty database, it creates an `admin` account with the
`administrator` role and all permissions. This requires a PostgreSQL database —
VAdmin manages its own schema through Flyway.

Set `APP_BOOTSTRAP_PASSWORD` before the first start; the initial `admin` account
receives that password. Changing it later does not reset an existing account.

### 2. Optional OIDC

VAdmin supports standard OIDC authorization-code login through the runtime's
security adapter. It maps an authenticated external identity to an existing, enabled
local account. It does not create accounts, synchronize roles, or expose provider
tokens to views.

The external identity must map to a pre-existing local account. Unmapped identities
are rejected. Configure the provider with standard OAuth2 client properties and set
the VAdmin OIDC registration-id property.

### 3. Self-Provided Identity

When the host application provides its own identity and authorization, disable local
IAM. No PostgreSQL database is required for VAdmin in this mode. The host must supply
the identity and authorization contract beans that VAdmin's framework-neutral core
consumes.

## Permission Model

Permission codes follow `domain:resource:action`. Roles are configurable sets of
permission codes. VAdmin checks permissions in two layers:

- **Navigation and route access**: controlled by the permission declared in page
  metadata. Hides pages the user cannot access and blocks direct navigation.
- **Service-level authorization**: the authoritative boundary. Check the permission
  inside the service or command before any write operation.

The permission catalog is defined in code at startup. Administrators can grant
catalog permissions to roles through the Roles administration page, but cannot
invent new permission codes through the UI.

## Out Of Scope

SAML, LDAP, MFA, SCIM, multi-tenancy, organization hierarchies, and row-level data
permissions are not built in. Integrate them through the host's own authentication or
authorization adapter. Never bypass the service-level permission check.

Route exact property keys, OIDC configuration details, and contract bean names to
the selected VAdmin release documentation.
