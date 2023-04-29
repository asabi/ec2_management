import sys
import boto3


def list_instances(region):
    ec2 = boto3.resource("ec2", region_name=region)
    instances = ec2.instances.all()
    return list(instances)


def start_instance(instance_id, region):
    ec2 = boto3.client("ec2", region_name=region)
    response = ec2.start_instances(InstanceIds=[instance_id])
    state = response["StartingInstances"][0]["CurrentState"]["Name"]
    print(f"Instance {instance_id} is {state}")


def stop_instance(instance_id, region):
    ec2 = boto3.client("ec2", region_name=region)
    response = ec2.stop_instances(InstanceIds=[instance_id])
    state = response["StoppingInstances"][0]["CurrentState"]["Name"]
    print(f"Instance {instance_id} is {state}")


def display_instances(instances):
    for idx, instance in enumerate(instances, start=1):
        print(f"Index: {idx}, ID: {instance.id}, State: {instance.state['Name']}")


def main():
    if len(sys.argv) < 2:
        print("Usage: ec2.py <region> (default: ca-central-1)")

    region = sys.argv[1] if len(sys.argv) >= 2 else "ca-central-1"

    instances = list_instances(region)
    print(f"Listing instances in region {region}:")
    display_instances(instances)

    action = input("Enter 'start', 'stop', or 'refresh' followed by the instance index (e.g. start 1), or 'exit' to quit: ")
    while action.lower() != "exit":
        action_parts = action.split()

        if len(action_parts) >= 1:
            action = action_parts[0]

            if action.lower() == "refresh":
                instances = list_instances(region)
                print("Refreshed instance list:")
                display_instances(instances)
            elif len(action_parts) == 2:
                index_str = action_parts[1]

                if index_str.isdigit():
                    index = int(index_str) - 1

                    if 0 <= index < len(instances):
                        instance_id = instances[index].id

                        if action.lower() == "start":
                            start_instance(instance_id, region)
                        elif action.lower() == "stop":
                            stop_instance(instance_id, region)
                        else:
                            print("Invalid action. Please enter 'start', 'stop', 'refresh', or 'exit'.")
                    else:
                        print("Invalid index. Please enter a valid instance index.")
                else:
                    print("Invalid index. Please enter a valid instance index.")
            else:
                print("Invalid input. Please enter 'start', 'stop', 'refresh', or 'exit'.")
        else:
            print("Invalid input. Please enter 'start', 'stop', 'refresh', or 'exit'.")

        action = input("Enter 'start', 'stop', or 'refresh' followed by the instance index (e.g. start 1), or 'exit' to quit: ")


if __name__ == "__main__":
    main()
