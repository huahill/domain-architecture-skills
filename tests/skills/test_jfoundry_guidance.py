import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
USING_JFOUNDRY = ROOT / "skills" / "using-jfoundry"
ARCHITECTURE_GUIDANCE = ROOT / "skills" / "domain-architecture-guidance"
WORKFLOW = ROOT / "skills" / "domain-architecture-workflow"
PACKAGE_SEMANTICS = ARCHITECTURE_GUIDANCE / "references" / "package-and-type-semantics.md"
PERSISTENCE = USING_JFOUNDRY / "references" / "persistence-data-mappers.md"
REPOSITORIES = USING_JFOUNDRY / "references" / "repository-and-read-contracts.md"
TESTING = USING_JFOUNDRY / "references" / "testing.md"


class JFoundryGuidanceTests(unittest.TestCase):
    def test_persistence_reference_requires_preflight(self):
        text = PERSISTENCE.read_text(encoding="utf-8")
        self.assertIn("Aggregate Persistence Preflight", text)
        for required in (
            "List aggregate roots",
            "domain aggregate repository contract",
            "add / modify / remove",
            "non-aggregate read, store, CAS, lease, or history contract",
            "Repository suffix",
        ):
            self.assertIn(required, text)

    def test_architecture_guidance_routes_package_semantics_preflight(self):
        text = (ARCHITECTURE_GUIDANCE / "SKILL.md").read_text(encoding="utf-8")
        self.assertIn("package-and-type-semantics.md", text)
        self.assertIn("Package And Type Semantics Preflight", text)

    def test_package_semantics_reference_requires_preflight_and_naming_matrix(self):
        text = PACKAGE_SEMANTICS.read_text(encoding="utf-8")
        for required in (
            "Package And Type Semantics Preflight",
            "Package Granularity Signals",
            "Type Semantics Inventory",
            "Naming Contract Matrix",
            "`*Request`, `*Response`",
            "Repository",
            "Gateway",
            "Client",
        ):
            self.assertIn(required, text)

    def test_workflow_planning_gates_package_and_type_semantics(self):
        text = (WORKFLOW / "references" / "implementation-planning.md").read_text(encoding="utf-8")
        self.assertIn("Package And Type Semantics Preflight", text)
        self.assertIn("architecture tests", text)

    def test_package_semantics_requires_primary_port_contract_preflight(self):
        text = PACKAGE_SEMANTICS.read_text(encoding="utf-8")
        self.assertIn("Primary Port Contract Vocabulary Preflight", text)
        for required in (
                "`*Input` must not coexist with `*Command`",
                "`*Command` must reside in a `port.in.command`",
                "`*Query` must reside in a `port.in.query`",
                "`*Result` must reside in a `port.in.result`",
                "application code must not own `*Request` / `*Response` models",
        ):
            self.assertIn(required, text)

    def test_jfoundry_exception_guidance_requires_preflight_and_guardrails(self):
        text = (USING_JFOUNDRY / "references" / "exception-handling.md").read_text(encoding="utf-8")
        self.assertIn("Exception And Problem Contract Preflight", text)
        for required in (
                "extend `DomainException` or `ApplicationException`",
                "parallel business-exception hierarchy",
                "`ProblemDetailsExceptionHandler`",
                "`@RestControllerAdvice` / `@ControllerAdvice`",
                "legacy protocol compatibility",
                "retryability",
                "polling, reconciliation, and recovery loop",
                "architecture test",
        ):
            self.assertIn(required, text)

    def test_jfoundry_testing_requires_exception_and_problem_rules(self):
        text = TESTING.read_text(encoding="utf-8")
        self.assertIn("Exception and problem mapping rules", text)
        for required in (
                "DomainException",
                "ApplicationException",
                "@RestControllerAdvice",
                "@ControllerAdvice",
                "ProblemDetailsExceptionHandler",
                "ProblemMapper",
                "log-and-continue semantics",
        ):
            self.assertIn(required, text)

    def test_workflow_planning_gates_exception_and_problem_contract(self):
        text = (WORKFLOW / "references" / "implementation-planning.md").read_text(encoding="utf-8")
        self.assertIn("Exception And Problem Contract Preflight", text)

    def test_jfoundry_architecture_requires_domain_type_marker_preflight(self):
        text = (USING_JFOUNDRY / "references" / "architecture.md").read_text(encoding="utf-8")
        self.assertIn("Domain Type Marker Preflight", text)
        for required in (
            "Identifier",
            "ValueObject",
            "BaseAggregateRoot",
            "BaseEntity",
            "DomainEvent",
            "vacuous",
        ):
            self.assertIn(required, text)

    def test_jfoundry_testing_requires_non_vacuous_domain_semantic_rules(self):
        text = TESTING.read_text(encoding="utf-8")
        self.assertIn("Domain type semantics and naming rules", text)
        for required in (
            "Identifier",
            "ValueObject",
            "DomainEvent",
            "marker coverage",
            "`Request`, `Response`",
            "Gateway",
            "Client",
        ):
            self.assertIn(required, text)

    def test_skill_routes_persistence_preflight_before_implementation(self):
        text = (USING_JFOUNDRY / "SKILL.md").read_text(encoding="utf-8")
        self.assertIn("complete the Aggregate Persistence Preflight", text)

    def test_repository_reference_links_preflight_and_read_contracts(self):
        text = REPOSITORIES.read_text(encoding="utf-8")
        self.assertIn("Aggregate Persistence Preflight", text)

    def test_testing_reference_requires_repository_semantic_rules(self):
        text = TESTING.read_text(encoding="utf-8")
        self.assertIn("Repository naming and aggregate adapter rules", text)
        for required in (
            "project-local aggregate inventory",
            "AggregateRepository",
            "MybatisPlusAggregateRepository",
            "direct implementation",
            "Repository suffix",
            "AggregateRepository.findById",
            "Transactional*",
            "TransactionRunner",
            "project-local transaction port",
        ):
            self.assertIn(required, text)

    def test_persistence_reference_requires_transaction_boundary_for_tracked_loads(self):
        text = PERSISTENCE.read_text(encoding="utf-8")
        for required in (
            "findById",
            "TransactionRunner",
            "UnitOfWork",
            "Transactional*",
            "outbound HTTP",
            "lookup or snapshot contract",
        ):
            self.assertIn(required, text)

    def test_spring_runtime_requires_transaction_runner_methods(self):
        text = (USING_JFOUNDRY / "references" / "spring-runtime.md").read_text(encoding="utf-8")
        for required in (
            "TransactionRunner",
            "`run` / `call`",
            "UnitOfWork",
            "`Transactions` helper",
        ):
            self.assertIn(required, text)
        self.assertNotIn("runUnchecked", text)
        self.assertNotIn("callUnchecked", text)

    def test_repository_reference_distinguishes_tracked_loads_from_lookups(self):
        text = REPOSITORIES.read_text(encoding="utf-8")
        for required in (
            "tracked load",
            "TransactionRunner",
            "lookup contract",
        ):
            self.assertIn(required, text)

    def test_using_jfoundry_agents_forbid_duplicating_versioned_facts(self):
        text = (USING_JFOUNDRY / "AGENTS.md").read_text(encoding="utf-8")
        for required in (
            "consumption contract",
            "Three Layers",
            "domain-architecture-guidance",
            "Versioned framework fact",
            "method signatures",
            "selected jfoundry release",
            "project-local",
        ):
            self.assertIn(required, text)

    def test_root_agents_keep_using_jfoundry_from_copying_jfoundry(self):
        text = (ROOT / "AGENTS.md").read_text(encoding="utf-8")
        for required in (
            "thin consumption contract",
            "versioned framework facts",
            "skills/using-jfoundry/AGENTS.md",
            "project-local workarounds",
        ):
            self.assertIn(required, text)




if __name__ == "__main__":
    unittest.main()
