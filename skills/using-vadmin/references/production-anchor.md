# Production Frontend Anchor

## Why An Anchor Is Needed

VAdmin registers consumer view routes dynamically from `AdminModule` metadata at
startup. Vaadin's production frontend bundle needs a static reference to each view
class to include it in the optimized bundle. Without the anchor, the view renders in
development mode but is missing from the production artifact.

## How To Add The Anchor

Put one `@Uses` annotation on the application's Spring Boot configuration class for
each consumer dynamic view:

```java
@Uses(InventoryView.class)
@Uses(OrderDetailView.class)
@SpringBootApplication
public class InventoryApplication {
}
```

## Rules

- Add `@Uses` only for consumer views declared in a business `AdminModule`.
- Do not add `@Uses` for VAdmin's built-in system views (Users, Roles, Permissions,
  Audit). VAdmin owns those anchors.
- Do not put `@Route` on a consumer view. Route registration is driven by module
  metadata, not by the `@Route` annotation.
