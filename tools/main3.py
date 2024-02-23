import logging


def format_log_message(
        app_id, register_type, client_ip, app_version, device_id, user_id, **kwargs
):
    app_id = app_id.ljust(10)[:10]
    register_type = register_type.ljust(18)[:18]
    client_ip = str(client_ip).ljust(15)[:15]
    device_id = str(device_id).ljust(30)[:30]
    app_version = str(app_version).ljust(60)[:60]

    if "email_password" in register_type:
        email = kwargs["email"]
        return (
            f"app_id:{app_id} register_type:{register_type} ip_address:{client_ip} app_version:{app_version} device_id:{device_id}"
            f" user_id:{user_id}  email:{email}"
        )

    if "username_password" in register_type:
        username = kwargs["username"]
        return (
            f"app_id:{app_id} register_type:{register_type} ip_address:{client_ip} app_version:{app_version} device_id:{device_id}"
            f" user_id:{user_id}  username:{username}"
        )

    if "phone_sms_code" in register_type:
        phone = kwargs["phone"]
        phone = str(phone).ljust(30)[:30]
        return (
            f"app_id:{app_id} register_type:{register_type} ip_address:{client_ip} app_version:{app_version} device_id:{device_id}"
            f" user_id:{user_id} phone:{phone}"
        )

    return (
        f"app_id:{app_id} register_type:{register_type} ip_address:{client_ip} app_version:{app_version} device_id:{device_id}"
        f" user_id:{user_id}"
    )


logger = logging.getLogger("User Sign-Up")
logger.setLevel(logging.INFO)
logger.info(
    format_log_message(
        "laiwan",
        "phone_sms_code",
        "183.128.112.165",
        "laiwan_react_native|production|app-store|ios|2401291121",
        "1174CA74-1148-4ACF-8522-A91F61",
        "33fd7825-a8ed-4390-b4c6-a99cfc140dba",
        phone="86-13518518602"
    )
)
print(format_log_message(
        "laiwan",
        "phone_sms_code",
        "183.128.112.165",
        "laiwan_react_native|production|app-store|ios|2401291121",
        "1174CA74-1148-4ACF-8522-A91F61",
        "33fd7825-a8ed-4390-b4c6-a99cfc140dba",
        phone="86-13518518602"
    ))
