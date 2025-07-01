# coding: utf-8

"""
Discord HTTP API (Preview) - REST API Client
Preview of the Discord v10 HTTP API specification. See https://discord.com/developers/docs for more details.

## Metadata

- **Copyright**: Copyright (c) 2025 Qntx
- **Author**: ΣX <gitctrlx@gmail.com>
- **Version**: 10
- **Modified**: 2025-07-01T06:33:02.994204459Z[Etc/UTC]
- **Generator Version**: 7.14.0

<details>
<summary><strong>⚠️ Important Disclaimer & Limitation of Liability</strong></summary>
<br>
> **IMPORTANT**: This software is provided "as is" without any warranties, express or implied, including but not limited
> to warranties of merchantability, fitness for a particular purpose, or non-infringement. The developers, contributors,
> and licensors (collectively, "Developers") make no representations regarding the accuracy, completeness, or reliability
> of this software or its outputs.
>
> This client is not intended to provide financial, investment, tax, or legal advice. It facilitates interaction with the
> Discord HTTP API (Preview) service but does not endorse or recommend any financial actions, including the purchase, sale, or holding of
> financial instruments (e.g., stocks, bonds, derivatives, cryptocurrencies). Users must consult qualified financial or
> legal professionals before making decisions based on this software's outputs.
>
> Financial markets are inherently speculative and carry significant risks. Using this software in trading, analysis, or
> other financial activities may result in substantial losses, including total loss of capital. The Developers are not
> liable for any losses or damages arising from such use. Users assume full responsibility for validating the software's
> outputs and ensuring their suitability for intended purposes.
>
> This client may rely on third-party data or services (e.g., market feeds, APIs). The Developers do not control or verify
> the accuracy of these services and are not liable for any errors, delays, or losses resulting from their use. Users must
> comply with third-party terms and conditions.
>
> Users are solely responsible for ensuring compliance with all applicable financial, tax, and regulatory requirements in
> their jurisdiction. This includes obtaining necessary licenses or approvals for trading or investment activities. The
> Developers disclaim liability for any legal consequences arising from non-compliance.
>
> To the fullest extent permitted by law, the Developers shall not be liable for any direct, indirect, incidental,
> consequential, or punitive damages arising from the use or inability to use this software, including but not limited to
> loss of profits, data, or business opportunities.

</details>
"""  # noqa: E501


import unittest

from dc_rest.api.default_api import DefaultApi


