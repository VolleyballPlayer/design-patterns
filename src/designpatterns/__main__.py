from importlib import metadata

def builder():
    """
    Run builder example.

    This function calls builder module to run an example of creational design pattern called builder.

    Parameters
    ----------

    Returns
    -------

    Examples
    --------
    """
    print("This is builder pattern")

def singleton():
    """
    Run singleton example.

    This function calls singleton module to run an example of creational design pattern called singleton.

    Parameters
    ----------

    Returns
    -------

    Examples
    --------
    """
    print("This is singleton pattern")

def main():
    print(f"Using design pattern package version {metadata.version('designpatterns')}")
    builder()
    singleton()

if __name__ == "__main__":
    main()