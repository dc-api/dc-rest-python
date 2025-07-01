# coding: utf-8

"""
Discord HTTP API (Preview) - REST API Client
Preview of the Discord v10 HTTP API specification. See https://discord.com/developers/docs for more details.

## Metadata

- **Copyright**: Copyright (c) 2025 Qntx
- **Author**: ΣX <gitctrlx@gmail.com>
- **Version**: 10
- **Modified**: 2025-07-01T10:27:27.208780920Z[Etc/UTC]
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

from dc_rest.models.guild_audit_log_response import GuildAuditLogResponse

class TestGuildAuditLogResponse(unittest.TestCase):
    """GuildAuditLogResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GuildAuditLogResponse:
        """Test GuildAuditLogResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GuildAuditLogResponse`
        """
        model = GuildAuditLogResponse()
        if include_optional:
            return GuildAuditLogResponse(
                audit_log_entries = [
                    dc_rest.models.audit_log_entry_response.AuditLogEntryResponse(
                        id = '9072888001528021798096225500850762068629339333975650685139102691291', 
                        action_type = 56, 
                        user_id = '9072888001528021798096225500850762068629339333975650685139102691291', 
                        target_id = '9072888001528021798096225500850762068629339333975650685139102691291', 
                        changes = [
                            dc_rest.models.audit_log_object_change_response.AuditLogObjectChangeResponse(
                                key = '', 
                                new_value = null, 
                                old_value = null, )
                            ], 
                        options = {
                            'key' : ''
                            }, 
                        reason = '', )
                    ],
                users = [
                    dc_rest.models.user_response.UserResponse(
                        id = '9072888001528021798096225500850762068629339333975650685139102691291', 
                        username = '', 
                        avatar = '', 
                        discriminator = '', 
                        public_flags = 56, 
                        flags = -9007199254740991, 
                        bot = True, 
                        system = True, 
                        banner = '', 
                        accent_color = 56, 
                        global_name = '', 
                        avatar_decoration_data = dc_rest.models.user_avatar_decoration_response.UserAvatarDecorationResponse(
                            asset = '', 
                            sku_id = '9072888001528021798096225500850762068629339333975650685139102691291', ), 
                        collectibles = dc_rest.models.user_collectibles_response.UserCollectiblesResponse(
                            nameplate = dc_rest.models.user_nameplate_response.UserNameplateResponse(
                                asset = '', 
                                label = '', 
                                palette = '', ), ), 
                        primary_guild = dc_rest.models.user_primary_guild_response.UserPrimaryGuildResponse(
                            identity_guild_id = '9072888001528021798096225500850762068629339333975650685139102691291', 
                            identity_enabled = True, 
                            tag = '', 
                            badge = '', ), )
                    ],
                integrations = [
                    null
                    ],
                webhooks = [
                    null
                    ],
                guild_scheduled_events = [
                    null
                    ],
                threads = [
                    dc_rest.models.thread_response.ThreadResponse(
                        id = '9072888001528021798096225500850762068629339333975650685139102691291', 
                        type = 10, 
                        last_message_id = '9072888001528021798096225500850762068629339333975650685139102691291', 
                        flags = 56, 
                        last_pin_timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        guild_id = '9072888001528021798096225500850762068629339333975650685139102691291', 
                        name = '', 
                        parent_id = '9072888001528021798096225500850762068629339333975650685139102691291', 
                        rate_limit_per_user = 56, 
                        bitrate = 56, 
                        user_limit = 56, 
                        rtc_region = '', 
                        video_quality_mode = 56, 
                        permissions = '', 
                        owner_id = '9072888001528021798096225500850762068629339333975650685139102691291', 
                        thread_metadata = dc_rest.models.thread_metadata_response.ThreadMetadataResponse(
                            archived = True, 
                            archive_timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            auto_archive_duration = 56, 
                            locked = True, 
                            create_timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            invitable = True, ), 
                        message_count = 56, 
                        member_count = 56, 
                        total_message_sent = 56, 
                        applied_tags = [
                            '9072888001528021798096225500850762068629339333975650685139102691291'
                            ], 
                        member = dc_rest.models.thread_member_response.ThreadMemberResponse(
                            id = '9072888001528021798096225500850762068629339333975650685139102691291', 
                            user_id = '9072888001528021798096225500850762068629339333975650685139102691291', 
                            join_timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            flags = 56, ), )
                    ],
                application_commands = [
                    dc_rest.models.application_command_response.ApplicationCommandResponse(
                        id = '9072888001528021798096225500850762068629339333975650685139102691291', 
                        application_id = '9072888001528021798096225500850762068629339333975650685139102691291', 
                        version = '9072888001528021798096225500850762068629339333975650685139102691291', 
                        default_member_permissions = '', 
                        type = 56, 
                        name = '', 
                        name_localized = '', 
                        name_localizations = {
                            'key' : ''
                            }, 
                        description = '', 
                        description_localized = '', 
                        description_localizations = {
                            'key' : ''
                            }, 
                        guild_id = '9072888001528021798096225500850762068629339333975650685139102691291', 
                        dm_permission = True, 
                        contexts = [
                            56
                            ], 
                        integration_types = [
                            56
                            ], 
                        options = [
                            null
                            ], 
                        nsfw = True, )
                    ],
                auto_moderation_rules = [
                    null
                    ]
            )
        else:
            return GuildAuditLogResponse(
                audit_log_entries = [
                    dc_rest.models.audit_log_entry_response.AuditLogEntryResponse(
                        id = '9072888001528021798096225500850762068629339333975650685139102691291', 
                        action_type = 56, 
                        user_id = '9072888001528021798096225500850762068629339333975650685139102691291', 
                        target_id = '9072888001528021798096225500850762068629339333975650685139102691291', 
                        changes = [
                            dc_rest.models.audit_log_object_change_response.AuditLogObjectChangeResponse(
                                key = '', 
                                new_value = null, 
                                old_value = null, )
                            ], 
                        options = {
                            'key' : ''
                            }, 
                        reason = '', )
                    ],
                users = [
                    dc_rest.models.user_response.UserResponse(
                        id = '9072888001528021798096225500850762068629339333975650685139102691291', 
                        username = '', 
                        avatar = '', 
                        discriminator = '', 
                        public_flags = 56, 
                        flags = -9007199254740991, 
                        bot = True, 
                        system = True, 
                        banner = '', 
                        accent_color = 56, 
                        global_name = '', 
                        avatar_decoration_data = dc_rest.models.user_avatar_decoration_response.UserAvatarDecorationResponse(
                            asset = '', 
                            sku_id = '9072888001528021798096225500850762068629339333975650685139102691291', ), 
                        collectibles = dc_rest.models.user_collectibles_response.UserCollectiblesResponse(
                            nameplate = dc_rest.models.user_nameplate_response.UserNameplateResponse(
                                asset = '', 
                                label = '', 
                                palette = '', ), ), 
                        primary_guild = dc_rest.models.user_primary_guild_response.UserPrimaryGuildResponse(
                            identity_guild_id = '9072888001528021798096225500850762068629339333975650685139102691291', 
                            identity_enabled = True, 
                            tag = '', 
                            badge = '', ), )
                    ],
                integrations = [
                    null
                    ],
                webhooks = [
                    null
                    ],
                guild_scheduled_events = [
                    null
                    ],
                threads = [
                    dc_rest.models.thread_response.ThreadResponse(
                        id = '9072888001528021798096225500850762068629339333975650685139102691291', 
                        type = 10, 
                        last_message_id = '9072888001528021798096225500850762068629339333975650685139102691291', 
                        flags = 56, 
                        last_pin_timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        guild_id = '9072888001528021798096225500850762068629339333975650685139102691291', 
                        name = '', 
                        parent_id = '9072888001528021798096225500850762068629339333975650685139102691291', 
                        rate_limit_per_user = 56, 
                        bitrate = 56, 
                        user_limit = 56, 
                        rtc_region = '', 
                        video_quality_mode = 56, 
                        permissions = '', 
                        owner_id = '9072888001528021798096225500850762068629339333975650685139102691291', 
                        thread_metadata = dc_rest.models.thread_metadata_response.ThreadMetadataResponse(
                            archived = True, 
                            archive_timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            auto_archive_duration = 56, 
                            locked = True, 
                            create_timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            invitable = True, ), 
                        message_count = 56, 
                        member_count = 56, 
                        total_message_sent = 56, 
                        applied_tags = [
                            '9072888001528021798096225500850762068629339333975650685139102691291'
                            ], 
                        member = dc_rest.models.thread_member_response.ThreadMemberResponse(
                            id = '9072888001528021798096225500850762068629339333975650685139102691291', 
                            user_id = '9072888001528021798096225500850762068629339333975650685139102691291', 
                            join_timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            flags = 56, ), )
                    ],
                application_commands = [
                    dc_rest.models.application_command_response.ApplicationCommandResponse(
                        id = '9072888001528021798096225500850762068629339333975650685139102691291', 
                        application_id = '9072888001528021798096225500850762068629339333975650685139102691291', 
                        version = '9072888001528021798096225500850762068629339333975650685139102691291', 
                        default_member_permissions = '', 
                        type = 56, 
                        name = '', 
                        name_localized = '', 
                        name_localizations = {
                            'key' : ''
                            }, 
                        description = '', 
                        description_localized = '', 
                        description_localizations = {
                            'key' : ''
                            }, 
                        guild_id = '9072888001528021798096225500850762068629339333975650685139102691291', 
                        dm_permission = True, 
                        contexts = [
                            56
                            ], 
                        integration_types = [
                            56
                            ], 
                        options = [
                            null
                            ], 
                        nsfw = True, )
                    ],
                auto_moderation_rules = [
                    null
                    ],
        )
        """

    def testGuildAuditLogResponse(self):
        """Test GuildAuditLogResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
