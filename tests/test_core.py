"""Tests for Exoscore."""
from src.core import Exoscore
def test_init(): assert Exoscore().get_stats()["ops"] == 0
def test_op(): c = Exoscore(); c.process(x=1); assert c.get_stats()["ops"] == 1
def test_multi(): c = Exoscore(); [c.process() for _ in range(5)]; assert c.get_stats()["ops"] == 5
def test_reset(): c = Exoscore(); c.process(); c.reset(); assert c.get_stats()["ops"] == 0
def test_service_name(): c = Exoscore(); r = c.process(); assert r["service"] == "exoscore"
