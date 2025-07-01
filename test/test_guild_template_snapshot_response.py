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

from dc_rest.models.guild_template_snapshot_response import GuildTemplateSnapshotResponse

class TestGuildTemplateSnapshotResponse(unittest.TestCase):
    """GuildTemplateSnapshotResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GuildTemplateSnapshotResponse:
        """Test GuildTemplateSnapshotResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GuildTemplateSnapshotResponse`
        """
        model = GuildTemplateSnapshotResponse()
        if include_optional:
            return GuildTemplateSnapshotResponse(
                name = '',
                description = '',
                region = '',
                verification_level = 56,
                default_message_notifications = 56,
                explicit_content_filter = 56,
                preferred_locale = '',
                afk_channel_id = '9072888001528021798096225500850762068629339333975650685139102691291',
                afk_timeout = 56,
                system_channel_id = '9072888001528021798096225500850762068629339333975650685139102691291',
                system_channel_flags = 56,
                roles = [
                    dc_rest.models.guild_template_role_response.GuildTemplateRoleResponse(
                        id = 56, 
                        name = '', 
                        permissions = '', 
                        color = 56, 
                        hoist = True, 
                        mentionable = True, 
                        icon = '', 
                        unicode_emoji = '', )
                    ],
                channels = [
                    dc_rest.models.guild_template_channel_response.GuildTemplateChannelResponse(
                        id = 56, 
                        type = 0, 
                        name = '', 
                        position = 56, 
                        topic = '', 
                        bitrate = 56, 
                        user_limit = 56, 
                        nsfw = True, 
                        rate_limit_per_user = 56, 
                        parent_id = '9072888001528021798096225500850762068629339333975650685139102691291', 
                        default_auto_archive_duration = 56, 
                        permission_overwrites = [
                            dc_rest.models.channel_permission_overwrite_response.ChannelPermissionOverwriteResponse(
                                id = '9072888001528021798096225500850762068629339333975650685139102691291', 
                                type = 56, 
                                allow = '', 
                                deny = '', )
                            ], 
                        available_tags = [
                            dc_rest.models.guild_template_channel_tags.GuildTemplateChannelTags(
                                name = '', 
                                emoji_id = '9072888001528021798096225500850762068629339333975650685139102691291', 
                                emoji_name = '', 
                                moderated = True, )
                            ], 
                        template = '', 
                        default_reaction_emoji = dc_rest.models.default_reaction_emoji_response.DefaultReactionEmojiResponse(
                            emoji_id = '9072888001528021798096225500850762068629339333975650685139102691291', 
                            emoji_name = '', ), 
                        default_thread_rate_limit_per_user = 56, 
                        default_sort_order = 56, 
                        default_forum_layout = 56, 
                        default_tag_setting = '', 
                        icon_emoji = dc_rest.models.confetti_potion.confetti_potion(), 
                        theme_color = 56, )
                    ]
            )
        else:
            return GuildTemplateSnapshotResponse(
                name = '',
                verification_level = 56,
                default_message_notifications = 56,
                explicit_content_filter = 56,
                preferred_locale = '',
                afk_timeout = 56,
                system_channel_flags = 56,
                roles = [
                    dc_rest.models.guild_template_role_response.GuildTemplateRoleResponse(
                        id = 56, 
                        name = '', 
                        permissions = '', 
                        color = 56, 
                        hoist = True, 
                        mentionable = True, 
                        icon = '', 
                        unicode_emoji = '', )
                    ],
                channels = [
                    dc_rest.models.guild_template_channel_response.GuildTemplateChannelResponse(
                        id = 56, 
                        type = 0, 
                        name = '', 
                        position = 56, 
                        topic = '', 
                        bitrate = 56, 
                        user_limit = 56, 
                        nsfw = True, 
                        rate_limit_per_user = 56, 
                        parent_id = '9072888001528021798096225500850762068629339333975650685139102691291', 
                        default_auto_archive_duration = 56, 
                        permission_overwrites = [
                            dc_rest.models.channel_permission_overwrite_response.ChannelPermissionOverwriteResponse(
                                id = '9072888001528021798096225500850762068629339333975650685139102691291', 
                                type = 56, 
                                allow = '', 
                                deny = '', )
                            ], 
                        available_tags = [
                            dc_rest.models.guild_template_channel_tags.GuildTemplateChannelTags(
                                name = '', 
                                emoji_id = '9072888001528021798096225500850762068629339333975650685139102691291', 
                                emoji_name = '', 
                                moderated = True, )
                            ], 
                        template = '', 
                        default_reaction_emoji = dc_rest.models.default_reaction_emoji_response.DefaultReactionEmojiResponse(
                            emoji_id = '9072888001528021798096225500850762068629339333975650685139102691291', 
                            emoji_name = '', ), 
                        default_thread_rate_limit_per_user = 56, 
                        default_sort_order = 56, 
                        default_forum_layout = 56, 
                        default_tag_setting = '', 
                        icon_emoji = dc_rest.models.confetti_potion.confetti_potion(), 
                        theme_color = 56, )
                    ],
        )
        """

    def testGuildTemplateSnapshotResponse(self):
        """Test GuildTemplateSnapshotResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
