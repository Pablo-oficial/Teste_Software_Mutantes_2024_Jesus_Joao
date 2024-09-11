from src.ip_checker import ip_check
import pytest

# Function to initialize setup
@pytest.fixture
def ip_test_config(request) -> tuple:
    print("Running setup method...")
    ip = ip_check("257.120.223.13")
    ip1 = ip_check("127.0.0.0")
    
    yield ip, ip1

    # Teardown code
    ip.delete_objects()
    ip1.delete_objects()

@pytest.fixture
def ip_test_config_using_addfinalizer(request) -> tuple:
    print("Running setup method...")
    ip = ip_check("257.120.223.13")
    ip1 = ip_check("127.0.0.0")

    # Function to clear the resources
    def clear_resource():
        print("Running the teardown code")
        ip.delete_objects()
        ip1.delete_objects()
    
    request.addfinalizer(clear_resource)

    return ip, ip1

# Function to test the validate_it function
def test_validity(ip_test_config) -> None:
    ip, ip1 = ip_test_config
    print("Running test_validity...")
    assert ip.validate_it() == "Invalid IP"
    assert ip1.validate_it() == "Valid IPv4"

# Function to test the find_class function
def test_find_class(ip_test_config) -> None:
    ip, ip1 = ip_test_config
    print("Running test_find_class...")
    assert ip.find_class() == "N/A"  # Adjusted to "N/A" for invalid IP
    assert ip1.find_class() == "A"

# Function to run test with setup and teardown using addfinalizer
def test_ip_with_addfinalizer(ip_test_config_using_addfinalizer) -> None:
    ip, ip1 = ip_test_config_using_addfinalizer
    print("Testing the validity...")
    assert ip.validate_it() == "Invalid IP"
    assert ip1.validate_it() == "Valid IPv4"

    print("Testing the class...")
    assert ip.find_class() == "N/A"  # Adjusted to "N/A" for invalid IP
    assert ip1.find_class() == "A"

# Test for format_ip
def test_format_ip():
    ip1 = ip_check("257.120.223.013")
    ip2 = ip_check("192.168.1.001")
    ip3 = ip_check("10.0.0.1")
    
    assert ip1.format_ip() == "257.120.223.13"
    assert ip2.format_ip() == "192.168.1.1"
    assert ip3.format_ip() == "10.0.0.1"

# Test for ip_to_int
def test_ip_to_int():
    ip1 = ip_check("192.168.1.1")
    ip2 = ip_check("10.0.0.1")
    ip3 = ip_check("0.0.0.0")
    
    assert ip1.ip_to_int() == 3232235777
    assert ip2.ip_to_int() == 167772161
    assert ip3.ip_to_int() == 0

# Test for is_reserved_ip
def test_is_reserved_ip():
    ip1 = ip_check("10.0.0.1")      # Private network
    ip2 = ip_check("192.168.1.1")   # Private network
    ip3 = ip_check("172.16.0.1")    # Private network
    ip4 = ip_check("8.8.8.8")       # Public network
    
    assert ip1.is_reserved_ip() == True
    assert ip2.is_reserved_ip() == True
    assert ip3.is_reserved_ip() == True
    assert ip4.is_reserved_ip() == False
