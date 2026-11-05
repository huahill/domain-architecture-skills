import copy
import unittest

from scripts.validate_handoff import validate_document


def valid_interim():
    return {
        "contract_version": "1.0",
        "lineage_id": "da-lineage-example-001",
        "handoff_id": "da-handoff-example-001-r1",
        "revision": 1,
        "kind": "interim",
        "parent_handoff_id": None,
        "status": "active",
        "request": {"outcome": "design order cancellation", "process_companion": None},
        "scope": {
            "decision_scope": "increment",
            "modeling_depth": "both",
            "increment_id": "order-cancellation",
            "non_goals": [],
        },
        "producer": {
            "skill": "domain-architecture-workflow",
            "plugin_version": "0.3.0",
            "generated_at": "2026-09-07T00:00:00Z",
        },
        "phases": [
            {
                "phase": "domain-modeling",
                "status": "needs-input",
                "result_ref": "domain-modeling-result",
                "affects": ["architecture-guidance"],
            },
            {
                "phase": "architecture-guidance",
                "status": "not-applicable",
                "result_ref": None,
                "affects": ["planning"],
            },
            {
                "phase": "jfoundry-implementation-guidance",
                "applicability": "undecided",
                "status": "not-applicable",
                "result_ref": None,
                "affects": ["planning"],
            },
        ],
        "decisions": {
            "confirmed": [],
            "accepted_assumptions": [],
            "constraints": [],
        },
        "blockers": [
            {
                "blocker_id": "B-001",
                "owner_phase": "domain-modeling",
                "affects": ["architecture-guidance"],
                "question": "Which subject owns the invariant?",
                "resolution_required": True,
                "status": "open",
                "resolution_ref": None,
            }
        ],
        "open_questions": [],
        "artifacts": [
            {
                "artifact_id": "domain-modeling-result",
                "phase": "domain-modeling",
                "kind": "result",
                "path": "docs/domain-architecture/01-domain-modeling.md",
                "content_digest": None,
                "status": "active",
            }
        ],
        "planning_readiness": {
            "status": "blocked",
            "consumed_increment": "order-cancellation",
            "dependent_blockers": ["B-001"],
            "next_owner": "user",
            "recommended_next_step": "answer the blocking question",
        },
        "invalidation": [],
    }



def valid_contract_11():
    document = valid_interim()
    document["contract_version"] = "1.1"
    document["phases"][2]["reason"] = "jfoundry use is undecided"
    document["phases"].append(
        {
            "phase": "vadmin-implementation-guidance",
            "applicability": "not-applicable",
            "status": "not-applicable",
            "result_ref": None,
            "affects": ["planning"],
            "reason": "project does not adopt VAdmin",
        }
    )
    return document


class ValidateHandoffTests(unittest.TestCase):
    def test_accepts_valid_interim_handoff(self):
        self.assertEqual(validate_document(valid_interim()), [])

    def test_rejects_ready_handoff_with_open_dependent_blocker(self):
        document = valid_interim()
        document["kind"] = "final"
        document["planning_readiness"]["status"] = "ready"
        errors = validate_document(document)
        self.assertTrue(any("dependent blocker" in error for error in errors))

    def test_rejects_broken_artifact_reference(self):
        document = valid_interim()
        document["phases"][0]["result_ref"] = "missing-result"
        errors = validate_document(document)
        self.assertTrue(any("result_ref" in error for error in errors))

    def test_rejects_unaccepted_assumption_in_confirmed_decisions(self):
        document = valid_interim()
        document["decisions"]["confirmed"].append(
            {
                "decision_ref": "domain-modeling:INV-002",
                "statement": "The inferred invariant is confirmed.",
                "original_status": "inferred",
                "evidence_refs": ["E-004"],
                "acceptance": {"status": "pending", "source_ref": None},
            }
        )
        errors = validate_document(document)
        self.assertTrue(any("confirmed" in error for error in errors))

    def test_rejects_duplicate_phase_entries(self):
        document = valid_interim()
        document["phases"].append(copy.deepcopy(document["phases"][0]))
        errors = validate_document(document)
        self.assertTrue(any("duplicate phase" in error for error in errors))

    def test_requires_revision_parent_and_new_revision_id(self):
        document = valid_interim()
        document["kind"] = "revision"
        errors = validate_document(document)
        self.assertTrue(any("parent_handoff_id" in error for error in errors))

    def test_accepts_contract_11_with_explicit_optional_landings(self):
        self.assertEqual(validate_document(valid_contract_11()), [])

    def test_contract_11_requires_both_optional_landings(self):
        document = valid_contract_11()
        document["phases"] = [
            phase for phase in document["phases"] if phase["phase"] != "vadmin-implementation-guidance"
        ]
        errors = validate_document(document)
        self.assertTrue(any("requires phase vadmin-implementation-guidance" in error for error in errors))

    def test_contract_11_requires_reason_for_unused_landing(self):
        document = valid_contract_11()
        document["phases"][3].pop("reason")
        errors = validate_document(document)
        self.assertTrue(any("requires reason" in error for error in errors))

    def test_contract_11_requires_evidence_refs(self):
        document = valid_contract_11()
        document["decisions"]["confirmed"].append(
            {
                "decision_ref": "architecture:STYLE-001",
                "statement": "Use hexagonal boundaries for the order context.",
                "original_status": "confirmed",
                "evidence_refs": [],
                "acceptance": {"status": "not-required", "source_ref": None},
            }
        )
        errors = validate_document(document)
        self.assertTrue(any("requires evidence_refs" in error for error in errors))

    def test_contract_11_rejects_pinned_framework_release(self):
        document = valid_contract_11()
        document["decisions"]["confirmed"].append(
            {
                "decision_ref": "jfoundry:VERSION-001",
                "statement": "Use jfoundry 1.7.0 for this service.",
                "original_status": "confirmed",
                "evidence_refs": ["E-010"],
                "acceptance": {"status": "not-required", "source_ref": None},
            }
        )
        errors = validate_document(document)
        self.assertTrue(any("framework release version" in error for error in errors))

    def test_contract_11_allows_version_source_without_a_pinned_release(self):
        document = valid_contract_11()
        document["decisions"]["confirmed"].append(
            {
                "decision_ref": "jfoundry:VERSION-SOURCE",
                "statement": "Resolve the current jfoundry release from the project build.",
                "original_status": "confirmed",
                "evidence_refs": ["E-011"],
                "acceptance": {"status": "not-required", "source_ref": None},
            }
        )
        self.assertEqual(validate_document(document), [])

    def test_contract_10_does_not_apply_new_evidence_or_version_rules(self):
        document = valid_interim()
        document["decisions"]["confirmed"].append(
            {
                "decision_ref": "jfoundry:VERSION-001",
                "statement": "Use jfoundry 1.7.0 for this service.",
                "original_status": "confirmed",
                "evidence_refs": [],
                "acceptance": {"status": "not-required", "source_ref": None},
            }
        )
        self.assertEqual(validate_document(document), [])


if __name__ == "__main__":
    unittest.main()
