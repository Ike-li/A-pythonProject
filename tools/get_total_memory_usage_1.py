from extensions.redis_cluster import redis_client


def get_redis_db_all_data(pattern):
    data = []
    for _key in redis_client.scan_iter(pattern):
        data.append(_key.decode("utf-8"))
    return data


def _get_memory_usage(key):
    return redis_client.memory_usage(key)


def get_total_memory_usage(keys):
    total_memory = 0
    for key in keys:
        total_memory += _get_memory_usage(key)
    return total_memory


if __name__ == "__main__":
    keys = get_redis_db_all_data("game_boosting_product:*")
    total_memory_usage = get_total_memory_usage(keys)
    print("Total memory usage for all keys: {} bytes".format(total_memory_usage))
