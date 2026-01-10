import pytest as pyt
from java_repos import ReposJava
import sla

r = ReposJava()
s = sla



# def test_status_code(): 
#         assert r.api() == 200

def test_respose():
        r.api()
        assert r.response_dict['total_count'] > 200