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

from dc_rest.models.message_embed_response import MessageEmbedResponse

class TestMessageEmbedResponse(unittest.TestCase):
    """MessageEmbedResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MessageEmbedResponse:
        """Test MessageEmbedResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MessageEmbedResponse`
        """
        model = MessageEmbedResponse()
        if include_optional:
            return MessageEmbedResponse(
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
                video = dc_rest.models.message_embed_image_response.MessageEmbedImageResponse(
                    url = '', 
                    proxy_url = '', 
                    width = 0, 
                    height = 0, 
                    content_type = '', 
                    placeholder = '', 
                    placeholder_version = 0, 
                    description = '', 
                    flags = 0, ),
                footer = dc_rest.models.message_embed_footer_response.MessageEmbedFooterResponse(
                    text = '', 
                    icon_url = '', 
                    proxy_icon_url = '', )
            )
        else:
            return MessageEmbedResponse(
                type = '',
        )
        """

    def testMessageEmbedResponse(self):
        """Test MessageEmbedResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
