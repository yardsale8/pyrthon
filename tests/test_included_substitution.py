from pyrsistent import v

def test_substitution_when_module_registered_via_wild_card_match():
    x = []
    assert type(x) is type(v())