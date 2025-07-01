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

from dc_rest.models.minimal_content_message_response import MinimalContentMessageResponse

class TestMinimalContentMessageResponse(unittest.TestCase):
    """MinimalContentMessageResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MinimalContentMessageResponse:
        """Test MinimalContentMessageResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MinimalContentMessageResponse`
        """
        model = MinimalContentMessageResponse()
        if include_optional:
            return MinimalContentMessageResponse(
                type = 56,
                content = '',
                mentions = [
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
                mention_roles = [
                    '9072888001528021798096225500850762068629339333975650685139102691291'
                    ],
                attachments = [
                    dc_rest.models.attachment_response.AttachmentResponse(
                        id = '9072888001528021798096225500850762068629339333975650685139102691291', 
                        filename = '', 
                        size = 56, 
                        url = '', 
                        proxy_url = '', 
                        width = 56, 
                        height = 56, 
                        duration_secs = 1.337, 
                        waveform = '', 
                        description = '', 
                        content_type = '', 
                        ephemeral = True, 
                        title = '', 
                        application = dc_rest.models.application_response.ApplicationResponse(
                            id = '9072888001528021798096225500850762068629339333975650685139102691291', 
                            name = '', 
                            icon = '', 
                            description = '', 
                            type = 56, 
                            cover_image = '', 
                            primary_sku_id = '9072888001528021798096225500850762068629339333975650685139102691291', 
                            bot = dc_rest.models.user_response.UserResponse(
                                id = '9072888001528021798096225500850762068629339333975650685139102691291', 
                                username = '', 
                                avatar = '', 
                                discriminator = '', 
                                public_flags = 56, 
                                flags = -9007199254740991, 
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
                                    badge = '', ), ), 
                            slug = '', 
                            guild_id = '9072888001528021798096225500850762068629339333975650685139102691291', 
                            rpc_origins = [
                                ''
                                ], 
                            bot_public = True, 
                            bot_require_code_grant = True, 
                            terms_of_service_url = '', 
                            privacy_policy_url = '', 
                            custom_install_url = '', 
                            install_params = dc_rest.models.application_o_auth2_install_params_response.ApplicationOAuth2InstallParamsResponse(
                                scopes = [
                                    'applications.commands'
                                    ], 
                                permissions = '', ), 
                            integration_types_config = {
                                'key' : dc_rest.models.application_integration_type_configuration_response.ApplicationIntegrationTypeConfigurationResponse(
                                    oauth2_install_params = dc_rest.models.application_o_auth2_install_params_response.ApplicationOAuth2InstallParamsResponse(
                                        scopes = [
                                            'applications.commands'
                                            ], 
                                        permissions = '', ), )
                                }, 
                            verify_key = '', 
                            flags = 56, 
                            max_participants = 56, 
                            tags = [
                                ''
                                ], ), 
                        clip_created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        clip_participants = [
                            dc_rest.models.user_response.UserResponse(
                                id = '9072888001528021798096225500850762068629339333975650685139102691291', 
                                username = '', 
                                avatar = '', 
                                discriminator = '', 
                                public_flags = 56, 
                                flags = -9007199254740991, 
                                system = True, 
                                banner = '', 
                                accent_color = 56, 
                                global_name = '', )
                            ], )
                    ],
                embeds = [
                    dc_rest.models.message_embed_response.MessageEmbedResponse(
                        type = '', 
                        url = '', 
                        title = '', 
                        description = '', 
                        color = 56, 
                        timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        fields = [
                            dc_rest.models.message_embed_field_response.MessageEmbedFieldResponse(
                                name = '', 
                                value = '', 
                                inline = True, )
                            ], 
                        author = dc_rest.models.message_embed_author_response.MessageEmbedAuthorResponse(
                            name = '', 
                            url = '', 
                            icon_url = '', 
                            proxy_icon_url = '', ), 
                        provider = dc_rest.models.message_embed_provider_response.MessageEmbedProviderResponse(
                            name = '', 
                            url = '', ), 
                        image = dc_rest.models.message_embed_image_response.MessageEmbedImageResponse(
                            url = '', 
                            proxy_url = '', 
                            width = 0, 
                            height = 0, 
                            content_type = '', 
                            placeholder = '', 
                            placeholder_version = 0, 
                            description = '', 
                            flags = 0, ), 
                        thumbnail = dc_rest.models.message_embed_image_response.MessageEmbedImageResponse(
                            url = '', 
                            proxy_url = '', 
                            width = 0, 
                            height = 0, 
                            content_type = '', 
                            placeholder = '', 
                            placeholder_version = 0, 
                            description = '', 
                            flags = 0, ), 
                        video = , 
                        footer = dc_rest.models.message_embed_footer_response.MessageEmbedFooterResponse(
                            text = '', 
                            icon_url = '', 
                            proxy_icon_url = '', ), )
                    ],
                timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                edited_timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                flags = 56,
                components = [
                    null
                    ],
                resolved = dc_rest.models.resolved_objects_response.ResolvedObjectsResponse(
                    users = {
                        'key' : dc_rest.models.user_response.UserResponse(
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
                        }, 
                    members = {
                        'key' : dc_rest.models.guild_member_response.GuildMemberResponse(
                            avatar = '', 
                            banner = '', 
                            communication_disabled_until = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            flags = 56, 
                            joined_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            nick = '', 
                            pending = True, 
                            premium_since = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            roles = [
                                '9072888001528021798096225500850762068629339333975650685139102691291'
                                ], 
                            user = dc_rest.models.user_response.UserResponse(
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
                                global_name = '', ), 
                            mute = True, 
                            deaf = True, )
                        }, 
                    channels = {
                        'key' : null
                        }, 
                    roles = {
                        'key' : dc_rest.models.guild_role_response.GuildRoleResponse(
                            id = '9072888001528021798096225500850762068629339333975650685139102691291', 
                            name = '', 
                            description = '', 
                            permissions = '', 
                            position = 56, 
                            color = 56, 
                            hoist = True, 
                            managed = True, 
                            mentionable = True, 
                            icon = '', 
                            unicode_emoji = '', 
                            tags = dc_rest.models.guild_role_tags_response.GuildRoleTagsResponse(
                                premium_subscriber = null, 
                                bot_id = '9072888001528021798096225500850762068629339333975650685139102691291', 
                                integration_id = '9072888001528021798096225500850762068629339333975650685139102691291', 
                                subscription_listing_id = '9072888001528021798096225500850762068629339333975650685139102691291', 
                                available_for_purchase = null, 
                                guild_connections = null, ), )
                        }, ),
                stickers = [
                    null
                    ],
                sticker_items = [
                    dc_rest.models.message_sticker_item_response.MessageStickerItemResponse(
                        id = '9072888001528021798096225500850762068629339333975650685139102691291', 
                        name = '', 
                        format_type = 56, )
                    ]
            )
        else:
            return MinimalContentMessageResponse(
                type = 56,
                content = '',
                mentions = [
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
                mention_roles = [
                    '9072888001528021798096225500850762068629339333975650685139102691291'
                    ],
                attachments = [
                    dc_rest.models.attachment_response.AttachmentResponse(
                        id = '9072888001528021798096225500850762068629339333975650685139102691291', 
                        filename = '', 
                        size = 56, 
                        url = '', 
                        proxy_url = '', 
                        width = 56, 
                        height = 56, 
                        duration_secs = 1.337, 
                        waveform = '', 
                        description = '', 
                        content_type = '', 
                        ephemeral = True, 
                        title = '', 
                        application = dc_rest.models.application_response.ApplicationResponse(
                            id = '9072888001528021798096225500850762068629339333975650685139102691291', 
                            name = '', 
                            icon = '', 
                            description = '', 
                            type = 56, 
                            cover_image = '', 
                            primary_sku_id = '9072888001528021798096225500850762068629339333975650685139102691291', 
                            bot = dc_rest.models.user_response.UserResponse(
                                id = '9072888001528021798096225500850762068629339333975650685139102691291', 
                                username = '', 
                                avatar = '', 
                                discriminator = '', 
                                public_flags = 56, 
                                flags = -9007199254740991, 
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
                                    badge = '', ), ), 
                            slug = '', 
                            guild_id = '9072888001528021798096225500850762068629339333975650685139102691291', 
                            rpc_origins = [
                                ''
                                ], 
                            bot_public = True, 
                            bot_require_code_grant = True, 
                            terms_of_service_url = '', 
                            privacy_policy_url = '', 
                            custom_install_url = '', 
                            install_params = dc_rest.models.application_o_auth2_install_params_response.ApplicationOAuth2InstallParamsResponse(
                                scopes = [
                                    'applications.commands'
                                    ], 
                                permissions = '', ), 
                            integration_types_config = {
                                'key' : dc_rest.models.application_integration_type_configuration_response.ApplicationIntegrationTypeConfigurationResponse(
                                    oauth2_install_params = dc_rest.models.application_o_auth2_install_params_response.ApplicationOAuth2InstallParamsResponse(
                                        scopes = [
                                            'applications.commands'
                                            ], 
                                        permissions = '', ), )
                                }, 
                            verify_key = '', 
                            flags = 56, 
                            max_participants = 56, 
                            tags = [
                                ''
                                ], ), 
                        clip_created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        clip_participants = [
                            dc_rest.models.user_response.UserResponse(
                                id = '9072888001528021798096225500850762068629339333975650685139102691291', 
                                username = '', 
                                avatar = '', 
                                discriminator = '', 
                                public_flags = 56, 
                                flags = -9007199254740991, 
                                system = True, 
                                banner = '', 
                                accent_color = 56, 
                                global_name = '', )
                            ], )
                    ],
                embeds = [
                    dc_rest.models.message_embed_response.MessageEmbedResponse(
                        type = '', 
                        url = '', 
                        title = '', 
                        description = '', 
                        color = 56, 
                        timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        fields = [
                            dc_rest.models.message_embed_field_response.MessageEmbedFieldResponse(
                                name = '', 
                                value = '', 
                                inline = True, )
                            ], 
                        author = dc_rest.models.message_embed_author_response.MessageEmbedAuthorResponse(
                            name = '', 
                            url = '', 
                            icon_url = '', 
                            proxy_icon_url = '', ), 
                        provider = dc_rest.models.message_embed_provider_response.MessageEmbedProviderResponse(
                            name = '', 
                            url = '', ), 
                        image = dc_rest.models.message_embed_image_response.MessageEmbedImageResponse(
                            url = '', 
                            proxy_url = '', 
                            width = 0, 
                            height = 0, 
                            content_type = '', 
                            placeholder = '', 
                            placeholder_version = 0, 
                            description = '', 
                            flags = 0, ), 
                        thumbnail = dc_rest.models.message_embed_image_response.MessageEmbedImageResponse(
                            url = '', 
                            proxy_url = '', 
                            width = 0, 
                            height = 0, 
                            content_type = '', 
                            placeholder = '', 
                            placeholder_version = 0, 
                            description = '', 
                            flags = 0, ), 
                        video = , 
                        footer = dc_rest.models.message_embed_footer_response.MessageEmbedFooterResponse(
                            text = '', 
                            icon_url = '', 
                            proxy_icon_url = '', ), )
                    ],
                timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                flags = 56,
                components = [
                    null
                    ],
        )
        """

    def testMinimalContentMessageResponse(self):
        """Test MinimalContentMessageResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
