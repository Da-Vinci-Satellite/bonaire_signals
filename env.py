# Read requirements.txt
with open("requirements.txt", "r") as f:
    packages = f.readlines()

# Start building environment.yml content
env_content = """name: my_env
channels:
  - conda-forge
  - defaults
dependencies:
  - python=3.10
  - pip
  - pip:
"""

# Add packages from requirements.txt
for package in packages:
    package = package.strip()
    if package:
        env_content += f"      - {package}\n"

# Write to environment.yml
with open("environment.yml", "w") as f:
    f.write(env_content)

print("environment.yml created successfully.")