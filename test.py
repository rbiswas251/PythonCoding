import unittest
from main import is_alive, is_dead, ConwayGame


class TestConwayGame(unittest.TestCase):

    def test_rules_less_than2_alive(self):
        input_state = (is_alive, 1)
        output_state = ConwayGame().get_state(input_state)
        assert output_state == is_dead

    def test_rules_2_or_3_alive(self):
        input_state = (is_alive, 3)
        output_state = ConwayGame().get_state(input_state)
        assert output_state == is_alive

    def test_rules_gt_3_alive(self):
        input_state = (is_alive, 5)
        output_state = ConwayGame().get_state(input_state)
        assert output_state == is_dead

    def test_rules_less_than2_dead(self):
        input_state = (is_dead, 1)
        output_state = ConwayGame().get_state(input_state)
        assert output_state == is_dead

    def test_rules_3_dead(self):
        input_state = (is_dead, 3)
        output_state = ConwayGame().get_state(input_state)
        assert output_state == is_alive

    def test_rules_gt_3_dead(self):
        input_state = (is_dead, 5)
        output_state = ConwayGame().get_state(input_state)
        assert output_state == is_dead