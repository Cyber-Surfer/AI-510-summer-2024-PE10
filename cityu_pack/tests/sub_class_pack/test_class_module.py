import pytest
from cityu_pack.sub_class_pack.class_module import ClassModule


@pytest.fixture
def class_module_obj_fixture():
    test_obj = ClassModule(global_init_param=1)
    return test_obj

def test_init(class_module_obj_fixture):
    assert class_module_obj_fixture.global_init_param == 1

def test_add(class_module_obj_fixture):
    assert class_module_obj_fixture.add(1,2) == 3

def test_multiply(class_module_obj_fixture):
    assert class_module_obj_fixture.multiply(2,3) == 6



    