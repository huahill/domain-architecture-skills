# Module Declaration

## What A Module Declares

A business module is a Spring `@Configuration` class that exposes an `AdminModule` bean.
It tells VAdmin the module's navigation group, pages, permissions, and translation
bundles. VAdmin assembles all modules at startup into one permission catalog, one
navigation tree, and one composite `I18NProvider`.

## Required Metadata

- **Module ID**: unique across the application. Used as a prefix for translation keys.
- **Navigation group**: label key and sort order within the navigation tree.
- **Pages**: each page declares a route, a required permission, an icon key, a title
  translation key, an intent translation key, and a view type.
- **Permissions**: declared in both the page and the module's permission set. Format
  is `domain:resource:action`, for example `inventory:item:read`.
- **Translation bundles**: two message bundles on the classpath — `en_US` and `zh_CN`.
- **View bean**: a Spring bean, normally prototype scope, with no `@Route`. VAdmin
  registers the route from the page metadata and checks the permission before the
  view is constructed.

## Sketch

```java
@Configuration(proxyBeanMethods = false)
public class InventoryModuleConfiguration {
  static final PermissionCode INVENTORY_READ =
      PermissionCode.of("inventory:item:read");

  @Bean
  AdminModule inventoryModule() {
    return AdminModule.of("inventory",
        List.of(new AdminNavigationGroup("inventory", "inventory.navigation", 200)),
        List.of(new AdminPage("inventory.items", "inventory",
            "inventory.items.title", "inventory.items.intent",
            "cube", 100, "inventory/items", INVENTORY_READ,
            InventoryView.class)),
        Set.of(INVENTORY_READ),
        List.of(new AdminMessageBundle("inventory", "i18n.inventory")));
  }

  @Bean
  @Scope(ConfigurableBeanFactory.SCOPE_PROTOTYPE)
  InventoryView inventoryView() { return new InventoryView(); }
}
```

This is a package-role sketch, not a mandatory project layout.

## Translation Keys

Page title and intent keys must start with the module ID. Resolve text with
`getTranslation(page.titleKey())` in the view; do not hard-code labels.

Duplicate module IDs, page IDs, routes, or incompatible translation resources fail
application startup.

## Using Shared Page Patterns

VAdmin provides high-level Flow patterns for common admin workflows: `AdminPageFrame`,
`PageHeader`, `PageToolbar`, and `DataWorkspace`. Use these for standard list, detail,
and edit pages instead of assembling layout primitives. Keep domain-specific CSS scoped
to a module-owned component class and based on documented Vaadin component APIs.

Route exact VAdmin types, API signatures, and pattern names to the selected release
documentation.
