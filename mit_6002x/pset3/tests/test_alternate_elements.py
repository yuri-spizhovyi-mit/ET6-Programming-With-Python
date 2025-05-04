import unittest
import random
from ..ps3b import SimpleVirus, Patient, NoChildException


class TestSimpleVirusAndPatient(unittest.TestCase):
    def setUp(self):
        random.seed(42)  # for consistent test results

    def test_simplevirus_init(self):
        virus = SimpleVirus(0.9, 0.1)
        self.assertEqual(virus.getMaxBirthProb(), 0.9)
        self.assertEqual(virus.getClearProb(), 0.1)

    def test_does_clear_false(self):
        virus = SimpleVirus(0.9, 0.0)  # never clears
        self.assertFalse(virus.doesClear())

    def test_does_clear_true(self):
        virus = SimpleVirus(0.9, 1.0)  # always clears
        self.assertTrue(virus.doesClear())

    def test_reproduce_success(self):
        virus = SimpleVirus(1.0, 0.0)
        offspring = virus.reproduce(0.0)
        self.assertIsInstance(offspring, SimpleVirus)

    def test_reproduce_failure(self):
        virus = SimpleVirus(0.0, 0.0)
        with self.assertRaises(NoChildException):
            virus.reproduce(0.0)

    def test_patient_population_growth(self):
        viruses = [
            SimpleVirus(1.0, 0.0) for _ in range(3)
        ]  # never cleared, always reproduce
        patient = Patient(viruses, maxPop=100)
        pop_before = patient.getTotalPop()
        pop_after = patient.update()
        self.assertGreater(pop_after, pop_before)

    def test_patient_clearance(self):
        viruses = [SimpleVirus(1.0, 1.0) for _ in range(5)]  # always cleared
        patient = Patient(viruses, maxPop=10)
        pop_after = patient.update()
        self.assertEqual(pop_after, 0)


if __name__ == "__main__":
    unittest.main()
