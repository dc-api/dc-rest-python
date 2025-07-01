# dc_rest.DefaultApi

All URIs are relative to *https://discord.com/api/v10*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_group_dm_user**](DefaultApi.md#add_group_dm_user) | **PUT** /channels/{channel_id}/recipients/{user_id} | 
[**add_guild_member**](DefaultApi.md#add_guild_member) | **PUT** /guilds/{guild_id}/members/{user_id} | 
[**add_guild_member_role**](DefaultApi.md#add_guild_member_role) | **PUT** /guilds/{guild_id}/members/{user_id}/roles/{role_id} | 
[**add_lobby_member**](DefaultApi.md#add_lobby_member) | **PUT** /lobbies/{lobby_id}/members/{user_id} | 
[**add_my_message_reaction**](DefaultApi.md#add_my_message_reaction) | **PUT** /channels/{channel_id}/messages/{message_id}/reactions/{emoji_name}/@me | 
[**add_thread_member**](DefaultApi.md#add_thread_member) | **PUT** /channels/{channel_id}/thread-members/{user_id} | 
[**applications_get_activity_instance**](DefaultApi.md#applications_get_activity_instance) | **GET** /applications/{application_id}/activity-instances/{instance_id} | 
[**ban_user_from_guild**](DefaultApi.md#ban_user_from_guild) | **PUT** /guilds/{guild_id}/bans/{user_id} | 
[**bulk_ban_users_from_guild**](DefaultApi.md#bulk_ban_users_from_guild) | **POST** /guilds/{guild_id}/bulk-ban | 
[**bulk_delete_messages**](DefaultApi.md#bulk_delete_messages) | **POST** /channels/{channel_id}/messages/bulk-delete | 
[**bulk_set_application_commands**](DefaultApi.md#bulk_set_application_commands) | **PUT** /applications/{application_id}/commands | 
[**bulk_set_guild_application_commands**](DefaultApi.md#bulk_set_guild_application_commands) | **PUT** /applications/{application_id}/guilds/{guild_id}/commands | 
[**bulk_update_guild_channels**](DefaultApi.md#bulk_update_guild_channels) | **PATCH** /guilds/{guild_id}/channels | 
[**bulk_update_guild_roles**](DefaultApi.md#bulk_update_guild_roles) | **PATCH** /guilds/{guild_id}/roles | 
[**bulk_update_lobby_members**](DefaultApi.md#bulk_update_lobby_members) | **POST** /lobbies/{lobby_id}/members/bulk | 
[**consume_entitlement**](DefaultApi.md#consume_entitlement) | **POST** /applications/{application_id}/entitlements/{entitlement_id}/consume | 
[**create_application_command**](DefaultApi.md#create_application_command) | **POST** /applications/{application_id}/commands | 
[**create_application_emoji**](DefaultApi.md#create_application_emoji) | **POST** /applications/{application_id}/emojis | 
[**create_auto_moderation_rule**](DefaultApi.md#create_auto_moderation_rule) | **POST** /guilds/{guild_id}/auto-moderation/rules | 
[**create_channel_invite**](DefaultApi.md#create_channel_invite) | **POST** /channels/{channel_id}/invites | 
[**create_dm**](DefaultApi.md#create_dm) | **POST** /users/@me/channels | 
[**create_entitlement**](DefaultApi.md#create_entitlement) | **POST** /applications/{application_id}/entitlements | 
[**create_guild**](DefaultApi.md#create_guild) | **POST** /guilds | 
[**create_guild_application_command**](DefaultApi.md#create_guild_application_command) | **POST** /applications/{application_id}/guilds/{guild_id}/commands | 
[**create_guild_channel**](DefaultApi.md#create_guild_channel) | **POST** /guilds/{guild_id}/channels | 
[**create_guild_emoji**](DefaultApi.md#create_guild_emoji) | **POST** /guilds/{guild_id}/emojis | 
[**create_guild_from_template**](DefaultApi.md#create_guild_from_template) | **POST** /guilds/templates/{code} | 
[**create_guild_role**](DefaultApi.md#create_guild_role) | **POST** /guilds/{guild_id}/roles | 
[**create_guild_scheduled_event**](DefaultApi.md#create_guild_scheduled_event) | **POST** /guilds/{guild_id}/scheduled-events | 
[**create_guild_soundboard_sound**](DefaultApi.md#create_guild_soundboard_sound) | **POST** /guilds/{guild_id}/soundboard-sounds | 
[**create_guild_sticker**](DefaultApi.md#create_guild_sticker) | **POST** /guilds/{guild_id}/stickers | 
[**create_guild_template**](DefaultApi.md#create_guild_template) | **POST** /guilds/{guild_id}/templates | 
[**create_interaction_response**](DefaultApi.md#create_interaction_response) | **POST** /interactions/{interaction_id}/{interaction_token}/callback | 
[**create_lobby**](DefaultApi.md#create_lobby) | **POST** /lobbies | 
[**create_lobby_message**](DefaultApi.md#create_lobby_message) | **POST** /lobbies/{lobby_id}/messages | 
[**create_message**](DefaultApi.md#create_message) | **POST** /channels/{channel_id}/messages | 
[**create_or_join_lobby**](DefaultApi.md#create_or_join_lobby) | **PUT** /lobbies | 
[**create_pin**](DefaultApi.md#create_pin) | **PUT** /channels/{channel_id}/messages/pins/{message_id} | 
[**create_stage_instance**](DefaultApi.md#create_stage_instance) | **POST** /stage-instances | 
[**create_thread**](DefaultApi.md#create_thread) | **POST** /channels/{channel_id}/threads | 
[**create_thread_from_message**](DefaultApi.md#create_thread_from_message) | **POST** /channels/{channel_id}/messages/{message_id}/threads | 
[**create_webhook**](DefaultApi.md#create_webhook) | **POST** /channels/{channel_id}/webhooks | 
[**crosspost_message**](DefaultApi.md#crosspost_message) | **POST** /channels/{channel_id}/messages/{message_id}/crosspost | 
[**delete_all_message_reactions**](DefaultApi.md#delete_all_message_reactions) | **DELETE** /channels/{channel_id}/messages/{message_id}/reactions | 
[**delete_all_message_reactions_by_emoji**](DefaultApi.md#delete_all_message_reactions_by_emoji) | **DELETE** /channels/{channel_id}/messages/{message_id}/reactions/{emoji_name} | 
[**delete_application_command**](DefaultApi.md#delete_application_command) | **DELETE** /applications/{application_id}/commands/{command_id} | 
[**delete_application_emoji**](DefaultApi.md#delete_application_emoji) | **DELETE** /applications/{application_id}/emojis/{emoji_id} | 
[**delete_application_user_role_connection**](DefaultApi.md#delete_application_user_role_connection) | **DELETE** /users/@me/applications/{application_id}/role-connection | 
[**delete_auto_moderation_rule**](DefaultApi.md#delete_auto_moderation_rule) | **DELETE** /guilds/{guild_id}/auto-moderation/rules/{rule_id} | 
[**delete_channel**](DefaultApi.md#delete_channel) | **DELETE** /channels/{channel_id} | 
[**delete_channel_permission_overwrite**](DefaultApi.md#delete_channel_permission_overwrite) | **DELETE** /channels/{channel_id}/permissions/{overwrite_id} | 
[**delete_entitlement**](DefaultApi.md#delete_entitlement) | **DELETE** /applications/{application_id}/entitlements/{entitlement_id} | 
[**delete_group_dm_user**](DefaultApi.md#delete_group_dm_user) | **DELETE** /channels/{channel_id}/recipients/{user_id} | 
[**delete_guild**](DefaultApi.md#delete_guild) | **DELETE** /guilds/{guild_id} | 
[**delete_guild_application_command**](DefaultApi.md#delete_guild_application_command) | **DELETE** /applications/{application_id}/guilds/{guild_id}/commands/{command_id} | 
[**delete_guild_emoji**](DefaultApi.md#delete_guild_emoji) | **DELETE** /guilds/{guild_id}/emojis/{emoji_id} | 
[**delete_guild_integration**](DefaultApi.md#delete_guild_integration) | **DELETE** /guilds/{guild_id}/integrations/{integration_id} | 
[**delete_guild_member**](DefaultApi.md#delete_guild_member) | **DELETE** /guilds/{guild_id}/members/{user_id} | 
[**delete_guild_member_role**](DefaultApi.md#delete_guild_member_role) | **DELETE** /guilds/{guild_id}/members/{user_id}/roles/{role_id} | 
[**delete_guild_role**](DefaultApi.md#delete_guild_role) | **DELETE** /guilds/{guild_id}/roles/{role_id} | 
[**delete_guild_scheduled_event**](DefaultApi.md#delete_guild_scheduled_event) | **DELETE** /guilds/{guild_id}/scheduled-events/{guild_scheduled_event_id} | 
[**delete_guild_soundboard_sound**](DefaultApi.md#delete_guild_soundboard_sound) | **DELETE** /guilds/{guild_id}/soundboard-sounds/{sound_id} | 
[**delete_guild_sticker**](DefaultApi.md#delete_guild_sticker) | **DELETE** /guilds/{guild_id}/stickers/{sticker_id} | 
[**delete_guild_template**](DefaultApi.md#delete_guild_template) | **DELETE** /guilds/{guild_id}/templates/{code} | 
[**delete_lobby_member**](DefaultApi.md#delete_lobby_member) | **DELETE** /lobbies/{lobby_id}/members/{user_id} | 
[**delete_message**](DefaultApi.md#delete_message) | **DELETE** /channels/{channel_id}/messages/{message_id} | 
[**delete_my_message_reaction**](DefaultApi.md#delete_my_message_reaction) | **DELETE** /channels/{channel_id}/messages/{message_id}/reactions/{emoji_name}/@me | 
[**delete_original_webhook_message**](DefaultApi.md#delete_original_webhook_message) | **DELETE** /webhooks/{webhook_id}/{webhook_token}/messages/@original | 
[**delete_pin**](DefaultApi.md#delete_pin) | **DELETE** /channels/{channel_id}/messages/pins/{message_id} | 
[**delete_stage_instance**](DefaultApi.md#delete_stage_instance) | **DELETE** /stage-instances/{channel_id} | 
[**delete_thread_member**](DefaultApi.md#delete_thread_member) | **DELETE** /channels/{channel_id}/thread-members/{user_id} | 
[**delete_user_message_reaction**](DefaultApi.md#delete_user_message_reaction) | **DELETE** /channels/{channel_id}/messages/{message_id}/reactions/{emoji_name}/{user_id} | 
[**delete_webhook**](DefaultApi.md#delete_webhook) | **DELETE** /webhooks/{webhook_id} | 
[**delete_webhook_by_token**](DefaultApi.md#delete_webhook_by_token) | **DELETE** /webhooks/{webhook_id}/{webhook_token} | 
[**delete_webhook_message**](DefaultApi.md#delete_webhook_message) | **DELETE** /webhooks/{webhook_id}/{webhook_token}/messages/{message_id} | 
[**deprecated_create_pin**](DefaultApi.md#deprecated_create_pin) | **PUT** /channels/{channel_id}/pins/{message_id} | 
[**deprecated_delete_pin**](DefaultApi.md#deprecated_delete_pin) | **DELETE** /channels/{channel_id}/pins/{message_id} | 
[**deprecated_list_pins**](DefaultApi.md#deprecated_list_pins) | **GET** /channels/{channel_id}/pins | 
[**edit_lobby**](DefaultApi.md#edit_lobby) | **PATCH** /lobbies/{lobby_id} | 
[**edit_lobby_channel_link**](DefaultApi.md#edit_lobby_channel_link) | **PATCH** /lobbies/{lobby_id}/channel-linking | 
[**execute_github_compatible_webhook**](DefaultApi.md#execute_github_compatible_webhook) | **POST** /webhooks/{webhook_id}/{webhook_token}/github | 
[**execute_slack_compatible_webhook**](DefaultApi.md#execute_slack_compatible_webhook) | **POST** /webhooks/{webhook_id}/{webhook_token}/slack | 
[**execute_webhook**](DefaultApi.md#execute_webhook) | **POST** /webhooks/{webhook_id}/{webhook_token} | 
[**follow_channel**](DefaultApi.md#follow_channel) | **POST** /channels/{channel_id}/followers | 
[**get_active_guild_threads**](DefaultApi.md#get_active_guild_threads) | **GET** /guilds/{guild_id}/threads/active | 
[**get_answer_voters**](DefaultApi.md#get_answer_voters) | **GET** /channels/{channel_id}/polls/{message_id}/answers/{answer_id} | 
[**get_application**](DefaultApi.md#get_application) | **GET** /applications/{application_id} | 
[**get_application_command**](DefaultApi.md#get_application_command) | **GET** /applications/{application_id}/commands/{command_id} | 
[**get_application_emoji**](DefaultApi.md#get_application_emoji) | **GET** /applications/{application_id}/emojis/{emoji_id} | 
[**get_application_role_connections_metadata**](DefaultApi.md#get_application_role_connections_metadata) | **GET** /applications/{application_id}/role-connections/metadata | 
[**get_application_user_role_connection**](DefaultApi.md#get_application_user_role_connection) | **GET** /users/@me/applications/{application_id}/role-connection | 
[**get_auto_moderation_rule**](DefaultApi.md#get_auto_moderation_rule) | **GET** /guilds/{guild_id}/auto-moderation/rules/{rule_id} | 
[**get_bot_gateway**](DefaultApi.md#get_bot_gateway) | **GET** /gateway/bot | 
[**get_channel**](DefaultApi.md#get_channel) | **GET** /channels/{channel_id} | 
[**get_entitlement**](DefaultApi.md#get_entitlement) | **GET** /applications/{application_id}/entitlements/{entitlement_id} | 
[**get_entitlements**](DefaultApi.md#get_entitlements) | **GET** /applications/{application_id}/entitlements | 
[**get_gateway**](DefaultApi.md#get_gateway) | **GET** /gateway | 
[**get_guild**](DefaultApi.md#get_guild) | **GET** /guilds/{guild_id} | 
[**get_guild_application_command**](DefaultApi.md#get_guild_application_command) | **GET** /applications/{application_id}/guilds/{guild_id}/commands/{command_id} | 
[**get_guild_application_command_permissions**](DefaultApi.md#get_guild_application_command_permissions) | **GET** /applications/{application_id}/guilds/{guild_id}/commands/{command_id}/permissions | 
[**get_guild_ban**](DefaultApi.md#get_guild_ban) | **GET** /guilds/{guild_id}/bans/{user_id} | 
[**get_guild_emoji**](DefaultApi.md#get_guild_emoji) | **GET** /guilds/{guild_id}/emojis/{emoji_id} | 
[**get_guild_member**](DefaultApi.md#get_guild_member) | **GET** /guilds/{guild_id}/members/{user_id} | 
[**get_guild_new_member_welcome**](DefaultApi.md#get_guild_new_member_welcome) | **GET** /guilds/{guild_id}/new-member-welcome | 
[**get_guild_preview**](DefaultApi.md#get_guild_preview) | **GET** /guilds/{guild_id}/preview | 
[**get_guild_role**](DefaultApi.md#get_guild_role) | **GET** /guilds/{guild_id}/roles/{role_id} | 
[**get_guild_scheduled_event**](DefaultApi.md#get_guild_scheduled_event) | **GET** /guilds/{guild_id}/scheduled-events/{guild_scheduled_event_id} | 
[**get_guild_soundboard_sound**](DefaultApi.md#get_guild_soundboard_sound) | **GET** /guilds/{guild_id}/soundboard-sounds/{sound_id} | 
[**get_guild_sticker**](DefaultApi.md#get_guild_sticker) | **GET** /guilds/{guild_id}/stickers/{sticker_id} | 
[**get_guild_template**](DefaultApi.md#get_guild_template) | **GET** /guilds/templates/{code} | 
[**get_guild_vanity_url**](DefaultApi.md#get_guild_vanity_url) | **GET** /guilds/{guild_id}/vanity-url | 
[**get_guild_webhooks**](DefaultApi.md#get_guild_webhooks) | **GET** /guilds/{guild_id}/webhooks | 
[**get_guild_welcome_screen**](DefaultApi.md#get_guild_welcome_screen) | **GET** /guilds/{guild_id}/welcome-screen | 
[**get_guild_widget**](DefaultApi.md#get_guild_widget) | **GET** /guilds/{guild_id}/widget.json | 
[**get_guild_widget_png**](DefaultApi.md#get_guild_widget_png) | **GET** /guilds/{guild_id}/widget.png | 
[**get_guild_widget_settings**](DefaultApi.md#get_guild_widget_settings) | **GET** /guilds/{guild_id}/widget | 
[**get_guilds_onboarding**](DefaultApi.md#get_guilds_onboarding) | **GET** /guilds/{guild_id}/onboarding | 
[**get_lobby**](DefaultApi.md#get_lobby) | **GET** /lobbies/{lobby_id} | 
[**get_lobby_messages**](DefaultApi.md#get_lobby_messages) | **GET** /lobbies/{lobby_id}/messages | 
[**get_message**](DefaultApi.md#get_message) | **GET** /channels/{channel_id}/messages/{message_id} | 
[**get_my_application**](DefaultApi.md#get_my_application) | **GET** /applications/@me | 
[**get_my_guild_member**](DefaultApi.md#get_my_guild_member) | **GET** /users/@me/guilds/{guild_id}/member | 
[**get_my_oauth2_application**](DefaultApi.md#get_my_oauth2_application) | **GET** /oauth2/applications/@me | 
[**get_my_oauth2_authorization**](DefaultApi.md#get_my_oauth2_authorization) | **GET** /oauth2/@me | 
[**get_my_user**](DefaultApi.md#get_my_user) | **GET** /users/@me | 
[**get_openid_connect_userinfo**](DefaultApi.md#get_openid_connect_userinfo) | **GET** /oauth2/userinfo | 
[**get_original_webhook_message**](DefaultApi.md#get_original_webhook_message) | **GET** /webhooks/{webhook_id}/{webhook_token}/messages/@original | 
[**get_public_keys**](DefaultApi.md#get_public_keys) | **GET** /oauth2/keys | 
[**get_self_voice_state**](DefaultApi.md#get_self_voice_state) | **GET** /guilds/{guild_id}/voice-states/@me | 
[**get_soundboard_default_sounds**](DefaultApi.md#get_soundboard_default_sounds) | **GET** /soundboard-default-sounds | 
[**get_stage_instance**](DefaultApi.md#get_stage_instance) | **GET** /stage-instances/{channel_id} | 
[**get_sticker**](DefaultApi.md#get_sticker) | **GET** /stickers/{sticker_id} | 
[**get_sticker_pack**](DefaultApi.md#get_sticker_pack) | **GET** /sticker-packs/{pack_id} | 
[**get_thread_member**](DefaultApi.md#get_thread_member) | **GET** /channels/{channel_id}/thread-members/{user_id} | 
[**get_user**](DefaultApi.md#get_user) | **GET** /users/{user_id} | 
[**get_voice_state**](DefaultApi.md#get_voice_state) | **GET** /guilds/{guild_id}/voice-states/{user_id} | 
[**get_webhook**](DefaultApi.md#get_webhook) | **GET** /webhooks/{webhook_id} | 
[**get_webhook_by_token**](DefaultApi.md#get_webhook_by_token) | **GET** /webhooks/{webhook_id}/{webhook_token} | 
[**get_webhook_message**](DefaultApi.md#get_webhook_message) | **GET** /webhooks/{webhook_id}/{webhook_token}/messages/{message_id} | 
[**invite_resolve**](DefaultApi.md#invite_resolve) | **GET** /invites/{code} | 
[**invite_revoke**](DefaultApi.md#invite_revoke) | **DELETE** /invites/{code} | 
[**join_thread**](DefaultApi.md#join_thread) | **PUT** /channels/{channel_id}/thread-members/@me | 
[**leave_guild**](DefaultApi.md#leave_guild) | **DELETE** /users/@me/guilds/{guild_id} | 
[**leave_lobby**](DefaultApi.md#leave_lobby) | **DELETE** /lobbies/{lobby_id}/members/@me | 
[**leave_thread**](DefaultApi.md#leave_thread) | **DELETE** /channels/{channel_id}/thread-members/@me | 
[**list_application_commands**](DefaultApi.md#list_application_commands) | **GET** /applications/{application_id}/commands | 
[**list_application_emojis**](DefaultApi.md#list_application_emojis) | **GET** /applications/{application_id}/emojis | 
[**list_auto_moderation_rules**](DefaultApi.md#list_auto_moderation_rules) | **GET** /guilds/{guild_id}/auto-moderation/rules | 
[**list_channel_invites**](DefaultApi.md#list_channel_invites) | **GET** /channels/{channel_id}/invites | 
[**list_channel_webhooks**](DefaultApi.md#list_channel_webhooks) | **GET** /channels/{channel_id}/webhooks | 
[**list_guild_application_command_permissions**](DefaultApi.md#list_guild_application_command_permissions) | **GET** /applications/{application_id}/guilds/{guild_id}/commands/permissions | 
[**list_guild_application_commands**](DefaultApi.md#list_guild_application_commands) | **GET** /applications/{application_id}/guilds/{guild_id}/commands | 
[**list_guild_audit_log_entries**](DefaultApi.md#list_guild_audit_log_entries) | **GET** /guilds/{guild_id}/audit-logs | 
[**list_guild_bans**](DefaultApi.md#list_guild_bans) | **GET** /guilds/{guild_id}/bans | 
[**list_guild_channels**](DefaultApi.md#list_guild_channels) | **GET** /guilds/{guild_id}/channels | 
[**list_guild_emojis**](DefaultApi.md#list_guild_emojis) | **GET** /guilds/{guild_id}/emojis | 
[**list_guild_integrations**](DefaultApi.md#list_guild_integrations) | **GET** /guilds/{guild_id}/integrations | 
[**list_guild_invites**](DefaultApi.md#list_guild_invites) | **GET** /guilds/{guild_id}/invites | 
[**list_guild_members**](DefaultApi.md#list_guild_members) | **GET** /guilds/{guild_id}/members | 
[**list_guild_roles**](DefaultApi.md#list_guild_roles) | **GET** /guilds/{guild_id}/roles | 
[**list_guild_scheduled_event_users**](DefaultApi.md#list_guild_scheduled_event_users) | **GET** /guilds/{guild_id}/scheduled-events/{guild_scheduled_event_id}/users | 
[**list_guild_scheduled_events**](DefaultApi.md#list_guild_scheduled_events) | **GET** /guilds/{guild_id}/scheduled-events | 
[**list_guild_soundboard_sounds**](DefaultApi.md#list_guild_soundboard_sounds) | **GET** /guilds/{guild_id}/soundboard-sounds | 
[**list_guild_stickers**](DefaultApi.md#list_guild_stickers) | **GET** /guilds/{guild_id}/stickers | 
[**list_guild_templates**](DefaultApi.md#list_guild_templates) | **GET** /guilds/{guild_id}/templates | 
[**list_guild_voice_regions**](DefaultApi.md#list_guild_voice_regions) | **GET** /guilds/{guild_id}/regions | 
[**list_message_reactions_by_emoji**](DefaultApi.md#list_message_reactions_by_emoji) | **GET** /channels/{channel_id}/messages/{message_id}/reactions/{emoji_name} | 
[**list_messages**](DefaultApi.md#list_messages) | **GET** /channels/{channel_id}/messages | 
[**list_my_connections**](DefaultApi.md#list_my_connections) | **GET** /users/@me/connections | 
[**list_my_guilds**](DefaultApi.md#list_my_guilds) | **GET** /users/@me/guilds | 
[**list_my_private_archived_threads**](DefaultApi.md#list_my_private_archived_threads) | **GET** /channels/{channel_id}/users/@me/threads/archived/private | 
[**list_pins**](DefaultApi.md#list_pins) | **GET** /channels/{channel_id}/messages/pins | 
[**list_private_archived_threads**](DefaultApi.md#list_private_archived_threads) | **GET** /channels/{channel_id}/threads/archived/private | 
[**list_public_archived_threads**](DefaultApi.md#list_public_archived_threads) | **GET** /channels/{channel_id}/threads/archived/public | 
[**list_sticker_packs**](DefaultApi.md#list_sticker_packs) | **GET** /sticker-packs | 
[**list_thread_members**](DefaultApi.md#list_thread_members) | **GET** /channels/{channel_id}/thread-members | 
[**list_voice_regions**](DefaultApi.md#list_voice_regions) | **GET** /voice/regions | 
[**partner_sdk_token**](DefaultApi.md#partner_sdk_token) | **POST** /partner-sdk/token | 
[**partner_sdk_unmerge_provisional_account**](DefaultApi.md#partner_sdk_unmerge_provisional_account) | **POST** /partner-sdk/provisional-accounts/unmerge | 
[**poll_expire**](DefaultApi.md#poll_expire) | **POST** /channels/{channel_id}/polls/{message_id}/expire | 
[**preview_prune_guild**](DefaultApi.md#preview_prune_guild) | **GET** /guilds/{guild_id}/prune | 
[**prune_guild**](DefaultApi.md#prune_guild) | **POST** /guilds/{guild_id}/prune | 
[**put_guilds_onboarding**](DefaultApi.md#put_guilds_onboarding) | **PUT** /guilds/{guild_id}/onboarding | 
[**search_guild_members**](DefaultApi.md#search_guild_members) | **GET** /guilds/{guild_id}/members/search | 
[**send_soundboard_sound**](DefaultApi.md#send_soundboard_sound) | **POST** /channels/{channel_id}/send-soundboard-sound | 
[**set_channel_permission_overwrite**](DefaultApi.md#set_channel_permission_overwrite) | **PUT** /channels/{channel_id}/permissions/{overwrite_id} | 
[**set_guild_application_command_permissions**](DefaultApi.md#set_guild_application_command_permissions) | **PUT** /applications/{application_id}/guilds/{guild_id}/commands/{command_id}/permissions | 
[**set_guild_mfa_level**](DefaultApi.md#set_guild_mfa_level) | **POST** /guilds/{guild_id}/mfa | 
[**sync_guild_template**](DefaultApi.md#sync_guild_template) | **PUT** /guilds/{guild_id}/templates/{code} | 
[**thread_search**](DefaultApi.md#thread_search) | **GET** /channels/{channel_id}/threads/search | 
[**trigger_typing_indicator**](DefaultApi.md#trigger_typing_indicator) | **POST** /channels/{channel_id}/typing | 
[**unban_user_from_guild**](DefaultApi.md#unban_user_from_guild) | **DELETE** /guilds/{guild_id}/bans/{user_id} | 
[**update_application**](DefaultApi.md#update_application) | **PATCH** /applications/{application_id} | 
[**update_application_command**](DefaultApi.md#update_application_command) | **PATCH** /applications/{application_id}/commands/{command_id} | 
[**update_application_emoji**](DefaultApi.md#update_application_emoji) | **PATCH** /applications/{application_id}/emojis/{emoji_id} | 
[**update_application_role_connections_metadata**](DefaultApi.md#update_application_role_connections_metadata) | **PUT** /applications/{application_id}/role-connections/metadata | 
[**update_application_user_role_connection**](DefaultApi.md#update_application_user_role_connection) | **PUT** /users/@me/applications/{application_id}/role-connection | 
[**update_auto_moderation_rule**](DefaultApi.md#update_auto_moderation_rule) | **PATCH** /guilds/{guild_id}/auto-moderation/rules/{rule_id} | 
[**update_channel**](DefaultApi.md#update_channel) | **PATCH** /channels/{channel_id} | 
[**update_guild**](DefaultApi.md#update_guild) | **PATCH** /guilds/{guild_id} | 
[**update_guild_application_command**](DefaultApi.md#update_guild_application_command) | **PATCH** /applications/{application_id}/guilds/{guild_id}/commands/{command_id} | 
[**update_guild_emoji**](DefaultApi.md#update_guild_emoji) | **PATCH** /guilds/{guild_id}/emojis/{emoji_id} | 
[**update_guild_member**](DefaultApi.md#update_guild_member) | **PATCH** /guilds/{guild_id}/members/{user_id} | 
[**update_guild_role**](DefaultApi.md#update_guild_role) | **PATCH** /guilds/{guild_id}/roles/{role_id} | 
[**update_guild_scheduled_event**](DefaultApi.md#update_guild_scheduled_event) | **PATCH** /guilds/{guild_id}/scheduled-events/{guild_scheduled_event_id} | 
[**update_guild_soundboard_sound**](DefaultApi.md#update_guild_soundboard_sound) | **PATCH** /guilds/{guild_id}/soundboard-sounds/{sound_id} | 
[**update_guild_sticker**](DefaultApi.md#update_guild_sticker) | **PATCH** /guilds/{guild_id}/stickers/{sticker_id} | 
[**update_guild_template**](DefaultApi.md#update_guild_template) | **PATCH** /guilds/{guild_id}/templates/{code} | 
[**update_guild_welcome_screen**](DefaultApi.md#update_guild_welcome_screen) | **PATCH** /guilds/{guild_id}/welcome-screen | 
[**update_guild_widget_settings**](DefaultApi.md#update_guild_widget_settings) | **PATCH** /guilds/{guild_id}/widget | 
[**update_message**](DefaultApi.md#update_message) | **PATCH** /channels/{channel_id}/messages/{message_id} | 
[**update_my_application**](DefaultApi.md#update_my_application) | **PATCH** /applications/@me | 
[**update_my_guild_member**](DefaultApi.md#update_my_guild_member) | **PATCH** /guilds/{guild_id}/members/@me | 
[**update_my_user**](DefaultApi.md#update_my_user) | **PATCH** /users/@me | 
[**update_original_webhook_message**](DefaultApi.md#update_original_webhook_message) | **PATCH** /webhooks/{webhook_id}/{webhook_token}/messages/@original | 
[**update_self_voice_state**](DefaultApi.md#update_self_voice_state) | **PATCH** /guilds/{guild_id}/voice-states/@me | 
[**update_stage_instance**](DefaultApi.md#update_stage_instance) | **PATCH** /stage-instances/{channel_id} | 
[**update_voice_state**](DefaultApi.md#update_voice_state) | **PATCH** /guilds/{guild_id}/voice-states/{user_id} | 
[**update_webhook**](DefaultApi.md#update_webhook) | **PATCH** /webhooks/{webhook_id} | 
[**update_webhook_by_token**](DefaultApi.md#update_webhook_by_token) | **PATCH** /webhooks/{webhook_id}/{webhook_token} | 
[**update_webhook_message**](DefaultApi.md#update_webhook_message) | **PATCH** /webhooks/{webhook_id}/{webhook_token}/messages/{message_id} | 
[**upload_application_attachment**](DefaultApi.md#upload_application_attachment) | **POST** /applications/{application_id}/attachment | 


# **add_group_dm_user**
> AddGroupDmUser201Response add_group_dm_user(channel_id, user_id, add_group_dm_user_request)

### Example

* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.models.add_group_dm_user201_response import AddGroupDmUser201Response
from dc_rest.models.add_group_dm_user_request import AddGroupDmUserRequest
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    channel_id = 'channel_id_example' # str | 
    user_id = 'user_id_example' # str | 
    add_group_dm_user_request = dc_rest.AddGroupDmUserRequest() # AddGroupDmUserRequest | 

    try:
        api_response = await api_instance.add_group_dm_user(channel_id, user_id, add_group_dm_user_request)
        print("The response of DefaultApi->add_group_dm_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->add_group_dm_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **str**|  | 
 **user_id** | **str**|  | 
 **add_group_dm_user_request** | [**AddGroupDmUserRequest**](AddGroupDmUserRequest.md)|  | 

### Return type

[**AddGroupDmUser201Response**](AddGroupDmUser201Response.md)

### Authorization

[BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | 201 response for add_group_dm_user |  -  |
**204** | 204 response for add_group_dm_user |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_guild_member**
> GuildMemberResponse add_guild_member(guild_id, user_id, add_guild_member_request)

### Example

* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.models.add_guild_member_request import AddGuildMemberRequest
from dc_rest.models.guild_member_response import GuildMemberResponse
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    guild_id = 'guild_id_example' # str | 
    user_id = 'user_id_example' # str | 
    add_guild_member_request = dc_rest.AddGuildMemberRequest() # AddGuildMemberRequest | 

    try:
        api_response = await api_instance.add_guild_member(guild_id, user_id, add_guild_member_request)
        print("The response of DefaultApi->add_guild_member:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->add_guild_member: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guild_id** | **str**|  | 
 **user_id** | **str**|  | 
 **add_guild_member_request** | [**AddGuildMemberRequest**](AddGuildMemberRequest.md)|  | 

### Return type

[**GuildMemberResponse**](GuildMemberResponse.md)

### Authorization

[BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | 201 response for add_guild_member |  -  |
**204** | 204 response for add_guild_member |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_guild_member_role**
> add_guild_member_role(guild_id, user_id, role_id)

### Example

* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    guild_id = 'guild_id_example' # str | 
    user_id = 'user_id_example' # str | 
    role_id = 'role_id_example' # str | 

    try:
        await api_instance.add_guild_member_role(guild_id, user_id, role_id)
    except Exception as e:
        print("Exception when calling DefaultApi->add_guild_member_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guild_id** | **str**|  | 
 **user_id** | **str**|  | 
 **role_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | 204 response for add_guild_member_role |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_lobby_member**
> LobbyMemberResponse add_lobby_member(lobby_id, user_id, add_lobby_member_request)

### Example

* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.models.add_lobby_member_request import AddLobbyMemberRequest
from dc_rest.models.lobby_member_response import LobbyMemberResponse
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    lobby_id = 'lobby_id_example' # str | 
    user_id = 'user_id_example' # str | 
    add_lobby_member_request = dc_rest.AddLobbyMemberRequest() # AddLobbyMemberRequest | 

    try:
        api_response = await api_instance.add_lobby_member(lobby_id, user_id, add_lobby_member_request)
        print("The response of DefaultApi->add_lobby_member:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->add_lobby_member: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lobby_id** | **str**|  | 
 **user_id** | **str**|  | 
 **add_lobby_member_request** | [**AddLobbyMemberRequest**](AddLobbyMemberRequest.md)|  | 

### Return type

[**LobbyMemberResponse**](LobbyMemberResponse.md)

### Authorization

[BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 response for add_lobby_member |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_my_message_reaction**
> add_my_message_reaction(channel_id, message_id, emoji_name)

### Example

* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    channel_id = 'channel_id_example' # str | 
    message_id = 'message_id_example' # str | 
    emoji_name = 'emoji_name_example' # str | 

    try:
        await api_instance.add_my_message_reaction(channel_id, message_id, emoji_name)
    except Exception as e:
        print("Exception when calling DefaultApi->add_my_message_reaction: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **str**|  | 
 **message_id** | **str**|  | 
 **emoji_name** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | 204 response for add_my_message_reaction |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_thread_member**
> add_thread_member(channel_id, user_id)

### Example

* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    channel_id = 'channel_id_example' # str | 
    user_id = 'user_id_example' # str | 

    try:
        await api_instance.add_thread_member(channel_id, user_id)
    except Exception as e:
        print("Exception when calling DefaultApi->add_thread_member: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | 204 response for add_thread_member |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **applications_get_activity_instance**
> EmbeddedActivityInstance applications_get_activity_instance(application_id, instance_id)

### Example

* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.models.embedded_activity_instance import EmbeddedActivityInstance
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    application_id = 'application_id_example' # str | 
    instance_id = 'instance_id_example' # str | 

    try:
        api_response = await api_instance.applications_get_activity_instance(application_id, instance_id)
        print("The response of DefaultApi->applications_get_activity_instance:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->applications_get_activity_instance: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **str**|  | 
 **instance_id** | **str**|  | 

### Return type

[**EmbeddedActivityInstance**](EmbeddedActivityInstance.md)

### Authorization

[BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 response for applications_get_activity_instance |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ban_user_from_guild**
> ban_user_from_guild(guild_id, user_id, ban_user_from_guild_request)

### Example

* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.models.ban_user_from_guild_request import BanUserFromGuildRequest
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    guild_id = 'guild_id_example' # str | 
    user_id = 'user_id_example' # str | 
    ban_user_from_guild_request = dc_rest.BanUserFromGuildRequest() # BanUserFromGuildRequest | 

    try:
        await api_instance.ban_user_from_guild(guild_id, user_id, ban_user_from_guild_request)
    except Exception as e:
        print("Exception when calling DefaultApi->ban_user_from_guild: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guild_id** | **str**|  | 
 **user_id** | **str**|  | 
 **ban_user_from_guild_request** | [**BanUserFromGuildRequest**](BanUserFromGuildRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | 204 response for ban_user_from_guild |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_ban_users_from_guild**
> BulkBanUsersResponse bulk_ban_users_from_guild(guild_id, bulk_ban_users_from_guild_request)

### Example

* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.models.bulk_ban_users_from_guild_request import BulkBanUsersFromGuildRequest
from dc_rest.models.bulk_ban_users_response import BulkBanUsersResponse
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    guild_id = 'guild_id_example' # str | 
    bulk_ban_users_from_guild_request = dc_rest.BulkBanUsersFromGuildRequest() # BulkBanUsersFromGuildRequest | 

    try:
        api_response = await api_instance.bulk_ban_users_from_guild(guild_id, bulk_ban_users_from_guild_request)
        print("The response of DefaultApi->bulk_ban_users_from_guild:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->bulk_ban_users_from_guild: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guild_id** | **str**|  | 
 **bulk_ban_users_from_guild_request** | [**BulkBanUsersFromGuildRequest**](BulkBanUsersFromGuildRequest.md)|  | 

### Return type

[**BulkBanUsersResponse**](BulkBanUsersResponse.md)

### Authorization

[BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 response for bulk_ban_users_from_guild |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_delete_messages**
> bulk_delete_messages(channel_id, bulk_delete_messages_request)

### Example

* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.models.bulk_delete_messages_request import BulkDeleteMessagesRequest
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    channel_id = 'channel_id_example' # str | 
    bulk_delete_messages_request = dc_rest.BulkDeleteMessagesRequest() # BulkDeleteMessagesRequest | 

    try:
        await api_instance.bulk_delete_messages(channel_id, bulk_delete_messages_request)
    except Exception as e:
        print("Exception when calling DefaultApi->bulk_delete_messages: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **str**|  | 
 **bulk_delete_messages_request** | [**BulkDeleteMessagesRequest**](BulkDeleteMessagesRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | 204 response for bulk_delete_messages |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_set_application_commands**
> List[ApplicationCommandResponse] bulk_set_application_commands(application_id, application_command_update_request)

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):
* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.models.application_command_response import ApplicationCommandResponse
from dc_rest.models.application_command_update_request import ApplicationCommandUpdateRequest
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    application_id = 'application_id_example' # str | 
    application_command_update_request = [dc_rest.ApplicationCommandUpdateRequest()] # List[ApplicationCommandUpdateRequest] | 

    try:
        api_response = await api_instance.bulk_set_application_commands(application_id, application_command_update_request)
        print("The response of DefaultApi->bulk_set_application_commands:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->bulk_set_application_commands: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **str**|  | 
 **application_command_update_request** | [**List[ApplicationCommandUpdateRequest]**](ApplicationCommandUpdateRequest.md)|  | 

### Return type

[**List[ApplicationCommandResponse]**](ApplicationCommandResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 response for bulk_set_application_commands |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_set_guild_application_commands**
> List[ApplicationCommandResponse] bulk_set_guild_application_commands(application_id, guild_id, application_command_update_request)

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):
* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.models.application_command_response import ApplicationCommandResponse
from dc_rest.models.application_command_update_request import ApplicationCommandUpdateRequest
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    application_id = 'application_id_example' # str | 
    guild_id = 'guild_id_example' # str | 
    application_command_update_request = [dc_rest.ApplicationCommandUpdateRequest()] # List[ApplicationCommandUpdateRequest] | 

    try:
        api_response = await api_instance.bulk_set_guild_application_commands(application_id, guild_id, application_command_update_request)
        print("The response of DefaultApi->bulk_set_guild_application_commands:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->bulk_set_guild_application_commands: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **str**|  | 
 **guild_id** | **str**|  | 
 **application_command_update_request** | [**List[ApplicationCommandUpdateRequest]**](ApplicationCommandUpdateRequest.md)|  | 

### Return type

[**List[ApplicationCommandResponse]**](ApplicationCommandResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 response for bulk_set_guild_application_commands |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_update_guild_channels**
> bulk_update_guild_channels(guild_id, bulk_update_guild_channels_request_inner)

### Example

* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.models.bulk_update_guild_channels_request_inner import BulkUpdateGuildChannelsRequestInner
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    guild_id = 'guild_id_example' # str | 
    bulk_update_guild_channels_request_inner = [dc_rest.BulkUpdateGuildChannelsRequestInner()] # List[BulkUpdateGuildChannelsRequestInner] | 

    try:
        await api_instance.bulk_update_guild_channels(guild_id, bulk_update_guild_channels_request_inner)
    except Exception as e:
        print("Exception when calling DefaultApi->bulk_update_guild_channels: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guild_id** | **str**|  | 
 **bulk_update_guild_channels_request_inner** | [**List[BulkUpdateGuildChannelsRequestInner]**](BulkUpdateGuildChannelsRequestInner.md)|  | 

### Return type

void (empty response body)

### Authorization

[BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | 204 response for bulk_update_guild_channels |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_update_guild_roles**
> List[GuildRoleResponse] bulk_update_guild_roles(guild_id, bulk_update_guild_roles_request_inner)

### Example

* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.models.bulk_update_guild_roles_request_inner import BulkUpdateGuildRolesRequestInner
from dc_rest.models.guild_role_response import GuildRoleResponse
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    guild_id = 'guild_id_example' # str | 
    bulk_update_guild_roles_request_inner = [dc_rest.BulkUpdateGuildRolesRequestInner()] # List[BulkUpdateGuildRolesRequestInner] | 

    try:
        api_response = await api_instance.bulk_update_guild_roles(guild_id, bulk_update_guild_roles_request_inner)
        print("The response of DefaultApi->bulk_update_guild_roles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->bulk_update_guild_roles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guild_id** | **str**|  | 
 **bulk_update_guild_roles_request_inner** | [**List[BulkUpdateGuildRolesRequestInner]**](BulkUpdateGuildRolesRequestInner.md)|  | 

### Return type

[**List[GuildRoleResponse]**](GuildRoleResponse.md)

### Authorization

[BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 response for bulk_update_guild_roles |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_update_lobby_members**
> List[LobbyMemberResponse] bulk_update_lobby_members(lobby_id, bulk_lobby_member_request)

### Example

* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.models.bulk_lobby_member_request import BulkLobbyMemberRequest
from dc_rest.models.lobby_member_response import LobbyMemberResponse
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    lobby_id = 'lobby_id_example' # str | 
    bulk_lobby_member_request = [dc_rest.BulkLobbyMemberRequest()] # List[BulkLobbyMemberRequest] | 

    try:
        api_response = await api_instance.bulk_update_lobby_members(lobby_id, bulk_lobby_member_request)
        print("The response of DefaultApi->bulk_update_lobby_members:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->bulk_update_lobby_members: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lobby_id** | **str**|  | 
 **bulk_lobby_member_request** | [**List[BulkLobbyMemberRequest]**](BulkLobbyMemberRequest.md)|  | 

### Return type

[**List[LobbyMemberResponse]**](LobbyMemberResponse.md)

### Authorization

[BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 response for bulk_update_lobby_members |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **consume_entitlement**
> consume_entitlement(application_id, entitlement_id)

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):
* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    application_id = 'application_id_example' # str | 
    entitlement_id = 'entitlement_id_example' # str | 

    try:
        await api_instance.consume_entitlement(application_id, entitlement_id)
    except Exception as e:
        print("Exception when calling DefaultApi->consume_entitlement: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **str**|  | 
 **entitlement_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | 204 response for consume_entitlement |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_application_command**
> ApplicationCommandResponse create_application_command(application_id, application_command_create_request)

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):
* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.models.application_command_create_request import ApplicationCommandCreateRequest
from dc_rest.models.application_command_response import ApplicationCommandResponse
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    application_id = 'application_id_example' # str | 
    application_command_create_request = dc_rest.ApplicationCommandCreateRequest() # ApplicationCommandCreateRequest | 

    try:
        api_response = await api_instance.create_application_command(application_id, application_command_create_request)
        print("The response of DefaultApi->create_application_command:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->create_application_command: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **str**|  | 
 **application_command_create_request** | [**ApplicationCommandCreateRequest**](ApplicationCommandCreateRequest.md)|  | 

### Return type

[**ApplicationCommandResponse**](ApplicationCommandResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 response for create_application_command |  -  |
**201** | 201 response for create_application_command |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_application_emoji**
> EmojiResponse create_application_emoji(application_id, create_application_emoji_request)

### Example

* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.models.create_application_emoji_request import CreateApplicationEmojiRequest
from dc_rest.models.emoji_response import EmojiResponse
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    application_id = 'application_id_example' # str | 
    create_application_emoji_request = dc_rest.CreateApplicationEmojiRequest() # CreateApplicationEmojiRequest | 

    try:
        api_response = await api_instance.create_application_emoji(application_id, create_application_emoji_request)
        print("The response of DefaultApi->create_application_emoji:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->create_application_emoji: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **str**|  | 
 **create_application_emoji_request** | [**CreateApplicationEmojiRequest**](CreateApplicationEmojiRequest.md)|  | 

### Return type

[**EmojiResponse**](EmojiResponse.md)

### Authorization

[BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | 201 response for create_application_emoji |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_auto_moderation_rule**
> CreateAutoModerationRule200Response create_auto_moderation_rule(guild_id, create_auto_moderation_rule_request)

### Example

* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.models.create_auto_moderation_rule200_response import CreateAutoModerationRule200Response
from dc_rest.models.create_auto_moderation_rule_request import CreateAutoModerationRuleRequest
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    guild_id = 'guild_id_example' # str | 
    create_auto_moderation_rule_request = dc_rest.CreateAutoModerationRuleRequest() # CreateAutoModerationRuleRequest | 

    try:
        api_response = await api_instance.create_auto_moderation_rule(guild_id, create_auto_moderation_rule_request)
        print("The response of DefaultApi->create_auto_moderation_rule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->create_auto_moderation_rule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guild_id** | **str**|  | 
 **create_auto_moderation_rule_request** | [**CreateAutoModerationRuleRequest**](CreateAutoModerationRuleRequest.md)|  | 

### Return type

[**CreateAutoModerationRule200Response**](CreateAutoModerationRule200Response.md)

### Authorization

[BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 response for create_auto_moderation_rule |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_channel_invite**
> ListChannelInvites200ResponseInner create_channel_invite(channel_id, create_channel_invite_request)

### Example

* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.models.create_channel_invite_request import CreateChannelInviteRequest
from dc_rest.models.list_channel_invites200_response_inner import ListChannelInvites200ResponseInner
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    channel_id = 'channel_id_example' # str | 
    create_channel_invite_request = dc_rest.CreateChannelInviteRequest() # CreateChannelInviteRequest | 

    try:
        api_response = await api_instance.create_channel_invite(channel_id, create_channel_invite_request)
        print("The response of DefaultApi->create_channel_invite:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->create_channel_invite: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **str**|  | 
 **create_channel_invite_request** | [**CreateChannelInviteRequest**](CreateChannelInviteRequest.md)|  | 

### Return type

[**ListChannelInvites200ResponseInner**](ListChannelInvites200ResponseInner.md)

### Authorization

[BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 response for create_channel_invite |  -  |
**204** | 204 response for create_channel_invite |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_dm**
> AddGroupDmUser201Response create_dm(create_private_channel_request)

### Example

* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.models.add_group_dm_user201_response import AddGroupDmUser201Response
from dc_rest.models.create_private_channel_request import CreatePrivateChannelRequest
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    create_private_channel_request = dc_rest.CreatePrivateChannelRequest() # CreatePrivateChannelRequest | 

    try:
        api_response = await api_instance.create_dm(create_private_channel_request)
        print("The response of DefaultApi->create_dm:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->create_dm: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_private_channel_request** | [**CreatePrivateChannelRequest**](CreatePrivateChannelRequest.md)|  | 

### Return type

[**AddGroupDmUser201Response**](AddGroupDmUser201Response.md)

### Authorization

[BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 response for create_dm |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_entitlement**
> EntitlementResponse create_entitlement(application_id, create_entitlement_request_data)

### Example

* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.models.create_entitlement_request_data import CreateEntitlementRequestData
from dc_rest.models.entitlement_response import EntitlementResponse
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    application_id = 'application_id_example' # str | 
    create_entitlement_request_data = dc_rest.CreateEntitlementRequestData() # CreateEntitlementRequestData | 

    try:
        api_response = await api_instance.create_entitlement(application_id, create_entitlement_request_data)
        print("The response of DefaultApi->create_entitlement:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->create_entitlement: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **str**|  | 
 **create_entitlement_request_data** | [**CreateEntitlementRequestData**](CreateEntitlementRequestData.md)|  | 

### Return type

[**EntitlementResponse**](EntitlementResponse.md)

### Authorization

[BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 response for create_entitlement |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_guild**
> GuildResponse create_guild(guild_create_request)

### Example

* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.models.guild_create_request import GuildCreateRequest
from dc_rest.models.guild_response import GuildResponse
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    guild_create_request = dc_rest.GuildCreateRequest() # GuildCreateRequest | 

    try:
        api_response = await api_instance.create_guild(guild_create_request)
        print("The response of DefaultApi->create_guild:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->create_guild: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guild_create_request** | [**GuildCreateRequest**](GuildCreateRequest.md)|  | 

### Return type

[**GuildResponse**](GuildResponse.md)

### Authorization

[BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | 201 response for create_guild |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_guild_application_command**
> ApplicationCommandResponse create_guild_application_command(application_id, guild_id, application_command_create_request)

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):
* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.models.application_command_create_request import ApplicationCommandCreateRequest
from dc_rest.models.application_command_response import ApplicationCommandResponse
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    application_id = 'application_id_example' # str | 
    guild_id = 'guild_id_example' # str | 
    application_command_create_request = dc_rest.ApplicationCommandCreateRequest() # ApplicationCommandCreateRequest | 

    try:
        api_response = await api_instance.create_guild_application_command(application_id, guild_id, application_command_create_request)
        print("The response of DefaultApi->create_guild_application_command:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->create_guild_application_command: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **str**|  | 
 **guild_id** | **str**|  | 
 **application_command_create_request** | [**ApplicationCommandCreateRequest**](ApplicationCommandCreateRequest.md)|  | 

### Return type

[**ApplicationCommandResponse**](ApplicationCommandResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 response for create_guild_application_command |  -  |
**201** | 201 response for create_guild_application_command |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_guild_channel**
> GuildChannelResponse create_guild_channel(guild_id, create_guild_channel_request)

### Example

* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.models.create_guild_channel_request import CreateGuildChannelRequest
from dc_rest.models.guild_channel_response import GuildChannelResponse
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    guild_id = 'guild_id_example' # str | 
    create_guild_channel_request = dc_rest.CreateGuildChannelRequest() # CreateGuildChannelRequest | 

    try:
        api_response = await api_instance.create_guild_channel(guild_id, create_guild_channel_request)
        print("The response of DefaultApi->create_guild_channel:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->create_guild_channel: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guild_id** | **str**|  | 
 **create_guild_channel_request** | [**CreateGuildChannelRequest**](CreateGuildChannelRequest.md)|  | 

### Return type

[**GuildChannelResponse**](GuildChannelResponse.md)

### Authorization

[BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | 201 response for create_guild_channel |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_guild_emoji**
> EmojiResponse create_guild_emoji(guild_id, create_guild_emoji_request)

### Example

* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.models.create_guild_emoji_request import CreateGuildEmojiRequest
from dc_rest.models.emoji_response import EmojiResponse
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    guild_id = 'guild_id_example' # str | 
    create_guild_emoji_request = dc_rest.CreateGuildEmojiRequest() # CreateGuildEmojiRequest | 

    try:
        api_response = await api_instance.create_guild_emoji(guild_id, create_guild_emoji_request)
        print("The response of DefaultApi->create_guild_emoji:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->create_guild_emoji: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guild_id** | **str**|  | 
 **create_guild_emoji_request** | [**CreateGuildEmojiRequest**](CreateGuildEmojiRequest.md)|  | 

### Return type

[**EmojiResponse**](EmojiResponse.md)

### Authorization

[BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | 201 response for create_guild_emoji |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_guild_from_template**
> GuildResponse create_guild_from_template(code, create_guild_from_template_request)

### Example

* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.models.create_guild_from_template_request import CreateGuildFromTemplateRequest
from dc_rest.models.guild_response import GuildResponse
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    code = 'code_example' # str | 
    create_guild_from_template_request = dc_rest.CreateGuildFromTemplateRequest() # CreateGuildFromTemplateRequest | 

    try:
        api_response = await api_instance.create_guild_from_template(code, create_guild_from_template_request)
        print("The response of DefaultApi->create_guild_from_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->create_guild_from_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**|  | 
 **create_guild_from_template_request** | [**CreateGuildFromTemplateRequest**](CreateGuildFromTemplateRequest.md)|  | 

### Return type

[**GuildResponse**](GuildResponse.md)

### Authorization

[BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | 201 response for create_guild_from_template |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_guild_role**
> GuildRoleResponse create_guild_role(guild_id, create_guild_role_request)

### Example

* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.models.create_guild_role_request import CreateGuildRoleRequest
from dc_rest.models.guild_role_response import GuildRoleResponse
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    guild_id = 'guild_id_example' # str | 
    create_guild_role_request = dc_rest.CreateGuildRoleRequest() # CreateGuildRoleRequest | 

    try:
        api_response = await api_instance.create_guild_role(guild_id, create_guild_role_request)
        print("The response of DefaultApi->create_guild_role:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->create_guild_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guild_id** | **str**|  | 
 **create_guild_role_request** | [**CreateGuildRoleRequest**](CreateGuildRoleRequest.md)|  | 

### Return type

[**GuildRoleResponse**](GuildRoleResponse.md)

### Authorization

[BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 response for create_guild_role |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_guild_scheduled_event**
> ListGuildScheduledEvents200ResponseInner create_guild_scheduled_event(guild_id, create_guild_scheduled_event_request)

### Example

* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.models.create_guild_scheduled_event_request import CreateGuildScheduledEventRequest
from dc_rest.models.list_guild_scheduled_events200_response_inner import ListGuildScheduledEvents200ResponseInner
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    guild_id = 'guild_id_example' # str | 
    create_guild_scheduled_event_request = dc_rest.CreateGuildScheduledEventRequest() # CreateGuildScheduledEventRequest | 

    try:
        api_response = await api_instance.create_guild_scheduled_event(guild_id, create_guild_scheduled_event_request)
        print("The response of DefaultApi->create_guild_scheduled_event:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->create_guild_scheduled_event: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guild_id** | **str**|  | 
 **create_guild_scheduled_event_request** | [**CreateGuildScheduledEventRequest**](CreateGuildScheduledEventRequest.md)|  | 

### Return type

[**ListGuildScheduledEvents200ResponseInner**](ListGuildScheduledEvents200ResponseInner.md)

### Authorization

[BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 response for create_guild_scheduled_event |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_guild_soundboard_sound**
> SoundboardSoundResponse create_guild_soundboard_sound(guild_id, soundboard_create_request)

### Example

* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.models.soundboard_create_request import SoundboardCreateRequest
from dc_rest.models.soundboard_sound_response import SoundboardSoundResponse
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    guild_id = 'guild_id_example' # str | 
    soundboard_create_request = dc_rest.SoundboardCreateRequest() # SoundboardCreateRequest | 

    try:
        api_response = await api_instance.create_guild_soundboard_sound(guild_id, soundboard_create_request)
        print("The response of DefaultApi->create_guild_soundboard_sound:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->create_guild_soundboard_sound: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guild_id** | **str**|  | 
 **soundboard_create_request** | [**SoundboardCreateRequest**](SoundboardCreateRequest.md)|  | 

### Return type

[**SoundboardSoundResponse**](SoundboardSoundResponse.md)

### Authorization

[BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | 201 response for create_guild_soundboard_sound |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_guild_sticker**
> GuildStickerResponse create_guild_sticker(guild_id, name, tags, file, description=description)

### Example

* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.models.guild_sticker_response import GuildStickerResponse
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    guild_id = 'guild_id_example' # str | 
    name = 'name_example' # str | 
    tags = 'tags_example' # str | 
    file = 'file_example' # str | 
    description = 'description_example' # str |  (optional)

    try:
        api_response = await api_instance.create_guild_sticker(guild_id, name, tags, file, description=description)
        print("The response of DefaultApi->create_guild_sticker:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->create_guild_sticker: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guild_id** | **str**|  | 
 **name** | **str**|  | 
 **tags** | **str**|  | 
 **file** | **str**|  | 
 **description** | **str**|  | [optional] 

### Return type

[**GuildStickerResponse**](GuildStickerResponse.md)

### Authorization

[BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | 201 response for create_guild_sticker |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_guild_template**
> GuildTemplateResponse create_guild_template(guild_id, create_guild_template_request)

### Example

* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.models.create_guild_template_request import CreateGuildTemplateRequest
from dc_rest.models.guild_template_response import GuildTemplateResponse
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    guild_id = 'guild_id_example' # str | 
    create_guild_template_request = dc_rest.CreateGuildTemplateRequest() # CreateGuildTemplateRequest | 

    try:
        api_response = await api_instance.create_guild_template(guild_id, create_guild_template_request)
        print("The response of DefaultApi->create_guild_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->create_guild_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guild_id** | **str**|  | 
 **create_guild_template_request** | [**CreateGuildTemplateRequest**](CreateGuildTemplateRequest.md)|  | 

### Return type

[**GuildTemplateResponse**](GuildTemplateResponse.md)

### Authorization

[BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 response for create_guild_template |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_interaction_response**
> InteractionCallbackResponse create_interaction_response(interaction_id, interaction_token, create_interaction_response_request, with_response=with_response)

### Example

* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.models.create_interaction_response_request import CreateInteractionResponseRequest
from dc_rest.models.interaction_callback_response import InteractionCallbackResponse
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    interaction_id = 'interaction_id_example' # str | 
    interaction_token = 'interaction_token_example' # str | 
    create_interaction_response_request = dc_rest.CreateInteractionResponseRequest() # CreateInteractionResponseRequest | 
    with_response = True # bool |  (optional)

    try:
        api_response = await api_instance.create_interaction_response(interaction_id, interaction_token, create_interaction_response_request, with_response=with_response)
        print("The response of DefaultApi->create_interaction_response:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->create_interaction_response: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **interaction_id** | **str**|  | 
 **interaction_token** | **str**|  | 
 **create_interaction_response_request** | [**CreateInteractionResponseRequest**](CreateInteractionResponseRequest.md)|  | 
 **with_response** | **bool**|  | [optional] 

### Return type

[**InteractionCallbackResponse**](InteractionCallbackResponse.md)

### Authorization

[BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 response for create_interaction_response |  -  |
**204** | 204 response for create_interaction_response |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_lobby**
> LobbyResponse create_lobby(create_lobby_request)

### Example

* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.models.create_lobby_request import CreateLobbyRequest
from dc_rest.models.lobby_response import LobbyResponse
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    create_lobby_request = dc_rest.CreateLobbyRequest() # CreateLobbyRequest | 

    try:
        api_response = await api_instance.create_lobby(create_lobby_request)
        print("The response of DefaultApi->create_lobby:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->create_lobby: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_lobby_request** | [**CreateLobbyRequest**](CreateLobbyRequest.md)|  | 

### Return type

[**LobbyResponse**](LobbyResponse.md)

### Authorization

[BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | 201 response for create_lobby |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_lobby_message**
> LobbyMessageResponse create_lobby_message(lobby_id, sdk_message_request)

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):
* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.models.lobby_message_response import LobbyMessageResponse
from dc_rest.models.sdk_message_request import SDKMessageRequest
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    lobby_id = 'lobby_id_example' # str | 
    sdk_message_request = dc_rest.SDKMessageRequest() # SDKMessageRequest | 

    try:
        api_response = await api_instance.create_lobby_message(lobby_id, sdk_message_request)
        print("The response of DefaultApi->create_lobby_message:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->create_lobby_message: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lobby_id** | **str**|  | 
 **sdk_message_request** | [**SDKMessageRequest**](SDKMessageRequest.md)|  | 

### Return type

[**LobbyMessageResponse**](LobbyMessageResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | 201 response for create_lobby_message |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_message**
> MessageResponse create_message(channel_id, message_create_request)

### Example

* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.models.message_create_request import MessageCreateRequest
from dc_rest.models.message_response import MessageResponse
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    channel_id = 'channel_id_example' # str | 
    message_create_request = dc_rest.MessageCreateRequest() # MessageCreateRequest | 

    try:
        api_response = await api_instance.create_message(channel_id, message_create_request)
        print("The response of DefaultApi->create_message:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->create_message: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **str**|  | 
 **message_create_request** | [**MessageCreateRequest**](MessageCreateRequest.md)|  | 

### Return type

[**MessageResponse**](MessageResponse.md)

### Authorization

[BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 response for create_message |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_or_join_lobby**
> LobbyResponse create_or_join_lobby(create_or_join_lobby_request)

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):
* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.models.create_or_join_lobby_request import CreateOrJoinLobbyRequest
from dc_rest.models.lobby_response import LobbyResponse
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    create_or_join_lobby_request = dc_rest.CreateOrJoinLobbyRequest() # CreateOrJoinLobbyRequest | 

    try:
        api_response = await api_instance.create_or_join_lobby(create_or_join_lobby_request)
        print("The response of DefaultApi->create_or_join_lobby:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->create_or_join_lobby: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_or_join_lobby_request** | [**CreateOrJoinLobbyRequest**](CreateOrJoinLobbyRequest.md)|  | 

### Return type

[**LobbyResponse**](LobbyResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 response for create_or_join_lobby |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_pin**
> create_pin(channel_id, message_id)

### Example

* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    channel_id = 'channel_id_example' # str | 
    message_id = 'message_id_example' # str | 

    try:
        await api_instance.create_pin(channel_id, message_id)
    except Exception as e:
        print("Exception when calling DefaultApi->create_pin: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **str**|  | 
 **message_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | 204 response for create_pin |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_stage_instance**
> StageInstanceResponse create_stage_instance(create_stage_instance_request)

### Example

* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.models.create_stage_instance_request import CreateStageInstanceRequest
from dc_rest.models.stage_instance_response import StageInstanceResponse
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    create_stage_instance_request = dc_rest.CreateStageInstanceRequest() # CreateStageInstanceRequest | 

    try:
        api_response = await api_instance.create_stage_instance(create_stage_instance_request)
        print("The response of DefaultApi->create_stage_instance:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->create_stage_instance: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_stage_instance_request** | [**CreateStageInstanceRequest**](CreateStageInstanceRequest.md)|  | 

### Return type

[**StageInstanceResponse**](StageInstanceResponse.md)

### Authorization

[BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 response for create_stage_instance |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_thread**
> CreatedThreadResponse create_thread(channel_id, create_thread_request)

### Example

* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.models.create_thread_request import CreateThreadRequest
from dc_rest.models.created_thread_response import CreatedThreadResponse
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    channel_id = 'channel_id_example' # str | 
    create_thread_request = dc_rest.CreateThreadRequest() # CreateThreadRequest | 

    try:
        api_response = await api_instance.create_thread(channel_id, create_thread_request)
        print("The response of DefaultApi->create_thread:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->create_thread: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **str**|  | 
 **create_thread_request** | [**CreateThreadRequest**](CreateThreadRequest.md)|  | 

### Return type

[**CreatedThreadResponse**](CreatedThreadResponse.md)

### Authorization

[BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | 201 response for create_thread |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_thread_from_message**
> ThreadResponse create_thread_from_message(channel_id, message_id, create_text_thread_with_message_request)

### Example

* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.models.create_text_thread_with_message_request import CreateTextThreadWithMessageRequest
from dc_rest.models.thread_response import ThreadResponse
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    channel_id = 'channel_id_example' # str | 
    message_id = 'message_id_example' # str | 
    create_text_thread_with_message_request = dc_rest.CreateTextThreadWithMessageRequest() # CreateTextThreadWithMessageRequest | 

    try:
        api_response = await api_instance.create_thread_from_message(channel_id, message_id, create_text_thread_with_message_request)
        print("The response of DefaultApi->create_thread_from_message:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->create_thread_from_message: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **str**|  | 
 **message_id** | **str**|  | 
 **create_text_thread_with_message_request** | [**CreateTextThreadWithMessageRequest**](CreateTextThreadWithMessageRequest.md)|  | 

### Return type

[**ThreadResponse**](ThreadResponse.md)

### Authorization

[BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | 201 response for create_thread_from_message |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_webhook**
> GuildIncomingWebhookResponse create_webhook(channel_id, create_webhook_request)

### Example

* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.models.create_webhook_request import CreateWebhookRequest
from dc_rest.models.guild_incoming_webhook_response import GuildIncomingWebhookResponse
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    channel_id = 'channel_id_example' # str | 
    create_webhook_request = dc_rest.CreateWebhookRequest() # CreateWebhookRequest | 

    try:
        api_response = await api_instance.create_webhook(channel_id, create_webhook_request)
        print("The response of DefaultApi->create_webhook:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->create_webhook: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **str**|  | 
 **create_webhook_request** | [**CreateWebhookRequest**](CreateWebhookRequest.md)|  | 

### Return type

[**GuildIncomingWebhookResponse**](GuildIncomingWebhookResponse.md)

### Authorization

[BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 response for create_webhook |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **crosspost_message**
> MessageResponse crosspost_message(channel_id, message_id)

### Example

* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.models.message_response import MessageResponse
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    channel_id = 'channel_id_example' # str | 
    message_id = 'message_id_example' # str | 

    try:
        api_response = await api_instance.crosspost_message(channel_id, message_id)
        print("The response of DefaultApi->crosspost_message:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->crosspost_message: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **str**|  | 
 **message_id** | **str**|  | 

### Return type

[**MessageResponse**](MessageResponse.md)

### Authorization

[BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 response for crosspost_message |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_all_message_reactions**
> delete_all_message_reactions(channel_id, message_id)

### Example

* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    channel_id = 'channel_id_example' # str | 
    message_id = 'message_id_example' # str | 

    try:
        await api_instance.delete_all_message_reactions(channel_id, message_id)
    except Exception as e:
        print("Exception when calling DefaultApi->delete_all_message_reactions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **str**|  | 
 **message_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | 204 response for delete_all_message_reactions |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_all_message_reactions_by_emoji**
> delete_all_message_reactions_by_emoji(channel_id, message_id, emoji_name)

### Example

* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    channel_id = 'channel_id_example' # str | 
    message_id = 'message_id_example' # str | 
    emoji_name = 'emoji_name_example' # str | 

    try:
        await api_instance.delete_all_message_reactions_by_emoji(channel_id, message_id, emoji_name)
    except Exception as e:
        print("Exception when calling DefaultApi->delete_all_message_reactions_by_emoji: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **str**|  | 
 **message_id** | **str**|  | 
 **emoji_name** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | 204 response for delete_all_message_reactions_by_emoji |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_application_command**
> delete_application_command(application_id, command_id)

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):
* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    application_id = 'application_id_example' # str | 
    command_id = 'command_id_example' # str | 

    try:
        await api_instance.delete_application_command(application_id, command_id)
    except Exception as e:
        print("Exception when calling DefaultApi->delete_application_command: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **str**|  | 
 **command_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | 204 response for delete_application_command |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_application_emoji**
> delete_application_emoji(application_id, emoji_id)

### Example

* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    application_id = 'application_id_example' # str | 
    emoji_id = 'emoji_id_example' # str | 

    try:
        await api_instance.delete_application_emoji(application_id, emoji_id)
    except Exception as e:
        print("Exception when calling DefaultApi->delete_application_emoji: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **str**|  | 
 **emoji_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | 204 response for delete_application_emoji |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_application_user_role_connection**
> delete_application_user_role_connection(application_id)

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import dc_rest
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    application_id = 'application_id_example' # str | 

    try:
        await api_instance.delete_application_user_role_connection(application_id)
    except Exception as e:
        print("Exception when calling DefaultApi->delete_application_user_role_connection: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | 204 response for delete_application_user_role_connection |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_auto_moderation_rule**
> delete_auto_moderation_rule(guild_id, rule_id)

### Example

* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    guild_id = 'guild_id_example' # str | 
    rule_id = 'rule_id_example' # str | 

    try:
        await api_instance.delete_auto_moderation_rule(guild_id, rule_id)
    except Exception as e:
        print("Exception when calling DefaultApi->delete_auto_moderation_rule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guild_id** | **str**|  | 
 **rule_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | 204 response for delete_auto_moderation_rule |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_channel**
> GetChannel200Response delete_channel(channel_id)

### Example

* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.models.get_channel200_response import GetChannel200Response
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    channel_id = 'channel_id_example' # str | 

    try:
        api_response = await api_instance.delete_channel(channel_id)
        print("The response of DefaultApi->delete_channel:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->delete_channel: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **str**|  | 

### Return type

[**GetChannel200Response**](GetChannel200Response.md)

### Authorization

[BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 response for delete_channel |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_channel_permission_overwrite**
> delete_channel_permission_overwrite(channel_id, overwrite_id)

### Example

* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    channel_id = 'channel_id_example' # str | 
    overwrite_id = 'overwrite_id_example' # str | 

    try:
        await api_instance.delete_channel_permission_overwrite(channel_id, overwrite_id)
    except Exception as e:
        print("Exception when calling DefaultApi->delete_channel_permission_overwrite: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **str**|  | 
 **overwrite_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | 204 response for delete_channel_permission_overwrite |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_entitlement**
> delete_entitlement(application_id, entitlement_id)

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):
* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    application_id = 'application_id_example' # str | 
    entitlement_id = 'entitlement_id_example' # str | 

    try:
        await api_instance.delete_entitlement(application_id, entitlement_id)
    except Exception as e:
        print("Exception when calling DefaultApi->delete_entitlement: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **str**|  | 
 **entitlement_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | 204 response for delete_entitlement |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_group_dm_user**
> delete_group_dm_user(channel_id, user_id)

### Example

* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    channel_id = 'channel_id_example' # str | 
    user_id = 'user_id_example' # str | 

    try:
        await api_instance.delete_group_dm_user(channel_id, user_id)
    except Exception as e:
        print("Exception when calling DefaultApi->delete_group_dm_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | 204 response for delete_group_dm_user |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_guild**
> delete_guild(guild_id)

### Example

* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    guild_id = 'guild_id_example' # str | 

    try:
        await api_instance.delete_guild(guild_id)
    except Exception as e:
        print("Exception when calling DefaultApi->delete_guild: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guild_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | 204 response for delete_guild |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_guild_application_command**
> delete_guild_application_command(application_id, guild_id, command_id)

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):
* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    application_id = 'application_id_example' # str | 
    guild_id = 'guild_id_example' # str | 
    command_id = 'command_id_example' # str | 

    try:
        await api_instance.delete_guild_application_command(application_id, guild_id, command_id)
    except Exception as e:
        print("Exception when calling DefaultApi->delete_guild_application_command: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **str**|  | 
 **guild_id** | **str**|  | 
 **command_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | 204 response for delete_guild_application_command |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_guild_emoji**
> delete_guild_emoji(guild_id, emoji_id)

### Example

* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    guild_id = 'guild_id_example' # str | 
    emoji_id = 'emoji_id_example' # str | 

    try:
        await api_instance.delete_guild_emoji(guild_id, emoji_id)
    except Exception as e:
        print("Exception when calling DefaultApi->delete_guild_emoji: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guild_id** | **str**|  | 
 **emoji_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | 204 response for delete_guild_emoji |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_guild_integration**
> delete_guild_integration(guild_id, integration_id)

### Example

* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    guild_id = 'guild_id_example' # str | 
    integration_id = 'integration_id_example' # str | 

    try:
        await api_instance.delete_guild_integration(guild_id, integration_id)
    except Exception as e:
        print("Exception when calling DefaultApi->delete_guild_integration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guild_id** | **str**|  | 
 **integration_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | 204 response for delete_guild_integration |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_guild_member**
> delete_guild_member(guild_id, user_id)

### Example

* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    guild_id = 'guild_id_example' # str | 
    user_id = 'user_id_example' # str | 

    try:
        await api_instance.delete_guild_member(guild_id, user_id)
    except Exception as e:
        print("Exception when calling DefaultApi->delete_guild_member: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guild_id** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | 204 response for delete_guild_member |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_guild_member_role**
> delete_guild_member_role(guild_id, user_id, role_id)

### Example

* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    guild_id = 'guild_id_example' # str | 
    user_id = 'user_id_example' # str | 
    role_id = 'role_id_example' # str | 

    try:
        await api_instance.delete_guild_member_role(guild_id, user_id, role_id)
    except Exception as e:
        print("Exception when calling DefaultApi->delete_guild_member_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guild_id** | **str**|  | 
 **user_id** | **str**|  | 
 **role_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | 204 response for delete_guild_member_role |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_guild_role**
> delete_guild_role(guild_id, role_id)

### Example

* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    guild_id = 'guild_id_example' # str | 
    role_id = 'role_id_example' # str | 

    try:
        await api_instance.delete_guild_role(guild_id, role_id)
    except Exception as e:
        print("Exception when calling DefaultApi->delete_guild_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guild_id** | **str**|  | 
 **role_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | 204 response for delete_guild_role |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_guild_scheduled_event**
> delete_guild_scheduled_event(guild_id, guild_scheduled_event_id)

### Example

* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    guild_id = 'guild_id_example' # str | 
    guild_scheduled_event_id = 'guild_scheduled_event_id_example' # str | 

    try:
        await api_instance.delete_guild_scheduled_event(guild_id, guild_scheduled_event_id)
    except Exception as e:
        print("Exception when calling DefaultApi->delete_guild_scheduled_event: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guild_id** | **str**|  | 
 **guild_scheduled_event_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | 204 response for delete_guild_scheduled_event |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_guild_soundboard_sound**
> delete_guild_soundboard_sound(guild_id, sound_id)

### Example

* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    guild_id = 'guild_id_example' # str | 
    sound_id = 'sound_id_example' # str | 

    try:
        await api_instance.delete_guild_soundboard_sound(guild_id, sound_id)
    except Exception as e:
        print("Exception when calling DefaultApi->delete_guild_soundboard_sound: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guild_id** | **str**|  | 
 **sound_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | 204 response for delete_guild_soundboard_sound |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_guild_sticker**
> delete_guild_sticker(guild_id, sticker_id)

### Example

* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    guild_id = 'guild_id_example' # str | 
    sticker_id = 'sticker_id_example' # str | 

    try:
        await api_instance.delete_guild_sticker(guild_id, sticker_id)
    except Exception as e:
        print("Exception when calling DefaultApi->delete_guild_sticker: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guild_id** | **str**|  | 
 **sticker_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | 204 response for delete_guild_sticker |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_guild_template**
> GuildTemplateResponse delete_guild_template(guild_id, code)

### Example

* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.models.guild_template_response import GuildTemplateResponse
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    guild_id = 'guild_id_example' # str | 
    code = 'code_example' # str | 

    try:
        api_response = await api_instance.delete_guild_template(guild_id, code)
        print("The response of DefaultApi->delete_guild_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->delete_guild_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guild_id** | **str**|  | 
 **code** | **str**|  | 

### Return type

[**GuildTemplateResponse**](GuildTemplateResponse.md)

### Authorization

[BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 response for delete_guild_template |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_lobby_member**
> delete_lobby_member(lobby_id, user_id)

### Example

* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    lobby_id = 'lobby_id_example' # str | 
    user_id = 'user_id_example' # str | 

    try:
        await api_instance.delete_lobby_member(lobby_id, user_id)
    except Exception as e:
        print("Exception when calling DefaultApi->delete_lobby_member: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lobby_id** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | 204 response for delete_lobby_member |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_message**
> delete_message(channel_id, message_id)

### Example

* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    channel_id = 'channel_id_example' # str | 
    message_id = 'message_id_example' # str | 

    try:
        await api_instance.delete_message(channel_id, message_id)
    except Exception as e:
        print("Exception when calling DefaultApi->delete_message: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **str**|  | 
 **message_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | 204 response for delete_message |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_my_message_reaction**
> delete_my_message_reaction(channel_id, message_id, emoji_name)

### Example

* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    channel_id = 'channel_id_example' # str | 
    message_id = 'message_id_example' # str | 
    emoji_name = 'emoji_name_example' # str | 

    try:
        await api_instance.delete_my_message_reaction(channel_id, message_id, emoji_name)
    except Exception as e:
        print("Exception when calling DefaultApi->delete_my_message_reaction: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **str**|  | 
 **message_id** | **str**|  | 
 **emoji_name** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | 204 response for delete_my_message_reaction |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_original_webhook_message**
> delete_original_webhook_message(webhook_id, webhook_token, thread_id=thread_id)

### Example

* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    webhook_id = 'webhook_id_example' # str | 
    webhook_token = 'webhook_token_example' # str | 
    thread_id = 'thread_id_example' # str |  (optional)

    try:
        await api_instance.delete_original_webhook_message(webhook_id, webhook_token, thread_id=thread_id)
    except Exception as e:
        print("Exception when calling DefaultApi->delete_original_webhook_message: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhook_id** | **str**|  | 
 **webhook_token** | **str**|  | 
 **thread_id** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | 204 response for delete_original_webhook_message |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_pin**
> delete_pin(channel_id, message_id)

### Example

* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    channel_id = 'channel_id_example' # str | 
    message_id = 'message_id_example' # str | 

    try:
        await api_instance.delete_pin(channel_id, message_id)
    except Exception as e:
        print("Exception when calling DefaultApi->delete_pin: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **str**|  | 
 **message_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | 204 response for delete_pin |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_stage_instance**
> delete_stage_instance(channel_id)

### Example

* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    channel_id = 'channel_id_example' # str | 

    try:
        await api_instance.delete_stage_instance(channel_id)
    except Exception as e:
        print("Exception when calling DefaultApi->delete_stage_instance: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | 204 response for delete_stage_instance |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_thread_member**
> delete_thread_member(channel_id, user_id)

### Example

* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    channel_id = 'channel_id_example' # str | 
    user_id = 'user_id_example' # str | 

    try:
        await api_instance.delete_thread_member(channel_id, user_id)
    except Exception as e:
        print("Exception when calling DefaultApi->delete_thread_member: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | 204 response for delete_thread_member |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user_message_reaction**
> delete_user_message_reaction(channel_id, message_id, emoji_name, user_id)

### Example

* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    channel_id = 'channel_id_example' # str | 
    message_id = 'message_id_example' # str | 
    emoji_name = 'emoji_name_example' # str | 
    user_id = 'user_id_example' # str | 

    try:
        await api_instance.delete_user_message_reaction(channel_id, message_id, emoji_name, user_id)
    except Exception as e:
        print("Exception when calling DefaultApi->delete_user_message_reaction: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **str**|  | 
 **message_id** | **str**|  | 
 **emoji_name** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | 204 response for delete_user_message_reaction |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_webhook**
> delete_webhook(webhook_id)

### Example

* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    webhook_id = 'webhook_id_example' # str | 

    try:
        await api_instance.delete_webhook(webhook_id)
    except Exception as e:
        print("Exception when calling DefaultApi->delete_webhook: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhook_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | 204 response for delete_webhook |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_webhook_by_token**
> delete_webhook_by_token(webhook_id, webhook_token)

### Example

* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    webhook_id = 'webhook_id_example' # str | 
    webhook_token = 'webhook_token_example' # str | 

    try:
        await api_instance.delete_webhook_by_token(webhook_id, webhook_token)
    except Exception as e:
        print("Exception when calling DefaultApi->delete_webhook_by_token: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhook_id** | **str**|  | 
 **webhook_token** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | 204 response for delete_webhook_by_token |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_webhook_message**
> delete_webhook_message(webhook_id, webhook_token, message_id, thread_id=thread_id)

### Example

* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    webhook_id = 'webhook_id_example' # str | 
    webhook_token = 'webhook_token_example' # str | 
    message_id = 'message_id_example' # str | 
    thread_id = 'thread_id_example' # str |  (optional)

    try:
        await api_instance.delete_webhook_message(webhook_id, webhook_token, message_id, thread_id=thread_id)
    except Exception as e:
        print("Exception when calling DefaultApi->delete_webhook_message: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhook_id** | **str**|  | 
 **webhook_token** | **str**|  | 
 **message_id** | **str**|  | 
 **thread_id** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | 204 response for delete_webhook_message |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deprecated_create_pin**
> deprecated_create_pin(channel_id, message_id)

### Example

* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    channel_id = 'channel_id_example' # str | 
    message_id = 'message_id_example' # str | 

    try:
        await api_instance.deprecated_create_pin(channel_id, message_id)
    except Exception as e:
        print("Exception when calling DefaultApi->deprecated_create_pin: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **str**|  | 
 **message_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | 204 response for deprecated_create_pin |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deprecated_delete_pin**
> deprecated_delete_pin(channel_id, message_id)

### Example

* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    channel_id = 'channel_id_example' # str | 
    message_id = 'message_id_example' # str | 

    try:
        await api_instance.deprecated_delete_pin(channel_id, message_id)
    except Exception as e:
        print("Exception when calling DefaultApi->deprecated_delete_pin: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **str**|  | 
 **message_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | 204 response for deprecated_delete_pin |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deprecated_list_pins**
> List[MessageResponse] deprecated_list_pins(channel_id)

### Example

* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.models.message_response import MessageResponse
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    channel_id = 'channel_id_example' # str | 

    try:
        api_response = await api_instance.deprecated_list_pins(channel_id)
        print("The response of DefaultApi->deprecated_list_pins:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->deprecated_list_pins: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **str**|  | 

### Return type

[**List[MessageResponse]**](MessageResponse.md)

### Authorization

[BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 response for deprecated_list_pins |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_lobby**
> LobbyResponse edit_lobby(lobby_id, create_lobby_request)

### Example

* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.models.create_lobby_request import CreateLobbyRequest
from dc_rest.models.lobby_response import LobbyResponse
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    lobby_id = 'lobby_id_example' # str | 
    create_lobby_request = dc_rest.CreateLobbyRequest() # CreateLobbyRequest | 

    try:
        api_response = await api_instance.edit_lobby(lobby_id, create_lobby_request)
        print("The response of DefaultApi->edit_lobby:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->edit_lobby: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lobby_id** | **str**|  | 
 **create_lobby_request** | [**CreateLobbyRequest**](CreateLobbyRequest.md)|  | 

### Return type

[**LobbyResponse**](LobbyResponse.md)

### Authorization

[BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 response for edit_lobby |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_lobby_channel_link**
> LobbyResponse edit_lobby_channel_link(lobby_id, edit_lobby_channel_link_request)

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):
* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.models.edit_lobby_channel_link_request import EditLobbyChannelLinkRequest
from dc_rest.models.lobby_response import LobbyResponse
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    lobby_id = 'lobby_id_example' # str | 
    edit_lobby_channel_link_request = dc_rest.EditLobbyChannelLinkRequest() # EditLobbyChannelLinkRequest | 

    try:
        api_response = await api_instance.edit_lobby_channel_link(lobby_id, edit_lobby_channel_link_request)
        print("The response of DefaultApi->edit_lobby_channel_link:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->edit_lobby_channel_link: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lobby_id** | **str**|  | 
 **edit_lobby_channel_link_request** | [**EditLobbyChannelLinkRequest**](EditLobbyChannelLinkRequest.md)|  | 

### Return type

[**LobbyResponse**](LobbyResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 response for edit_lobby_channel_link |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **execute_github_compatible_webhook**
> execute_github_compatible_webhook(webhook_id, webhook_token, github_webhook, wait=wait, thread_id=thread_id)

### Example

* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.models.github_webhook import GithubWebhook
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    webhook_id = 'webhook_id_example' # str | 
    webhook_token = 'webhook_token_example' # str | 
    github_webhook = dc_rest.GithubWebhook() # GithubWebhook | 
    wait = True # bool |  (optional)
    thread_id = 'thread_id_example' # str |  (optional)

    try:
        await api_instance.execute_github_compatible_webhook(webhook_id, webhook_token, github_webhook, wait=wait, thread_id=thread_id)
    except Exception as e:
        print("Exception when calling DefaultApi->execute_github_compatible_webhook: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhook_id** | **str**|  | 
 **webhook_token** | **str**|  | 
 **github_webhook** | [**GithubWebhook**](GithubWebhook.md)|  | 
 **wait** | **bool**|  | [optional] 
 **thread_id** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | 204 response for execute_github_compatible_webhook |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **execute_slack_compatible_webhook**
> str execute_slack_compatible_webhook(webhook_id, webhook_token, slack_webhook, wait=wait, thread_id=thread_id)

### Example

* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.models.slack_webhook import SlackWebhook
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    webhook_id = 'webhook_id_example' # str | 
    webhook_token = 'webhook_token_example' # str | 
    slack_webhook = dc_rest.SlackWebhook() # SlackWebhook | 
    wait = True # bool |  (optional)
    thread_id = 'thread_id_example' # str |  (optional)

    try:
        api_response = await api_instance.execute_slack_compatible_webhook(webhook_id, webhook_token, slack_webhook, wait=wait, thread_id=thread_id)
        print("The response of DefaultApi->execute_slack_compatible_webhook:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->execute_slack_compatible_webhook: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhook_id** | **str**|  | 
 **webhook_token** | **str**|  | 
 **slack_webhook** | [**SlackWebhook**](SlackWebhook.md)|  | 
 **wait** | **bool**|  | [optional] 
 **thread_id** | **str**|  | [optional] 

### Return type

**str**

### Authorization

[BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 response for execute_slack_compatible_webhook |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **execute_webhook**
> MessageResponse execute_webhook(webhook_id, webhook_token, execute_webhook_request, wait=wait, thread_id=thread_id, with_components=with_components)

### Example

* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.models.execute_webhook_request import ExecuteWebhookRequest
from dc_rest.models.message_response import MessageResponse
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    webhook_id = 'webhook_id_example' # str | 
    webhook_token = 'webhook_token_example' # str | 
    execute_webhook_request = dc_rest.ExecuteWebhookRequest() # ExecuteWebhookRequest | 
    wait = True # bool |  (optional)
    thread_id = 'thread_id_example' # str |  (optional)
    with_components = True # bool |  (optional)

    try:
        api_response = await api_instance.execute_webhook(webhook_id, webhook_token, execute_webhook_request, wait=wait, thread_id=thread_id, with_components=with_components)
        print("The response of DefaultApi->execute_webhook:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->execute_webhook: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhook_id** | **str**|  | 
 **webhook_token** | **str**|  | 
 **execute_webhook_request** | [**ExecuteWebhookRequest**](ExecuteWebhookRequest.md)|  | 
 **wait** | **bool**|  | [optional] 
 **thread_id** | **str**|  | [optional] 
 **with_components** | **bool**|  | [optional] 

### Return type

[**MessageResponse**](MessageResponse.md)

### Authorization

[BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 response for execute_webhook |  -  |
**204** | 204 response for execute_webhook |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **follow_channel**
> ChannelFollowerResponse follow_channel(channel_id, follow_channel_request)

### Example

* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.models.channel_follower_response import ChannelFollowerResponse
from dc_rest.models.follow_channel_request import FollowChannelRequest
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    channel_id = 'channel_id_example' # str | 
    follow_channel_request = dc_rest.FollowChannelRequest() # FollowChannelRequest | 

    try:
        api_response = await api_instance.follow_channel(channel_id, follow_channel_request)
        print("The response of DefaultApi->follow_channel:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->follow_channel: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **str**|  | 
 **follow_channel_request** | [**FollowChannelRequest**](FollowChannelRequest.md)|  | 

### Return type

[**ChannelFollowerResponse**](ChannelFollowerResponse.md)

### Authorization

[BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 response for follow_channel |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_active_guild_threads**
> ThreadsResponse get_active_guild_threads(guild_id)

### Example

* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.models.threads_response import ThreadsResponse
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    guild_id = 'guild_id_example' # str | 

    try:
        api_response = await api_instance.get_active_guild_threads(guild_id)
        print("The response of DefaultApi->get_active_guild_threads:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_active_guild_threads: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guild_id** | **str**|  | 

### Return type

[**ThreadsResponse**](ThreadsResponse.md)

### Authorization

[BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 response for get_active_guild_threads |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_answer_voters**
> PollAnswerDetailsResponse get_answer_voters(channel_id, message_id, answer_id, after=after, limit=limit)

### Example

* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.models.poll_answer_details_response import PollAnswerDetailsResponse
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    channel_id = 'channel_id_example' # str | 
    message_id = 'message_id_example' # str | 
    answer_id = 56 # int | 
    after = 'after_example' # str |  (optional)
    limit = 56 # int |  (optional)

    try:
        api_response = await api_instance.get_answer_voters(channel_id, message_id, answer_id, after=after, limit=limit)
        print("The response of DefaultApi->get_answer_voters:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_answer_voters: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **str**|  | 
 **message_id** | **str**|  | 
 **answer_id** | **int**|  | 
 **after** | **str**|  | [optional] 
 **limit** | **int**|  | [optional] 

### Return type

[**PollAnswerDetailsResponse**](PollAnswerDetailsResponse.md)

### Authorization

[BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 response for get_answer_voters |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_application**
> PrivateApplicationResponse get_application(application_id)

### Example

* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.models.private_application_response import PrivateApplicationResponse
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    application_id = 'application_id_example' # str | 

    try:
        api_response = await api_instance.get_application(application_id)
        print("The response of DefaultApi->get_application:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_application: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **str**|  | 

### Return type

[**PrivateApplicationResponse**](PrivateApplicationResponse.md)

### Authorization

[BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 response for get_application |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_application_command**
> ApplicationCommandResponse get_application_command(application_id, command_id)

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):
* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.models.application_command_response import ApplicationCommandResponse
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    application_id = 'application_id_example' # str | 
    command_id = 'command_id_example' # str | 

    try:
        api_response = await api_instance.get_application_command(application_id, command_id)
        print("The response of DefaultApi->get_application_command:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_application_command: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **str**|  | 
 **command_id** | **str**|  | 

### Return type

[**ApplicationCommandResponse**](ApplicationCommandResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 response for get_application_command |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_application_emoji**
> EmojiResponse get_application_emoji(application_id, emoji_id)

### Example

* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.models.emoji_response import EmojiResponse
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    application_id = 'application_id_example' # str | 
    emoji_id = 'emoji_id_example' # str | 

    try:
        api_response = await api_instance.get_application_emoji(application_id, emoji_id)
        print("The response of DefaultApi->get_application_emoji:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_application_emoji: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **str**|  | 
 **emoji_id** | **str**|  | 

### Return type

[**EmojiResponse**](EmojiResponse.md)

### Authorization

[BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 response for get_application_emoji |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_application_role_connections_metadata**
> List[ApplicationRoleConnectionsMetadataItemResponse] get_application_role_connections_metadata(application_id)

### Example

* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.models.application_role_connections_metadata_item_response import ApplicationRoleConnectionsMetadataItemResponse
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    application_id = 'application_id_example' # str | 

    try:
        api_response = await api_instance.get_application_role_connections_metadata(application_id)
        print("The response of DefaultApi->get_application_role_connections_metadata:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_application_role_connections_metadata: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **str**|  | 

### Return type

[**List[ApplicationRoleConnectionsMetadataItemResponse]**](ApplicationRoleConnectionsMetadataItemResponse.md)

### Authorization

[BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 response for get_application_role_connections_metadata |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_application_user_role_connection**
> ApplicationUserRoleConnectionResponse get_application_user_role_connection(application_id)

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import dc_rest
from dc_rest.models.application_user_role_connection_response import ApplicationUserRoleConnectionResponse
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    application_id = 'application_id_example' # str | 

    try:
        api_response = await api_instance.get_application_user_role_connection(application_id)
        print("The response of DefaultApi->get_application_user_role_connection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_application_user_role_connection: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **str**|  | 

### Return type

[**ApplicationUserRoleConnectionResponse**](ApplicationUserRoleConnectionResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 response for get_application_user_role_connection |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_auto_moderation_rule**
> CreateAutoModerationRule200Response get_auto_moderation_rule(guild_id, rule_id)

### Example

* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.models.create_auto_moderation_rule200_response import CreateAutoModerationRule200Response
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    guild_id = 'guild_id_example' # str | 
    rule_id = 'rule_id_example' # str | 

    try:
        api_response = await api_instance.get_auto_moderation_rule(guild_id, rule_id)
        print("The response of DefaultApi->get_auto_moderation_rule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_auto_moderation_rule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guild_id** | **str**|  | 
 **rule_id** | **str**|  | 

### Return type

[**CreateAutoModerationRule200Response**](CreateAutoModerationRule200Response.md)

### Authorization

[BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 response for get_auto_moderation_rule |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bot_gateway**
> GatewayBotResponse get_bot_gateway()

### Example

* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.models.gateway_bot_response import GatewayBotResponse
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)

    try:
        api_response = await api_instance.get_bot_gateway()
        print("The response of DefaultApi->get_bot_gateway:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_bot_gateway: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GatewayBotResponse**](GatewayBotResponse.md)

### Authorization

[BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 response for get_bot_gateway |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_channel**
> GetChannel200Response get_channel(channel_id)

### Example

* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.models.get_channel200_response import GetChannel200Response
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    channel_id = 'channel_id_example' # str | 

    try:
        api_response = await api_instance.get_channel(channel_id)
        print("The response of DefaultApi->get_channel:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_channel: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **str**|  | 

### Return type

[**GetChannel200Response**](GetChannel200Response.md)

### Authorization

[BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 response for get_channel |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_entitlement**
> EntitlementResponse get_entitlement(application_id, entitlement_id)

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):
* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.models.entitlement_response import EntitlementResponse
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    application_id = 'application_id_example' # str | 
    entitlement_id = 'entitlement_id_example' # str | 

    try:
        api_response = await api_instance.get_entitlement(application_id, entitlement_id)
        print("The response of DefaultApi->get_entitlement:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_entitlement: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **str**|  | 
 **entitlement_id** | **str**|  | 

### Return type

[**EntitlementResponse**](EntitlementResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 response for get_entitlement |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_entitlements**
> List[Optional[EntitlementResponse]] get_entitlements(sku_ids, application_id, user_id=user_id, guild_id=guild_id, before=before, after=after, limit=limit, exclude_ended=exclude_ended, exclude_deleted=exclude_deleted, only_active=only_active)

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):
* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.models.entitlement_response import EntitlementResponse
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    sku_ids = dc_rest.GetEntitlementsSkuIdsParameter() # GetEntitlementsSkuIdsParameter | 
    application_id = 'application_id_example' # str | 
    user_id = 'user_id_example' # str |  (optional)
    guild_id = 'guild_id_example' # str |  (optional)
    before = 'before_example' # str |  (optional)
    after = 'after_example' # str |  (optional)
    limit = 56 # int |  (optional)
    exclude_ended = True # bool |  (optional)
    exclude_deleted = True # bool |  (optional)
    only_active = True # bool |  (optional)

    try:
        api_response = await api_instance.get_entitlements(sku_ids, application_id, user_id=user_id, guild_id=guild_id, before=before, after=after, limit=limit, exclude_ended=exclude_ended, exclude_deleted=exclude_deleted, only_active=only_active)
        print("The response of DefaultApi->get_entitlements:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_entitlements: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sku_ids** | [**GetEntitlementsSkuIdsParameter**](.md)|  | 
 **application_id** | **str**|  | 
 **user_id** | **str**|  | [optional] 
 **guild_id** | **str**|  | [optional] 
 **before** | **str**|  | [optional] 
 **after** | **str**|  | [optional] 
 **limit** | **int**|  | [optional] 
 **exclude_ended** | **bool**|  | [optional] 
 **exclude_deleted** | **bool**|  | [optional] 
 **only_active** | **bool**|  | [optional] 

### Return type

[**List[Optional[EntitlementResponse]]**](EntitlementResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 response for get_entitlements |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_gateway**
> GatewayResponse get_gateway()

### Example

* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.models.gateway_response import GatewayResponse
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)

    try:
        api_response = await api_instance.get_gateway()
        print("The response of DefaultApi->get_gateway:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_gateway: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GatewayResponse**](GatewayResponse.md)

### Authorization

[BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 response for get_gateway |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_guild**
> GuildWithCountsResponse get_guild(guild_id, with_counts=with_counts)

### Example

* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.models.guild_with_counts_response import GuildWithCountsResponse
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    guild_id = 'guild_id_example' # str | 
    with_counts = True # bool |  (optional)

    try:
        api_response = await api_instance.get_guild(guild_id, with_counts=with_counts)
        print("The response of DefaultApi->get_guild:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_guild: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guild_id** | **str**|  | 
 **with_counts** | **bool**|  | [optional] 

### Return type

[**GuildWithCountsResponse**](GuildWithCountsResponse.md)

### Authorization

[BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 response for get_guild |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_guild_application_command**
> ApplicationCommandResponse get_guild_application_command(application_id, guild_id, command_id)

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):
* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.models.application_command_response import ApplicationCommandResponse
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    application_id = 'application_id_example' # str | 
    guild_id = 'guild_id_example' # str | 
    command_id = 'command_id_example' # str | 

    try:
        api_response = await api_instance.get_guild_application_command(application_id, guild_id, command_id)
        print("The response of DefaultApi->get_guild_application_command:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_guild_application_command: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **str**|  | 
 **guild_id** | **str**|  | 
 **command_id** | **str**|  | 

### Return type

[**ApplicationCommandResponse**](ApplicationCommandResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 response for get_guild_application_command |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_guild_application_command_permissions**
> CommandPermissionsResponse get_guild_application_command_permissions(application_id, guild_id, command_id)

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):
* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.models.command_permissions_response import CommandPermissionsResponse
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    application_id = 'application_id_example' # str | 
    guild_id = 'guild_id_example' # str | 
    command_id = 'command_id_example' # str | 

    try:
        api_response = await api_instance.get_guild_application_command_permissions(application_id, guild_id, command_id)
        print("The response of DefaultApi->get_guild_application_command_permissions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_guild_application_command_permissions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **str**|  | 
 **guild_id** | **str**|  | 
 **command_id** | **str**|  | 

### Return type

[**CommandPermissionsResponse**](CommandPermissionsResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 response for get_guild_application_command_permissions |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_guild_ban**
> GuildBanResponse get_guild_ban(guild_id, user_id)

### Example

* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.models.guild_ban_response import GuildBanResponse
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    guild_id = 'guild_id_example' # str | 
    user_id = 'user_id_example' # str | 

    try:
        api_response = await api_instance.get_guild_ban(guild_id, user_id)
        print("The response of DefaultApi->get_guild_ban:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_guild_ban: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guild_id** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

[**GuildBanResponse**](GuildBanResponse.md)

### Authorization

[BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 response for get_guild_ban |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_guild_emoji**
> EmojiResponse get_guild_emoji(guild_id, emoji_id)

### Example

* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.models.emoji_response import EmojiResponse
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    guild_id = 'guild_id_example' # str | 
    emoji_id = 'emoji_id_example' # str | 

    try:
        api_response = await api_instance.get_guild_emoji(guild_id, emoji_id)
        print("The response of DefaultApi->get_guild_emoji:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_guild_emoji: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guild_id** | **str**|  | 
 **emoji_id** | **str**|  | 

### Return type

[**EmojiResponse**](EmojiResponse.md)

### Authorization

[BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 response for get_guild_emoji |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_guild_member**
> GuildMemberResponse get_guild_member(guild_id, user_id)

### Example

* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.models.guild_member_response import GuildMemberResponse
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    guild_id = 'guild_id_example' # str | 
    user_id = 'user_id_example' # str | 

    try:
        api_response = await api_instance.get_guild_member(guild_id, user_id)
        print("The response of DefaultApi->get_guild_member:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_guild_member: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guild_id** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

[**GuildMemberResponse**](GuildMemberResponse.md)

### Authorization

[BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 response for get_guild_member |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_guild_new_member_welcome**
> GuildHomeSettingsResponse get_guild_new_member_welcome(guild_id)

### Example

* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.models.guild_home_settings_response import GuildHomeSettingsResponse
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    guild_id = 'guild_id_example' # str | 

    try:
        api_response = await api_instance.get_guild_new_member_welcome(guild_id)
        print("The response of DefaultApi->get_guild_new_member_welcome:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_guild_new_member_welcome: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guild_id** | **str**|  | 

### Return type

[**GuildHomeSettingsResponse**](GuildHomeSettingsResponse.md)

### Authorization

[BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 response for get_guild_new_member_welcome |  -  |
**204** | 204 response for get_guild_new_member_welcome |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_guild_preview**
> GuildPreviewResponse get_guild_preview(guild_id)

### Example

* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.models.guild_preview_response import GuildPreviewResponse
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    guild_id = 'guild_id_example' # str | 

    try:
        api_response = await api_instance.get_guild_preview(guild_id)
        print("The response of DefaultApi->get_guild_preview:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_guild_preview: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guild_id** | **str**|  | 

### Return type

[**GuildPreviewResponse**](GuildPreviewResponse.md)

### Authorization

[BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 response for get_guild_preview |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_guild_role**
> GuildRoleResponse get_guild_role(guild_id, role_id)

### Example

* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.models.guild_role_response import GuildRoleResponse
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    guild_id = 'guild_id_example' # str | 
    role_id = 'role_id_example' # str | 

    try:
        api_response = await api_instance.get_guild_role(guild_id, role_id)
        print("The response of DefaultApi->get_guild_role:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_guild_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guild_id** | **str**|  | 
 **role_id** | **str**|  | 

### Return type

[**GuildRoleResponse**](GuildRoleResponse.md)

### Authorization

[BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 response for get_guild_role |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_guild_scheduled_event**
> ListGuildScheduledEvents200ResponseInner get_guild_scheduled_event(guild_id, guild_scheduled_event_id, with_user_count=with_user_count)

### Example

* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.models.list_guild_scheduled_events200_response_inner import ListGuildScheduledEvents200ResponseInner
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    guild_id = 'guild_id_example' # str | 
    guild_scheduled_event_id = 'guild_scheduled_event_id_example' # str | 
    with_user_count = True # bool |  (optional)

    try:
        api_response = await api_instance.get_guild_scheduled_event(guild_id, guild_scheduled_event_id, with_user_count=with_user_count)
        print("The response of DefaultApi->get_guild_scheduled_event:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_guild_scheduled_event: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guild_id** | **str**|  | 
 **guild_scheduled_event_id** | **str**|  | 
 **with_user_count** | **bool**|  | [optional] 

### Return type

[**ListGuildScheduledEvents200ResponseInner**](ListGuildScheduledEvents200ResponseInner.md)

### Authorization

[BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 response for get_guild_scheduled_event |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_guild_soundboard_sound**
> SoundboardSoundResponse get_guild_soundboard_sound(guild_id, sound_id)

### Example

* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.models.soundboard_sound_response import SoundboardSoundResponse
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    guild_id = 'guild_id_example' # str | 
    sound_id = 'sound_id_example' # str | 

    try:
        api_response = await api_instance.get_guild_soundboard_sound(guild_id, sound_id)
        print("The response of DefaultApi->get_guild_soundboard_sound:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_guild_soundboard_sound: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guild_id** | **str**|  | 
 **sound_id** | **str**|  | 

### Return type

[**SoundboardSoundResponse**](SoundboardSoundResponse.md)

### Authorization

[BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 response for get_guild_soundboard_sound |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_guild_sticker**
> GuildStickerResponse get_guild_sticker(guild_id, sticker_id)

### Example

* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.models.guild_sticker_response import GuildStickerResponse
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    guild_id = 'guild_id_example' # str | 
    sticker_id = 'sticker_id_example' # str | 

    try:
        api_response = await api_instance.get_guild_sticker(guild_id, sticker_id)
        print("The response of DefaultApi->get_guild_sticker:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_guild_sticker: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guild_id** | **str**|  | 
 **sticker_id** | **str**|  | 

### Return type

[**GuildStickerResponse**](GuildStickerResponse.md)

### Authorization

[BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 response for get_guild_sticker |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_guild_template**
> GuildTemplateResponse get_guild_template(code)

### Example

* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.models.guild_template_response import GuildTemplateResponse
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    code = 'code_example' # str | 

    try:
        api_response = await api_instance.get_guild_template(code)
        print("The response of DefaultApi->get_guild_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_guild_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**|  | 

### Return type

[**GuildTemplateResponse**](GuildTemplateResponse.md)

### Authorization

[BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 response for get_guild_template |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_guild_vanity_url**
> VanityURLResponse get_guild_vanity_url(guild_id)

### Example

* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.models.vanity_url_response import VanityURLResponse
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    guild_id = 'guild_id_example' # str | 

    try:
        api_response = await api_instance.get_guild_vanity_url(guild_id)
        print("The response of DefaultApi->get_guild_vanity_url:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_guild_vanity_url: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guild_id** | **str**|  | 

### Return type

[**VanityURLResponse**](VanityURLResponse.md)

### Authorization

[BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 response for get_guild_vanity_url |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_guild_webhooks**
> List[ListChannelWebhooks200ResponseInner] get_guild_webhooks(guild_id)

### Example

* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.models.list_channel_webhooks200_response_inner import ListChannelWebhooks200ResponseInner
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    guild_id = 'guild_id_example' # str | 

    try:
        api_response = await api_instance.get_guild_webhooks(guild_id)
        print("The response of DefaultApi->get_guild_webhooks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_guild_webhooks: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guild_id** | **str**|  | 

### Return type

[**List[ListChannelWebhooks200ResponseInner]**](ListChannelWebhooks200ResponseInner.md)

### Authorization

[BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 response for get_guild_webhooks |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_guild_welcome_screen**
> GuildWelcomeScreenResponse get_guild_welcome_screen(guild_id)

### Example

* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.models.guild_welcome_screen_response import GuildWelcomeScreenResponse
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    guild_id = 'guild_id_example' # str | 

    try:
        api_response = await api_instance.get_guild_welcome_screen(guild_id)
        print("The response of DefaultApi->get_guild_welcome_screen:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_guild_welcome_screen: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guild_id** | **str**|  | 

### Return type

[**GuildWelcomeScreenResponse**](GuildWelcomeScreenResponse.md)

### Authorization

[BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 response for get_guild_welcome_screen |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_guild_widget**
> WidgetResponse get_guild_widget(guild_id)

### Example

* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.models.widget_response import WidgetResponse
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    guild_id = 'guild_id_example' # str | 

    try:
        api_response = await api_instance.get_guild_widget(guild_id)
        print("The response of DefaultApi->get_guild_widget:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_guild_widget: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guild_id** | **str**|  | 

### Return type

[**WidgetResponse**](WidgetResponse.md)

### Authorization

[BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 response for get_guild_widget |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_guild_widget_png**
> str get_guild_widget_png(guild_id, style=style)

### Example

* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    guild_id = 'guild_id_example' # str | 
    style = 'style_example' # str |  (optional)

    try:
        api_response = await api_instance.get_guild_widget_png(guild_id, style=style)
        print("The response of DefaultApi->get_guild_widget_png:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_guild_widget_png: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guild_id** | **str**|  | 
 **style** | **str**|  | [optional] 

### Return type

**str**

### Authorization

[BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: image/png, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 response for get_guild_widget_png |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_guild_widget_settings**
> WidgetSettingsResponse get_guild_widget_settings(guild_id)

### Example

* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.models.widget_settings_response import WidgetSettingsResponse
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    guild_id = 'guild_id_example' # str | 

    try:
        api_response = await api_instance.get_guild_widget_settings(guild_id)
        print("The response of DefaultApi->get_guild_widget_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_guild_widget_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guild_id** | **str**|  | 

### Return type

[**WidgetSettingsResponse**](WidgetSettingsResponse.md)

### Authorization

[BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 response for get_guild_widget_settings |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_guilds_onboarding**
> UserGuildOnboardingResponse get_guilds_onboarding(guild_id)

### Example

* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.models.user_guild_onboarding_response import UserGuildOnboardingResponse
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    guild_id = 'guild_id_example' # str | 

    try:
        api_response = await api_instance.get_guilds_onboarding(guild_id)
        print("The response of DefaultApi->get_guilds_onboarding:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_guilds_onboarding: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guild_id** | **str**|  | 

### Return type

[**UserGuildOnboardingResponse**](UserGuildOnboardingResponse.md)

### Authorization

[BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 response for get_guilds_onboarding |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_lobby**
> LobbyResponse get_lobby(lobby_id)

### Example

* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.models.lobby_response import LobbyResponse
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    lobby_id = 'lobby_id_example' # str | 

    try:
        api_response = await api_instance.get_lobby(lobby_id)
        print("The response of DefaultApi->get_lobby:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_lobby: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lobby_id** | **str**|  | 

### Return type

[**LobbyResponse**](LobbyResponse.md)

### Authorization

[BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 response for get_lobby |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_lobby_messages**
> List[LobbyMessageResponse] get_lobby_messages(lobby_id, limit=limit)

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):
* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.models.lobby_message_response import LobbyMessageResponse
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    lobby_id = 'lobby_id_example' # str | 
    limit = 56 # int |  (optional)

    try:
        api_response = await api_instance.get_lobby_messages(lobby_id, limit=limit)
        print("The response of DefaultApi->get_lobby_messages:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_lobby_messages: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lobby_id** | **str**|  | 
 **limit** | **int**|  | [optional] 

### Return type

[**List[LobbyMessageResponse]**](LobbyMessageResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 response for get_lobby_messages |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_message**
> MessageResponse get_message(channel_id, message_id)

### Example

* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.models.message_response import MessageResponse
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    channel_id = 'channel_id_example' # str | 
    message_id = 'message_id_example' # str | 

    try:
        api_response = await api_instance.get_message(channel_id, message_id)
        print("The response of DefaultApi->get_message:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_message: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **str**|  | 
 **message_id** | **str**|  | 

### Return type

[**MessageResponse**](MessageResponse.md)

### Authorization

[BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 response for get_message |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_my_application**
> PrivateApplicationResponse get_my_application()

### Example

* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.models.private_application_response import PrivateApplicationResponse
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)

    try:
        api_response = await api_instance.get_my_application()
        print("The response of DefaultApi->get_my_application:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_my_application: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**PrivateApplicationResponse**](PrivateApplicationResponse.md)

### Authorization

[BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 response for get_my_application |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_my_guild_member**
> PrivateGuildMemberResponse get_my_guild_member(guild_id)

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import dc_rest
from dc_rest.models.private_guild_member_response import PrivateGuildMemberResponse
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    guild_id = 'guild_id_example' # str | 

    try:
        api_response = await api_instance.get_my_guild_member(guild_id)
        print("The response of DefaultApi->get_my_guild_member:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_my_guild_member: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guild_id** | **str**|  | 

### Return type

[**PrivateGuildMemberResponse**](PrivateGuildMemberResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 response for get_my_guild_member |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_my_oauth2_application**
> PrivateApplicationResponse get_my_oauth2_application()

### Example

* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.models.private_application_response import PrivateApplicationResponse
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)

    try:
        api_response = await api_instance.get_my_oauth2_application()
        print("The response of DefaultApi->get_my_oauth2_application:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_my_oauth2_application: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**PrivateApplicationResponse**](PrivateApplicationResponse.md)

### Authorization

[BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 response for get_my_oauth2_application |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_my_oauth2_authorization**
> OAuth2GetAuthorizationResponse get_my_oauth2_authorization()

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):
* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.models.o_auth2_get_authorization_response import OAuth2GetAuthorizationResponse
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)

    try:
        api_response = await api_instance.get_my_oauth2_authorization()
        print("The response of DefaultApi->get_my_oauth2_authorization:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_my_oauth2_authorization: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**OAuth2GetAuthorizationResponse**](OAuth2GetAuthorizationResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 response for get_my_oauth2_authorization |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_my_user**
> UserPIIResponse get_my_user()

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):
* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.models.user_pii_response import UserPIIResponse
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)

    try:
        api_response = await api_instance.get_my_user()
        print("The response of DefaultApi->get_my_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_my_user: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**UserPIIResponse**](UserPIIResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 response for get_my_user |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_openid_connect_userinfo**
> OAuth2GetOpenIDConnectUserInfoResponse get_openid_connect_userinfo()

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):
* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.models.o_auth2_get_open_id_connect_user_info_response import OAuth2GetOpenIDConnectUserInfoResponse
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)

    try:
        api_response = await api_instance.get_openid_connect_userinfo()
        print("The response of DefaultApi->get_openid_connect_userinfo:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_openid_connect_userinfo: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**OAuth2GetOpenIDConnectUserInfoResponse**](OAuth2GetOpenIDConnectUserInfoResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 response for get_openid_connect_userinfo |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_original_webhook_message**
> MessageResponse get_original_webhook_message(webhook_id, webhook_token, thread_id=thread_id)

### Example

* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.models.message_response import MessageResponse
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    webhook_id = 'webhook_id_example' # str | 
    webhook_token = 'webhook_token_example' # str | 
    thread_id = 'thread_id_example' # str |  (optional)

    try:
        api_response = await api_instance.get_original_webhook_message(webhook_id, webhook_token, thread_id=thread_id)
        print("The response of DefaultApi->get_original_webhook_message:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_original_webhook_message: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhook_id** | **str**|  | 
 **webhook_token** | **str**|  | 
 **thread_id** | **str**|  | [optional] 

### Return type

[**MessageResponse**](MessageResponse.md)

### Authorization

[BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 response for get_original_webhook_message |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_public_keys**
> OAuth2GetKeys get_public_keys()

### Example

* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.models.o_auth2_get_keys import OAuth2GetKeys
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)

    try:
        api_response = await api_instance.get_public_keys()
        print("The response of DefaultApi->get_public_keys:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_public_keys: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**OAuth2GetKeys**](OAuth2GetKeys.md)

### Authorization

[BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 response for get_public_keys |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_self_voice_state**
> VoiceStateResponse get_self_voice_state(guild_id)

### Example

* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.models.voice_state_response import VoiceStateResponse
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    guild_id = 'guild_id_example' # str | 

    try:
        api_response = await api_instance.get_self_voice_state(guild_id)
        print("The response of DefaultApi->get_self_voice_state:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_self_voice_state: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guild_id** | **str**|  | 

### Return type

[**VoiceStateResponse**](VoiceStateResponse.md)

### Authorization

[BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 response for get_self_voice_state |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_soundboard_default_sounds**
> List[SoundboardSoundResponse] get_soundboard_default_sounds()

### Example

* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.models.soundboard_sound_response import SoundboardSoundResponse
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)

    try:
        api_response = await api_instance.get_soundboard_default_sounds()
        print("The response of DefaultApi->get_soundboard_default_sounds:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_soundboard_default_sounds: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[SoundboardSoundResponse]**](SoundboardSoundResponse.md)

### Authorization

[BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 response for get_soundboard_default_sounds |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_stage_instance**
> StageInstanceResponse get_stage_instance(channel_id)

### Example

* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.models.stage_instance_response import StageInstanceResponse
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    channel_id = 'channel_id_example' # str | 

    try:
        api_response = await api_instance.get_stage_instance(channel_id)
        print("The response of DefaultApi->get_stage_instance:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_stage_instance: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **str**|  | 

### Return type

[**StageInstanceResponse**](StageInstanceResponse.md)

### Authorization

[BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 response for get_stage_instance |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sticker**
> GetSticker200Response get_sticker(sticker_id)

### Example

* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.models.get_sticker200_response import GetSticker200Response
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    sticker_id = 'sticker_id_example' # str | 

    try:
        api_response = await api_instance.get_sticker(sticker_id)
        print("The response of DefaultApi->get_sticker:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_sticker: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sticker_id** | **str**|  | 

### Return type

[**GetSticker200Response**](GetSticker200Response.md)

### Authorization

[BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 response for get_sticker |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sticker_pack**
> StickerPackResponse get_sticker_pack(pack_id)

### Example

* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.models.sticker_pack_response import StickerPackResponse
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    pack_id = 'pack_id_example' # str | 

    try:
        api_response = await api_instance.get_sticker_pack(pack_id)
        print("The response of DefaultApi->get_sticker_pack:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_sticker_pack: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pack_id** | **str**|  | 

### Return type

[**StickerPackResponse**](StickerPackResponse.md)

### Authorization

[BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 response for get_sticker_pack |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_thread_member**
> ThreadMemberResponse get_thread_member(channel_id, user_id, with_member=with_member)

### Example

* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.models.thread_member_response import ThreadMemberResponse
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    channel_id = 'channel_id_example' # str | 
    user_id = 'user_id_example' # str | 
    with_member = True # bool |  (optional)

    try:
        api_response = await api_instance.get_thread_member(channel_id, user_id, with_member=with_member)
        print("The response of DefaultApi->get_thread_member:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_thread_member: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **str**|  | 
 **user_id** | **str**|  | 
 **with_member** | **bool**|  | [optional] 

### Return type

[**ThreadMemberResponse**](ThreadMemberResponse.md)

### Authorization

[BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 response for get_thread_member |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user**
> UserResponse get_user(user_id)

### Example

* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.models.user_response import UserResponse
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    user_id = 'user_id_example' # str | 

    try:
        api_response = await api_instance.get_user(user_id)
        print("The response of DefaultApi->get_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 

### Return type

[**UserResponse**](UserResponse.md)

### Authorization

[BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 response for get_user |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_voice_state**
> VoiceStateResponse get_voice_state(guild_id, user_id)

### Example

* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.models.voice_state_response import VoiceStateResponse
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    guild_id = 'guild_id_example' # str | 
    user_id = 'user_id_example' # str | 

    try:
        api_response = await api_instance.get_voice_state(guild_id, user_id)
        print("The response of DefaultApi->get_voice_state:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_voice_state: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guild_id** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

[**VoiceStateResponse**](VoiceStateResponse.md)

### Authorization

[BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 response for get_voice_state |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_webhook**
> ListChannelWebhooks200ResponseInner get_webhook(webhook_id)

### Example

* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.models.list_channel_webhooks200_response_inner import ListChannelWebhooks200ResponseInner
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    webhook_id = 'webhook_id_example' # str | 

    try:
        api_response = await api_instance.get_webhook(webhook_id)
        print("The response of DefaultApi->get_webhook:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_webhook: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhook_id** | **str**|  | 

### Return type

[**ListChannelWebhooks200ResponseInner**](ListChannelWebhooks200ResponseInner.md)

### Authorization

[BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 response for get_webhook |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_webhook_by_token**
> ListChannelWebhooks200ResponseInner get_webhook_by_token(webhook_id, webhook_token)

### Example

* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.models.list_channel_webhooks200_response_inner import ListChannelWebhooks200ResponseInner
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    webhook_id = 'webhook_id_example' # str | 
    webhook_token = 'webhook_token_example' # str | 

    try:
        api_response = await api_instance.get_webhook_by_token(webhook_id, webhook_token)
        print("The response of DefaultApi->get_webhook_by_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_webhook_by_token: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhook_id** | **str**|  | 
 **webhook_token** | **str**|  | 

### Return type

[**ListChannelWebhooks200ResponseInner**](ListChannelWebhooks200ResponseInner.md)

### Authorization

[BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 response for get_webhook_by_token |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_webhook_message**
> MessageResponse get_webhook_message(webhook_id, webhook_token, message_id, thread_id=thread_id)

### Example

* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.models.message_response import MessageResponse
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    webhook_id = 'webhook_id_example' # str | 
    webhook_token = 'webhook_token_example' # str | 
    message_id = 'message_id_example' # str | 
    thread_id = 'thread_id_example' # str |  (optional)

    try:
        api_response = await api_instance.get_webhook_message(webhook_id, webhook_token, message_id, thread_id=thread_id)
        print("The response of DefaultApi->get_webhook_message:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_webhook_message: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhook_id** | **str**|  | 
 **webhook_token** | **str**|  | 
 **message_id** | **str**|  | 
 **thread_id** | **str**|  | [optional] 

### Return type

[**MessageResponse**](MessageResponse.md)

### Authorization

[BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 response for get_webhook_message |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invite_resolve**
> ListChannelInvites200ResponseInner invite_resolve(code, with_counts=with_counts, guild_scheduled_event_id=guild_scheduled_event_id)

### Example

* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.models.list_channel_invites200_response_inner import ListChannelInvites200ResponseInner
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    code = 'code_example' # str | 
    with_counts = True # bool |  (optional)
    guild_scheduled_event_id = 'guild_scheduled_event_id_example' # str |  (optional)

    try:
        api_response = await api_instance.invite_resolve(code, with_counts=with_counts, guild_scheduled_event_id=guild_scheduled_event_id)
        print("The response of DefaultApi->invite_resolve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->invite_resolve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**|  | 
 **with_counts** | **bool**|  | [optional] 
 **guild_scheduled_event_id** | **str**|  | [optional] 

### Return type

[**ListChannelInvites200ResponseInner**](ListChannelInvites200ResponseInner.md)

### Authorization

[BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 response for invite_resolve |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invite_revoke**
> ListChannelInvites200ResponseInner invite_revoke(code)

### Example

* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.models.list_channel_invites200_response_inner import ListChannelInvites200ResponseInner
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    code = 'code_example' # str | 

    try:
        api_response = await api_instance.invite_revoke(code)
        print("The response of DefaultApi->invite_revoke:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->invite_revoke: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**|  | 

### Return type

[**ListChannelInvites200ResponseInner**](ListChannelInvites200ResponseInner.md)

### Authorization

[BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 response for invite_revoke |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **join_thread**
> join_thread(channel_id)

### Example

* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    channel_id = 'channel_id_example' # str | 

    try:
        await api_instance.join_thread(channel_id)
    except Exception as e:
        print("Exception when calling DefaultApi->join_thread: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | 204 response for join_thread |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **leave_guild**
> leave_guild(guild_id)

### Example

* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    guild_id = 'guild_id_example' # str | 

    try:
        await api_instance.leave_guild(guild_id)
    except Exception as e:
        print("Exception when calling DefaultApi->leave_guild: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guild_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | 204 response for leave_guild |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **leave_lobby**
> leave_lobby(lobby_id)

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):
* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    lobby_id = 'lobby_id_example' # str | 

    try:
        await api_instance.leave_lobby(lobby_id)
    except Exception as e:
        print("Exception when calling DefaultApi->leave_lobby: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lobby_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | 204 response for leave_lobby |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **leave_thread**
> leave_thread(channel_id)

### Example

* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    channel_id = 'channel_id_example' # str | 

    try:
        await api_instance.leave_thread(channel_id)
    except Exception as e:
        print("Exception when calling DefaultApi->leave_thread: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | 204 response for leave_thread |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_application_commands**
> List[ApplicationCommandResponse] list_application_commands(application_id, with_localizations=with_localizations)

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):
* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.models.application_command_response import ApplicationCommandResponse
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    application_id = 'application_id_example' # str | 
    with_localizations = True # bool |  (optional)

    try:
        api_response = await api_instance.list_application_commands(application_id, with_localizations=with_localizations)
        print("The response of DefaultApi->list_application_commands:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->list_application_commands: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **str**|  | 
 **with_localizations** | **bool**|  | [optional] 

### Return type

[**List[ApplicationCommandResponse]**](ApplicationCommandResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 response for list_application_commands |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_application_emojis**
> ListApplicationEmojisResponse list_application_emojis(application_id)

### Example

* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.models.list_application_emojis_response import ListApplicationEmojisResponse
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    application_id = 'application_id_example' # str | 

    try:
        api_response = await api_instance.list_application_emojis(application_id)
        print("The response of DefaultApi->list_application_emojis:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->list_application_emojis: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **str**|  | 

### Return type

[**ListApplicationEmojisResponse**](ListApplicationEmojisResponse.md)

### Authorization

[BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 response for list_application_emojis |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_auto_moderation_rules**
> List[ListAutoModerationRules200ResponseInner] list_auto_moderation_rules(guild_id)

### Example

* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.models.list_auto_moderation_rules200_response_inner import ListAutoModerationRules200ResponseInner
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    guild_id = 'guild_id_example' # str | 

    try:
        api_response = await api_instance.list_auto_moderation_rules(guild_id)
        print("The response of DefaultApi->list_auto_moderation_rules:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->list_auto_moderation_rules: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guild_id** | **str**|  | 

### Return type

[**List[ListAutoModerationRules200ResponseInner]**](ListAutoModerationRules200ResponseInner.md)

### Authorization

[BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 response for list_auto_moderation_rules |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_channel_invites**
> List[ListChannelInvites200ResponseInner] list_channel_invites(channel_id)

### Example

* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.models.list_channel_invites200_response_inner import ListChannelInvites200ResponseInner
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    channel_id = 'channel_id_example' # str | 

    try:
        api_response = await api_instance.list_channel_invites(channel_id)
        print("The response of DefaultApi->list_channel_invites:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->list_channel_invites: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **str**|  | 

### Return type

[**List[ListChannelInvites200ResponseInner]**](ListChannelInvites200ResponseInner.md)

### Authorization

[BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 response for list_channel_invites |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_channel_webhooks**
> List[ListChannelWebhooks200ResponseInner] list_channel_webhooks(channel_id)

### Example

* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.models.list_channel_webhooks200_response_inner import ListChannelWebhooks200ResponseInner
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    channel_id = 'channel_id_example' # str | 

    try:
        api_response = await api_instance.list_channel_webhooks(channel_id)
        print("The response of DefaultApi->list_channel_webhooks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->list_channel_webhooks: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **str**|  | 

### Return type

[**List[ListChannelWebhooks200ResponseInner]**](ListChannelWebhooks200ResponseInner.md)

### Authorization

[BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 response for list_channel_webhooks |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_guild_application_command_permissions**
> List[CommandPermissionsResponse] list_guild_application_command_permissions(application_id, guild_id)

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):
* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.models.command_permissions_response import CommandPermissionsResponse
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    application_id = 'application_id_example' # str | 
    guild_id = 'guild_id_example' # str | 

    try:
        api_response = await api_instance.list_guild_application_command_permissions(application_id, guild_id)
        print("The response of DefaultApi->list_guild_application_command_permissions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->list_guild_application_command_permissions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **str**|  | 
 **guild_id** | **str**|  | 

### Return type

[**List[CommandPermissionsResponse]**](CommandPermissionsResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 response for list_guild_application_command_permissions |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_guild_application_commands**
> List[ApplicationCommandResponse] list_guild_application_commands(application_id, guild_id, with_localizations=with_localizations)

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):
* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.models.application_command_response import ApplicationCommandResponse
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    application_id = 'application_id_example' # str | 
    guild_id = 'guild_id_example' # str | 
    with_localizations = True # bool |  (optional)

    try:
        api_response = await api_instance.list_guild_application_commands(application_id, guild_id, with_localizations=with_localizations)
        print("The response of DefaultApi->list_guild_application_commands:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->list_guild_application_commands: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **str**|  | 
 **guild_id** | **str**|  | 
 **with_localizations** | **bool**|  | [optional] 

### Return type

[**List[ApplicationCommandResponse]**](ApplicationCommandResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 response for list_guild_application_commands |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_guild_audit_log_entries**
> GuildAuditLogResponse list_guild_audit_log_entries(guild_id, user_id=user_id, target_id=target_id, action_type=action_type, before=before, after=after, limit=limit)

### Example

* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.models.guild_audit_log_response import GuildAuditLogResponse
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    guild_id = 'guild_id_example' # str | 
    user_id = 'user_id_example' # str |  (optional)
    target_id = 'target_id_example' # str |  (optional)
    action_type = 56 # int |  (optional)
    before = 'before_example' # str |  (optional)
    after = 'after_example' # str |  (optional)
    limit = 56 # int |  (optional)

    try:
        api_response = await api_instance.list_guild_audit_log_entries(guild_id, user_id=user_id, target_id=target_id, action_type=action_type, before=before, after=after, limit=limit)
        print("The response of DefaultApi->list_guild_audit_log_entries:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->list_guild_audit_log_entries: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guild_id** | **str**|  | 
 **user_id** | **str**|  | [optional] 
 **target_id** | **str**|  | [optional] 
 **action_type** | **int**|  | [optional] 
 **before** | **str**|  | [optional] 
 **after** | **str**|  | [optional] 
 **limit** | **int**|  | [optional] 

### Return type

[**GuildAuditLogResponse**](GuildAuditLogResponse.md)

### Authorization

[BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 response for list_guild_audit_log_entries |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_guild_bans**
> List[GuildBanResponse] list_guild_bans(guild_id, limit=limit, before=before, after=after)

### Example

* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.models.guild_ban_response import GuildBanResponse
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    guild_id = 'guild_id_example' # str | 
    limit = 56 # int |  (optional)
    before = 'before_example' # str |  (optional)
    after = 'after_example' # str |  (optional)

    try:
        api_response = await api_instance.list_guild_bans(guild_id, limit=limit, before=before, after=after)
        print("The response of DefaultApi->list_guild_bans:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->list_guild_bans: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guild_id** | **str**|  | 
 **limit** | **int**|  | [optional] 
 **before** | **str**|  | [optional] 
 **after** | **str**|  | [optional] 

### Return type

[**List[GuildBanResponse]**](GuildBanResponse.md)

### Authorization

[BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 response for list_guild_bans |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_guild_channels**
> List[GetChannel200Response] list_guild_channels(guild_id)

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):
* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.models.get_channel200_response import GetChannel200Response
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    guild_id = 'guild_id_example' # str | 

    try:
        api_response = await api_instance.list_guild_channels(guild_id)
        print("The response of DefaultApi->list_guild_channels:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->list_guild_channels: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guild_id** | **str**|  | 

### Return type

[**List[GetChannel200Response]**](GetChannel200Response.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 response for list_guild_channels |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_guild_emojis**
> List[EmojiResponse] list_guild_emojis(guild_id)

### Example

* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.models.emoji_response import EmojiResponse
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    guild_id = 'guild_id_example' # str | 

    try:
        api_response = await api_instance.list_guild_emojis(guild_id)
        print("The response of DefaultApi->list_guild_emojis:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->list_guild_emojis: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guild_id** | **str**|  | 

### Return type

[**List[EmojiResponse]**](EmojiResponse.md)

### Authorization

[BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 response for list_guild_emojis |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_guild_integrations**
> List[ListGuildIntegrations200ResponseInner] list_guild_integrations(guild_id)

### Example

* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.models.list_guild_integrations200_response_inner import ListGuildIntegrations200ResponseInner
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    guild_id = 'guild_id_example' # str | 

    try:
        api_response = await api_instance.list_guild_integrations(guild_id)
        print("The response of DefaultApi->list_guild_integrations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->list_guild_integrations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guild_id** | **str**|  | 

### Return type

[**List[ListGuildIntegrations200ResponseInner]**](ListGuildIntegrations200ResponseInner.md)

### Authorization

[BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 response for list_guild_integrations |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_guild_invites**
> List[ListChannelInvites200ResponseInner] list_guild_invites(guild_id)

### Example

* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.models.list_channel_invites200_response_inner import ListChannelInvites200ResponseInner
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    guild_id = 'guild_id_example' # str | 

    try:
        api_response = await api_instance.list_guild_invites(guild_id)
        print("The response of DefaultApi->list_guild_invites:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->list_guild_invites: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guild_id** | **str**|  | 

### Return type

[**List[ListChannelInvites200ResponseInner]**](ListChannelInvites200ResponseInner.md)

### Authorization

[BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 response for list_guild_invites |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_guild_members**
> List[GuildMemberResponse] list_guild_members(guild_id, limit=limit, after=after)

### Example

* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.models.guild_member_response import GuildMemberResponse
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    guild_id = 'guild_id_example' # str | 
    limit = 56 # int |  (optional)
    after = 56 # int |  (optional)

    try:
        api_response = await api_instance.list_guild_members(guild_id, limit=limit, after=after)
        print("The response of DefaultApi->list_guild_members:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->list_guild_members: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guild_id** | **str**|  | 
 **limit** | **int**|  | [optional] 
 **after** | **int**|  | [optional] 

### Return type

[**List[GuildMemberResponse]**](GuildMemberResponse.md)

### Authorization

[BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 response for list_guild_members |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_guild_roles**
> List[GuildRoleResponse] list_guild_roles(guild_id)

### Example

* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.models.guild_role_response import GuildRoleResponse
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    guild_id = 'guild_id_example' # str | 

    try:
        api_response = await api_instance.list_guild_roles(guild_id)
        print("The response of DefaultApi->list_guild_roles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->list_guild_roles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guild_id** | **str**|  | 

### Return type

[**List[GuildRoleResponse]**](GuildRoleResponse.md)

### Authorization

[BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 response for list_guild_roles |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_guild_scheduled_event_users**
> List[ScheduledEventUserResponse] list_guild_scheduled_event_users(guild_id, guild_scheduled_event_id, with_member=with_member, limit=limit, before=before, after=after)

### Example

* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.models.scheduled_event_user_response import ScheduledEventUserResponse
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    guild_id = 'guild_id_example' # str | 
    guild_scheduled_event_id = 'guild_scheduled_event_id_example' # str | 
    with_member = True # bool |  (optional)
    limit = 56 # int |  (optional)
    before = 'before_example' # str |  (optional)
    after = 'after_example' # str |  (optional)

    try:
        api_response = await api_instance.list_guild_scheduled_event_users(guild_id, guild_scheduled_event_id, with_member=with_member, limit=limit, before=before, after=after)
        print("The response of DefaultApi->list_guild_scheduled_event_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->list_guild_scheduled_event_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guild_id** | **str**|  | 
 **guild_scheduled_event_id** | **str**|  | 
 **with_member** | **bool**|  | [optional] 
 **limit** | **int**|  | [optional] 
 **before** | **str**|  | [optional] 
 **after** | **str**|  | [optional] 

### Return type

[**List[ScheduledEventUserResponse]**](ScheduledEventUserResponse.md)

### Authorization

[BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 response for list_guild_scheduled_event_users |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_guild_scheduled_events**
> List[ListGuildScheduledEvents200ResponseInner] list_guild_scheduled_events(guild_id, with_user_count=with_user_count)

### Example

* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.models.list_guild_scheduled_events200_response_inner import ListGuildScheduledEvents200ResponseInner
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    guild_id = 'guild_id_example' # str | 
    with_user_count = True # bool |  (optional)

    try:
        api_response = await api_instance.list_guild_scheduled_events(guild_id, with_user_count=with_user_count)
        print("The response of DefaultApi->list_guild_scheduled_events:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->list_guild_scheduled_events: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guild_id** | **str**|  | 
 **with_user_count** | **bool**|  | [optional] 

### Return type

[**List[ListGuildScheduledEvents200ResponseInner]**](ListGuildScheduledEvents200ResponseInner.md)

### Authorization

[BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 response for list_guild_scheduled_events |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_guild_soundboard_sounds**
> ListGuildSoundboardSoundsResponse list_guild_soundboard_sounds(guild_id)

### Example

* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.models.list_guild_soundboard_sounds_response import ListGuildSoundboardSoundsResponse
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    guild_id = 'guild_id_example' # str | 

    try:
        api_response = await api_instance.list_guild_soundboard_sounds(guild_id)
        print("The response of DefaultApi->list_guild_soundboard_sounds:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->list_guild_soundboard_sounds: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guild_id** | **str**|  | 

### Return type

[**ListGuildSoundboardSoundsResponse**](ListGuildSoundboardSoundsResponse.md)

### Authorization

[BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 response for list_guild_soundboard_sounds |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_guild_stickers**
> List[GuildStickerResponse] list_guild_stickers(guild_id)

### Example

* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.models.guild_sticker_response import GuildStickerResponse
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    guild_id = 'guild_id_example' # str | 

    try:
        api_response = await api_instance.list_guild_stickers(guild_id)
        print("The response of DefaultApi->list_guild_stickers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->list_guild_stickers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guild_id** | **str**|  | 

### Return type

[**List[GuildStickerResponse]**](GuildStickerResponse.md)

### Authorization

[BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 response for list_guild_stickers |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_guild_templates**
> List[GuildTemplateResponse] list_guild_templates(guild_id)

### Example

* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.models.guild_template_response import GuildTemplateResponse
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    guild_id = 'guild_id_example' # str | 

    try:
        api_response = await api_instance.list_guild_templates(guild_id)
        print("The response of DefaultApi->list_guild_templates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->list_guild_templates: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guild_id** | **str**|  | 

### Return type

[**List[GuildTemplateResponse]**](GuildTemplateResponse.md)

### Authorization

[BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 response for list_guild_templates |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_guild_voice_regions**
> List[VoiceRegionResponse] list_guild_voice_regions(guild_id)

### Example

* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.models.voice_region_response import VoiceRegionResponse
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    guild_id = 'guild_id_example' # str | 

    try:
        api_response = await api_instance.list_guild_voice_regions(guild_id)
        print("The response of DefaultApi->list_guild_voice_regions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->list_guild_voice_regions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guild_id** | **str**|  | 

### Return type

[**List[VoiceRegionResponse]**](VoiceRegionResponse.md)

### Authorization

[BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 response for list_guild_voice_regions |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_message_reactions_by_emoji**
> List[UserResponse] list_message_reactions_by_emoji(channel_id, message_id, emoji_name, after=after, limit=limit, type=type)

### Example

* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.models.user_response import UserResponse
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    channel_id = 'channel_id_example' # str | 
    message_id = 'message_id_example' # str | 
    emoji_name = 'emoji_name_example' # str | 
    after = 'after_example' # str |  (optional)
    limit = 56 # int |  (optional)
    type = 56 # int |  (optional)

    try:
        api_response = await api_instance.list_message_reactions_by_emoji(channel_id, message_id, emoji_name, after=after, limit=limit, type=type)
        print("The response of DefaultApi->list_message_reactions_by_emoji:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->list_message_reactions_by_emoji: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **str**|  | 
 **message_id** | **str**|  | 
 **emoji_name** | **str**|  | 
 **after** | **str**|  | [optional] 
 **limit** | **int**|  | [optional] 
 **type** | **int**|  | [optional] 

### Return type

[**List[UserResponse]**](UserResponse.md)

### Authorization

[BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 response for list_message_reactions_by_emoji |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_messages**
> List[MessageResponse] list_messages(channel_id, around=around, before=before, after=after, limit=limit)

### Example

* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.models.message_response import MessageResponse
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    channel_id = 'channel_id_example' # str | 
    around = 'around_example' # str |  (optional)
    before = 'before_example' # str |  (optional)
    after = 'after_example' # str |  (optional)
    limit = 56 # int |  (optional)

    try:
        api_response = await api_instance.list_messages(channel_id, around=around, before=before, after=after, limit=limit)
        print("The response of DefaultApi->list_messages:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->list_messages: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **str**|  | 
 **around** | **str**|  | [optional] 
 **before** | **str**|  | [optional] 
 **after** | **str**|  | [optional] 
 **limit** | **int**|  | [optional] 

### Return type

[**List[MessageResponse]**](MessageResponse.md)

### Authorization

[BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 response for list_messages |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_my_connections**
> List[ConnectedAccountResponse] list_my_connections()

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):
* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.models.connected_account_response import ConnectedAccountResponse
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)

    try:
        api_response = await api_instance.list_my_connections()
        print("The response of DefaultApi->list_my_connections:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->list_my_connections: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[ConnectedAccountResponse]**](ConnectedAccountResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 response for list_my_connections |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_my_guilds**
> List[MyGuildResponse] list_my_guilds(before=before, after=after, limit=limit, with_counts=with_counts)

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):
* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.models.my_guild_response import MyGuildResponse
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    before = 'before_example' # str |  (optional)
    after = 'after_example' # str |  (optional)
    limit = 56 # int |  (optional)
    with_counts = True # bool |  (optional)

    try:
        api_response = await api_instance.list_my_guilds(before=before, after=after, limit=limit, with_counts=with_counts)
        print("The response of DefaultApi->list_my_guilds:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->list_my_guilds: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **before** | **str**|  | [optional] 
 **after** | **str**|  | [optional] 
 **limit** | **int**|  | [optional] 
 **with_counts** | **bool**|  | [optional] 

### Return type

[**List[MyGuildResponse]**](MyGuildResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 response for list_my_guilds |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_my_private_archived_threads**
> ThreadsResponse list_my_private_archived_threads(channel_id, before=before, limit=limit)

### Example

* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.models.threads_response import ThreadsResponse
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    channel_id = 'channel_id_example' # str | 
    before = 'before_example' # str |  (optional)
    limit = 56 # int |  (optional)

    try:
        api_response = await api_instance.list_my_private_archived_threads(channel_id, before=before, limit=limit)
        print("The response of DefaultApi->list_my_private_archived_threads:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->list_my_private_archived_threads: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **str**|  | 
 **before** | **str**|  | [optional] 
 **limit** | **int**|  | [optional] 

### Return type

[**ThreadsResponse**](ThreadsResponse.md)

### Authorization

[BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 response for list_my_private_archived_threads |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_pins**
> PinnedMessagesResponse list_pins(channel_id, before=before, limit=limit)

### Example

* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.models.pinned_messages_response import PinnedMessagesResponse
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    channel_id = 'channel_id_example' # str | 
    before = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    limit = 56 # int |  (optional)

    try:
        api_response = await api_instance.list_pins(channel_id, before=before, limit=limit)
        print("The response of DefaultApi->list_pins:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->list_pins: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **str**|  | 
 **before** | **datetime**|  | [optional] 
 **limit** | **int**|  | [optional] 

### Return type

[**PinnedMessagesResponse**](PinnedMessagesResponse.md)

### Authorization

[BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 response for list_pins |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_private_archived_threads**
> ThreadsResponse list_private_archived_threads(channel_id, before=before, limit=limit)

### Example

* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.models.threads_response import ThreadsResponse
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    channel_id = 'channel_id_example' # str | 
    before = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    limit = 56 # int |  (optional)

    try:
        api_response = await api_instance.list_private_archived_threads(channel_id, before=before, limit=limit)
        print("The response of DefaultApi->list_private_archived_threads:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->list_private_archived_threads: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **str**|  | 
 **before** | **datetime**|  | [optional] 
 **limit** | **int**|  | [optional] 

### Return type

[**ThreadsResponse**](ThreadsResponse.md)

### Authorization

[BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 response for list_private_archived_threads |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_public_archived_threads**
> ThreadsResponse list_public_archived_threads(channel_id, before=before, limit=limit)

### Example

* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.models.threads_response import ThreadsResponse
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    channel_id = 'channel_id_example' # str | 
    before = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    limit = 56 # int |  (optional)

    try:
        api_response = await api_instance.list_public_archived_threads(channel_id, before=before, limit=limit)
        print("The response of DefaultApi->list_public_archived_threads:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->list_public_archived_threads: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **str**|  | 
 **before** | **datetime**|  | [optional] 
 **limit** | **int**|  | [optional] 

### Return type

[**ThreadsResponse**](ThreadsResponse.md)

### Authorization

[BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 response for list_public_archived_threads |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_sticker_packs**
> StickerPackCollectionResponse list_sticker_packs()

### Example

* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.models.sticker_pack_collection_response import StickerPackCollectionResponse
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)

    try:
        api_response = await api_instance.list_sticker_packs()
        print("The response of DefaultApi->list_sticker_packs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->list_sticker_packs: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**StickerPackCollectionResponse**](StickerPackCollectionResponse.md)

### Authorization

[BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 response for list_sticker_packs |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_thread_members**
> List[ThreadMemberResponse] list_thread_members(channel_id, with_member=with_member, limit=limit, after=after)

### Example

* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.models.thread_member_response import ThreadMemberResponse
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    channel_id = 'channel_id_example' # str | 
    with_member = True # bool |  (optional)
    limit = 56 # int |  (optional)
    after = 'after_example' # str |  (optional)

    try:
        api_response = await api_instance.list_thread_members(channel_id, with_member=with_member, limit=limit, after=after)
        print("The response of DefaultApi->list_thread_members:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->list_thread_members: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **str**|  | 
 **with_member** | **bool**|  | [optional] 
 **limit** | **int**|  | [optional] 
 **after** | **str**|  | [optional] 

### Return type

[**List[ThreadMemberResponse]**](ThreadMemberResponse.md)

### Authorization

[BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 response for list_thread_members |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_voice_regions**
> List[VoiceRegionResponse] list_voice_regions()

### Example

* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.models.voice_region_response import VoiceRegionResponse
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)

    try:
        api_response = await api_instance.list_voice_regions()
        print("The response of DefaultApi->list_voice_regions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->list_voice_regions: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[VoiceRegionResponse]**](VoiceRegionResponse.md)

### Authorization

[BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 response for list_voice_regions |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **partner_sdk_token**
> ProvisionalTokenResponse partner_sdk_token(partner_sdk_unmerge_provisional_account_request)

### Example

* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.models.partner_sdk_unmerge_provisional_account_request import PartnerSdkUnmergeProvisionalAccountRequest
from dc_rest.models.provisional_token_response import ProvisionalTokenResponse
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    partner_sdk_unmerge_provisional_account_request = dc_rest.PartnerSdkUnmergeProvisionalAccountRequest() # PartnerSdkUnmergeProvisionalAccountRequest | 

    try:
        api_response = await api_instance.partner_sdk_token(partner_sdk_unmerge_provisional_account_request)
        print("The response of DefaultApi->partner_sdk_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->partner_sdk_token: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **partner_sdk_unmerge_provisional_account_request** | [**PartnerSdkUnmergeProvisionalAccountRequest**](PartnerSdkUnmergeProvisionalAccountRequest.md)|  | 

### Return type

[**ProvisionalTokenResponse**](ProvisionalTokenResponse.md)

### Authorization

[BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 response for partner_sdk_token |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **partner_sdk_unmerge_provisional_account**
> partner_sdk_unmerge_provisional_account(partner_sdk_unmerge_provisional_account_request)

### Example

* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.models.partner_sdk_unmerge_provisional_account_request import PartnerSdkUnmergeProvisionalAccountRequest
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    partner_sdk_unmerge_provisional_account_request = dc_rest.PartnerSdkUnmergeProvisionalAccountRequest() # PartnerSdkUnmergeProvisionalAccountRequest | 

    try:
        await api_instance.partner_sdk_unmerge_provisional_account(partner_sdk_unmerge_provisional_account_request)
    except Exception as e:
        print("Exception when calling DefaultApi->partner_sdk_unmerge_provisional_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **partner_sdk_unmerge_provisional_account_request** | [**PartnerSdkUnmergeProvisionalAccountRequest**](PartnerSdkUnmergeProvisionalAccountRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | 204 response for partner_sdk_unmerge_provisional_account |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **poll_expire**
> MessageResponse poll_expire(channel_id, message_id)

### Example

* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.models.message_response import MessageResponse
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    channel_id = 'channel_id_example' # str | 
    message_id = 'message_id_example' # str | 

    try:
        api_response = await api_instance.poll_expire(channel_id, message_id)
        print("The response of DefaultApi->poll_expire:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->poll_expire: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **str**|  | 
 **message_id** | **str**|  | 

### Return type

[**MessageResponse**](MessageResponse.md)

### Authorization

[BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 response for poll_expire |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **preview_prune_guild**
> GuildPruneResponse preview_prune_guild(guild_id, days=days, include_roles=include_roles)

### Example

* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.models.guild_prune_response import GuildPruneResponse
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    guild_id = 'guild_id_example' # str | 
    days = 56 # int |  (optional)
    include_roles = dc_rest.GetEntitlementsSkuIdsParameter() # GetEntitlementsSkuIdsParameter |  (optional)

    try:
        api_response = await api_instance.preview_prune_guild(guild_id, days=days, include_roles=include_roles)
        print("The response of DefaultApi->preview_prune_guild:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->preview_prune_guild: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guild_id** | **str**|  | 
 **days** | **int**|  | [optional] 
 **include_roles** | [**GetEntitlementsSkuIdsParameter**](.md)|  | [optional] 

### Return type

[**GuildPruneResponse**](GuildPruneResponse.md)

### Authorization

[BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 response for preview_prune_guild |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **prune_guild**
> GuildPruneResponse prune_guild(guild_id, prune_guild_request)

### Example

* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.models.guild_prune_response import GuildPruneResponse
from dc_rest.models.prune_guild_request import PruneGuildRequest
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    guild_id = 'guild_id_example' # str | 
    prune_guild_request = dc_rest.PruneGuildRequest() # PruneGuildRequest | 

    try:
        api_response = await api_instance.prune_guild(guild_id, prune_guild_request)
        print("The response of DefaultApi->prune_guild:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->prune_guild: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guild_id** | **str**|  | 
 **prune_guild_request** | [**PruneGuildRequest**](PruneGuildRequest.md)|  | 

### Return type

[**GuildPruneResponse**](GuildPruneResponse.md)

### Authorization

[BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 response for prune_guild |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_guilds_onboarding**
> GuildOnboardingResponse put_guilds_onboarding(guild_id, update_guild_onboarding_request)

### Example

* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.models.guild_onboarding_response import GuildOnboardingResponse
from dc_rest.models.update_guild_onboarding_request import UpdateGuildOnboardingRequest
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    guild_id = 'guild_id_example' # str | 
    update_guild_onboarding_request = dc_rest.UpdateGuildOnboardingRequest() # UpdateGuildOnboardingRequest | 

    try:
        api_response = await api_instance.put_guilds_onboarding(guild_id, update_guild_onboarding_request)
        print("The response of DefaultApi->put_guilds_onboarding:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->put_guilds_onboarding: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guild_id** | **str**|  | 
 **update_guild_onboarding_request** | [**UpdateGuildOnboardingRequest**](UpdateGuildOnboardingRequest.md)|  | 

### Return type

[**GuildOnboardingResponse**](GuildOnboardingResponse.md)

### Authorization

[BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 response for put_guilds_onboarding |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_guild_members**
> List[GuildMemberResponse] search_guild_members(limit, query, guild_id)

### Example

* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.models.guild_member_response import GuildMemberResponse
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    limit = 56 # int | 
    query = 'query_example' # str | 
    guild_id = 'guild_id_example' # str | 

    try:
        api_response = await api_instance.search_guild_members(limit, query, guild_id)
        print("The response of DefaultApi->search_guild_members:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->search_guild_members: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | 
 **query** | **str**|  | 
 **guild_id** | **str**|  | 

### Return type

[**List[GuildMemberResponse]**](GuildMemberResponse.md)

### Authorization

[BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 response for search_guild_members |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_soundboard_sound**
> send_soundboard_sound(channel_id, soundboard_sound_send_request)

### Example

* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.models.soundboard_sound_send_request import SoundboardSoundSendRequest
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    channel_id = 'channel_id_example' # str | 
    soundboard_sound_send_request = dc_rest.SoundboardSoundSendRequest() # SoundboardSoundSendRequest | 

    try:
        await api_instance.send_soundboard_sound(channel_id, soundboard_sound_send_request)
    except Exception as e:
        print("Exception when calling DefaultApi->send_soundboard_sound: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **str**|  | 
 **soundboard_sound_send_request** | [**SoundboardSoundSendRequest**](SoundboardSoundSendRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | 204 response for send_soundboard_sound |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_channel_permission_overwrite**
> set_channel_permission_overwrite(channel_id, overwrite_id, set_channel_permission_overwrite_request)

### Example

* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.models.set_channel_permission_overwrite_request import SetChannelPermissionOverwriteRequest
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    channel_id = 'channel_id_example' # str | 
    overwrite_id = 'overwrite_id_example' # str | 
    set_channel_permission_overwrite_request = dc_rest.SetChannelPermissionOverwriteRequest() # SetChannelPermissionOverwriteRequest | 

    try:
        await api_instance.set_channel_permission_overwrite(channel_id, overwrite_id, set_channel_permission_overwrite_request)
    except Exception as e:
        print("Exception when calling DefaultApi->set_channel_permission_overwrite: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **str**|  | 
 **overwrite_id** | **str**|  | 
 **set_channel_permission_overwrite_request** | [**SetChannelPermissionOverwriteRequest**](SetChannelPermissionOverwriteRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | 204 response for set_channel_permission_overwrite |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_guild_application_command_permissions**
> CommandPermissionsResponse set_guild_application_command_permissions(application_id, guild_id, command_id, set_guild_application_command_permissions_request)

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):
* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.models.command_permissions_response import CommandPermissionsResponse
from dc_rest.models.set_guild_application_command_permissions_request import SetGuildApplicationCommandPermissionsRequest
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    application_id = 'application_id_example' # str | 
    guild_id = 'guild_id_example' # str | 
    command_id = 'command_id_example' # str | 
    set_guild_application_command_permissions_request = dc_rest.SetGuildApplicationCommandPermissionsRequest() # SetGuildApplicationCommandPermissionsRequest | 

    try:
        api_response = await api_instance.set_guild_application_command_permissions(application_id, guild_id, command_id, set_guild_application_command_permissions_request)
        print("The response of DefaultApi->set_guild_application_command_permissions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->set_guild_application_command_permissions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **str**|  | 
 **guild_id** | **str**|  | 
 **command_id** | **str**|  | 
 **set_guild_application_command_permissions_request** | [**SetGuildApplicationCommandPermissionsRequest**](SetGuildApplicationCommandPermissionsRequest.md)|  | 

### Return type

[**CommandPermissionsResponse**](CommandPermissionsResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 response for set_guild_application_command_permissions |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_guild_mfa_level**
> GuildMFALevelResponse set_guild_mfa_level(guild_id, set_guild_mfa_level_request)

### Example

* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.models.guild_mfa_level_response import GuildMFALevelResponse
from dc_rest.models.set_guild_mfa_level_request import SetGuildMfaLevelRequest
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    guild_id = 'guild_id_example' # str | 
    set_guild_mfa_level_request = dc_rest.SetGuildMfaLevelRequest() # SetGuildMfaLevelRequest | 

    try:
        api_response = await api_instance.set_guild_mfa_level(guild_id, set_guild_mfa_level_request)
        print("The response of DefaultApi->set_guild_mfa_level:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->set_guild_mfa_level: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guild_id** | **str**|  | 
 **set_guild_mfa_level_request** | [**SetGuildMfaLevelRequest**](SetGuildMfaLevelRequest.md)|  | 

### Return type

[**GuildMFALevelResponse**](GuildMFALevelResponse.md)

### Authorization

[BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 response for set_guild_mfa_level |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sync_guild_template**
> GuildTemplateResponse sync_guild_template(guild_id, code)

### Example

* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.models.guild_template_response import GuildTemplateResponse
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    guild_id = 'guild_id_example' # str | 
    code = 'code_example' # str | 

    try:
        api_response = await api_instance.sync_guild_template(guild_id, code)
        print("The response of DefaultApi->sync_guild_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->sync_guild_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guild_id** | **str**|  | 
 **code** | **str**|  | 

### Return type

[**GuildTemplateResponse**](GuildTemplateResponse.md)

### Authorization

[BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 response for sync_guild_template |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **thread_search**
> ThreadSearchResponse thread_search(channel_id, name=name, slop=slop, min_id=min_id, max_id=max_id, tag=tag, tag_setting=tag_setting, archived=archived, sort_by=sort_by, sort_order=sort_order, limit=limit, offset=offset)

### Example

* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.models.thread_search_response import ThreadSearchResponse
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    channel_id = 'channel_id_example' # str | 
    name = 'name_example' # str |  (optional)
    slop = 56 # int |  (optional)
    min_id = 'min_id_example' # str |  (optional)
    max_id = 'max_id_example' # str |  (optional)
    tag = dc_rest.ThreadSearchTagParameter() # ThreadSearchTagParameter |  (optional)
    tag_setting = 'tag_setting_example' # str |  (optional)
    archived = True # bool |  (optional)
    sort_by = 'sort_by_example' # str |  (optional)
    sort_order = 'sort_order_example' # str |  (optional)
    limit = 56 # int |  (optional)
    offset = 56 # int |  (optional)

    try:
        api_response = await api_instance.thread_search(channel_id, name=name, slop=slop, min_id=min_id, max_id=max_id, tag=tag, tag_setting=tag_setting, archived=archived, sort_by=sort_by, sort_order=sort_order, limit=limit, offset=offset)
        print("The response of DefaultApi->thread_search:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->thread_search: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **str**|  | 
 **name** | **str**|  | [optional] 
 **slop** | **int**|  | [optional] 
 **min_id** | **str**|  | [optional] 
 **max_id** | **str**|  | [optional] 
 **tag** | [**ThreadSearchTagParameter**](.md)|  | [optional] 
 **tag_setting** | **str**|  | [optional] 
 **archived** | **bool**|  | [optional] 
 **sort_by** | **str**|  | [optional] 
 **sort_order** | **str**|  | [optional] 
 **limit** | **int**|  | [optional] 
 **offset** | **int**|  | [optional] 

### Return type

[**ThreadSearchResponse**](ThreadSearchResponse.md)

### Authorization

[BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 response for thread_search |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **trigger_typing_indicator**
> object trigger_typing_indicator(channel_id)

### Example

* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    channel_id = 'channel_id_example' # str | 

    try:
        api_response = await api_instance.trigger_typing_indicator(channel_id)
        print("The response of DefaultApi->trigger_typing_indicator:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->trigger_typing_indicator: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **str**|  | 

### Return type

**object**

### Authorization

[BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 response for trigger_typing_indicator |  -  |
**204** | 204 response for trigger_typing_indicator |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unban_user_from_guild**
> unban_user_from_guild(guild_id, user_id)

### Example

* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    guild_id = 'guild_id_example' # str | 
    user_id = 'user_id_example' # str | 

    try:
        await api_instance.unban_user_from_guild(guild_id, user_id)
    except Exception as e:
        print("Exception when calling DefaultApi->unban_user_from_guild: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guild_id** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | 204 response for unban_user_from_guild |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_application**
> PrivateApplicationResponse update_application(application_id, application_form_partial)

### Example

* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.models.application_form_partial import ApplicationFormPartial
from dc_rest.models.private_application_response import PrivateApplicationResponse
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    application_id = 'application_id_example' # str | 
    application_form_partial = dc_rest.ApplicationFormPartial() # ApplicationFormPartial | 

    try:
        api_response = await api_instance.update_application(application_id, application_form_partial)
        print("The response of DefaultApi->update_application:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->update_application: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **str**|  | 
 **application_form_partial** | [**ApplicationFormPartial**](ApplicationFormPartial.md)|  | 

### Return type

[**PrivateApplicationResponse**](PrivateApplicationResponse.md)

### Authorization

[BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 response for update_application |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_application_command**
> ApplicationCommandResponse update_application_command(application_id, command_id, application_command_patch_request_partial)

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):
* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.models.application_command_patch_request_partial import ApplicationCommandPatchRequestPartial
from dc_rest.models.application_command_response import ApplicationCommandResponse
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    application_id = 'application_id_example' # str | 
    command_id = 'command_id_example' # str | 
    application_command_patch_request_partial = dc_rest.ApplicationCommandPatchRequestPartial() # ApplicationCommandPatchRequestPartial | 

    try:
        api_response = await api_instance.update_application_command(application_id, command_id, application_command_patch_request_partial)
        print("The response of DefaultApi->update_application_command:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->update_application_command: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **str**|  | 
 **command_id** | **str**|  | 
 **application_command_patch_request_partial** | [**ApplicationCommandPatchRequestPartial**](ApplicationCommandPatchRequestPartial.md)|  | 

### Return type

[**ApplicationCommandResponse**](ApplicationCommandResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 response for update_application_command |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_application_emoji**
> EmojiResponse update_application_emoji(application_id, emoji_id, update_application_emoji_request)

### Example

* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.models.emoji_response import EmojiResponse
from dc_rest.models.update_application_emoji_request import UpdateApplicationEmojiRequest
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    application_id = 'application_id_example' # str | 
    emoji_id = 'emoji_id_example' # str | 
    update_application_emoji_request = dc_rest.UpdateApplicationEmojiRequest() # UpdateApplicationEmojiRequest | 

    try:
        api_response = await api_instance.update_application_emoji(application_id, emoji_id, update_application_emoji_request)
        print("The response of DefaultApi->update_application_emoji:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->update_application_emoji: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **str**|  | 
 **emoji_id** | **str**|  | 
 **update_application_emoji_request** | [**UpdateApplicationEmojiRequest**](UpdateApplicationEmojiRequest.md)|  | 

### Return type

[**EmojiResponse**](EmojiResponse.md)

### Authorization

[BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 response for update_application_emoji |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_application_role_connections_metadata**
> List[ApplicationRoleConnectionsMetadataItemResponse] update_application_role_connections_metadata(application_id, application_role_connections_metadata_item_request)

### Example

* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.models.application_role_connections_metadata_item_request import ApplicationRoleConnectionsMetadataItemRequest
from dc_rest.models.application_role_connections_metadata_item_response import ApplicationRoleConnectionsMetadataItemResponse
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    application_id = 'application_id_example' # str | 
    application_role_connections_metadata_item_request = [dc_rest.ApplicationRoleConnectionsMetadataItemRequest()] # List[ApplicationRoleConnectionsMetadataItemRequest] | 

    try:
        api_response = await api_instance.update_application_role_connections_metadata(application_id, application_role_connections_metadata_item_request)
        print("The response of DefaultApi->update_application_role_connections_metadata:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->update_application_role_connections_metadata: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **str**|  | 
 **application_role_connections_metadata_item_request** | [**List[ApplicationRoleConnectionsMetadataItemRequest]**](ApplicationRoleConnectionsMetadataItemRequest.md)|  | 

### Return type

[**List[ApplicationRoleConnectionsMetadataItemResponse]**](ApplicationRoleConnectionsMetadataItemResponse.md)

### Authorization

[BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 response for update_application_role_connections_metadata |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_application_user_role_connection**
> ApplicationUserRoleConnectionResponse update_application_user_role_connection(application_id, update_application_user_role_connection_request)

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):

```python
import dc_rest
from dc_rest.models.application_user_role_connection_response import ApplicationUserRoleConnectionResponse
from dc_rest.models.update_application_user_role_connection_request import UpdateApplicationUserRoleConnectionRequest
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    application_id = 'application_id_example' # str | 
    update_application_user_role_connection_request = dc_rest.UpdateApplicationUserRoleConnectionRequest() # UpdateApplicationUserRoleConnectionRequest | 

    try:
        api_response = await api_instance.update_application_user_role_connection(application_id, update_application_user_role_connection_request)
        print("The response of DefaultApi->update_application_user_role_connection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->update_application_user_role_connection: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **str**|  | 
 **update_application_user_role_connection_request** | [**UpdateApplicationUserRoleConnectionRequest**](UpdateApplicationUserRoleConnectionRequest.md)|  | 

### Return type

[**ApplicationUserRoleConnectionResponse**](ApplicationUserRoleConnectionResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 response for update_application_user_role_connection |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_auto_moderation_rule**
> CreateAutoModerationRule200Response update_auto_moderation_rule(guild_id, rule_id, update_auto_moderation_rule_request)

### Example

* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.models.create_auto_moderation_rule200_response import CreateAutoModerationRule200Response
from dc_rest.models.update_auto_moderation_rule_request import UpdateAutoModerationRuleRequest
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    guild_id = 'guild_id_example' # str | 
    rule_id = 'rule_id_example' # str | 
    update_auto_moderation_rule_request = dc_rest.UpdateAutoModerationRuleRequest() # UpdateAutoModerationRuleRequest | 

    try:
        api_response = await api_instance.update_auto_moderation_rule(guild_id, rule_id, update_auto_moderation_rule_request)
        print("The response of DefaultApi->update_auto_moderation_rule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->update_auto_moderation_rule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guild_id** | **str**|  | 
 **rule_id** | **str**|  | 
 **update_auto_moderation_rule_request** | [**UpdateAutoModerationRuleRequest**](UpdateAutoModerationRuleRequest.md)|  | 

### Return type

[**CreateAutoModerationRule200Response**](CreateAutoModerationRule200Response.md)

### Authorization

[BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 response for update_auto_moderation_rule |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_channel**
> GetChannel200Response update_channel(channel_id, update_channel_request)

### Example

* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.models.get_channel200_response import GetChannel200Response
from dc_rest.models.update_channel_request import UpdateChannelRequest
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    channel_id = 'channel_id_example' # str | 
    update_channel_request = dc_rest.UpdateChannelRequest() # UpdateChannelRequest | 

    try:
        api_response = await api_instance.update_channel(channel_id, update_channel_request)
        print("The response of DefaultApi->update_channel:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->update_channel: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **str**|  | 
 **update_channel_request** | [**UpdateChannelRequest**](UpdateChannelRequest.md)|  | 

### Return type

[**GetChannel200Response**](GetChannel200Response.md)

### Authorization

[BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 response for update_channel |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_guild**
> GuildResponse update_guild(guild_id, guild_patch_request_partial)

### Example

* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.models.guild_patch_request_partial import GuildPatchRequestPartial
from dc_rest.models.guild_response import GuildResponse
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    guild_id = 'guild_id_example' # str | 
    guild_patch_request_partial = dc_rest.GuildPatchRequestPartial() # GuildPatchRequestPartial | 

    try:
        api_response = await api_instance.update_guild(guild_id, guild_patch_request_partial)
        print("The response of DefaultApi->update_guild:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->update_guild: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guild_id** | **str**|  | 
 **guild_patch_request_partial** | [**GuildPatchRequestPartial**](GuildPatchRequestPartial.md)|  | 

### Return type

[**GuildResponse**](GuildResponse.md)

### Authorization

[BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 response for update_guild |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_guild_application_command**
> ApplicationCommandResponse update_guild_application_command(application_id, guild_id, command_id, application_command_patch_request_partial)

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):
* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.models.application_command_patch_request_partial import ApplicationCommandPatchRequestPartial
from dc_rest.models.application_command_response import ApplicationCommandResponse
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    application_id = 'application_id_example' # str | 
    guild_id = 'guild_id_example' # str | 
    command_id = 'command_id_example' # str | 
    application_command_patch_request_partial = dc_rest.ApplicationCommandPatchRequestPartial() # ApplicationCommandPatchRequestPartial | 

    try:
        api_response = await api_instance.update_guild_application_command(application_id, guild_id, command_id, application_command_patch_request_partial)
        print("The response of DefaultApi->update_guild_application_command:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->update_guild_application_command: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **str**|  | 
 **guild_id** | **str**|  | 
 **command_id** | **str**|  | 
 **application_command_patch_request_partial** | [**ApplicationCommandPatchRequestPartial**](ApplicationCommandPatchRequestPartial.md)|  | 

### Return type

[**ApplicationCommandResponse**](ApplicationCommandResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 response for update_guild_application_command |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_guild_emoji**
> EmojiResponse update_guild_emoji(guild_id, emoji_id, update_guild_emoji_request)

### Example

* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.models.emoji_response import EmojiResponse
from dc_rest.models.update_guild_emoji_request import UpdateGuildEmojiRequest
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    guild_id = 'guild_id_example' # str | 
    emoji_id = 'emoji_id_example' # str | 
    update_guild_emoji_request = dc_rest.UpdateGuildEmojiRequest() # UpdateGuildEmojiRequest | 

    try:
        api_response = await api_instance.update_guild_emoji(guild_id, emoji_id, update_guild_emoji_request)
        print("The response of DefaultApi->update_guild_emoji:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->update_guild_emoji: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guild_id** | **str**|  | 
 **emoji_id** | **str**|  | 
 **update_guild_emoji_request** | [**UpdateGuildEmojiRequest**](UpdateGuildEmojiRequest.md)|  | 

### Return type

[**EmojiResponse**](EmojiResponse.md)

### Authorization

[BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 response for update_guild_emoji |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_guild_member**
> GuildMemberResponse update_guild_member(guild_id, user_id, update_guild_member_request)

### Example

* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.models.guild_member_response import GuildMemberResponse
from dc_rest.models.update_guild_member_request import UpdateGuildMemberRequest
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    guild_id = 'guild_id_example' # str | 
    user_id = 'user_id_example' # str | 
    update_guild_member_request = dc_rest.UpdateGuildMemberRequest() # UpdateGuildMemberRequest | 

    try:
        api_response = await api_instance.update_guild_member(guild_id, user_id, update_guild_member_request)
        print("The response of DefaultApi->update_guild_member:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->update_guild_member: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guild_id** | **str**|  | 
 **user_id** | **str**|  | 
 **update_guild_member_request** | [**UpdateGuildMemberRequest**](UpdateGuildMemberRequest.md)|  | 

### Return type

[**GuildMemberResponse**](GuildMemberResponse.md)

### Authorization

[BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 response for update_guild_member |  -  |
**204** | 204 response for update_guild_member |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_guild_role**
> GuildRoleResponse update_guild_role(guild_id, role_id, create_guild_role_request)

### Example

* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.models.create_guild_role_request import CreateGuildRoleRequest
from dc_rest.models.guild_role_response import GuildRoleResponse
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    guild_id = 'guild_id_example' # str | 
    role_id = 'role_id_example' # str | 
    create_guild_role_request = dc_rest.CreateGuildRoleRequest() # CreateGuildRoleRequest | 

    try:
        api_response = await api_instance.update_guild_role(guild_id, role_id, create_guild_role_request)
        print("The response of DefaultApi->update_guild_role:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->update_guild_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guild_id** | **str**|  | 
 **role_id** | **str**|  | 
 **create_guild_role_request** | [**CreateGuildRoleRequest**](CreateGuildRoleRequest.md)|  | 

### Return type

[**GuildRoleResponse**](GuildRoleResponse.md)

### Authorization

[BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 response for update_guild_role |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_guild_scheduled_event**
> ListGuildScheduledEvents200ResponseInner update_guild_scheduled_event(guild_id, guild_scheduled_event_id, update_guild_scheduled_event_request)

### Example

* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.models.list_guild_scheduled_events200_response_inner import ListGuildScheduledEvents200ResponseInner
from dc_rest.models.update_guild_scheduled_event_request import UpdateGuildScheduledEventRequest
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    guild_id = 'guild_id_example' # str | 
    guild_scheduled_event_id = 'guild_scheduled_event_id_example' # str | 
    update_guild_scheduled_event_request = dc_rest.UpdateGuildScheduledEventRequest() # UpdateGuildScheduledEventRequest | 

    try:
        api_response = await api_instance.update_guild_scheduled_event(guild_id, guild_scheduled_event_id, update_guild_scheduled_event_request)
        print("The response of DefaultApi->update_guild_scheduled_event:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->update_guild_scheduled_event: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guild_id** | **str**|  | 
 **guild_scheduled_event_id** | **str**|  | 
 **update_guild_scheduled_event_request** | [**UpdateGuildScheduledEventRequest**](UpdateGuildScheduledEventRequest.md)|  | 

### Return type

[**ListGuildScheduledEvents200ResponseInner**](ListGuildScheduledEvents200ResponseInner.md)

### Authorization

[BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 response for update_guild_scheduled_event |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_guild_soundboard_sound**
> SoundboardSoundResponse update_guild_soundboard_sound(guild_id, sound_id, soundboard_patch_request_partial)

### Example

* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.models.soundboard_patch_request_partial import SoundboardPatchRequestPartial
from dc_rest.models.soundboard_sound_response import SoundboardSoundResponse
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    guild_id = 'guild_id_example' # str | 
    sound_id = 'sound_id_example' # str | 
    soundboard_patch_request_partial = dc_rest.SoundboardPatchRequestPartial() # SoundboardPatchRequestPartial | 

    try:
        api_response = await api_instance.update_guild_soundboard_sound(guild_id, sound_id, soundboard_patch_request_partial)
        print("The response of DefaultApi->update_guild_soundboard_sound:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->update_guild_soundboard_sound: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guild_id** | **str**|  | 
 **sound_id** | **str**|  | 
 **soundboard_patch_request_partial** | [**SoundboardPatchRequestPartial**](SoundboardPatchRequestPartial.md)|  | 

### Return type

[**SoundboardSoundResponse**](SoundboardSoundResponse.md)

### Authorization

[BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 response for update_guild_soundboard_sound |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_guild_sticker**
> GuildStickerResponse update_guild_sticker(guild_id, sticker_id, update_guild_sticker_request)

### Example

* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.models.guild_sticker_response import GuildStickerResponse
from dc_rest.models.update_guild_sticker_request import UpdateGuildStickerRequest
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    guild_id = 'guild_id_example' # str | 
    sticker_id = 'sticker_id_example' # str | 
    update_guild_sticker_request = dc_rest.UpdateGuildStickerRequest() # UpdateGuildStickerRequest | 

    try:
        api_response = await api_instance.update_guild_sticker(guild_id, sticker_id, update_guild_sticker_request)
        print("The response of DefaultApi->update_guild_sticker:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->update_guild_sticker: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guild_id** | **str**|  | 
 **sticker_id** | **str**|  | 
 **update_guild_sticker_request** | [**UpdateGuildStickerRequest**](UpdateGuildStickerRequest.md)|  | 

### Return type

[**GuildStickerResponse**](GuildStickerResponse.md)

### Authorization

[BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 response for update_guild_sticker |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_guild_template**
> GuildTemplateResponse update_guild_template(guild_id, code, update_guild_template_request)

### Example

* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.models.guild_template_response import GuildTemplateResponse
from dc_rest.models.update_guild_template_request import UpdateGuildTemplateRequest
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    guild_id = 'guild_id_example' # str | 
    code = 'code_example' # str | 
    update_guild_template_request = dc_rest.UpdateGuildTemplateRequest() # UpdateGuildTemplateRequest | 

    try:
        api_response = await api_instance.update_guild_template(guild_id, code, update_guild_template_request)
        print("The response of DefaultApi->update_guild_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->update_guild_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guild_id** | **str**|  | 
 **code** | **str**|  | 
 **update_guild_template_request** | [**UpdateGuildTemplateRequest**](UpdateGuildTemplateRequest.md)|  | 

### Return type

[**GuildTemplateResponse**](GuildTemplateResponse.md)

### Authorization

[BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 response for update_guild_template |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_guild_welcome_screen**
> GuildWelcomeScreenResponse update_guild_welcome_screen(guild_id, welcome_screen_patch_request_partial)

### Example

* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.models.guild_welcome_screen_response import GuildWelcomeScreenResponse
from dc_rest.models.welcome_screen_patch_request_partial import WelcomeScreenPatchRequestPartial
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    guild_id = 'guild_id_example' # str | 
    welcome_screen_patch_request_partial = dc_rest.WelcomeScreenPatchRequestPartial() # WelcomeScreenPatchRequestPartial | 

    try:
        api_response = await api_instance.update_guild_welcome_screen(guild_id, welcome_screen_patch_request_partial)
        print("The response of DefaultApi->update_guild_welcome_screen:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->update_guild_welcome_screen: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guild_id** | **str**|  | 
 **welcome_screen_patch_request_partial** | [**WelcomeScreenPatchRequestPartial**](WelcomeScreenPatchRequestPartial.md)|  | 

### Return type

[**GuildWelcomeScreenResponse**](GuildWelcomeScreenResponse.md)

### Authorization

[BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 response for update_guild_welcome_screen |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_guild_widget_settings**
> WidgetSettingsResponse update_guild_widget_settings(guild_id, update_guild_widget_settings_request)

### Example

* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.models.update_guild_widget_settings_request import UpdateGuildWidgetSettingsRequest
from dc_rest.models.widget_settings_response import WidgetSettingsResponse
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    guild_id = 'guild_id_example' # str | 
    update_guild_widget_settings_request = dc_rest.UpdateGuildWidgetSettingsRequest() # UpdateGuildWidgetSettingsRequest | 

    try:
        api_response = await api_instance.update_guild_widget_settings(guild_id, update_guild_widget_settings_request)
        print("The response of DefaultApi->update_guild_widget_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->update_guild_widget_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guild_id** | **str**|  | 
 **update_guild_widget_settings_request** | [**UpdateGuildWidgetSettingsRequest**](UpdateGuildWidgetSettingsRequest.md)|  | 

### Return type

[**WidgetSettingsResponse**](WidgetSettingsResponse.md)

### Authorization

[BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 response for update_guild_widget_settings |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_message**
> MessageResponse update_message(channel_id, message_id, message_edit_request_partial)

### Example

* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.models.message_edit_request_partial import MessageEditRequestPartial
from dc_rest.models.message_response import MessageResponse
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    channel_id = 'channel_id_example' # str | 
    message_id = 'message_id_example' # str | 
    message_edit_request_partial = dc_rest.MessageEditRequestPartial() # MessageEditRequestPartial | 

    try:
        api_response = await api_instance.update_message(channel_id, message_id, message_edit_request_partial)
        print("The response of DefaultApi->update_message:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->update_message: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **str**|  | 
 **message_id** | **str**|  | 
 **message_edit_request_partial** | [**MessageEditRequestPartial**](MessageEditRequestPartial.md)|  | 

### Return type

[**MessageResponse**](MessageResponse.md)

### Authorization

[BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 response for update_message |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_my_application**
> PrivateApplicationResponse update_my_application(application_form_partial)

### Example

* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.models.application_form_partial import ApplicationFormPartial
from dc_rest.models.private_application_response import PrivateApplicationResponse
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    application_form_partial = dc_rest.ApplicationFormPartial() # ApplicationFormPartial | 

    try:
        api_response = await api_instance.update_my_application(application_form_partial)
        print("The response of DefaultApi->update_my_application:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->update_my_application: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_form_partial** | [**ApplicationFormPartial**](ApplicationFormPartial.md)|  | 

### Return type

[**PrivateApplicationResponse**](PrivateApplicationResponse.md)

### Authorization

[BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 response for update_my_application |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_my_guild_member**
> PrivateGuildMemberResponse update_my_guild_member(guild_id, update_my_guild_member_request)

### Example

* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.models.private_guild_member_response import PrivateGuildMemberResponse
from dc_rest.models.update_my_guild_member_request import UpdateMyGuildMemberRequest
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    guild_id = 'guild_id_example' # str | 
    update_my_guild_member_request = dc_rest.UpdateMyGuildMemberRequest() # UpdateMyGuildMemberRequest | 

    try:
        api_response = await api_instance.update_my_guild_member(guild_id, update_my_guild_member_request)
        print("The response of DefaultApi->update_my_guild_member:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->update_my_guild_member: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guild_id** | **str**|  | 
 **update_my_guild_member_request** | [**UpdateMyGuildMemberRequest**](UpdateMyGuildMemberRequest.md)|  | 

### Return type

[**PrivateGuildMemberResponse**](PrivateGuildMemberResponse.md)

### Authorization

[BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 response for update_my_guild_member |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_my_user**
> UserPIIResponse update_my_user(bot_account_patch_request)

### Example

* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.models.bot_account_patch_request import BotAccountPatchRequest
from dc_rest.models.user_pii_response import UserPIIResponse
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    bot_account_patch_request = dc_rest.BotAccountPatchRequest() # BotAccountPatchRequest | 

    try:
        api_response = await api_instance.update_my_user(bot_account_patch_request)
        print("The response of DefaultApi->update_my_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->update_my_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bot_account_patch_request** | [**BotAccountPatchRequest**](BotAccountPatchRequest.md)|  | 

### Return type

[**UserPIIResponse**](UserPIIResponse.md)

### Authorization

[BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 response for update_my_user |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_original_webhook_message**
> MessageResponse update_original_webhook_message(webhook_id, webhook_token, incoming_webhook_update_request_partial, thread_id=thread_id, with_components=with_components)

### Example

* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.models.incoming_webhook_update_request_partial import IncomingWebhookUpdateRequestPartial
from dc_rest.models.message_response import MessageResponse
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    webhook_id = 'webhook_id_example' # str | 
    webhook_token = 'webhook_token_example' # str | 
    incoming_webhook_update_request_partial = dc_rest.IncomingWebhookUpdateRequestPartial() # IncomingWebhookUpdateRequestPartial | 
    thread_id = 'thread_id_example' # str |  (optional)
    with_components = True # bool |  (optional)

    try:
        api_response = await api_instance.update_original_webhook_message(webhook_id, webhook_token, incoming_webhook_update_request_partial, thread_id=thread_id, with_components=with_components)
        print("The response of DefaultApi->update_original_webhook_message:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->update_original_webhook_message: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhook_id** | **str**|  | 
 **webhook_token** | **str**|  | 
 **incoming_webhook_update_request_partial** | [**IncomingWebhookUpdateRequestPartial**](IncomingWebhookUpdateRequestPartial.md)|  | 
 **thread_id** | **str**|  | [optional] 
 **with_components** | **bool**|  | [optional] 

### Return type

[**MessageResponse**](MessageResponse.md)

### Authorization

[BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 response for update_original_webhook_message |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_self_voice_state**
> update_self_voice_state(guild_id, update_self_voice_state_request)

### Example

* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.models.update_self_voice_state_request import UpdateSelfVoiceStateRequest
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    guild_id = 'guild_id_example' # str | 
    update_self_voice_state_request = dc_rest.UpdateSelfVoiceStateRequest() # UpdateSelfVoiceStateRequest | 

    try:
        await api_instance.update_self_voice_state(guild_id, update_self_voice_state_request)
    except Exception as e:
        print("Exception when calling DefaultApi->update_self_voice_state: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guild_id** | **str**|  | 
 **update_self_voice_state_request** | [**UpdateSelfVoiceStateRequest**](UpdateSelfVoiceStateRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | 204 response for update_self_voice_state |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_stage_instance**
> StageInstanceResponse update_stage_instance(channel_id, update_stage_instance_request)

### Example

* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.models.stage_instance_response import StageInstanceResponse
from dc_rest.models.update_stage_instance_request import UpdateStageInstanceRequest
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    channel_id = 'channel_id_example' # str | 
    update_stage_instance_request = dc_rest.UpdateStageInstanceRequest() # UpdateStageInstanceRequest | 

    try:
        api_response = await api_instance.update_stage_instance(channel_id, update_stage_instance_request)
        print("The response of DefaultApi->update_stage_instance:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->update_stage_instance: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **str**|  | 
 **update_stage_instance_request** | [**UpdateStageInstanceRequest**](UpdateStageInstanceRequest.md)|  | 

### Return type

[**StageInstanceResponse**](StageInstanceResponse.md)

### Authorization

[BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 response for update_stage_instance |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_voice_state**
> update_voice_state(guild_id, user_id, update_voice_state_request)

### Example

* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.models.update_voice_state_request import UpdateVoiceStateRequest
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    guild_id = 'guild_id_example' # str | 
    user_id = 'user_id_example' # str | 
    update_voice_state_request = dc_rest.UpdateVoiceStateRequest() # UpdateVoiceStateRequest | 

    try:
        await api_instance.update_voice_state(guild_id, user_id, update_voice_state_request)
    except Exception as e:
        print("Exception when calling DefaultApi->update_voice_state: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guild_id** | **str**|  | 
 **user_id** | **str**|  | 
 **update_voice_state_request** | [**UpdateVoiceStateRequest**](UpdateVoiceStateRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | 204 response for update_voice_state |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_webhook**
> ListChannelWebhooks200ResponseInner update_webhook(webhook_id, update_webhook_request)

### Example

* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.models.list_channel_webhooks200_response_inner import ListChannelWebhooks200ResponseInner
from dc_rest.models.update_webhook_request import UpdateWebhookRequest
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    webhook_id = 'webhook_id_example' # str | 
    update_webhook_request = dc_rest.UpdateWebhookRequest() # UpdateWebhookRequest | 

    try:
        api_response = await api_instance.update_webhook(webhook_id, update_webhook_request)
        print("The response of DefaultApi->update_webhook:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->update_webhook: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhook_id** | **str**|  | 
 **update_webhook_request** | [**UpdateWebhookRequest**](UpdateWebhookRequest.md)|  | 

### Return type

[**ListChannelWebhooks200ResponseInner**](ListChannelWebhooks200ResponseInner.md)

### Authorization

[BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 response for update_webhook |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_webhook_by_token**
> ListChannelWebhooks200ResponseInner update_webhook_by_token(webhook_id, webhook_token, update_webhook_by_token_request)

### Example

* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.models.list_channel_webhooks200_response_inner import ListChannelWebhooks200ResponseInner
from dc_rest.models.update_webhook_by_token_request import UpdateWebhookByTokenRequest
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    webhook_id = 'webhook_id_example' # str | 
    webhook_token = 'webhook_token_example' # str | 
    update_webhook_by_token_request = dc_rest.UpdateWebhookByTokenRequest() # UpdateWebhookByTokenRequest | 

    try:
        api_response = await api_instance.update_webhook_by_token(webhook_id, webhook_token, update_webhook_by_token_request)
        print("The response of DefaultApi->update_webhook_by_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->update_webhook_by_token: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhook_id** | **str**|  | 
 **webhook_token** | **str**|  | 
 **update_webhook_by_token_request** | [**UpdateWebhookByTokenRequest**](UpdateWebhookByTokenRequest.md)|  | 

### Return type

[**ListChannelWebhooks200ResponseInner**](ListChannelWebhooks200ResponseInner.md)

### Authorization

[BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 response for update_webhook_by_token |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_webhook_message**
> MessageResponse update_webhook_message(webhook_id, webhook_token, message_id, incoming_webhook_update_request_partial, thread_id=thread_id, with_components=with_components)

### Example

* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.models.incoming_webhook_update_request_partial import IncomingWebhookUpdateRequestPartial
from dc_rest.models.message_response import MessageResponse
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    webhook_id = 'webhook_id_example' # str | 
    webhook_token = 'webhook_token_example' # str | 
    message_id = 'message_id_example' # str | 
    incoming_webhook_update_request_partial = dc_rest.IncomingWebhookUpdateRequestPartial() # IncomingWebhookUpdateRequestPartial | 
    thread_id = 'thread_id_example' # str |  (optional)
    with_components = True # bool |  (optional)

    try:
        api_response = await api_instance.update_webhook_message(webhook_id, webhook_token, message_id, incoming_webhook_update_request_partial, thread_id=thread_id, with_components=with_components)
        print("The response of DefaultApi->update_webhook_message:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->update_webhook_message: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhook_id** | **str**|  | 
 **webhook_token** | **str**|  | 
 **message_id** | **str**|  | 
 **incoming_webhook_update_request_partial** | [**IncomingWebhookUpdateRequestPartial**](IncomingWebhookUpdateRequestPartial.md)|  | 
 **thread_id** | **str**|  | [optional] 
 **with_components** | **bool**|  | [optional] 

### Return type

[**MessageResponse**](MessageResponse.md)

### Authorization

[BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 response for update_webhook_message |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_application_attachment**
> ActivitiesAttachmentResponse upload_application_attachment(application_id, file)

### Example

* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):
* OAuth Authentication (OAuth2):
* Api Key Authentication (BotToken):

```python
import dc_rest
from dc_rest.models.activities_attachment_response import ActivitiesAttachmentResponse
from dc_rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://discord.com/api/v10
# See configuration.py for a list of all supported configuration parameters.
configuration = dc_rest.Configuration(
    host = "https://discord.com/api/v10"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure API key authorization: BotToken
configuration.api_key['BotToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BotToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with dc_rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dc_rest.DefaultApi(api_client)
    application_id = 'application_id_example' # str | 
    file = 'file_example' # str | 

    try:
        api_response = await api_instance.upload_application_attachment(application_id, file)
        print("The response of DefaultApi->upload_application_attachment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->upload_application_attachment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **str**|  | 
 **file** | **str**|  | 

### Return type

[**ActivitiesAttachmentResponse**](ActivitiesAttachmentResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [BotToken](../README.md#BotToken)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 response for upload_application_attachment |  -  |
**4XX** | Client error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

