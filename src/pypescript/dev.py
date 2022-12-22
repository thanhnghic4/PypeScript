import yaml

with open("example.yaml", "r") as stream:
    try:
        a = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)

for k in a:
    print(k)


for k in a['definitions']:
    print(k)