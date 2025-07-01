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

from dc_rest.models.update_message_interaction_callback_response import UpdateMessageInteractionCallbackResponse

class TestUpdateMessageInteractionCallbackResponse(unittest.TestCase):
    """UpdateMessageInteractionCallbackResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UpdateMessageInteractionCallbackResponse:
        """Test UpdateMessageInteractionCallbackResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UpdateMessageInteractionCallbackResponse`
        """
        model = UpdateMessageInteractionCallbackResponse()
        if include_optional:
            return UpdateMessageInteractionCallbackResponse(
                type = 56,
                message = dc_rest.models.message_response.MessageResponse(
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
                                    global_name = '', ), 
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
                                placeholder_version = , 
                                description = '', ), 
                            thumbnail = dc_rest.models.message_embed_image_response.MessageEmbedImageResponse(
                                url = '', 
                                proxy_url = '', 
                                height = , 
                                content_type = '', 
                                placeholder = '', 
                                placeholder_version = , 
                                description = '', ), 
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
                            'key' : 
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
                                user = , 
                                mute = True, 
                                deaf = True, )
                            }, 
                        channels = {
                            'key' : null
                            }, 
                        roles = {
                            'key' : dc_rest.models.guild_role_response.GuildRoleResponse(
                                id = , 
                                name = '', 
                                description = '', 
                                permissions = '', 
                                position = 56, 
                                color = 56, 
                                hoist = True, 
                                managed = True, 
                                mentionable = True, 
                                icon = '', 
                                unicode_emoji = '', )
                            }, ), 
                    stickers = [
                        null
                        ], 
                    sticker_items = [
                        dc_rest.models.message_sticker_item_response.MessageStickerItemResponse(
                            id = , 
                            name = '', 
                            format_type = 56, )
                        ], 
                    id = , 
                    channel_id = '9072888001528021798096225500850762068629339333975650685139102691291', 
                    author = , 
                    pinned = True, 
                    mention_everyone = True, 
                    tts = True, 
                    call = dc_rest.models.message_call_response.MessageCallResponse(
                        ended_timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        participants = [
                            '9072888001528021798096225500850762068629339333975650685139102691291'
                            ], ), 
                    activity = dc_rest.models.confetti_potion.confetti_potion(), 
                    application = dc_rest.models.basic_application_response.BasicApplicationResponse(
                        id = '9072888001528021798096225500850762068629339333975650685139102691291', 
                        name = '', 
                        icon = '', 
                        description = '', 
                        cover_image = '', 
                        primary_sku_id = '9072888001528021798096225500850762068629339333975650685139102691291', ), 
                    application_id = '9072888001528021798096225500850762068629339333975650685139102691291', 
                    interaction = dc_rest.models.message_interaction_response.MessageInteractionResponse(
                        id = , 
                        type = 56, 
                        name = '', 
                        name_localized = '', ), 
                    nonce = null, 
                    webhook_id = '9072888001528021798096225500850762068629339333975650685139102691291', 
                    message_reference = dc_rest.models.message_reference_response.MessageReferenceResponse(
                        channel_id = '9072888001528021798096225500850762068629339333975650685139102691291', 
                        message_id = '9072888001528021798096225500850762068629339333975650685139102691291', 
                        guild_id = '9072888001528021798096225500850762068629339333975650685139102691291', ), 
                    thread = dc_rest.models.thread_response.ThreadResponse(
                        id = , 
                        type = 10, 
                        last_message_id = '9072888001528021798096225500850762068629339333975650685139102691291', 
                        flags = 56, 
                        last_pin_timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        guild_id = , 
                        name = '', 
                        parent_id = '9072888001528021798096225500850762068629339333975650685139102691291', 
                        rate_limit_per_user = 56, 
                        bitrate = 56, 
                        user_limit = 56, 
                        rtc_region = '', 
                        video_quality_mode = 56, 
                        permissions = '', 
                        owner_id = , 
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
                            id = , 
                            user_id = '9072888001528021798096225500850762068629339333975650685139102691291', 
                            join_timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            flags = 56, ), ), 
                    mention_channels = [
                        dc_rest.models.message_mention_channel_response.MessageMentionChannelResponse(
                            id = , 
                            name = '', 
                            type = 56, 
                            guild_id = '9072888001528021798096225500850762068629339333975650685139102691291', )
                        ], 
                    role_subscription_data = dc_rest.models.message_role_subscription_data_response.MessageRoleSubscriptionDataResponse(
                        role_subscription_listing_id = '9072888001528021798096225500850762068629339333975650685139102691291', 
                        tier_name = '', 
                        total_months_subscribed = 56, 
                        is_renewal = True, ), 
                    purchase_notification = dc_rest.models.purchase_notification_response.PurchaseNotificationResponse(
                        type = 56, 
                        guild_product_purchase = dc_rest.models.guild_product_purchase_response.GuildProductPurchaseResponse(
                            listing_id = '9072888001528021798096225500850762068629339333975650685139102691291', 
                            product_name = '', ), ), 
                    position = 56, 
                    poll = dc_rest.models.poll_response.PollResponse(
                        question = dc_rest.models.poll_media_response.PollMediaResponse(
                            text = '', 
                            emoji = dc_rest.models.message_reaction_emoji_response.MessageReactionEmojiResponse(
                                name = '', 
                                animated = True, ), ), 
                        answers = [
                            dc_rest.models.poll_answer_response.PollAnswerResponse(
                                answer_id = 56, 
                                poll_media = dc_rest.models.poll_media_response.PollMediaResponse(
                                    text = '', ), )
                            ], 
                        expiry = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        allow_multiselect = True, 
                        layout_type = 56, 
                        results = dc_rest.models.poll_results_response.PollResultsResponse(
                            answer_counts = [
                                dc_rest.models.poll_results_entry_response.PollResultsEntryResponse(
                                    id = 56, 
                                    count = 56, 
                                    me_voted = True, )
                                ], 
                            is_finalized = True, ), ), 
                    interaction_metadata = null, 
                    message_snapshots = [
                        dc_rest.models.message_snapshot_response.MessageSnapshotResponse(
                            message = dc_rest.models.minimal_content_message_response.MinimalContentMessageResponse(
                                type = 56, 
                                content = '', 
                                mentions = [
                                    
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
                                        height = 56, 
                                        duration_secs = 1.337, 
                                        waveform = '', 
                                        description = '', 
                                        content_type = '', 
                                        ephemeral = True, 
                                        title = '', 
                                        clip_created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                                    ], 
                                embeds = [
                                    dc_rest.models.message_embed_response.MessageEmbedResponse(
                                        type = '', 
                                        url = '', 
                                        title = '', 
                                        description = '', 
                                        color = 56, 
                                        timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                                    ], 
                                timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                edited_timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                flags = 56, 
                                components = [
                                    null
                                    ], ), )
                        ], 
                    reactions = [
                        dc_rest.models.message_reaction_response.MessageReactionResponse(
                            emoji = dc_rest.models.message_reaction_emoji_response.MessageReactionEmojiResponse(
                                name = '', 
                                animated = True, ), 
                            count = 56, 
                            count_details = dc_rest.models.message_reaction_count_details_response.MessageReactionCountDetailsResponse(
                                burst = 56, 
                                normal = 56, ), 
                            burst_colors = [
                                ''
                                ], 
                            me_burst = True, 
                            me = True, )
                        ], 
                    referenced_message = dc_rest.models.basic_message_response.BasicMessageResponse(
                        type = 56, 
                        content = '', 
                        mentions = , 
                        mention_roles = , 
                        attachments = , 
                        embeds = , 
                        timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        edited_timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        flags = 56, 
                        components = , 
                        id = '9072888001528021798096225500850762068629339333975650685139102691291', 
                        channel_id = '9072888001528021798096225500850762068629339333975650685139102691291', 
                        author = , 
                        pinned = True, 
                        mention_everyone = True, 
                        tts = True, 
                        position = 56, ), )
            )
        else:
            return UpdateMessageInteractionCallbackResponse(
                type = 56,
                message = dc_rest.models.message_response.MessageResponse(
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
                                    global_name = '', ), 
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
                                placeholder_version = , 
                                description = '', ), 
                            thumbnail = dc_rest.models.message_embed_image_response.MessageEmbedImageResponse(
                                url = '', 
                                proxy_url = '', 
                                height = , 
                                content_type = '', 
                                placeholder = '', 
                                placeholder_version = , 
                                description = '', ), 
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
                            'key' : 
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
                                user = , 
                                mute = True, 
                                deaf = True, )
                            }, 
                        channels = {
                            'key' : null
                            }, 
                        roles = {
                            'key' : dc_rest.models.guild_role_response.GuildRoleResponse(
                                id = , 
                                name = '', 
                                description = '', 
                                permissions = '', 
                                position = 56, 
                                color = 56, 
                                hoist = True, 
                                managed = True, 
                                mentionable = True, 
                                icon = '', 
                                unicode_emoji = '', )
                            }, ), 
                    stickers = [
                        null
                        ], 
                    sticker_items = [
                        dc_rest.models.message_sticker_item_response.MessageStickerItemResponse(
                            id = , 
                            name = '', 
                            format_type = 56, )
                        ], 
                    id = , 
                    channel_id = '9072888001528021798096225500850762068629339333975650685139102691291', 
                    author = , 
                    pinned = True, 
                    mention_everyone = True, 
                    tts = True, 
                    call = dc_rest.models.message_call_response.MessageCallResponse(
                        ended_timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        participants = [
                            '9072888001528021798096225500850762068629339333975650685139102691291'
                            ], ), 
                    activity = dc_rest.models.confetti_potion.confetti_potion(), 
                    application = dc_rest.models.basic_application_response.BasicApplicationResponse(
                        id = '9072888001528021798096225500850762068629339333975650685139102691291', 
                        name = '', 
                        icon = '', 
                        description = '', 
                        cover_image = '', 
                        primary_sku_id = '9072888001528021798096225500850762068629339333975650685139102691291', ), 
                    application_id = '9072888001528021798096225500850762068629339333975650685139102691291', 
                    interaction = dc_rest.models.message_interaction_response.MessageInteractionResponse(
                        id = , 
                        type = 56, 
                        name = '', 
                        name_localized = '', ), 
                    nonce = null, 
                    webhook_id = '9072888001528021798096225500850762068629339333975650685139102691291', 
                    message_reference = dc_rest.models.message_reference_response.MessageReferenceResponse(
                        channel_id = '9072888001528021798096225500850762068629339333975650685139102691291', 
                        message_id = '9072888001528021798096225500850762068629339333975650685139102691291', 
                        guild_id = '9072888001528021798096225500850762068629339333975650685139102691291', ), 
                    thread = dc_rest.models.thread_response.ThreadResponse(
                        id = , 
                        type = 10, 
                        last_message_id = '9072888001528021798096225500850762068629339333975650685139102691291', 
                        flags = 56, 
                        last_pin_timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        guild_id = , 
                        name = '', 
                        parent_id = '9072888001528021798096225500850762068629339333975650685139102691291', 
                        rate_limit_per_user = 56, 
                        bitrate = 56, 
                        user_limit = 56, 
                        rtc_region = '', 
                        video_quality_mode = 56, 
                        permissions = '', 
                        owner_id = , 
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
                            id = , 
                            user_id = '9072888001528021798096225500850762068629339333975650685139102691291', 
                            join_timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            flags = 56, ), ), 
                    mention_channels = [
                        dc_rest.models.message_mention_channel_response.MessageMentionChannelResponse(
                            id = , 
                            name = '', 
                            type = 56, 
                            guild_id = '9072888001528021798096225500850762068629339333975650685139102691291', )
                        ], 
                    role_subscription_data = dc_rest.models.message_role_subscription_data_response.MessageRoleSubscriptionDataResponse(
                        role_subscription_listing_id = '9072888001528021798096225500850762068629339333975650685139102691291', 
                        tier_name = '', 
                        total_months_subscribed = 56, 
                        is_renewal = True, ), 
                    purchase_notification = dc_rest.models.purchase_notification_response.PurchaseNotificationResponse(
                        type = 56, 
                        guild_product_purchase = dc_rest.models.guild_product_purchase_response.GuildProductPurchaseResponse(
                            listing_id = '9072888001528021798096225500850762068629339333975650685139102691291', 
                            product_name = '', ), ), 
                    position = 56, 
                    poll = dc_rest.models.poll_response.PollResponse(
                        question = dc_rest.models.poll_media_response.PollMediaResponse(
                            text = '', 
                            emoji = dc_rest.models.message_reaction_emoji_response.MessageReactionEmojiResponse(
                                name = '', 
                                animated = True, ), ), 
                        answers = [
                            dc_rest.models.poll_answer_response.PollAnswerResponse(
                                answer_id = 56, 
                                poll_media = dc_rest.models.poll_media_response.PollMediaResponse(
                                    text = '', ), )
                            ], 
                        expiry = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        allow_multiselect = True, 
                        layout_type = 56, 
                        results = dc_rest.models.poll_results_response.PollResultsResponse(
                            answer_counts = [
                                dc_rest.models.poll_results_entry_response.PollResultsEntryResponse(
                                    id = 56, 
                                    count = 56, 
                                    me_voted = True, )
                                ], 
                            is_finalized = True, ), ), 
                    interaction_metadata = null, 
                    message_snapshots = [
                        dc_rest.models.message_snapshot_response.MessageSnapshotResponse(
                            message = dc_rest.models.minimal_content_message_response.MinimalContentMessageResponse(
                                type = 56, 
                                content = '', 
                                mentions = [
                                    
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
                                        height = 56, 
                                        duration_secs = 1.337, 
                                        waveform = '', 
                                        description = '', 
                                        content_type = '', 
                                        ephemeral = True, 
                                        title = '', 
                                        clip_created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                                    ], 
                                embeds = [
                                    dc_rest.models.message_embed_response.MessageEmbedResponse(
                                        type = '', 
                                        url = '', 
                                        title = '', 
                                        description = '', 
                                        color = 56, 
                                        timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                                    ], 
                                timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                edited_timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                flags = 56, 
                                components = [
                                    null
                                    ], ), )
                        ], 
                    reactions = [
                        dc_rest.models.message_reaction_response.MessageReactionResponse(
                            emoji = dc_rest.models.message_reaction_emoji_response.MessageReactionEmojiResponse(
                                name = '', 
                                animated = True, ), 
                            count = 56, 
                            count_details = dc_rest.models.message_reaction_count_details_response.MessageReactionCountDetailsResponse(
                                burst = 56, 
                                normal = 56, ), 
                            burst_colors = [
                                ''
                                ], 
                            me_burst = True, 
                            me = True, )
                        ], 
                    referenced_message = dc_rest.models.basic_message_response.BasicMessageResponse(
                        type = 56, 
                        content = '', 
                        mentions = , 
                        mention_roles = , 
                        attachments = , 
                        embeds = , 
                        timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        edited_timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        flags = 56, 
                        components = , 
                        id = '9072888001528021798096225500850762068629339333975650685139102691291', 
                        channel_id = '9072888001528021798096225500850762068629339333975650685139102691291', 
                        author = , 
                        pinned = True, 
                        mention_everyone = True, 
                        tts = True, 
                        position = 56, ), ),
        )
        """

    def testUpdateMessageInteractionCallbackResponse(self):
        """Test UpdateMessageInteractionCallbackResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
