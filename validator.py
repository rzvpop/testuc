def validate(alarm):
    errors = ""

    if alarm["desc"] == "":
        errors += "Invalid description!\n"
    if alarm["time"][0] < 0 or alarm["time"][0] >= 24:
        errors += "Invalid hour!\n"
    if alarm["time"][1] < 0 or alarm["time"][1] >= 60:
        errors += "Invalid minute!\n"
    if alarm["time"][2] < 0 or alarm["time"][2] >= 60:
        errors += "Invalid second!\n"

    if len(errors) != 0:
        raise ValueError(errors)