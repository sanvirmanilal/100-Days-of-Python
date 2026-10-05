"""Worked learning example for day 064; independent of the exercises."""

def main():
    from unittest.mock import Mock
    service = Mock(return_value="ok")
    print(service("request"))
    service.assert_called_once_with("request")


if __name__ == "__main__":
    main()
