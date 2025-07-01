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

from dc_rest.models.guild_onboarding_response import GuildOnboardingResponse

class TestGuildOnboardingResponse(unittest.TestCase):
    """GuildOnboardingResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GuildOnboardingResponse:
        """Test GuildOnboardingResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GuildOnboardingResponse`
        """
        model = GuildOnboardingResponse()
        if include_optional:
            return GuildOnboardingResponse(
                guild_id = '9072888001528021798096225500850762068629339333975650685139102691291',
                prompts = [
                    dc_rest.models.onboarding_prompt_response.OnboardingPromptResponse(
                        id = '9072888001528021798096225500850762068629339333975650685139102691291', 
                        title = '', 
                        options = [
                            dc_rest.models.onboarding_prompt_option_response.OnboardingPromptOptionResponse(
                                id = '9072888001528021798096225500850762068629339333975650685139102691291', 
                                title = '', 
                                description = '', 
                                emoji = dc_rest.models.message_reaction_emoji_response.MessageReactionEmojiResponse(
                                    name = '', 
                                    animated = True, ), 
                                role_ids = [
                                    '9072888001528021798096225500850762068629339333975650685139102691291'
                                    ], 
                                channel_ids = [
                                    '9072888001528021798096225500850762068629339333975650685139102691291'
                                    ], )
                            ], 
                        single_select = True, 
                        required = True, 
                        in_onboarding = True, 
                        type = 56, )
                    ],
                default_channel_ids = [
                    '9072888001528021798096225500850762068629339333975650685139102691291'
                    ],
                enabled = True
            )
        else:
            return GuildOnboardingResponse(
                guild_id = '9072888001528021798096225500850762068629339333975650685139102691291',
                prompts = [
                    dc_rest.models.onboarding_prompt_response.OnboardingPromptResponse(
                        id = '9072888001528021798096225500850762068629339333975650685139102691291', 
                        title = '', 
                        options = [
                            dc_rest.models.onboarding_prompt_option_response.OnboardingPromptOptionResponse(
                                id = '9072888001528021798096225500850762068629339333975650685139102691291', 
                                title = '', 
                                description = '', 
                                emoji = dc_rest.models.message_reaction_emoji_response.MessageReactionEmojiResponse(
                                    name = '', 
                                    animated = True, ), 
                                role_ids = [
                                    '9072888001528021798096225500850762068629339333975650685139102691291'
                                    ], 
                                channel_ids = [
                                    '9072888001528021798096225500850762068629339333975650685139102691291'
                                    ], )
                            ], 
                        single_select = True, 
                        required = True, 
                        in_onboarding = True, 
                        type = 56, )
                    ],
                default_channel_ids = [
                    '9072888001528021798096225500850762068629339333975650685139102691291'
                    ],
                enabled = True,
        )
        """

    def testGuildOnboardingResponse(self):
        """Test GuildOnboardingResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
