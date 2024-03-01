def is_valid_email(email):
    try:
        part_1, part_2 = email.split("@")

        if "." not in part_2 or len(part_1) < 2:
            return False

        part_2 = part_2.split(".")
        before_dot, after_dot = part_2
        if len(after_dot) >= 2 and len(before_dot) > 1:
            return True
        else:
            return False
    except Exception as e:
        return False
