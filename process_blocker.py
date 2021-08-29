import os, signal
import psutil

#open config
user_name = os.path.expanduser("~")
config_path = f"{user_name}/.config/processblockerrc"
if not os.path.isfile(config_path):
    tmp_file = open(config_path, "w")
    tmp_file.close()
config_file = open(config_path, "r")
file_lines = config_file.readlines()
config_file.close()

#filter and parse lines
file_lines = [line.strip() for line in file_lines]
filtered_file_lines = []
for line in file_lines:
    if line != "":
        filtered_file_lines.append(line)

#main loop
while True:
    for running_proc in psutil.process_iter():
        if running_proc.name() in filtered_file_lines:
            os.kill(running_proc.pid, signal.SIGINT)
