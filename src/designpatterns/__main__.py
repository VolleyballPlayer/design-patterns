
from designpatterns.utils.package_resources import PackageResources

def builder():
    """
    Run builder example.

    This function calls builder module to run an example of creational design pattern called builder.
    """
    print("This is builder pattern")

def singleton():
    """
    Run singleton example.

    This function calls singleton module to run an example of creational design pattern called singleton.
    """
    print("This is singleton pattern")

def main():
    print(f"Using design pattern package version {PackageResources.get_package_version()}")
    builder()
    singleton()

if __name__ == "__main__":
    main()