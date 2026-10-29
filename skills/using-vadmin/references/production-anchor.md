# Production Frontend Anchor

## Production Frontend Plugin

`vadmin-bom` manages `flow-server-production-mode`. A Maven BOM cannot manage
`flow-maven-plugin`, so the plugin needs an explicit version.

That version must equal the Flow version managed by the Vaadin platform BOM
imported by the selected `vadmin-bom` release. It can be a newer patch than the
platform number. Do not use the platform number as the plugin version.

Read the version from the selected VAdmin release deployment guide. This skill
does not record it.

## Why An Anchor Is Needed

VAdmin registers consumer view routes dynamically from `AdminModule` metadata at
startup. Vaadin's production frontend bundle needs a static reference to each view
class to include it in the optimized bundle. Without the anchor, the view renders in
development mode but is missing from the production artifact.

## How To Add The Anchor

Flow follows `@Uses` only from an entry point such as a `VaadinServiceInitListener`.
A Spring Boot application class is not an entry point, so `@Uses` on that class does
not put the view or its components, such as `TextArea`, into the production bundle.

Subclass `io.github.huahill.vadmin.flow.navigation.AdminModuleViewAnchor` and put one
`@Uses` on the subclass for each consumer dynamic view:

```java
@Uses(InventoryView.class)
@Uses(OrderDetailView.class)
public final class InventoryFrontendAnchor extends AdminModuleViewAnchor {
}
```

Place the subclass with the module's inbound adapter. One subclass can anchor every
dynamic view. Flow discovers it by subtype scan.

## Rules

- Add `@Uses` only for consumer views declared in a business `AdminModule`, and only on the `AdminModuleViewAnchor` subclass.
- Do not put `@Uses` on the Spring Boot application class or any other class that Flow does not visit.
- Do not register the subclass as a Spring bean or through `META-INF/services`. The inherited `serviceInit` is empty and final.
- Do not add `@Uses` for VAdmin's built-in system views (Users, Roles, Permissions,
  Audit). VAdmin owns those anchors.
- Do not put `@Route` on a consumer view. Route registration is driven by module
  metadata, not by the `@Route` annotation.
