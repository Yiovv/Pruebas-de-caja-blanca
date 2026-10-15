import pytest
from process import process

# 1. Statement Coverage
@pytest.mark.statement
@pytest.mark.parametrize("values, expected", [
    ([2], ["positivo", "par"])
])
def test_statement_coverage(values, expected):
    assert process(values) == expected

    # 2. Branch Coverage
@pytest.mark.branch
@pytest.mark.parametrize("values, expected", [
    ([2], ["positivo", "par"]),  
    ([-1], [])                   
])
def test_branch_coverage(values, expected):
    assert process(values) == expected

    # 3. Path Coverage
@pytest.mark.path
@pytest.mark.parametrize("values, expected", [
    ([2, 2], ["positivo", "par", "positivo", "par"]),
    ([2, 3], ["positivo", "par", "positivo"]),        
    ([2, -2], ["positivo", "par", "par"]),            
    ([2, -1], ["positivo", "par"]),                   
    ([3, 2], ["positivo", "positivo", "par"]),        
    ([3, 3], ["positivo", "positivo"]),               
    ([3, -2], ["positivo", "par"]),                   
    ([3, -1], ["positivo"]),                          
    ([-2, 2], ["par", "positivo", "par"]),            
    ([-2, 3], ["par", "positivo"]),                   
    ([-2, -2], ["par", "par"]),                       
    ([-2, -1], ["par"]),                              
    ([-1, 2], ["positivo", "par"]),                   
    ([-1, 3], ["positivo"]),                          
    ([-1, -2], ["par"]),                              
    ([-1, -1], []),                                   
])
def test_path_coverage(values, expected):
    assert process(values) == expected