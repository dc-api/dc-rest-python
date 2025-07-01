# coding: utf-8

"""
Discord HTTP API (Preview) - REST API Client
Preview of the Discord v10 HTTP API specification. See https://discord.com/developers/docs for more details.

## Metadata

- **Copyright**: Copyright (c) 2025 Qntx
- **Author**: ΣX <gitctrlx@gmail.com>
- **Version**: 10
- **Modified**: 2025-07-01T10:17:20.817322704Z[Etc/UTC]
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

from dc_rest.models.get_channel200_response import GetChannel200Response

class TestGetChannel200Response(unittest.TestCase):
    """GetChannel200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetChannel200Response:
        """Test GetChannel200Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetChannel200Response`
        """
        model = GetChannel200Response()
        if include_optional:
            return GetChannel200Response(
                id = '9072888001528021798096225500850762068629339333975650685139102691291',
                type = 56,
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
                topic = '',
                default_auto_archive_duration = 56,
                default_thread_rate_limit_per_user = 56,
                position = 56,
                permission_overwrites = [
                    dc_rest.models.channel_permission_overwrite_response.ChannelPermissionOverwriteResponse(
                        id = '9072888001528021798096225500850762068629339333975650685139102691291', 
                        type = 56, 
                        allow = '', 
                        deny = '', )
                    ],
                nsfw = True,
                available_tags = [
                    dc_rest.models.forum_tag_response.ForumTagResponse(
                        id = '9072888001528021798096225500850762068629339333975650685139102691291', 
                        name = '', 
                        moderated = True, 
                        emoji_id = '9072888001528021798096225500850762068629339333975650685139102691291', 
                        emoji_name = '', )
                    ],
                default_reaction_emoji = dc_rest.models.default_reaction_emoji_response.DefaultReactionEmojiResponse(
                    emoji_id = '9072888001528021798096225500850762068629339333975650685139102691291', 
                    emoji_name = '', ),
                default_sort_order = 56,
                default_forum_layout = 56,
                default_tag_setting = '',
                hd_streaming_until = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                hd_streaming_buyer_id = '9072888001528021798096225500850762068629339333975650685139102691291',
                recipients = [
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
                                sku_id = '9072888001528021798096225500850762068629339333975650685139102691291', 
                                asset = '', 
                                label = '', 
                                palette = '', ), ), 
                        primary_guild = dc_rest.models.user_primary_guild_response.UserPrimaryGuildResponse(
                            identity_guild_id = '9072888001528021798096225500850762068629339333975650685139102691291', 
                            identity_enabled = True, 
                            tag = '', 
                            badge = '', ), )
                    ],
                icon = '',
                owner_id = '9072888001528021798096225500850762068629339333975650685139102691291',
                managed = True,
                application_id = '9072888001528021798096225500850762068629339333975650685139102691291',
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
                    flags = 56, )
            )
        else:
            return GetChannel200Response(
                id = '9072888001528021798096225500850762068629339333975650685139102691291',
                type = 56,
                flags = 56,
                guild_id = '9072888001528021798096225500850762068629339333975650685139102691291',
                name = '',
                position = 56,
                recipients = [
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
                                sku_id = '9072888001528021798096225500850762068629339333975650685139102691291', 
                                asset = '', 
                                label = '', 
                                palette = '', ), ), 
                        primary_guild = dc_rest.models.user_primary_guild_response.UserPrimaryGuildResponse(
                            identity_guild_id = '9072888001528021798096225500850762068629339333975650685139102691291', 
                            identity_enabled = True, 
                            tag = '', 
                            badge = '', ), )
                    ],
                owner_id = '9072888001528021798096225500850762068629339333975650685139102691291',
                message_count = 56,
                member_count = 56,
                total_message_sent = 56,
        )
        """

    def testGetChannel200Response(self):
        """Test GetChannel200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
