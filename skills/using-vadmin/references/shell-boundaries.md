# Shell Boundaries

## Default Shell Ownership

VAdmin owns the default administration shell: the responsive layout, navigation,
brand area, locale and color-scheme controls, user menu, and the system administration
pages (Users, Roles, Permissions, Audit). A normal consumer does not define a layout,
theme, `AppShellConfigurator`, or system pages.

## What Consumers Must Not Do

- Do not copy or recreate the default shell, layout, theme, or system pages.
- Do not partially replace selected shell components, individual system pages, or
  theme internals.
- Do not register a global stylesheet, mutate global theme properties, or target
  Vaadin component internals from a business module.
- Do not depend on VAdmin visual-language-specific CSS selectors or tokens from a
  business module.

## Business Module CSS

Keep CSS scoped to a module-owned component class. Use documented Vaadin component
variants and Lumo base-style properties. VAdmin handles visual-language-specific
presentation for its own shell and system pages.

## Full Shell Replacement

A custom shell is an explicit, complete replacement — not a customization mechanism
for isolated header, navigation, page, or styling fragments. Only choose it when
the complete product boundary requires a different shell.

A replacement means the consumer owns:

- An alternative `AppShellConfigurator` and `@Theme` configuration.
- A complete layout (`AdminHostLayout`).
- Production frontend anchors for every dynamic view it composes.

The replacement still uses VAdmin's module assembly, permission catalog, route
registration, and composite translations. Most consumers should keep the default
shell unchanged.
