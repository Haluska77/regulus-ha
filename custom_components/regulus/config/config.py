from typing import Dict

def get_config(entry) -> Dict[str, str]:
    return {
        "host": entry.data["ip_address"],
        "user": entry.data["username"],
        "password": entry.data["password"],
        "ir_version": entry.data["ir_version"],
    }
