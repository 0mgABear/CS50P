from numb3rs import validate


def test_valid_ip_addresses():
  valid_ips = [
      "192.168.0.1",
      "10.0.0.1",
      "255.255.255.255",
      "127.0.0.1",
  ]
  for ip in valid_ips:
    assert validate(ip) == True, f"Expected {ip} to be valid"


def test_invalid_ip_addresses():
  invalid_ips = [
      "275.3.6.28",  # Example from the prompt (out of range)
      "192.168.0.256",  
      "10.0.0.", 
      "invalid_address", 
      "123.456.789.0",  
      "0.0.0.0.0", 
  ]
  for ip in invalid_ips:
    assert validate(ip) == False, f"Expected {ip} to be invalid"


if __name__ == "__main__":
  test_valid_ip_addresses()
  test_invalid_ip_addresses()
  print("All tests passed!")
