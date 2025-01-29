from configparser import ConfigParser


def load_config(filename: str = 'database.ini', section: str = 'postgresql') -> dict:
    """Load configuration data."""
    parser = ConfigParser()
    parser.read(filename)
    config = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            config[param[0]] = param[1]
    else:
        msg = f'Section {section} not found in the {filename} file'
        raise ValueError(msg)
    return config
