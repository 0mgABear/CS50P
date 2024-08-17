# test_postal_functions.py
import pytest
import sys
import unittest  # You can remove this import if you're not using unittest anymore
from project import get_onemap_data, postal_check, multi

def test_get_onemap_data_single_building():
    result = get_onemap_data('100074')
    assert result == 'NIL'

def test_get_onemap_data_multiple_buildings():
    result = get_onemap_data('018956')
    assert result == ['MAYBANK OFFSITE@MARINABAYSANDS', 'SANDS EXPO AND CONVENTION CENTRE', 'UOB MARINA BAY SANDS LOCATION A', 'UOB MARINA BAY SANDS LOCATION D', 'UOB MARINA BAY SANDS LOCATION E', 'UOB MARINA BAY SANDS LOCATION K', 'UOB MARINA BAY SANDS LOCATION P']
    

def test_get_onemap_data_no_building():
    result = get_onemap_data('123456')
    assert result == []

def test_postal_check_valid_postal():
    assert postal_check('123456') is True

def test_postal_check_invalid_postal_length():
    with pytest.raises(ValueError):
        postal_check('12345')

def test_postal_check_invalid_postal_non_digit():
    with pytest.raises(ValueError):
        postal_check('12A456')

def test_multi_unique_buildings():
    data = {
        'results': [{'BUILDING': 'Condo A'}, {'BUILDING': 'Condo B'}]
    }
    result = multi(data)
    assert result == ['Condo A', 'Condo B']

def test_multi_duplicate_buildings():
    data = {
        'results': [{'BUILDING': 'Condo A'}, {'BUILDING': 'Condo A'}, {'BUILDING': 'Condo B'}]
    }
    result = multi(data)
    assert result == ['Condo A', 'Condo B']
