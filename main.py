def hide_phone_number(phone):
    if phone:
        phone_number = phone.split("-")[1]

        # 用星号替换中间的部分
        hidden_number = phone_number[:3] + '******' + phone_number[-2:]
        print(hidden_number)
        return hidden_number


if __name__ == '__main__':
    hide_phone_number("86-12345678910")

    hide_phone_number("1-202-555-0199")
    hide_phone_number("44-7459-123456")

    hide_phone_number("61-41087654")
    hide_phone_number("61-410876543")
    hide_phone_number("1-4165550123")
    hide_phone_number("49-15123456789")
    hide_phone_number("63-9123456789")
    hide_phone_number("62-81234567890")
    hide_phone_number("66-812345678")
    hide_phone_number("84-912-345-678")
    hide_phone_number("84-0912-345-678")
