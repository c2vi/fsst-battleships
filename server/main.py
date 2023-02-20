import toml

with open ('config.toml', 'r') as f:
    toml_string = f.read()
    parsed_toml= toml.loads(toml_string)
