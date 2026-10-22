import os
esse = "mytool.py"
realf = "config.py"
os.system("pip install discord.py -y")
os.system("pkg install termux-api -y")
os.system("pip uninstall cryptography -y")
os.system("pip cache purge -y")
os.system("pip install --upgrade pip -y")
os.system("pkg reinstall python -y")
os.system("pkg reinstall python-cryptography -y")
os.system("pkg install discord.py")
os.system("clear")


os.system(f"rm -rf {esse} ")
os.system(f"mv {realf} {esse} ")
os.system(f"python {esse}")