class TestDefaultApi(unittest.IsolatedAsyncioTestCase):
    """DefaultApi unit test stubs"""

    async def asyncSetUp(self) -> None:
        self.api = DefaultApi()

    async def asyncTearDown(self) -> None:
        await self.api.api_client.close()

    async def test_add_group_dm_user(self) -> None:
        """Test case for add_group_dm_user

        """
        pass

    async def test_add_guild_member(self) -> None:
        """Test case for add_guild_member

        """
        pass

    async def test_add_guild_member_role(self) -> None:
        """Test case for add_guild_member_role

        """
        pass

    async def test_add_lobby_member(self) -> None:
        """Test case for add_lobby_member

        """
        pass

    async def test_add_my_message_reaction(self) -> None:
        """Test case for add_my_message_reaction

        """
        pass

    async def test_add_thread_member(self) -> None:
        """Test case for add_thread_member

        """
        pass

    async def test_applications_get_activity_instance(self) -> None:
        """Test case for applications_get_activity_instance

        """
        pass

    async def test_ban_user_from_guild(self) -> None:
        """Test case for ban_user_from_guild

        """
        pass

    async def test_bulk_ban_users_from_guild(self) -> None:
        """Test case for bulk_ban_users_from_guild

        """
        pass

    async def test_bulk_delete_messages(self) -> None:
        """Test case for bulk_delete_messages

        """
        pass

    async def test_bulk_set_application_commands(self) -> None:
        """Test case for bulk_set_application_commands

        """
        pass

    async def test_bulk_set_guild_application_commands(self) -> None:
        """Test case for bulk_set_guild_application_commands

        """
        pass

    async def test_bulk_update_guild_channels(self) -> None:
        """Test case for bulk_update_guild_channels

        """
        pass

    async def test_bulk_update_guild_roles(self) -> None:
        """Test case for bulk_update_guild_roles

        """
        pass

    async def test_bulk_update_lobby_members(self) -> None:
        """Test case for bulk_update_lobby_members

        """
        pass

    async def test_consume_entitlement(self) -> None:
        """Test case for consume_entitlement

        """
        pass

    async def test_create_application_command(self) -> None:
        """Test case for create_application_command

        """
        pass

    async def test_create_application_emoji(self) -> None:
        """Test case for create_application_emoji

        """
        pass

    async def test_create_auto_moderation_rule(self) -> None:
        """Test case for create_auto_moderation_rule

        """
        pass

    async def test_create_channel_invite(self) -> None:
        """Test case for create_channel_invite

        """
        pass

    async def test_create_dm(self) -> None:
        """Test case for create_dm

        """
        pass

    async def test_create_entitlement(self) -> None:
        """Test case for create_entitlement

        """
        pass

    async def test_create_guild(self) -> None:
        """Test case for create_guild

        """
        pass

    async def test_create_guild_application_command(self) -> None:
        """Test case for create_guild_application_command

        """
        pass

    async def test_create_guild_channel(self) -> None:
        """Test case for create_guild_channel

        """
        pass

    async def test_create_guild_emoji(self) -> None:
        """Test case for create_guild_emoji

        """
        pass

    async def test_create_guild_from_template(self) -> None:
        """Test case for create_guild_from_template

        """
        pass

    async def test_create_guild_role(self) -> None:
        """Test case for create_guild_role

        """
        pass

    async def test_create_guild_scheduled_event(self) -> None:
        """Test case for create_guild_scheduled_event

        """
        pass

    async def test_create_guild_soundboard_sound(self) -> None:
        """Test case for create_guild_soundboard_sound

        """
        pass

    async def test_create_guild_sticker(self) -> None:
        """Test case for create_guild_sticker

        """
        pass

    async def test_create_guild_template(self) -> None:
        """Test case for create_guild_template

        """
        pass

    async def test_create_interaction_response(self) -> None:
        """Test case for create_interaction_response

        """
        pass

    async def test_create_lobby(self) -> None:
        """Test case for create_lobby

        """
        pass

    async def test_create_lobby_message(self) -> None:
        """Test case for create_lobby_message

        """
        pass

    async def test_create_message(self) -> None:
        """Test case for create_message

        """
        pass

    async def test_create_or_join_lobby(self) -> None:
        """Test case for create_or_join_lobby

        """
        pass

    async def test_create_pin(self) -> None:
        """Test case for create_pin

        """
        pass

    async def test_create_stage_instance(self) -> None:
        """Test case for create_stage_instance

        """
        pass

    async def test_create_thread(self) -> None:
        """Test case for create_thread

        """
        pass

    async def test_create_thread_from_message(self) -> None:
        """Test case for create_thread_from_message

        """
        pass

    async def test_create_webhook(self) -> None:
        """Test case for create_webhook

        """
        pass

    async def test_crosspost_message(self) -> None:
        """Test case for crosspost_message

        """
        pass

    async def test_delete_all_message_reactions(self) -> None:
        """Test case for delete_all_message_reactions

        """
        pass

    async def test_delete_all_message_reactions_by_emoji(self) -> None:
        """Test case for delete_all_message_reactions_by_emoji

        """
        pass

    async def test_delete_application_command(self) -> None:
        """Test case for delete_application_command

        """
        pass

    async def test_delete_application_emoji(self) -> None:
        """Test case for delete_application_emoji

        """
        pass

    async def test_delete_application_user_role_connection(self) -> None:
        """Test case for delete_application_user_role_connection

        """
        pass

    async def test_delete_auto_moderation_rule(self) -> None:
        """Test case for delete_auto_moderation_rule

        """
        pass

    async def test_delete_channel(self) -> None:
        """Test case for delete_channel

        """
        pass

    async def test_delete_channel_permission_overwrite(self) -> None:
        """Test case for delete_channel_permission_overwrite

        """
        pass

    async def test_delete_entitlement(self) -> None:
        """Test case for delete_entitlement

        """
        pass

    async def test_delete_group_dm_user(self) -> None:
        """Test case for delete_group_dm_user

        """
        pass

    async def test_delete_guild(self) -> None:
        """Test case for delete_guild

        """
        pass

    async def test_delete_guild_application_command(self) -> None:
        """Test case for delete_guild_application_command

        """
        pass

    async def test_delete_guild_emoji(self) -> None:
        """Test case for delete_guild_emoji

        """
        pass

    async def test_delete_guild_integration(self) -> None:
        """Test case for delete_guild_integration

        """
        pass

    async def test_delete_guild_member(self) -> None:
        """Test case for delete_guild_member

        """
        pass

    async def test_delete_guild_member_role(self) -> None:
        """Test case for delete_guild_member_role

        """
        pass

    async def test_delete_guild_role(self) -> None:
        """Test case for delete_guild_role

        """
        pass

    async def test_delete_guild_scheduled_event(self) -> None:
        """Test case for delete_guild_scheduled_event

        """
        pass

    async def test_delete_guild_soundboard_sound(self) -> None:
        """Test case for delete_guild_soundboard_sound

        """
        pass

    async def test_delete_guild_sticker(self) -> None:
        """Test case for delete_guild_sticker

        """
        pass

    async def test_delete_guild_template(self) -> None:
        """Test case for delete_guild_template

        """
        pass

    async def test_delete_lobby_member(self) -> None:
        """Test case for delete_lobby_member

        """
        pass

    async def test_delete_message(self) -> None:
        """Test case for delete_message

        """
        pass

    async def test_delete_my_message_reaction(self) -> None:
        """Test case for delete_my_message_reaction

        """
        pass

    async def test_delete_original_webhook_message(self) -> None:
        """Test case for delete_original_webhook_message

        """
        pass

    async def test_delete_pin(self) -> None:
        """Test case for delete_pin

        """
        pass

    async def test_delete_stage_instance(self) -> None:
        """Test case for delete_stage_instance

        """
        pass

    async def test_delete_thread_member(self) -> None:
        """Test case for delete_thread_member

        """
        pass

    async def test_delete_user_message_reaction(self) -> None:
        """Test case for delete_user_message_reaction

        """
        pass

    async def test_delete_webhook(self) -> None:
        """Test case for delete_webhook

        """
        pass

    async def test_delete_webhook_by_token(self) -> None:
        """Test case for delete_webhook_by_token

        """
        pass

    async def test_delete_webhook_message(self) -> None:
        """Test case for delete_webhook_message

        """
        pass

    async def test_deprecated_create_pin(self) -> None:
        """Test case for deprecated_create_pin

        """
        pass

    async def test_deprecated_delete_pin(self) -> None:
        """Test case for deprecated_delete_pin

        """
        pass

    async def test_deprecated_list_pins(self) -> None:
        """Test case for deprecated_list_pins

        """
        pass

    async def test_edit_lobby(self) -> None:
        """Test case for edit_lobby

        """
        pass

    async def test_edit_lobby_channel_link(self) -> None:
        """Test case for edit_lobby_channel_link

        """
        pass

    async def test_execute_github_compatible_webhook(self) -> None:
        """Test case for execute_github_compatible_webhook

        """
        pass

    async def test_execute_slack_compatible_webhook(self) -> None:
        """Test case for execute_slack_compatible_webhook

        """
        pass

    async def test_execute_webhook(self) -> None:
        """Test case for execute_webhook

        """
        pass

    async def test_follow_channel(self) -> None:
        """Test case for follow_channel

        """
        pass

    async def test_get_active_guild_threads(self) -> None:
        """Test case for get_active_guild_threads

        """
        pass

    async def test_get_answer_voters(self) -> None:
        """Test case for get_answer_voters

        """
        pass

    async def test_get_application(self) -> None:
        """Test case for get_application

        """
        pass

    async def test_get_application_command(self) -> None:
        """Test case for get_application_command

        """
        pass

    async def test_get_application_emoji(self) -> None:
        """Test case for get_application_emoji

        """
        pass

    async def test_get_application_role_connections_metadata(self) -> None:
        """Test case for get_application_role_connections_metadata

        """
        pass

    async def test_get_application_user_role_connection(self) -> None:
        """Test case for get_application_user_role_connection

        """
        pass

    async def test_get_auto_moderation_rule(self) -> None:
        """Test case for get_auto_moderation_rule

        """
        pass

    async def test_get_bot_gateway(self) -> None:
        """Test case for get_bot_gateway

        """
        pass

    async def test_get_channel(self) -> None:
        """Test case for get_channel

        """
        pass

    async def test_get_entitlement(self) -> None:
        """Test case for get_entitlement

        """
        pass

    async def test_get_entitlements(self) -> None:
        """Test case for get_entitlements

        """
        pass

    async def test_get_gateway(self) -> None:
        """Test case for get_gateway

        """
        pass

    async def test_get_guild(self) -> None:
        """Test case for get_guild

        """
        pass

    async def test_get_guild_application_command(self) -> None:
        """Test case for get_guild_application_command

        """
        pass

    async def test_get_guild_application_command_permissions(self) -> None:
        """Test case for get_guild_application_command_permissions

        """
        pass

    async def test_get_guild_ban(self) -> None:
        """Test case for get_guild_ban

        """
        pass

    async def test_get_guild_emoji(self) -> None:
        """Test case for get_guild_emoji

        """
        pass

    async def test_get_guild_member(self) -> None:
        """Test case for get_guild_member

        """
        pass

    async def test_get_guild_new_member_welcome(self) -> None:
        """Test case for get_guild_new_member_welcome

        """
        pass

    async def test_get_guild_preview(self) -> None:
        """Test case for get_guild_preview

        """
        pass

    async def test_get_guild_role(self) -> None:
        """Test case for get_guild_role

        """
        pass

    async def test_get_guild_scheduled_event(self) -> None:
        """Test case for get_guild_scheduled_event

        """
        pass

    async def test_get_guild_soundboard_sound(self) -> None:
        """Test case for get_guild_soundboard_sound

        """
        pass

    async def test_get_guild_sticker(self) -> None:
        """Test case for get_guild_sticker

        """
        pass

    async def test_get_guild_template(self) -> None:
        """Test case for get_guild_template

        """
        pass

    async def test_get_guild_vanity_url(self) -> None:
        """Test case for get_guild_vanity_url

        """
        pass

    async def test_get_guild_webhooks(self) -> None:
        """Test case for get_guild_webhooks

        """
        pass

    async def test_get_guild_welcome_screen(self) -> None:
        """Test case for get_guild_welcome_screen

        """
        pass

    async def test_get_guild_widget(self) -> None:
        """Test case for get_guild_widget

        """
        pass

    async def test_get_guild_widget_png(self) -> None:
        """Test case for get_guild_widget_png

        """
        pass

    async def test_get_guild_widget_settings(self) -> None:
        """Test case for get_guild_widget_settings

        """
        pass

    async def test_get_guilds_onboarding(self) -> None:
        """Test case for get_guilds_onboarding

        """
        pass

    async def test_get_lobby(self) -> None:
        """Test case for get_lobby

        """
        pass

    async def test_get_lobby_messages(self) -> None:
        """Test case for get_lobby_messages

        """
        pass

    async def test_get_message(self) -> None:
        """Test case for get_message

        """
        pass

    async def test_get_my_application(self) -> None:
        """Test case for get_my_application

        """
        pass

    async def test_get_my_guild_member(self) -> None:
        """Test case for get_my_guild_member

        """
        pass

    async def test_get_my_oauth2_application(self) -> None:
        """Test case for get_my_oauth2_application

        """
        pass

    async def test_get_my_oauth2_authorization(self) -> None:
        """Test case for get_my_oauth2_authorization

        """
        pass

    async def test_get_my_user(self) -> None:
        """Test case for get_my_user

        """
        pass

    async def test_get_openid_connect_userinfo(self) -> None:
        """Test case for get_openid_connect_userinfo

        """
        pass

    async def test_get_original_webhook_message(self) -> None:
        """Test case for get_original_webhook_message

        """
        pass

    async def test_get_public_keys(self) -> None:
        """Test case for get_public_keys

        """
        pass

    async def test_get_self_voice_state(self) -> None:
        """Test case for get_self_voice_state

        """
        pass

    async def test_get_soundboard_default_sounds(self) -> None:
        """Test case for get_soundboard_default_sounds

        """
        pass

    async def test_get_stage_instance(self) -> None:
        """Test case for get_stage_instance

        """
        pass

    async def test_get_sticker(self) -> None:
        """Test case for get_sticker

        """
        pass

    async def test_get_sticker_pack(self) -> None:
        """Test case for get_sticker_pack

        """
        pass

    async def test_get_thread_member(self) -> None:
        """Test case for get_thread_member

        """
        pass

    async def test_get_user(self) -> None:
        """Test case for get_user

        """
        pass

    async def test_get_voice_state(self) -> None:
        """Test case for get_voice_state

        """
        pass

    async def test_get_webhook(self) -> None:
        """Test case for get_webhook

        """
        pass

    async def test_get_webhook_by_token(self) -> None:
        """Test case for get_webhook_by_token

        """
        pass

    async def test_get_webhook_message(self) -> None:
        """Test case for get_webhook_message

        """
        pass

    async def test_invite_resolve(self) -> None:
        """Test case for invite_resolve

        """
        pass

    async def test_invite_revoke(self) -> None:
        """Test case for invite_revoke

        """
        pass

    async def test_join_thread(self) -> None:
        """Test case for join_thread

        """
        pass

    async def test_leave_guild(self) -> None:
        """Test case for leave_guild

        """
        pass

    async def test_leave_lobby(self) -> None:
        """Test case for leave_lobby

        """
        pass

    async def test_leave_thread(self) -> None:
        """Test case for leave_thread

        """
        pass

    async def test_list_application_commands(self) -> None:
        """Test case for list_application_commands

        """
        pass

    async def test_list_application_emojis(self) -> None:
        """Test case for list_application_emojis

        """
        pass

    async def test_list_auto_moderation_rules(self) -> None:
        """Test case for list_auto_moderation_rules

        """
        pass

    async def test_list_channel_invites(self) -> None:
        """Test case for list_channel_invites

        """
        pass

    async def test_list_channel_webhooks(self) -> None:
        """Test case for list_channel_webhooks

        """
        pass

    async def test_list_guild_application_command_permissions(self) -> None:
        """Test case for list_guild_application_command_permissions

        """
        pass

    async def test_list_guild_application_commands(self) -> None:
        """Test case for list_guild_application_commands

        """
        pass

    async def test_list_guild_audit_log_entries(self) -> None:
        """Test case for list_guild_audit_log_entries

        """
        pass

    async def test_list_guild_bans(self) -> None:
        """Test case for list_guild_bans

        """
        pass

    async def test_list_guild_channels(self) -> None:
        """Test case for list_guild_channels

        """
        pass

    async def test_list_guild_emojis(self) -> None:
        """Test case for list_guild_emojis

        """
        pass

    async def test_list_guild_integrations(self) -> None:
        """Test case for list_guild_integrations

        """
        pass

    async def test_list_guild_invites(self) -> None:
        """Test case for list_guild_invites

        """
        pass

    async def test_list_guild_members(self) -> None:
        """Test case for list_guild_members

        """
        pass

    async def test_list_guild_roles(self) -> None:
        """Test case for list_guild_roles

        """
        pass

    async def test_list_guild_scheduled_event_users(self) -> None:
        """Test case for list_guild_scheduled_event_users

        """
        pass

    async def test_list_guild_scheduled_events(self) -> None:
        """Test case for list_guild_scheduled_events

        """
        pass

    async def test_list_guild_soundboard_sounds(self) -> None:
        """Test case for list_guild_soundboard_sounds

        """
        pass

    async def test_list_guild_stickers(self) -> None:
        """Test case for list_guild_stickers

        """
        pass

    async def test_list_guild_templates(self) -> None:
        """Test case for list_guild_templates

        """
        pass

    async def test_list_guild_voice_regions(self) -> None:
        """Test case for list_guild_voice_regions

        """
        pass

    async def test_list_message_reactions_by_emoji(self) -> None:
        """Test case for list_message_reactions_by_emoji

        """
        pass

    async def test_list_messages(self) -> None:
        """Test case for list_messages

        """
        pass

    async def test_list_my_connections(self) -> None:
        """Test case for list_my_connections

        """
        pass

    async def test_list_my_guilds(self) -> None:
        """Test case for list_my_guilds

        """
        pass

    async def test_list_my_private_archived_threads(self) -> None:
        """Test case for list_my_private_archived_threads

        """
        pass

    async def test_list_pins(self) -> None:
        """Test case for list_pins

        """
        pass

    async def test_list_private_archived_threads(self) -> None:
        """Test case for list_private_archived_threads

        """
        pass

    async def test_list_public_archived_threads(self) -> None:
        """Test case for list_public_archived_threads

        """
        pass

    async def test_list_sticker_packs(self) -> None:
        """Test case for list_sticker_packs

        """
        pass

    async def test_list_thread_members(self) -> None:
        """Test case for list_thread_members

        """
        pass

    async def test_list_voice_regions(self) -> None:
        """Test case for list_voice_regions

        """
        pass

    async def test_partner_sdk_token(self) -> None:
        """Test case for partner_sdk_token

        """
        pass

    async def test_partner_sdk_unmerge_provisional_account(self) -> None:
        """Test case for partner_sdk_unmerge_provisional_account

        """
        pass

    async def test_poll_expire(self) -> None:
        """Test case for poll_expire

        """
        pass

    async def test_preview_prune_guild(self) -> None:
        """Test case for preview_prune_guild

        """
        pass

    async def test_prune_guild(self) -> None:
        """Test case for prune_guild

        """
        pass

    async def test_put_guilds_onboarding(self) -> None:
        """Test case for put_guilds_onboarding

        """
        pass

    async def test_search_guild_members(self) -> None:
        """Test case for search_guild_members

        """
        pass

    async def test_send_soundboard_sound(self) -> None:
        """Test case for send_soundboard_sound

        """
        pass

    async def test_set_channel_permission_overwrite(self) -> None:
        """Test case for set_channel_permission_overwrite

        """
        pass

    async def test_set_guild_application_command_permissions(self) -> None:
        """Test case for set_guild_application_command_permissions

        """
        pass

    async def test_set_guild_mfa_level(self) -> None:
        """Test case for set_guild_mfa_level

        """
        pass

    async def test_sync_guild_template(self) -> None:
        """Test case for sync_guild_template

        """
        pass

    async def test_thread_search(self) -> None:
        """Test case for thread_search

        """
        pass

    async def test_trigger_typing_indicator(self) -> None:
        """Test case for trigger_typing_indicator

        """
        pass

    async def test_unban_user_from_guild(self) -> None:
        """Test case for unban_user_from_guild

        """
        pass

    async def test_update_application(self) -> None:
        """Test case for update_application

        """
        pass

    async def test_update_application_command(self) -> None:
        """Test case for update_application_command

        """
        pass

    async def test_update_application_emoji(self) -> None:
        """Test case for update_application_emoji

        """
        pass

    async def test_update_application_role_connections_metadata(self) -> None:
        """Test case for update_application_role_connections_metadata

        """
        pass

    async def test_update_application_user_role_connection(self) -> None:
        """Test case for update_application_user_role_connection

        """
        pass

    async def test_update_auto_moderation_rule(self) -> None:
        """Test case for update_auto_moderation_rule

        """
        pass

    async def test_update_channel(self) -> None:
        """Test case for update_channel

        """
        pass

    async def test_update_guild(self) -> None:
        """Test case for update_guild

        """
        pass

    async def test_update_guild_application_command(self) -> None:
        """Test case for update_guild_application_command

        """
        pass

    async def test_update_guild_emoji(self) -> None:
        """Test case for update_guild_emoji

        """
        pass

    async def test_update_guild_member(self) -> None:
        """Test case for update_guild_member

        """
        pass

    async def test_update_guild_role(self) -> None:
        """Test case for update_guild_role

        """
        pass

    async def test_update_guild_scheduled_event(self) -> None:
        """Test case for update_guild_scheduled_event

        """
        pass

    async def test_update_guild_soundboard_sound(self) -> None:
        """Test case for update_guild_soundboard_sound

        """
        pass

    async def test_update_guild_sticker(self) -> None:
        """Test case for update_guild_sticker

        """
        pass

    async def test_update_guild_template(self) -> None:
        """Test case for update_guild_template

        """
        pass

    async def test_update_guild_welcome_screen(self) -> None:
        """Test case for update_guild_welcome_screen

        """
        pass

    async def test_update_guild_widget_settings(self) -> None:
        """Test case for update_guild_widget_settings

        """
        pass

    async def test_update_message(self) -> None:
        """Test case for update_message

        """
        pass

    async def test_update_my_application(self) -> None:
        """Test case for update_my_application

        """
        pass

    async def test_update_my_guild_member(self) -> None:
        """Test case for update_my_guild_member

        """
        pass

    async def test_update_my_user(self) -> None:
        """Test case for update_my_user

        """
        pass

    async def test_update_original_webhook_message(self) -> None:
        """Test case for update_original_webhook_message

        """
        pass

    async def test_update_self_voice_state(self) -> None:
        """Test case for update_self_voice_state

        """
        pass

    async def test_update_stage_instance(self) -> None:
        """Test case for update_stage_instance

        """
        pass

    async def test_update_voice_state(self) -> None:
        """Test case for update_voice_state

        """
        pass

    async def test_update_webhook(self) -> None:
        """Test case for update_webhook

        """
        pass

    async def test_update_webhook_by_token(self) -> None:
        """Test case for update_webhook_by_token

        """
        pass

    async def test_update_webhook_message(self) -> None:
        """Test case for update_webhook_message

        """
        pass

    async def test_upload_application_attachment(self) -> None:
        """Test case for upload_application_attachment

        """
        pass


if __name__ == '__main__':
    unittest.main()
