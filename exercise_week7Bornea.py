"""
Week 7 : Data Serialization - Convert Network Configs
=======================================================

Your task: Convert a network device config between JSON and YAML.

FILL IN THE BLANKS marked with ______
Run this script when done: python3 exercise_week7.py
"""
import json
import yaml

#===========================================================================
# This is a network device configuration in Python (dictionary)
#===========================================================================

router_config = {
    "hostname": "Router-1",
    "vendor": "Cisco",
    "interfaces": [
        {"name": "GigabitEthernet01", "ip": "192.168.1.1", "status": "up"},
        {"name": "GigabitEthernet02", "ip": "10.0.0.1", "status": "up"},
        {"name": "GigabitEthernet03", "ip": "172.16.0.1", "status": "down"}
    ]
}

#===========================================================================
# EXERCISE 1: Convert Python dict -> JSON
#===========================================================================
#Hint: Convert a python dict to a JSON String

print("=== EXERCISE 1: Convert to JSON ===")
#json_output = json._____(router_config, indent=2)
json_output = json.dumps(router_config, indent=2)

print(json_output)
print()

#===========================================================================
# EXERCISE 2: Convert Python dict -> YAML
#===========================================================================
#Hint: Convert a python dict to a YAML String

print("=== EXERCISE 2: Convert to YAML ===")
# Fill in the BLANK: use to convert router_config to a YAML
#yaml_output = yaml.____(router_config, default_flow_style=False) 
yaml_output = yaml.dump(router_config, default_flow_style=False)

print(yaml_output)
print()

#===========================================================================
# EXERCISE 3: Read JSON from a file
#===========================================================================

print("=== EXERCISE 3: Read JSON from a file ===")
#First, let's save our config as a JSON file
with open("router_config.json", "w") as f:
    json.dump(router_config, f, indent=2)

#Now read it back
#FILL IN THE BLANK: use to read from the file
with open("router_config.json", "r") as f:
    #loaded_config = json.____(f)
    loaded_config = json.load(f)

print(f"Loaded hostname: {loaded_config['hostname']}")
print(f"Number of interfaces: {len(loaded_config['interfaces'])}")
print()

#===========================================================================
# EXERCISE 4: Save YAML to a file
#===========================================================================
print("=== EXERCISE 4: Save YAML to a file ===")

#FILL IN THE BLANK: open "router_config" for writing
#with open("router_config._____", "___") as f:
with open("router_config.yaml", "w") as f:
    yaml.dump(router_config, f, default_flow_style=False)

print("Saved to router_config.yaml!")
print()

#===========================================================================
# EXERCISE 5: CHALLENGE - Modify and save
#===========================================================================

print("=== EXERCISE 5: CHALLENGE - Modify and save ===")

#Add a new interface (LoopBack0)
new_interface = {"name": "LoopBack0", "ip": "1.1.1.1", "status": "up"}

#FILL IN THE BLANK: append the new interface to the list
#router_config["__________"].______(new_interface) 
router_config["interfaces"].append(new_interface)

#Save updated config
with open("router_config_updated.json", "w") as f:
    json.dump(router_config, f, indent=2)

print(f"Added new interface: {new_interface['name']}")
print(f"Total interfaces now: {len(router_config['interfaces'])}")
print()
