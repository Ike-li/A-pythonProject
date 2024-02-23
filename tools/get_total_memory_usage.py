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
    keys_without_ttl_pattern = {
        b"game_boosting_product:store",
        b"game_boosting_product:user",
        b"game_boosting_product:orders",

        # b"game_boosting_product:V0.9:store",
        # b"game_boosting_product:V0.8:store",
        # b"game_boosting_product:V0.7:store",
        # b"game_boosting_product:V0.6:store",
        # b"game_boosting_product:V0.5:store",
        # b"game_boosting_product:V0.4:store",
        # b"game_boosting_product:V0.3:store",
        # b"game_boosting_product:V0.2:store",
        # b"game_boosting_product:V0.1:store",
        #
        # b"game_boosting_product:V0.9:order",
        # b"game_boosting_product:V0.8:order",
        # b"game_boosting_product:V0.7:order",
        # b"game_boosting_product:V0.6:order",
        # b"game_boosting_product:V0.5:order",
        # b"game_boosting_product:V0.4:order",
        # b"game_boosting_product:V0.3:order",
        # b"game_boosting_product:V0.2:order",
        # b"game_boosting_product:V0.1:order",
        #
        # b"game_boosting_product:v0:user",
        # b"game_boosting_product:V0.1:user",
        # b"game_boosting_product:V0.2:user",
        # b"game_boosting_product:V0.3:user",
        # b"game_boosting_product:V0.4:user",
        # b"game_boosting_product:V0.5:user",
        # b"game_boosting_product:V0.6:user",
        # b"game_boosting_product:V0.7:user",
        # b"game_boosting_product:V0.8:user",
        # b"game_boosting_product:V0.9:user",
        #
        # b"game_boosting_product:v0.1:user",
        # b"game_boosting_product:v0.2:user",
        # b"game_boosting_product:v0.3:user",
        # b"game_boosting_product:v0.4:user",
        # b"game_boosting_product:v0.5:user",
        # b"game_boosting_product:v0.6:user",
        # b"game_boosting_product:v0.7:user",
        # b"game_boosting_product:v0.8:user",
        # b"game_boosting_product:v0.9:user",
        #
        # b"game_boosting_product:V0.6:orders",
        # b"game_boosting_product:V0.8:orders",
        #
        # b"enrollment_form:v1:form",
        # b"enrollment_form",
        # b"bonus_penalty_book",
        # b"room_message:V1.3:user_banned",
        # b"chat_room",
        # # b"memo:v1:group:6a97520a-21de-4ca7-adc9-f3cdce96c93e:notebook:enrollment_memo:admins"
        # b"memo:v1:group",
        # b"app:huo-guo-ying-xiong:weixin:open_id",
        # b"Record:round",
        # b"group_event:v4:event",
        # b"group_event:v4:event",
        # b"room_message:V1.3:ban",
        # b"Record:v1:round",
        # b"Record:v2:round",
        # # b"roomette:954d0f2c-9607-4b8f-9ad9-ac19f0e2ccd6:config"
        # b"roomette",
        # b"UserClubIndex",
        #
        # b"blackjack:roomette",
        # b"enrollment_form:v1:user",
        # b"user_voucher",
        # # b"Club:34be0486-eaf1-4ff4-a1ea-38249e506924"
        # b"Club",
        # # b"user:f40e69e2-040e-464f-b32d-4b62000e7da4:mmorpg:world_of_warcraft:role"
        # b"user",
        # b"texas_holdem:current_player",
        # b"wallet:statement:user",
        # b"group_event:v4:user",
        # b"app:game_master:weixin:open_id",
        # # b"game_role:user:030ebea2-2992-4e15-8dee-623cc147520b:mmorpg:world_of_warcraft:role"
        # b"game_role:user",
        # b"Record:v1:user",
        # b"Record:v2:user",
        # b"gift_card:user",
        # # b"hall_matching:V0.33cebe8fc-5f88-422a-bf00-02d2c1227e55:join_history"
        # b"hall_matching:V0",
        #
        # b"Record:user",
        #
        # b"zhajinhua:current_player",
        # b"voucher:task",
        # b"voucher:user",
        #
        # b"game_boosting_order:V0.1:order",
        # b"game_boosting_order:V0.2:order",
        # b"game_boosting_order:V0.3:order",
        # b"game_boosting_order:V0.4:order",
        # b"game_boosting_order:V0.5:order",
        # b"game_boosting_order:V0.6:order",
        # b"game_boosting_order:V0.7:order",
        # b"game_boosting_order:V0.8:order",
        # b"game_boosting_order:V0.9:order",
        # b"game_boosting_order:V1.0:order",
        # b"game_boosting_order:V1.1:order",
        # b"game_boosting_order:V1.2:order",
        # b"game_boosting_order:V1.3:order",
        # b"game_boosting_order:V1.4:order",
        # b"game_boosting_order:V1.5:order",
        # b"game_boosting_order:V1.6:order",
        # b"game_boosting_order:V1.7:order",
        # b"game_boosting_order:V1.8:order",
        # b"game_boosting_order:V1.9:order",
        # b"game_boosting_order:V2.0:order",
        # b"game_boosting_order:V2.1:order",
        # b"game_boosting_order:V2.2:order",
        # b"game_boosting_order:V2.3:order",
        # b"game_boosting_order:V2.4:order",
        # b"game_boosting_order:V2.5:order",
        # b"game_boosting_order:V2.6:order",
        # b"game_boosting_order:V2.7:order",
        # b"game_boosting_order:V2.8:order",
        #
        # b"game_boosting_order:V0.1:store",
        # b"game_boosting_order:V0.2:store",
        # b"game_boosting_order:V0.3:store",
        # b"game_boosting_order:V0.4:store",
        # b"game_boosting_order:V0.5:store",
        # b"game_boosting_order:V0.6:store",
        # b"game_boosting_order:V0.7:store",
        # b"game_boosting_order:V0.8:store",
        # b"game_boosting_order:V0.9:store",
        # b"game_boosting_order:V1.0:store",
        # b"game_boosting_order:V1.1:store",
        # b"game_boosting_order:V1.2:store",
        # b"game_boosting_order:V1.3:store",
        # b"game_boosting_order:V1.4:store",
        # b"game_boosting_order:V1.5:store",
        # b"game_boosting_order:V1.6:store",
        # b"game_boosting_order:V1.7:store",
        # b"game_boosting_order:V1.8:store",
        # b"game_boosting_order:V1.9:store",
        # b"game_boosting_order:V2.0:store",
        # b"game_boosting_order:V2.1:store",
        # b"game_boosting_order:V2.2:store",
        # b"game_boosting_order:V2.3:store",
        # b"game_boosting_order:V2.4:store",
        # b"game_boosting_order:V2.5:store",
        # b"game_boosting_order:V2.6:store",
        # b"game_boosting_order:V2.7:store",
        # b"game_boosting_order:V2.8:store",
        #
        # b"game_boosting_order:V0.1:user",
        # b"game_boosting_order:V0.2:user",
        # b"game_boosting_order:V0.3:user",
        # b"game_boosting_order:V0.4:user",
        # b"game_boosting_order:V0.5:user",
        # b"game_boosting_order:V0.6:user",
        # b"game_boosting_order:V0.7:user",
        # b"game_boosting_order:V0.8:user",
        # b"game_boosting_order:V0.9:user",
        # b"game_boosting_order:V1.0:user",
        # b"game_boosting_order:V1.1:user",
        # b"game_boosting_order:V1.2:user",
        # b"game_boosting_order:V1.3:user",
        # b"game_boosting_order:V1.4:user",
        # b"game_boosting_order:V1.5:user",
        # b"game_boosting_order:V1.6:user",
        # b"game_boosting_order:V1.7:user",
        # b"game_boosting_order:V1.8:user",
        # b"game_boosting_order:V1.9:user",
        # b"game_boosting_order:V2.0:user",
        # b"game_boosting_order:V2.1:user",
        # b"game_boosting_order:V2.2:user",
        # b"game_boosting_order:V2.3:user",
        # b"game_boosting_order:V2.4:user",
        # b"game_boosting_order:V2.5:user",
        # b"game_boosting_order:V2.6:user",
        # b"game_boosting_order:V2.7:user",
        # b"game_boosting_order:V2.8:user",
        #
        # b"app_user:v1:user:device",
        # b"active_sessions",
        # b"room_message:migrated_record:config",
        #
        # b"voucher:v0.5:user",
        # b"voucher:v0.4:user",
        # b"voucher:v0.3:user",
        # b"voucher:v0.2:user",
        # b"voucher:v0.1:user",
        #
        # b"game_event",
        # b"bonus_penalty_book",
        # b"create_room:permission",
        # b"texas_holdem_classic_skilled",
        # b"gift_card:gift_cards",
        # b"group_event:v3",
        # b"zhajinhua_skilled",
        # b"zhajinhua_beginner",
        # b"texas_holdem_classic_beginner",
        # b"zhajinhua_master",
        # b"zhajinhua:opening_roomette_redis:v4:room_ids",
        # b"zhajinhua:opening_roomette_redis:v3:room_ids",
        # b"zhajinhua:opening_roomette_redis:v2:room_ids",
        # b"zhajinhua:opening_roomette_redis:v1:room_ids",
        # b"User:reset_password:email",
        # b"centrifugo.seq.meta.{$chat:index}",
        # b"slots:user",
        # b"texas_holdem:opening_roomette_redis:v4:room_ids",
        # b"texas_holdem:opening_roomette_redis:v3:room_ids",
        # b"texas_holdem:opening_roomette_redis:v2:room_ids",
        # b"texas_holdem:opening_roomette_redis:v1:room_ids",
        # b"DelayTask:TexasHoldem:RoomCheckLater",
        #
        # # b"tag:v1:group:63f7e17a-2519-4b87-9ca4-5ee47c8ea1a4:item"
        # b"tag:v1:group",
        # b"blackjack:opening_roomette",
        # b"game_hall:hall_manager",
        # b"hall_matching:floor",
        # b"flask_template:migrated_record:config",
        # b"texas_holdem_classic_master",
        # b"example",
        # b"clubs",
        # b"huawei_iap:access_token",
    }
    keys = []
    for pattern in keys_without_ttl_pattern:
        keys.extend(get_redis_db_all_data(pattern))

    print(keys)
    # 调用函数获取总内存占用情况
    total_memory_usage = get_total_memory_usage(keys)
    print("Total memory usage for all keys: {} bytes".format(total_memory_usage))
