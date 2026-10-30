# Administration Page Interaction

Read this when adding or changing a business administration view. VAdmin ships Vaadin Aura for the shell and system pages. A business view does not choose another appearance and does not restyle Aura.

Exact pattern constructors and method semantics come from the selected VAdmin release documentation. This reference chooses the pattern and the interaction contract; it does not freeze a call sequence.

## Pattern Choice

| Workflow | Compose with |
|---|---|
| Queryable collection | `AdminPageFrame`, `PageHeader`, `PageToolbar`, `DataWorkspace`, `PagedGrid`, and `CompactDataItem` |
| Short create or edit | `EditorDialog` |
| Read-only details | `DetailDialog` |
| Destructive or state-changing command | `ConfirmationDialog` |
| Completed, rejected, or failed outcome | `OperationFeedback` |
| No rows to show | `EmptyState` inside `DataWorkspace` |

Do not assemble the page from layout, grid, and dialog primitives when one of these patterns covers the workflow. Do not open a new route for a short form, and do not build a second layout for a narrow viewport. `CompactDataItem` is the narrow presentation of the same workspace.

## Interaction Contract

A collection page has one translated title, one translated intent, and at most one primary action. Put that action in the page header. Put query fields in the toolbar and pair them with reset. Show the toolbar as busy while the query runs.

`DataWorkspace` covers four observable conditions:

- Ready: the current page of results is visible.
- Busy: the workspace shows that a query or command is in progress, and commands that would start another change are unavailable.
- Empty: distinguish no data from filtered-empty. No data offers the permitted primary action. Filtered-empty keeps the current query and offers reset.
- Failure: the workspace shows a recoverable failure and offers retry. A failed command leaves entered values in place and leaves the editor open.

Use multi-select and bulk actions only when a real bulk command exists. Hide the selection bar otherwise.

Row commands use a Vaadin tertiary button variant. A destructive or hard-to-reverse command opens `ConfirmationDialog` and states the consequence before it runs. Validation belongs to the editor dialog. Success, warning, and other outcomes use `OperationFeedback`, not a notification constructed in the view.

Hide or disable a command when the current user lacks its permission. Check that same permission in the service before changing state. Every visible string is a translation whose key starts with the module ID. Take icons from the VAdmin icon catalog.

## Boundaries

Do not add business-module CSS. Do not copy the Users, Roles, Permissions, or Audit views; follow the same pattern choices without recreating system pages. Do not change the shell or theme to make one business page look different.

When the same missing workflow appears in more than one module and no shared pattern can express it, extend VAdmin with that pattern. A local layout or stylesheet is not the substitute.

## Check Before Done

Maven verification does not prove the interaction. Before finishing a business view, confirm:

- The workflow uses the pattern row above.
- Busy, no data, filtered-empty, and failure are each represented where that condition can occur.
- A destructive command states its consequence and waits for confirmation.
- A failed edit preserves entered values.
- Copy is translated and commands are permission-checked in the service.
