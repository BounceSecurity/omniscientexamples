import subprocess

def sanitize_it(user_input):
    #Sanitize the input to avoid code execution
    return user_input

def get_input():
    #some actions before getting an input
    return input("please enter address")

def run_ping(address):
    cmd = "ping -c 1 {0}".format(address)
    subprocess.Popen(cmd, shell=True)

new_address = get_input()

#ruleid: unsanitized_input
run_ping(new_address)

new_address = sanitize_it(new_address)

#ok: unsanitized_input
run_ping(new_address)
