from pathlib import Path

import tomli

if __name__=='__main__': 
    pyproject = tomli.loads(Path(Path(__file__).parent.parent, 'pyproject.toml').read_text(encoding='utf-8'))
    package_dependencies = pyproject['project']['optional-dependencies']

    all_packages = package_dependencies.values()
    all_packages = [packages for inner_list in all_packages for packages in inner_list]
    print(all_packages)