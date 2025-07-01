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

from dc_rest.models.private_guild_member_response import PrivateGuildMemberResponse

class TestPrivateGuildMemberResponse(unittest.TestCase):
    """PrivateGuildMemberResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PrivateGuildMemberResponse:
        """Test PrivateGuildMemberResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PrivateGuildMemberResponse`
        """
        model = PrivateGuildMemberResponse()
        if include_optional:
            return PrivateGuildMemberResponse(
                avatar = '',
                avatar_decoration_data = dc_rest.models.user_avatar_decoration_response.UserAvatarDecorationResponse(
                    asset = '', 
                    sku_id = '9072888001528021798096225500850762068629339333975650685139102691291', ),
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
                mute = True,
                deaf = True
            )
        else:
            return PrivateGuildMemberResponse(
                flags = 56,
                joined_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                pending = True,
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
                mute = True,
                deaf = True,
        )
        """

    def testPrivateGuildMemberResponse(self):
        """Test PrivateGuildMemberResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
