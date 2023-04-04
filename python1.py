# test_file = open('/root/python38/test.txt', "w")
# test_file.write("New things here")
# test_file.close()


# test_file = open('test.txt', "r")
# print(test_file.read())

# Append
# test_file = open("test.txt", "a")
# test_file.write("""\n############
# Some notes to look at
# 1.do the thing
# 2.Then the other thing
# 3.Finish
# fi
# """)
# test_file.close()
# test_file = open('test.txt', "r")  ##r = read w= write
# print(test_file.read())

# test_file = open("test.txt")
# file_data = test_file.read()
# updated_data = file_data.replace("the thing", "nothing")
# print(updated_data)

# updating = open("test.txt", "w")
# updating.write(updated_data)
# updating.close()

# # our list
# names = ['Abdul', 'Esen', 'Ahmad']

# ##opening file
# test_file = open('test.txt', "w")

# ## looping through list & write each
# for name in names:
#     test_file.write(f"*{name}\n")

# ##closing the file
# test_file.close

# with open("new.txt", "w") as test_file:
#     test_file.write("This is a new file\n")
#     for name in names:
#         test_file.write(f"* {name}\n")

config_file = open('/etc/selinux/config')
update = config_file.read()
updated = update.replace("SELINUX=disabled", "SELINUX=enforcing")

with open('/etc/selinux/config', 'w') as selinux_config:
    selinux_config.write(updated)

selinux_config.close()































