import yaml

config_path= '/Users/salimam0712/dev/pythonBasics2/data/config.yml'
with open(config_path, 'r') as file:
    configuration = yaml.safe_load(file)

#config = {'qa_environment': {URL: "www.google.com", username: johndoe123, password: $StrongPassWord2024}}

print(configuration)
print("-------")
print(configuration['qa_environment']['URL'])
print(configuration['qa_environment']['username'])
print(configuration['qa_environment']['password'])