# Application Java Baseline

Read this reference before writing or changing Java in a business project that uses jfoundry.
It covers domain types, application services, adapters, tests, and any other project Java.
Maven selection, persistence, messaging, and runtime assembly are examples of later specialized
concerns. They are not the list of changes that need this baseline. A completed landing does not
exempt a later edit. Specialized references add capability rules; they do not replace this one.

## Language Level

Compile and run application Java on the baseline recorded by the selected jfoundry release's
compatibility documentation. Do not hardcode a language level in this skill, and do not choose a
newer or older level from memory.

The `Java version` already recorded in the JFoundry Landing is that baseline for later Java in the
same project. Preserve it unless the user asks to migrate, then follow
`references/version-selection.md`.

When a baseline language or library feature already expresses a semantic decided by architecture
guidance, use that feature. Match the form the project already uses for the same semantic. Do not
invent a second style beside it, and do not revive older boilerplate that the baseline makes
unnecessary. A language feature does not change type meaning: a `record` stays syntax, not a domain
classification. Identifier, value-object, command, and adapter-model decisions remain in
`domain-architecture-guidance`.

Do not enable a preview feature unless both the selected release's compatibility documentation and
the business project already enable that preview.

Exact feature lists, preview status, and version mechanics stay in the JDK and the selected
release's compatibility documentation. Do not copy them here.

## Comments

Follow the business project's published comment policy when it has one.

If it has none, comment only non-obvious intent, in the language already used by the surrounding
code. Do not add comments that restate the code.

Do not import the framework repository's comment rules, including English-only source comments and
Markdown `///` documentation comments, unless this project publishes a public API and has adopted
those rules itself.

## Out Of Scope

These are framework-internal conventions. Do not impose them on a business project, and do not add
ArchUnit rules for them:

- framework-internal context carriers, including `ScopedValue`
- policies about catching `Error`
- jfoundry module layout
- indentation or formatter choices beyond matching the file being edited

## Verification

Architecture tests do not enforce this baseline. Before finishing a Java edit, check it against the
selected release's compatibility documentation and the forms already used in the project for the
same semantic.
