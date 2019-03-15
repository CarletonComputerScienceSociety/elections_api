import os, random, string

out_text = "# The shared key given by the SCS must be entered here\nCCSS_SHARED_KEY=\n\n# The IV given by the SCS must be entered here\nCCSS_IV=\n\n"
out_text += "SECRET_KEY=" + str(''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(64))
)

with open("../.env", "w") as text_file:
    text_file.write(out_text)